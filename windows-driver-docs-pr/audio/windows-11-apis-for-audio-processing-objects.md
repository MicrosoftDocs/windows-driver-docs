---
title: Windows 11 APIs for Audio Processing Objects
description: Windows 11 introduces several new core audio APIs that improve the reliability of interaction with the audio stack. 
keywords:
- Audio Processing Object
- Audio processing architecture
- APO, APOs
- Audio Logging, Audio Events, Audio Threading
- Audio Effects Discovery
- Audio Settings, Audio Notifications
- Windows 11 audio 
- CAPX, Core Audio Processing Object Extensions
ms.date: 08/11/2023
---

# Windows 11 APIs for Audio Processing Objects

This topic introduces a set of new Windows 11 APIs for Audio Processing Objects (APOs) that are shipped with an audio driver. 

Windows allows third-party audio hardware manufacturers to include custom host-based digital signal processing effects. These effects are packaged as user-mode Audio Processing Objects (APOs). For more information, see [Windows Audio Processing Objects](windows-audio-processing-objects.md).

Some of the APIs described here enable new scenarios for Independent Hardware Vendors (IHV) and Independent Software Vendors (ISV), while other APIs are meant to provide alternatives that improve overall audio reliability and debugging capabilities.

- The [Acoustic Echo Cancellation (AEC) framework](#acoustic-echo-cancellation-aec) allows an APO to identify itself as an _AEC_ APO, granting access to a reference stream and additional controls.
- The [Settings framework](#settings-framework) will allow APOs to expose methods for querying and modifying the property store for audio effects (“FX property store”) on an audio endpoint. When these methods are implemented by an APO, they can be invoked by Hardware Support Apps (HSA) that are associated with that APO.
- The [Notifications framework](#notifications-framework) allows audio effects (APOs) to request notifications for handling volume, endpoint and audio effects property store changes.
- The [Logging framework](#logging-framework) aids in the development and debugging of APOs. 
- The [Threading framework](#threading-framework) allows APOs to be multithreaded by using an OS managed, MMCSS-registered thread pool.
- The [Audio Effects Discovery and Control APIs](#audio-effects-discovery-and-control-for-effects) allows the OS to detect, enable, and disable effects that are available for processing on a stream.

To leverage these new APIs, APOs are expected to utilize the new [IAudioSystemEffects3](/windows/win32/api/audioengineextensionapo/nn-audioengineextensionapo-iaudiosystemeffects3) interface. When an APO implements this interface, the OS interprets this as an implicit signal that the APO supports the APO Settings framework and allows the APO to subscribe for common audio related notifications from the audio engine.

## Windows 11 APO CAPX development requirements

Any new APOs that ship on a device for Windows 11 are required to be compliant with the APIs listed in this topic, validated via HLK. Additionally, any APOs leveraging AEC are expected to follow the implementation outlined in this topic, validated via HLK. Custom implementations for these core audio processing extensions (Settings, Logging, Notifications, Threading, AEC) are expected to leverage CAPX APIs. This will be validated through the Windows 11 HLK tests. For example, if an APO is using registry data to  save settings instead of using the Settings Framework, the associated HLK test will fail.

## Windows version requirements

The APIs described in this topic are available starting in build 22000 of the Windows 11 OS, WDK, and SDK. Windows 10 will not have support for these APIs. If an APO intends to function on both Windows 10 and Windows 11, it can examine whether it is being initialized with the [APOInitSystemEffects2](/windows/win32/api/audioenginebaseapo/ns-audioenginebaseapo-apoinitsystemeffects2) or the [APOInitSystemEffects3](/windows/win32/api/audioengineextensionapo/ns-audioengineextensionapo-apoinitsystemeffects3) structure to determine whether it is running on an OS that supports the CAPX APIs.

The latest versions of Windows, the WDK, and the SDK can be downloaded below through the Windows Insider Program. Partners that are engaged with Microsoft through Partner Center can also access this content through Collaborate. For more information about Collaborate, see [Introduction to Microsoft Collaborate](/collaborate/intro-to-mscollaborate).

- [Windows Insider Preview - ISO Download](https://www.microsoft.com/software-download/windowsinsiderpreviewiso)
- [Windows Insider Preview - WDK Download](https://www.microsoft.com/software-download/windowsinsiderpreviewWDK)
- [Windows Insider Preview - SDK Download](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK)

Windows 11 WHCP Content has been updated to provide partners the means to validate these APIs. 

The sample code for the content outlined in this topic can be found here: [Audio/SYSVAD/APO - github](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/)

## Acoustic Echo Cancellation (AEC)

Acoustic Echo Cancellation (AEC) is a common audio effect implemented by Independent Hardware Vendors (IHVs) and Independent Software Vendors (ISVs) as an Audio Processing Object (APO) in the microphone capture pipeline. This effect is different from other effects typically implemented by IHVs and ISVs in that it requires 2 inputs – an audio stream from the microphone and an audio stream from a render device that acts as the reference signal.

This new set of interfaces allows an AEC APO to identify itself as such to the audio engine. Doing so results in the audio engine configuring the APO appropriately with multiple inputs and a single output.

When the new AEC interfaces are implemented by an APO, the audio engine will:

- Configure the APO with an additional input that provides the APO with the reference stream from an appropriate render endpoint.
- Switch out the reference streams as the render device changes.
- Allow an APO to control the format of the input microphone and reference stream.
- Allow an APO to obtain timestamps on the microphone and reference streams.

### Previous approach - Windows 10

APOs are single input – single output objects. The audio engine provides an AEC APO the audio from the microphone endpoint at its input. To obtain the reference stream, an APO can either interact with the driver using proprietary interfaces to retrieve the reference audio from the render endpoint or use WASAPI to open a loopback stream on the render endpoint.

Both of the above approaches have drawbacks:

- An AEC APO that uses private channels to obtain a reference stream from the driver, typically can do so only from the integrated audio render device. As a result, echo cancellation won’t work if the user is playing audio out of the non-integrated device such as USB or Bluetooth audio device. Only the OS is aware of the right render endpoints that can serve as the reference endpoints.

- An APO can use WASAPI to pick the default render endpoint to perform echo cancellation. However, there are some pitfalls to be aware of when opening a loopback stream from the audiodg.exe process (which is where the APO is hosted).
    - The loopback stream cannot be opened/destroyed when the audio engine is calling into the main APO methods, as this can result in a deadlock.
    - A capture APO does not know the state of the streams of its clients. i.e. a capture app could have a capture stream in the ‘STOP’ state, however the APO is unaware of this state, and hence keeps the loopback stream open in the ‘RUN’ state, which is inefficient in terms of power consumption.

### API definition - AEC 

The AEC framework provides new structures and interfaces that APOs can leverage. These new structures and interfaces are described below.

#### APO_CONNECTION_PROPERTY_V2 structure 

APOs that implement the [IApoAcousticEchoCancellation](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iapoacousticechocancellation) interface will be passed an [APO_CONNECTION_PROPERTY_V2](/windows/win32/api/audioapotypes/ns-audioapotypes-apo_connection_property_v2) structure in its call to IAudioProcessingObjectRT::APOProcess. In addition to all the fields in the [APO_CONNECTION_PROPERTY](/windows/win32/api/audioapotypes/ns-audioapotypes-apo_connection_property) structure, version 2 of the structure also provides timestamp information for the audio buffers.

An APO can examine the APO_CONNECTION_PROPERTY.u32Signature field to determine whether the structure it receives from the audio engine is of type APO_CONNECTION_PROPERTY or APO_CONNECTION_PROPERTY_V2. APO_CONNECTION_PROPERTY structures have a signature of 
APO_CONNECTION_PROPERTY_SIGNATURE, while APO_CONNECTION_PROPERTY_V2 have a signature that equals APO_CONNECTION_PROPERTY_V2_SIGNATURE.
If the signature has a value that equals APO_CONNECTION_PROPERTY_V2_SIGNATURE, the pointer to the APO_CONNECTION_PROPERTY structure may be safely typecast to an APO_CONNECTION_PROPERTY_V2 pointer.

The following code is from the [Aec APO MFX sample - AecApoMfx.cpp](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/AecApo/AecApoMfx.cpp) and shows the recasting.

```cpp
    if (ppInputConnections[0]->u32Signature == APO_CONNECTION_PROPERTY_V2_SIGNATURE)
    {
        const APO_CONNECTION_PROPERTY_V2* connectionV2 = reinterpret_cast<const APO_CONNECTION_PROPERTY_V2*>(ppInputConnections[0]);
    }
```

#### IApoAcousticEchoCancellation

The  [IApoAcousticEchoCancellation interface](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iapoacousticechocancellation) has no explicit methods on it. Its purpose is to identify an AEC APO to the audio engine. This interface may only be implemented by mode effects (MFX) on capture endpoints. Implementing this interface on any other APO will lead to a failure in loading that APO. For general information about MFX, see [Audio Processing Objects Architecture](./audio-processing-object-architecture.md).

If the mode effect on a capture endpoint is implemented as a series of chained APOs, only the APO closest to the device may implement this interface.
APOs that implement this interface will be offered the APO_CONNECTION_PROPERTY_V2 structure in its call to [IAudioProcessingobjectRT::APOProcess](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-apoprocess). The APO can check for a APO_CONNECTION_PROPERTY_V2_SIGNATURE signature on the connection property and typecast the incoming APO_CONNECTION_PROPERTY structure to a APO_CONNECTION_PROPERTY_V2 structure. 

In recognition of the fact that AEC APOs usually run their algorithms at a specific sampling rate/channel count, the audio engine provides resampling support to APOs that implement the IApoAcousticEchoCancellation interface.

When an AEC APO returns APOERR_FORMAT_NOT_SUPPORTED in the call to IAudioProcessingObject::OutInputFormatSupported, the audio engine will call 
[IAudioProcessingObject::IsInputFormatSupported](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-isinputformatsupported) on the APO again with a NULL output format and a non-null input format, to obtain the APO’s suggested format. The audio engine will then resample microphone audio to the suggested format prior to sending it to the AEC APO. This eliminates the need for the AEC APO to implement sampling rate and channel count conversion.

#### IApoAuxiliaryInputConfiguration

The [IApoAuxiliaryInputConfiguration](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iapoauxiliaryinputconfiguration) interface provides methods that APOs can implement so that the audio engine can add and remove auxiliary input streams.

This interface is implemented by the AEC APO and used by the audio engine to initialize the reference input. In Windows 11, the AEC APO will only be initialized with a single auxiliary input – one that has the reference audio stream for echo cancellation.
The [AddAuxiliaryInput method](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iapoauxiliaryinputconfiguration-addauxiliaryinput) will be used to add the reference input to the APO. The initialization parameters will contain a reference to the render endpoint that the loopback stream is obtained from. 

The [IsInputFormatSupported method](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iapoauxiliaryinputconfiguration-isinputformatsupported) is called by the audio engine to negotiate formats on the auxiliary input. If the AEC APO prefers a specific format, it can return S_FALSE in the call to IsInputFormatSupported, and specify a suggested format. The audio engine will resample the reference audio to the suggested format and provide it at the auxiliary input of the AEC APO.

#### IApoAuxiliaryInputRT

The [IApoAuxiliaryInputRT](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iapoauxiliaryinputrt) interface is the realtime-safe interface used to drive the auxiliary inputs of an APO.

This interface is used to provide audio data on the auxiliary input to the APO. Note that the auxiliary audio inputs are not synchronized with the calls to [IAudioProcessingObjectRT::APOProcess](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-apoprocess). When there is no audio being rendered out the render endpoint, loopback data will not be available at the auxiliary input. i.e. there will be no calls to [IApoAuxiliaryInputRT::AcceptInput](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iapoauxiliaryinputrt-acceptinput)

##### Summary of AEC CAPX APIs

For more information, find additional information on the following pages.

-  [APO_CONNECTION_PROPERTY_V2 structure (audioapotypes.h)](/windows/win32/api/audioapotypes/ns-audioapotypes-apo_connection_property_v2)
-  [IApoAcousticEchoCancellation interface](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iapoacousticechocancellation)
-  [IApoAuxiliaryInputConfiguration](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iapoauxiliaryinputconfiguration)
-  [IApoAuxiliaryInputRT](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iapoauxiliaryinputrt)

### Sample code - AEC

Refer to the following Sysvad Audio AecApo code samples. 

- [Aec APO sample header - AecAPO.h](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/AecApo/AecApo.h)

- [Aec APO MFX sample - AecApoMfx.cpp](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/AecApo/AecApoMfx.cpp)

The following code from the [Aec APO sample header-  AecAPO.h](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/AecApo/AecApo.h) shows the three new public methods being added. 

```cpp
 public IApoAcousticEchoCancellation,
 public IApoAuxiliaryInputConfiguration,
 public IApoAuxiliaryInputRT

...

 COM_INTERFACE_ENTRY(IApoAcousticEchoCancellation)
 COM_INTERFACE_ENTRY(IApoAuxiliaryInputConfiguration)
 COM_INTERFACE_ENTRY(IApoAuxiliaryInputRT)

...


    // IAPOAuxiliaryInputConfiguration
    STDMETHOD(AddAuxiliaryInput)(
        DWORD dwInputId,
        UINT32 cbDataSize,
        BYTE *pbyData,
        APO_CONNECTION_DESCRIPTOR *pInputConnection
        ) override;
    STDMETHOD(RemoveAuxiliaryInput)(
        DWORD dwInputId
        ) override;
    STDMETHOD(IsInputFormatSupported)(
        IAudioMediaType* pRequestedInputFormat,
        IAudioMediaType** ppSupportedInputFormat
        ) override;
...

    // IAPOAuxiliaryInputRT
    STDMETHOD_(void, AcceptInput)(
        DWORD dwInputId,
        const APO_CONNECTION_PROPERTY *pInputConnection
        ) override;

    // IAudioSystemEffects3
    STDMETHODIMP GetControllableSystemEffectsList(_Outptr_result_buffer_maybenull_(*numEffects) AUDIO_SYSTEMEFFECT** effects, _Out_ UINT* numEffects, _In_opt_ HANDLE event) override
    {
        UNREFERENCED_PARAMETER(effects);
        UNREFERENCED_PARAMETER(numEffects);
        UNREFERENCED_PARAMETER(event);
        return S_OK; 
    }

```

The following code is from the [Aec APO MFX sample - AecApoMfx.cpp](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/AecApo/AecApoMfx.cpp) and shows the implementation of AddAuxiliaryInput, when the APO can only handle one auxiliary input.


```cpp
STDMETHODIMP
CAecApoMFX::AddAuxiliaryInput(
    DWORD dwInputId,
    UINT32 cbDataSize,
    BYTE *pbyData,
    APO_CONNECTION_DESCRIPTOR * pInputConnection
)
{
    HRESULT hResult = S_OK;

    CComPtr<IAudioMediaType> spSupportedType;
    ASSERT_NONREALTIME();

    IF_TRUE_ACTION_JUMP(m_bIsLocked, hResult = APOERR_APO_LOCKED, Exit);
    IF_TRUE_ACTION_JUMP(!m_bIsInitialized, hResult = APOERR_NOT_INITIALIZED, Exit);

    BOOL bSupported = FALSE;
    hResult = IsInputFormatSupportedForAec(pInputConnection->pFormat, &bSupported);
    IF_FAILED_JUMP(hResult, Exit);
    IF_TRUE_ACTION_JUMP(!bSupported, hResult = APOERR_FORMAT_NOT_SUPPORTED, Exit);

    // This APO can only handle 1 auxiliary input
    IF_TRUE_ACTION_JUMP(m_auxiliaryInputId != 0, hResult = APOERR_NUM_CONNECTIONS_INVALID, Exit);

    m_auxiliaryInputId = dwInputId;
```

Also review the sample code that shows the implementation of `CAecApoMFX::IsInputFormatSupported` and `CAecApoMFX::AcceptInput` as well as the handling of the `APO_CONNECTION_PROPERTY_V2`.

### Sequence of operations - AEC

On initialization: 

1. IAudioProcessingObject::Initialize
2. IApoAuxiliaryInputConfiguration::AddAuxiliaryInput
3. IAudioProcessingObjectConfiguration:: LockForProcess
4. IAudioProcessingObjectConfiguration ::UnlockForProcess
5. IApoAuxiliaryInputConfiguration::RemoveAuxiliaryInput

On render device change: 

1. IAudioProcessingObject::Initialize
2. IApoAuxiliaryInputConfiguration::AddAuxiliaryInput
3. IAudioProcessingObjectConfiguration::LockForProcess
4. Default device changes
5. IAudioProcessingObjectConfiguration::UnlockForProcess
6. IApoAuxiliaryInputConfiguration::RemoveAuxiliaryInput
7. IApoAuxiliaryInputConfiguration::AddAuxiliaryInput
8. IAudioProcessingObjectConfiguration::LockForProcess 

### Recommended buffering behavior - AEC

This is the recommended buffer behavior for AEC.

- Buffers obtained in the call to IApoAuxiliaryInputRT::AcceptInput should be written to a circular buffer without locking the main thread.
- On the call to IAudioProcessingObjectRT::APOProcess, the circular buffer should be read for the latest audio packet from the reference stream, and this packet should be used for running through the echo cancellation algorithm.
- Timestamps on the reference and microphone data may be used to line up the speaker and mic data.

## Reference Loopback Stream

By default, the loopback stream "taps into" (listens to) the audio stream prior to any volume or muting being applied.  A loopback stream tapped before volume has been applied is known as a pre-volume loopback stream.  An advantage of having a pre-volume loopback stream is a clear and uniform audio stream, regardless of the current volume setting.

Some AEC algorithms may prefer obtaining a loopback stream that has been connected after any volume processing (including being muted).  This configuration is known as post-volume loopback.

In the next major version of Windows AEC APOs can request post-volume loopback on supported endpoints.

### Limitations

Unlike pre-volume loopback streams, which are available for all render endpoints, post-volume loopback streams may not be available on all endpoints.

### Requesting Post-Volume Loopback

AEC APOs that wish to use post-volume loopback should implement the [IApoAcousticEchoCancellation2](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iapoacousticechocancellation2) interface.

An AEC APO can request post-volume loopback by returning the **APO_REFERENCE_STREAM_PROPERTIES_POST_VOLUME_LOOPBACK** flag via the Properties parameter in its implementation of [IApoAcousticEchoCancellation2::GetDesiredReferenceStreamProperties](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iapoacousticechocancellation2-getdesiredreferencestreamproperties).

Depending on the render endpoint currently being used, post-volume loopback may not be available.  An AEC APO is notified if post-volume loopback is being used when its [IApoAuxiliaryInputConfiguration::AddAuxiliaryInput](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iapoauxiliaryinputconfiguration-addauxiliaryinput) method is called. If the [AcousticEchoCanceller_Reference_Input](/windows/win32/api/audioengineextensionapo/ns-audioengineextensionapo-acousticechocanceller_reference_input) streamProperties field contains **APO_REFERENCE_STREAM_PROPERTIES_POST_VOLUME_LOOPBACK**, post-volume loopback is in use.

The following code from the AEC APO sample header- AecAPO.h shows the three new public methods being added.

```cpp
public:
  // IApoAcousticEchoCancellation2
  STDMETHOD(GetDesiredReferenceStreamProperties)(
    _Out_ APO_REFERENCE_STREAM_PROPERTIES * properties) override;

  // IApoAuxiliaryInputConfiguration
  STDMETHOD(AddAuxiliaryInput)(
    DWORD dwInputId,
    UINT32 cbDataSize,
    _In_ BYTE* pbyData,
    _In_ APO_CONNECTION_DESCRIPTOR *pInputConnection
    ) override;
```

The following code snippet is from the AEC APO MFX sample - AecApoMfx.cpp and shows the implementation of GetDesiredReferenceStreamProperties, and relevant portion of AddAuxiliaryInput.

```cpp
STDMETHODIMP SampleApo::GetDesiredReferenceStreamProperties(
  _Out_ APO_REFERENCE_STREAM_PROPERTIES * properties)
{
  RETURN_HR_IF_NULL(E_INVALIDARG, properties);

  // Always request that a post-volume loopback stream be used, if
  // available. We will find out which type of stream was actually
  // created when AddAuxiliaryInput is invoked.
  *properties = APO_REFERENCE_STREAM_PROPERTIES_POST_VOLUME_LOOPBACK;
  return S_OK;
}

STDMETHODIMP
CAecApoMFX::AddAuxiliaryInput(
    DWORD dwInputId,
    UINT32 cbDataSize,
    BYTE *pbyData,
    APO_CONNECTION_DESCRIPTOR * pInputConnection
)
{
   // Parameter checking skipped for brevity, please see sample for 
   // full implementation.

  AcousticEchoCanceller_Reference_Input* referenceInput = nullptr;
  APOInitSystemEffects3* papoSysFxInit3 = nullptr;

  if (cbDataSize == sizeof(AcousticEchoCanceller_Reference_Input))
  {
    referenceInput = 
      reinterpret_cast<AcousticEchoCanceller_Reference_Input*>(pbyData);

    if (WI_IsFlagSet(
          referenceInput->streamProperties,
          APO_REFERENCE_STREAM_PROPERTIES_POST_VOLUME_LOOPBACK))
    {
      // Post-volume loopback is being used.
      m_bUsingPostVolumeLoopback = TRUE;
        
      // Note that we can get to the APOInitSystemEffects3 from     
      // AcousticEchoCanceller_Reference_Input.
      papoSysFxInit3 = (APOInitSystemEffects3*)pbyData;
    }
    else  if (cbDataSize == sizeof(APOInitSystemEffects3))
    {
      // Post-volume loopback is not supported.
      papoSysFxInit3 = (APOInitSystemEffects3*)pbyData;
    }

    // Remainder of method skipped for brevity.
```

## Settings Framework

The Settings Framework allows APOs to expose methods for querying and modifying the property store for audio effects ("FX Property Store") on an audio endpoint. This framework can be used by APOs and by Hardware Support Apps (HSA) that wish to communicate settings to that APO. HSAs can be Universal Windows Platform (UWP) apps and require a special capability to invoke the APIs in the Settings Framework. For more information about HSA apps, see [UWP device apps](../devapps/index.md).

### FxProperty Store Structure

The new FxProperty store has three substores: Default, User, and Volatile. 

The "Default" subkey contains custom effects properties and is populated from the INF file. These properties do not persist across OS upgrades. For example, properties that are typically defined in an INF would fit here. These would then be re-populated from the INF.

The "User" subkey contains user settings pertaining to effects properties. These settings are persisted by the OS across upgrades and migrations.  For example, any presets that the user can configure that are expected to persist across upgrade.

The "Volatile" subkey contains volatile effects properties. These properties are lost upon device reboot and are cleared each time the endpoint transitions to active. These are expected to contain time variant properties (e.g. based on current running applications, device posture, etc.) For example, any settings that are dependent on the current environment.

The way to think about user versus default is whether you want the properties to persist across OS and driver upgrades. User properties will be persisted. Default properties will be re-populated from the INF.

#### APO Contexts

The CAPX settings framwork allows an APO author to group APO properties by *contexts*. Each APO can define its own context and update properties relative to its own context. The effects property store for an audio endpoint may have zero or more contexts. Vendors are free to create contexts however they choose, whether that is by SFX/MFX/EFX or by mode. A vendor could also choose to have a single context for all APOs shipped by that vendor.

### Settings Restricted Capability

The settings API is intended to support all OEMs and HSA developers interested in querying and modifying the audio effects settings associated with an audio device. This API is exposed to an HSA and Win32 applications to provide access to the property store through the restricted capability "audioDeviceConfiguration" that must be declared in the manifest. Additionally, a corresponding namespace must be declared as follows:

```xml
<Package
  xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities"
  IgnorableNamespaces="uap mp rescap">
  ...
 
  <Capabilities>
    <rescap:Capability Name="audioDeviceConfiguration" />
  </Capabilities>
</Package>
```
The [IAudioSystemEffectsPropertyStore](/windows/win32/api/mmdeviceapi/nn-mmdeviceapi-iaudiosystemeffectspropertystore) is readable and writable by an ISV/IHV service, a UWP store application, non-admin desktop applications, and APOs. Additionally, this can act as the mechanism for APOs to deliver messages back to a service or UWP store application.

>[!NOTE]
> This is a restricted capability: If an application is submitted with this capability to the Microsoft Store, it will trigger close scrutiny. 
> The app must be a Hardware Support App (HSA), and it will be examined to evaluate that it is indeed an HSA before the submission is approved.

### API definition - Settings Framework

The new [IAudioSystemEffectsPropertyStore](/windows/win32/api/mmdeviceapi/nn-mmdeviceapi-iaudiosystemeffectspropertystore) interface allows an HSA to access audio system effects property stores and register for property change notifications.

The [ActiveAudioInterfaceAsync](/windows/win32/api/mmdeviceapi/nf-mmdeviceapi-activateaudiointerfaceasync) function provides a method to obtain the [IAudioSystemEffectsPropertyStore](/windows/win32/api/mmdeviceapi/nn-mmdeviceapi-iaudiosystemeffectspropertystore) interface asynchronously. 

An app can receive notifications when the system effects property store changes, using the new [IAudioSystemEffectsPropertyChangeNotificationClient](/windows/win32/api/mmdeviceapi/nn-mmdeviceapi-iaudiosystemeffectspropertychangenotificationclient) callback interface.

#### Application attempting to get the IAudioSystemEffectsPropertyStore using IMMDevice::Activate 

The sample demonstrates how a Hardware Support App can use IMMDevice::Activate to activate IAudioSystemEffectsPropertyStore. The sample shows how to use IAudioSystemEffectsPropertyStore to open an IPropertyStore that has user settings.

```cpp
#include <mmdeviceapi.h>

// This function opens an IPropertyStore with user settings on the specified IMMDevice.
// Input parameters:
// device - IMMDevice object that identifies the audio endpoint.
// propertyStoreContext - GUID that identifies the property store. Each APO can have its own GUID. These 
// GUIDs are chosen by the audio driver at installation time.
HRESULT GetPropertyStoreFromMMDevice(_In_ IMMDevice* device,
    REFGUID propertyStoreContext,
    _COM_Outptr_ IPropertyStore** userPropertyStore)
{
    *userPropertyStore = nullptr;

    wil::unique_prop_variant activationParam;
    RETURN_IF_FAILED(InitPropVariantFromCLSID(propertyStoreContext, &activationParam));

    wil::com_ptr_nothrow<IAudioSystemEffectsPropertyStore> effectsPropertyStore;
    RETURN_IF_FAILED(device->Activate(__uuidof(effectsPropertyStore), CLSCTX_INPROC_SERVER, activationParam.addressof(), effectsPropertyStore.put_void()));

    RETURN_IF_FAILED(effectsPropertyStore->OpenUserPropertyStore(STGM_READWRITE, userPropertyStore));
    return S_OK;
}
```

#### Sample using ActivateAudioInterfaceAsync

This sample does the same thing as the previous sample, but instead of using IMMDevice, it uses the [ActivateAudioInterfaceAsync](/windows/win32/api/mmdeviceapi/nf-mmdeviceapi-activateaudiointerfaceasync) API to obtain the IAudioSystemEffectsPropertyStore interface asynchronously.

```cpp
include <mmdeviceapi.h>

class PropertyStoreHelper : 
    public winrt::implements<PropertyStoreHelper, IActivateAudioInterfaceCompletionHandler>
{
public:
    wil::unique_event_nothrow m_asyncOpCompletedEvent;

    HRESULT GetPropertyStoreAsync(
        _In_ PCWSTR deviceInterfacePath,
        REFGUID propertyStoreContext,
        _COM_Outptr_ IActivateAudioInterfaceAsyncOperation** operation);

    HRESULT GetPropertyStoreResult(_COM_Outptr_ IPropertyStore** userPropertyStore);

    // IActivateAudioInterfaceCompletionHandler
    STDMETHOD(ActivateCompleted)(_In_ IActivateAudioInterfaceAsyncOperation *activateOperation);

private:
    wil::com_ptr_nothrow<IPropertyStore> m_userPropertyStore;
    HRESULT m_hrAsyncOperationResult = E_FAIL;

    HRESULT GetUserPropertyStore(
        _In_ IActivateAudioInterfaceAsyncOperation* operation,
        _COM_Outptr_ IPropertyStore** userPropertyStore);
};

// This function opens an IPropertyStore with user settings asynchronously on the specified audio endpoint.
// Input parameters:
// deviceInterfacePath - the Device Interface Path string that identifies the audio endpoint. Can be 
// obtained from Windows.Devices.Enumeration.DeviceInformation.
// propertyStoreContext - GUID that identifies the property store. Each APO can have its own GUID. These 
// GUIDs are chosen by the audio driver at installation time.
//
// The function returns an IActivateAudioInterfaceAsyncOperation, which can be used to check the result of
// the asynchronous operation.
HRESULT PropertyStoreHelper::GetPropertyStoreAsync(
    _In_ PCWSTR deviceInterfacePath,
    REFGUID propertyStoreContext,
    _COM_Outptr_ IActivateAudioInterfaceAsyncOperation** operation)
{
    *operation = nullptr;

    wil::unique_prop_variant activationParam;
    RETURN_IF_FAILED(InitPropVariantFromCLSID(propertyStoreContext, &activationParam));

    RETURN_IF_FAILED(ActivateAudioInterfaceAsync(deviceInterfacePath,
        __uuidof(IAudioSystemEffectsPropertyStore),
        activationParam.addressof(),
        this,
        operation));
    return S_OK;
}

// Once the IPropertyStore is available, the app can call this function to retrieve it.
// (The m_asyncOpCompletedEvent event is signaled when the asynchronous operation to retrieve
// the IPropertyStore has completed.)
HRESULT PropertyStoreHelper::GetPropertyStoreResult(_COM_Outptr_ IPropertyStore** userPropertyStore)
{
    *userPropertyStore = nullptr;

    // First check if the asynchronous operation completed. If it failed, the error code
    // is stored in the m_hrAsyncOperationResult variable.
    RETURN_IF_FAILED(m_hrAsyncOperationResult);

    RETURN_IF_FAILED(m_userPropertyStore.copy_to(userPropertyStore));
    return S_OK;
}

// Implementation of IActivateAudioInterfaceCompletionHandler::ActivateCompleted.
STDMETHODIMP PropertyStoreHelper::ActivateCompleted(_In_ IActivateAudioInterfaceAsyncOperation* operation)
{
    m_hrAsyncOperationResult = GetUserPropertyStore(operation, m_userPropertyStore.put());

    // Always signal the event that our caller might be waiting on before we exit,
    // even in case of failure.
    m_asyncOpCompletedEvent.SetEvent();
    return S_OK;
}

HRESULT PropertyStoreHelper::GetUserPropertyStore(
    _In_ IActivateAudioInterfaceAsyncOperation* operation,
    _COM_Outptr_ IPropertyStore** userPropertyStore)
{
    *userPropertyStore = nullptr;

    // Check if the asynchronous operation completed successfully, and retrieve an
    // IUnknown pointer to the result.
    HRESULT hrActivateResult;
    wil::com_ptr_nothrow<IUnknown> audioInterfaceUnknown;
    RETURN_IF_FAILED(operation->GetActivateResult(&hrActivateResult, audioInterfaceUnknown.put()));
    RETURN_IF_FAILED(hrActivateResult);

    // Convert the result to IAudioSystemEffectsPropertyStore
    wil::com_ptr_nothrow<IAudioSystemEffectsPropertyStore> effctsPropertyStore;
    RETURN_IF_FAILED(audioInterfaceUnknown.query_to(&effectsPropertyStore));

    // Open an IPropertyStore with the user settings.
    RETURN_IF_FAILED(effectsPropertyStore->OpenUserPropertyStore(STGM_READWRITE, userPropertyStore));
    return S_OK;
}
```


#### 	IAudioProcessingObject::Initialize code using the IAudioSystemEffectsPropertyStore

The sample demonstrates the implementation of an APO can use the APOInitSystemEffects3 structure to retrieve the user, default and volatile IPropertyStore interfaces for the APO, during the initialization of the APO.

```cpp
#include <audioenginebaseapo.h>

// Partial implementation of APO to show how an APO that implements IAudioSystemEffects3 can handle
// being initialized with the APOInitSystemEffects3 structure.
class SampleApo : public winrt::implements<SampleApo, IAudioProcessingObject,
    IAudioSystemEffects, IAudioSystemEffects2, IAudioSystemEffects3>
{
public:
    // IAudioProcessingObject
    STDMETHOD(Initialize)(UINT32 cbDataSize, BYTE* pbyData);

    // Implementation of IAudioSystemEffects2, IAudioSystemEffects3 has been omitted from this sample for brevity.  

private:

    wil::com_ptr_nothrow<IPropertyStore> m_defaultStore;
    wil::com_ptr_nothrow<IPropertyStore> m_userStore;
    wil::com_ptr_nothrow<IPropertyStore> m_volatileStore;

    // Each APO has its own private collection of properties. The collection is dentified through a
    // a property store context GUID, which is defined below and in the audio driver INF file.
    const GUID m_propertyStoreContext = ...;
};

// Implementation of IAudioProcessingObject::Initialize
STDMETHODIMP SampleApo::Initialize(UINT32 cbDataSize, BYTE* pbyData)
{
    if (cbDataSize == sizeof(APOInitSystemEffects3))
    {
        // SampleApo supports the new IAudioSystemEffects3 interface so it will receive APOInitSystemEffects3
        // in pbyData if the audio driver has declared support for this.

        // Use IMMDevice to activate IAudioSystemEffectsPropertyStore that contains the default, user and
        // volatile settings.
        IMMDeviceCollection* deviceCollection = 
            reinterpret_cast<APOInitSystemEffects3*>(pbyData)->pDeviceCollection;
        if (deviceCollection != nullptr)
        {
            UINT32 numDevices;
            wil::com_ptr_nothrow<IMMDevice> endpoint;

            // Get the endpoint on which this APO has been created
            // (It is the last device in the device collection)
            if (SUCCEEDED(deviceCollection->GetCount(&numDevices)) &&
                numDevices > 0 &&
                SUCCEEDED(deviceCollection->Item(numDevices - 1, &endpoint)))
            {
                wil::unique_prop_variant activationParam;
                RETURN_IF_FAILED(InitPropVariantFromCLSID(m_propertyStoreContext, &activationParam));

                wil::com_ptr_nothrow<IAudioSystemEffectsPropertyStore> effectsPropertyStore;
                RETURN_IF_FAILED(endpoint->Activate(__uuidof(effectsPropertyStore), CLSCTX_ALL, &activationParam, effectsPropertyStore.put_void()));

                // Read default, user and volatile property values to set up initial operation of the APO
                RETURN_IF_FAILED(effectsPropertyStore->OpenDefaultPropertyStore(STGM_READWRITE, m_defaultStore.put()));
                RETURN_IF_FAILED(effectsPropertyStore->OpenUserPropertyStore(STGM_READWRITE, m_userStore.put()));
                RETURN_IF_FAILED(effectsPropertyStore->OpenVolatilePropertyStore(STGM_READWRITE, m_volatileStore.put()));

                // At this point the APO can read and write settings in the various property stores,
                // as appropriate. (Not shown.)
                // Note that APOInitSystemEffects3 contains all the members of APOInitSystemEffects2,
                // so an APO that knows how to initialize from APOInitSystemEffects2 can use the same
                // code to continue its initialization here.
            }
        }
    }
    else if (cbDataSize == sizeof(APOInitSystemEffects2))
    {
        // Use APOInitSystemEffects2 for the initialization of the APO.
        // If we get here, the audio driver did not declare support for IAudioSystemEffects3.
    }
    else if (cbDataSize == sizeof(APOInitSystemEffects))
    {
        // Use APOInitSystemEffects for the initialization of the APO.
    }

    return S_OK;
}
```

#### 	Application registering for property change notifications

The sample demonstrates the use of registration for property change notifications. This should not be used from with the APO, and should be utilized by Win32 applications.

```cpp
class PropertyChangeNotificationClient : public 
    winrt::implements<PropertyChangeNotificationClient, IAudioSystemEffectsPropertyChangeNotificationClient>
{
private:
    wil::com_ptr_nothrow<IAudioSystemEffectsPropertyStore> m_propertyStore;
    bool m_isListening = false;

public:
    HRESULT OpenPropertyStoreOnDefaultRenderEndpoint(REFGUID propertyStoreContext);
    HRESULT StartListeningForPropertyStoreChanges();
    HRESULT StopListeningForPropertyStoreChanges();

    // IAudioSystemEffectsPropertyChangeNotificationClient
    STDMETHOD(OnPropertyChanged)(AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE type, const PROPERTYKEY key);
};

// Open the IAudioSystemEffectsPropertyStore. This should be the first method invoked on this class.
HRESULT PropertyChangeNotificationClient::OpenPropertyStoreOnDefaultRenderEndpoint(
    REFGUID propertyStoreContext)
{
    wil::com_ptr_nothrow<IMMDeviceEnumerator> deviceEnumerator;
    RETURN_IF_FAILED(CoCreateInstance(__uuidof(MMDeviceEnumerator), nullptr, CLSCTX_INPROC_SERVER, IID_PPV_ARGS(&deviceEnumerator)));

    wil::com_ptr_nothrow<IMMDevice> device;
    RETURN_IF_FAILED(deviceEnumerator->GetDefaultAudioEndpoint(eRender, eConsole, device.put()));

    wil::unique_prop_variant activationParam;
    RETURN_IF_FAILED(InitPropVariantFromCLSID(propertyStoreContext, &activationParam));

    RETURN_IF_FAILED(device->Activate(__uuidof(m_propertyStore), CLSCTX_INPROC_SERVER,
        &activationParam, m_propertyStore.put_void()));
    return S_OK;
}

// Start subscribing to callbacks that are invoked when there are changes to any of the IPropertyStores
// that are managed by IAudioSystemEffectsPropertyStore.
// The OpenPropertyStoreOnDefaultRenderEndpoint should have been invoked prior to invoking this function.
HRESULT PropertyChangeNotificationClient::StartListeningForPropertyStoreChanges()
{
    RETURN_HR_IF(E_FAIL, !m_propertyStore);
    RETURN_IF_FAILED(m_propertyStore->RegisterPropertyChangeNotification(this));
    m_isListening = true;
    return S_OK;
}

// Unsubscrbe to event callbacks. Since IAudioSystemEffectsPropertyStore takes a reference on our
// PropertyChangeNotificationClient class, it is important that this method is invoked prior to cleanup,
// to break the circular reference.
HRESULT PropertyChangeNotificationClient::StopListeningForPropertyStoreChanges()
{
    if (m_propertyStore != nullptr && m_isListening)
    {
        RETURN_IF_FAILED(m_propertyStore->UnregisterPropertyChangeNotification(this));
        m_isListening = false;
    }
    return S_OK;
}

// Callback method that gets invoked when there have been changes to any of the IPropertyStores
// that are managed by IAudioSystemEffectsPropertyStore. Note that calls to 
// IAudioSystemEffectsPropertyChangeNotificationClient are not marshalled across COM apartments.
// Therefore, the OnPropertyChanged is most likely invoked on a different thread than the one used when
// invoking RegisterPropertyChangeNotification. If necessary, concurrent access to shared state should be
// protected with a critical section. 
STDMETHODIMP PropertyChangeNotificationClient::OnPropertyChanged(AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE type, const PROPERTYKEY key)
{
    if (type == AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE_USER)
    {
        // Handle changes to the User property store.

        wil::com_ptr_nothrow<IPropertyStore> userPropertyStore;
        RETURN_IF_FAILED(m_propertyStore->OpenUserPropertyStore(STGM_READ, userPropertyStore.put()));

        // Here we can call IPropertyStore::GetValue to read the current value of PROPERTYKEYs that we are
        // interested in.
    }
    else if (type == AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE_VOLATILE)
    {
        // Handle changes to the Volatile property store, if desired
    }

    return S_OK;
}
```


### Sample code - Settings Framework

This sample code is from the sysvad [SFX Swap APO sample - SwapAPOSFX.cpp](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/SwapAPO/swapaposfx.cpp#L300-L329).

```cpp
// SampleApo supports the new IAudioSystemEffects3 interface so it will receive APOInitSystemEffects3
// in pbyData if the audio driver has declared support for this.

// Use IMMDevice to activate IAudioSystemEffectsPropertyStore that contains the default, user and
// volatile settings.
IMMDeviceCollection* deviceCollection = reinterpret_cast<APOInitSystemEffects3*>(pbyData)->pDeviceCollection;
if (deviceCollection != nullptr)
{
    UINT32 numDevices;
    wil::com_ptr_nothrow<IMMDevice> endpoint;

    // Get the endpoint on which this APO has been created
    // (It is the last device in the device collection)
    if (SUCCEEDED(deviceCollection->GetCount(&numDevices)) && numDevices > 0 &&
        SUCCEEDED(deviceCollection->Item(numDevices - 1, &endpoint)))
    {
        wil::unique_prop_variant activationParam;
        hr = InitPropVariantFromCLSID(SWAP_APO_SFX_CONTEXT, &activationParam);
        IF_FAILED_JUMP(hr, Exit);

        wil::com_ptr_nothrow<IAudioSystemEffectsPropertyStore> effectsPropertyStore;
        hr = endpoint->Activate(__uuidof(effectsPropertyStore), CLSCTX_ALL, &activationParam, effectsPropertyStore.put_void());
        IF_FAILED_JUMP(hr, Exit);

        // This is where an APO might want to open the volatile or default property stores as well 
        // Use STGM_READWRITE if IPropertyStore::SetValue is needed.
        hr = effectsPropertyStore->OpenUserPropertyStore(STGM_READ, m_userStore.put());
        IF_FAILED_JUMP(hr, Exit);
    }
}
```

### INF section - Settings Framework

The INF file syntax to declare effect properties using the new CAPX settings framework is as follows:

```
HKR, FX\0\{ApoContext}\{Default|User}, %CUSTOM_PROPERTY_KEY%,,,
```

This replaces the older syntax for declaring effect properties as follows:

```
# Old way of declaring FX properties
HKR, FX\0, %CUSTOM_PROPERTY_KEY_1%,,,
```

The INF cannot have both the IAudioSystemEffectsPropertyStore entry and the IPropertyStore entry for the same audio endpoint. That is not supported.

Example showing use of the new property store:

```
HKR,FX\0\%SWAP_APO_CONTEXT%,%PKEY_FX_Association%,,%KSNODETYPE_ANY%
; Enable the channel swap in the APO
HKR,FX\0\%SWAP_APO_CONTEXT%\User,%PKEY_Endpoint_Enable_Channel_Swap_SFX%,REG_DWORD,0x1

PKEY_Endpoint_Enable_Channel_Swap_SFX = "{A44531EF-5377-4944-AE15-53789A9629C7},2"
REG_DWORD = 0x00010001 ; FLG_ADDREG_TYPE_DWORD
SWAP_APO_CONTEXT = "{24E7F619-5B33-4084-9607-878DA8722417}"
PKEY_FX_Association  = "{D04E05A6-594B-4FB6-A80D-01AF5EED7D1D},0"
KSNODETYPE_ANY   = "{00000000-0000-0000-0000-000000000000}"
```

## Notifications Framework

The Notifications framework allows audio effects (APOs) to request for and handle volume, endpoint, and audio effects property store change notifications. This framework is intended to replace existing APIs that are used by APOs to register and unregister for notifications.

The new API introduces an interface that APOs can utilize to declare the type of notifications that APO is interested in. Windows will query the APO for the notifications it is interested in, and forward the notification to the APOs. APOs no longer need to explicitly call the registration or unregistration APIs.

Notifications are delivered to an APO using a serial queue. When applicable, the first notification broadcasts initial state of the requested value (for example, the audio endpoint volume). Notifications stop once audiodg.exe stops intending to use an APO for streaming. APOs will stop receiving notifications after UnlockForProcess. It is still necessary to synchronize UnlockForProcess and any in-flight notifications.

### Implementation - Notifications Framework

To leverage the notifications framework, an APO declares what notifications it is interested in. There are no explicit registration/unregistration calls. All notifications to the APO are serialized, and it is important to not block the notification callback thread for too long. 

### API definition - Notifications Framework

The notification framework implements a new [IAudioProcessingObjectNotifications](/windows/win32/api/audioengineextensionapo/nn-audioengineextensionapo-iaudioprocessingobjectnotifications) interface that can be implemented by clients to register and receive common audio-related notifications for APO endpoint and system effect notifications. 

For more information, find additional content on the following pages:
-  [IAudioProcessingObjectNotifications](/windows/win32/api/audioengineextensionapo/nn-audioengineextensionapo-iaudioprocessingobjectnotifications)

### Sample code - Notifications Framework

The sample demonstrates how an APO can implement the IAudioProcessingObjectNotifications interface. In the GetApoNotificationRegistrationInfo method, the sample APO registers for notifications to changes to the system effects property stores.    
The HandleNotification method is invoked by the OS to notify the APO of changes that match what the APO had registered for. 

```cpp
class SampleApo : public winrt::implements<SampleApo, IAudioProcessingObject,
    IAudioSystemEffects, IAudioSystemEffects2, IAudioSystemEffects3,
    IAudioProcessingObjectNotifications>
{
public:
    // IAudioProcessingObjectNotifications
    STDMETHOD(GetApoNotificationRegistrationInfo)(
        _Out_writes_(count) APO_NOTIFICATION_DESCRIPTOR** apoNotifications, _Out_ DWORD* count);
    STDMETHOD_(void, HandleNotification)(_In_ APO_NOTIFICATION *apoNotification);

    // Implementation of IAudioSystemEffects2, IAudioSystemEffects3 has been omitted from this sample for brevity. 

private:
    wil::com_ptr_nothrow<IMMDevice> m_device;

    // Each APO has its own private collection of properties. The collection is dentified through a
    // a property store context GUID, which is defined below and in the audio driver INF file.
    const GUID m_propertyStoreContext = ...;

    float m_masterVolume = 1.0f;
    BOOL m_isMuted = FALSE;
    BOOL m_allowOffloading = FALSE;

    // The rest of the implementation of IAudioProcessingObject is omitted for brevity
};

// The OS invokes this method on the APO to find out what notifications the APO is interested in.
STDMETHODIMP SampleApo::GetApoNotificationRegistrationInfo(
    _Out_writes_(count) APO_NOTIFICATION_DESCRIPTOR** apoNotificationDescriptorsReturned,
    _Out_ DWORD* count)
{
    *apoNotificationDescriptorsReturned = nullptr;
    *count = 0;

    // Before this function can be called, our m_device member variable should already have been initialized.
    // This would typically be done in our implementation of IAudioProcessingObject::Initialize, by using
    // APOInitSystemEffects3::pDeviceCollection to obtain the last IMMDevice in the collection.
    RETURN_HR_IF_NULL(E_FAIL, m_device);

    // Let the OS know what notifications we are interested in by returning an array of
    // APO_NOTIFICATION_DESCRIPTORs.
    constexpr DWORD numDescriptors = 3;
    wil::unique_cotaskmem_ptr<APO_NOTIFICATION_DESCRIPTOR[]> apoNotificationDescriptors;

    apoNotificationDescriptors.reset(static_cast<APO_NOTIFICATION_DESCRIPTOR*>(
        CoTaskMemAlloc(sizeof(APO_NOTIFICATION_DESCRIPTOR) * numDescriptors)));
    RETURN_IF_NULL_ALLOC(apoNotificationDescriptors);

    // Our APO wants to get notified when any change occurs on the user property store on the audio endpoint
    // identified by m_device.
    // The user property store is different for each APO. Ours is identified by m_propertyStoreContext.
    apoNotificationDescriptors[0].type = APO_NOTIFICATION_TYPE_AUDIO_SYSTEM_EFFECTS_PROPERTY_CHANGE;
    (void)m_device.query_to(&apoNotificationDescriptors[0].audioSystemEffectsPropertyChange.device);
    apoNotificationDescriptors[0].audioSystemEffectsPropertyChange.propertyStoreContext =   m_propertyStoreContext;

    // Our APO wants to get notified when a endpoint property changes on the audio endpoint.
    apoNotificationDescriptors[1].type = APO_NOTIFICATION_TYPE_ENDPOINT_PROPERTY_CHANGE;
    (void)m_device.query_to(&apoNotificationDescriptors[1].audioEndpointPropertyChange.device);


    // Our APO also wants to get notified when the volume level changes on the audio endpoint.
    apoNotificationDescriptors   [2].type = APO_NOTIFICATION_TYPE_ENDPOINT_VOLUME;
    (void)m_device.query_to(&apoNotificationDescriptors[2].audioEndpointVolume.device);

    *apoNotificationDescriptorsReturned = apoNotificationDescriptors.release();
    *count = numDescriptors;
    return S_OK;
}

static bool IsSameEndpointId(IMMDevice* device1, IMMDevice* device2)
{
    bool isSameEndpointId = false;

    wil::unique_cotaskmem_string deviceId1;
    if (SUCCEEDED(device1->GetId(&deviceId1)))
    {
        wil::unique_cotaskmem_string deviceId2;
        if (SUCCEEDED(device2->GetId(&deviceId2)))
        {
            isSameEndpointId = (CompareStringOrdinal(deviceId1.get(), -1, deviceId2.get(), -1, TRUE) == CSTR_EQUAL);
        }
    }
    return isSameEndpointId;
}

// HandleNotification is called whenever there is a change that matches any of the
// APO_NOTIFICATION_DESCRIPTOR elements in the array that was returned by GetApoNotificationRegistrationInfo.
// Note that the APO will have to query each property once to get its initial value because this method is
// only invoked when any of the properties have changed.
STDMETHODIMP_(void) SampleApo::HandleNotification(_In_ APO_NOTIFICATION* apoNotification)
{
    // Check if a property in the user property store has changed.
    if (apoNotification->type == APO_NOTIFICATION_TYPE_AUDIO_SYSTEM_EFFECTS_PROPERTY_CHANGE
        && IsSameEndpointId(apoNotification->audioSystemEffectsPropertyChange.endpoint, m_device.get())
        && apoNotification->audioSystemEffectsPropertyChange.propertyStoreContext == m_propertyStoreContext
        && apoNotification->audioSystemEffectsPropertyChange.propertyStoreType == AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE_USER)
    {
        // Check if one of the properties that we are interested in has changed.
        // As an example, we check for "PKEY_Endpoint_Enable_Channel_Swap_SFX" which is a ficticious
        // PROPERTYKEY that could be set on our user property store.
        if (apoNotification->audioSystemEffectsPropertyChange.propertyKey ==
            PKEY_Endpoint_Enable_Channel_Swap_SFX)
        {
            wil::unique_prop_variant var;
            if (SUCCEEDED(apoNotification->audioSystemEffectsPropertyChange.propertyStore->GetValue(
                    PKEY_Endpoint_Enable_Channel_Swap_SFX, &var)) &&
                var.vt != VT_EMPTY)
            {
                // We have retrieved the property value. Now we can do something interesting with it.
            }
        }
    }
    else if (apoNotification->type == APO_NOTIFICATION_TYPE_ENDPOINT_PROPERTY_CHANGE
        
        && IsSameEndpointId(apoNotification->audioEndpointPropertyChange.endpoint, m_device.get())
    {
        // Handle changes to PROPERTYKEYs in the audio endpoint's own property store.
        // In this example, we are interested in a property called "PKEY_Endpoint_AllowOffloading" that the
        // user might change in the audio control panel, and we update our member variable if this
        // property changes.
        if (apoNotification->audioEndpointPropertyChange.propertyKey == PKEY_Endpoint_AllowOffloading)
        {
            wil::unique_prop_variant var;
            if (SUCCEEDED(propertyStore->GetValue(PKEY_Endpoint_AllowOffloading, &var)) && var.vt == VT_BOOL)
            {
                m_allowOffloading = var.boolVal;
            }
        }    
    }
    else if (apoNotification->type == APO_NOTIFICATION_TYPE_ENDPOINT_VOLUME
        
        && IsSameEndpointId(apoNotification->audioEndpointVolumeChange.endpoint, m_device.get())
    {
        // Handle endpoint volume change
        m_masterVolume = apoNotification->audioEndpointVolumeChange.volume->fMasterVolume;
        m_isMuted = apoNotification->audioEndpointVolumeChange.volume->bMuted;
    }
}
```

The following code is from the [Swap APO MFX sample - swapapomfx.cpp](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/SwapAPO/swapapomfx.cpp#L770-L794) and shows registering for events, by returning an array of APO_NOTIFICATION_DESCRIPTORs.

```cpp
HRESULT CSwapAPOMFX::GetApoNotificationRegistrationInfo(_Out_writes_(*count) APO_NOTIFICATION_DESCRIPTOR **apoNotifications, _Out_ DWORD *count)
{
    *apoNotifications = nullptr;
    *count = 0;

    RETURN_HR_IF_NULL(E_FAIL, m_device);

    // Let the OS know what notifications we are interested in by returning an array of
    // APO_NOTIFICATION_DESCRIPTORs.
    constexpr DWORD numDescriptors = 1;
    wil::unique_cotaskmem_ptr<APO_NOTIFICATION_DESCRIPTOR[]> apoNotificationDescriptors;

    apoNotificationDescriptors.reset(static_cast<APO_NOTIFICATION_DESCRIPTOR*>(
        CoTaskMemAlloc(sizeof(APO_NOTIFICATION_DESCRIPTOR) * numDescriptors)));
    RETURN_IF_NULL_ALLOC(apoNotificationDescriptors);

    // Our APO wants to get notified when a endpoint property changes on the audio endpoint.
    apoNotificationDescriptors[0].type = APO_NOTIFICATION_TYPE_ENDPOINT_PROPERTY_CHANGE;
    (void)m_device.query_to(&apoNotificationDescriptors[0].audioEndpointPropertyChange.device);

    *apoNotifications = apoNotificationDescriptors.release();
    *count = numDescriptors;

    return S_OK;
}
```

The following code is from the [SwapAPO MFX HandleNotifications sample - swapapomfx.cpp](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/SwapAPO/swapapomfx.cpp#L796-L827) and shows how to handle notifications. 

```cpp
void CSwapAPOMFX::HandleNotification(APO_NOTIFICATION *apoNotification)
{
    if (apoNotification->type == APO_NOTIFICATION_TYPE_ENDPOINT_PROPERTY_CHANGE)
    {
        // If either the master disable or our APO's enable properties changed...
        if (PK_EQUAL(apoNotification->audioEndpointPropertyChange.propertyKey, PKEY_Endpoint_Enable_Channel_Swap_MFX) ||
            PK_EQUAL(apoNotification->audioEndpointPropertyChange.propertyKey, PKEY_AudioEndpoint_Disable_SysFx))
        {
            struct KeyControl
            {
                PROPERTYKEY key;
                LONG* value;
            };

            KeyControl controls[] = {
                {PKEY_Endpoint_Enable_Channel_Swap_MFX, &m_fEnableSwapMFX},
            };

            m_apoLoggingService->ApoLog(APO_LOG_LEVEL_INFO, L"HandleNotification - pkey: " GUID_FORMAT_STRING L" %d", GUID_FORMAT_ARGS(apoNotification->audioEndpointPropertyChange.propertyKey.fmtid), apoNotification->audioEndpointPropertyChange.propertyKey.pid);

            for (int i = 0; i < ARRAYSIZE(controls); i++)
            {
                LONG fNewValue = true;

                // Get the state of whether channel swap MFX is enabled or not
                fNewValue = GetCurrentEffectsSetting(m_userStore.get(), controls[i].key, m_AudioProcessingMode);

                SetAudioSystemEffectState(m_effectInfos[i].id, fNewValue ? AUDIO_SYSTEMEFFECT_STATE_ON : AUDIO_SYSTEMEFFECT_STATE_OFF);
            }
        }
    }
}
```

## Logging Framework

The Logging framework provides APO developers with additional means of gathering data to improve development and debugging. This framework unifies the varying methods of logging used by different vendors and ties it to the audio trace logging providers to create more meaningful logging. The new framework provides a logging API, leaving the remainder of the work to be done by the OS.

The provider is defined as:

```
IMPLEMENT_TRACELOGGING_CLASS(ApoTelemetryProvider, "Microsoft.Windows.Audio.ApoTrace",
    // {8b4a0b51-5dcf-5a9c-2817-95d0ec876a87}
    (0x8b4a0b51, 0x5dcf, 0x5a9c, 0x28, 0x17, 0x95, 0xd0, 0xec, 0x87, 0x6a, 0x87));
``` 

Each APO has its own activity ID. Since this uses the existing trace logging mechanism, existing console tools can be used to filter for these events and display them in real-time.  You can use existing tools like tracelog and tracefmt as described in [Tools for Software Tracing - Windows drivers](../devtest/tools-for-software-tracing.md). For more information on trace sessions, see [Creating a Trace Session with a Control GUID](../devtest/creating-a-trace-session-with-a-control-guid.md).

The trace logging events are not marked as telemetry and will not be displayed as a telemetry provider in tools such as xperf.

### Implementation - Logging Framework

The logging framework is based on the logging mechanisms provided by ETW tracing. For more information about ETW, see [Event Tracing](/windows/win32/etw/event-tracing-portal). This is not meant for logging audio data, but rather to log events that are typically logged in production. Logging APIs should not be used from the real-time streaming thread as these have the potential to cause the pump thread to get pre-empted by the OS CPU scheduler. Logging should primarily be used for events that will help with debugging issues that are often found in the field.

### API definition - Logging Framework

The Logging framework introduces the [IAudioProcessingObjectLoggingService](/windows/win32/api/audioengineextensionapo/nn-audioengineextensionapo-iaudioprocessingobjectloggingservice) interface that provides a new logging service for APOs. 

For more information, see [IAudioProcessingObjectLoggingService](/windows/win32/api/audioengineextensionapo/nn-audioengineextensionapo-iaudioprocessingobjectloggingservice).

### Sample code - Logging Framework

The sample demonstrates the use of the method IAudioProcessingObjectLoggingService::ApoLog and how this interface pointer is obtained in IAudioProcessingObject::Initialize.

[AecApoMfx Logging Example](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/AecApo/AecApoMfx.cpp#L306-L310).



```cpp
class SampleApo : public winrt::implements<SampleApo, IAudioProcessingObject,
    IAudioSystemEffects, IAudioSystemEffects2, IAudioSystemEffects3>
{
private:
    wil::com_ptr_nothrow<IAudioProcessingObjectLoggingService> m_apoLoggingService;

public:
    // IAudioProcessingObject
    STDMETHOD(Initialize)(UINT32 cbDataSize, BYTE* pbyData);

    // Implementation of IAudioProcessingObject, IAudioSystemEffects2 andIAudioSystemEffects3 has been omitted for brevity.
};

// Implementation of IAudioProcessingObject::Initialize
STDMETHODIMP SampleApo::Initialize(UINT32 cbDataSize, BYTE* pbyData)
{
    if (cbDataSize == sizeof(APOInitSystemEffects3))
    {
        APOInitSystemEffects3* apoInitSystemEffects3 = reinterpret_cast<APOInitSystemEffects3*>(pbyData);

        // Try to get the logging service, but ignore errors as failure to do logging it is not fatal.
        (void)apoInitSystemEffects3->pServiceProvider->QueryService(SID_AudioProcessingObjectLoggingService, 
            __uuidof(IAudioProcessingObjectLoggingService), IID_PPV_ARGS(&m_apoLoggingService));
    }

    // Do other APO initialization work

    if (m_apoLoggingService != nullptr)
    {
        m_apoLoggingService->ApoLog(APO_LOG_LEVEL_INFO, L"APO Initializion completed");
    }
    return S_OK;
}
```

## Threading Framework

The threading framework enabling effects to be multithreaded by using work queues from an appropriate Multimedia Class Scheduler Service (MMCSS) task through a simple API. The creation of real-time serial work queues and their association with the main pump thread are handled by the OS. This framework allows APOs to queue short-running work items. Synchronization between tasks continues to be the responsibility of the APO. For more information about MMCSS threading, see [Multimedia Class Scheduler Service](/windows/win32/procthread/multimedia-class-scheduler-service) and [Real-Time Work Queue API](/windows/win32/procthread/platform-work-queue-api). 

### API definitions - Threading Framework

The Threading framework introduces the [IAudioProcessingObjectQueueService](/windows/win32/api/audioengineextensionapo/nn-audioengineextensionapo-iaudioprocessingobjectrtqueueservice) interface that provides access to the real time work queue for APOs. 

For more information, find additional content on the following pages:
-  [IAudioProcessingObjectQueueService](/windows/win32/api/audioengineextensionapo/nn-audioengineextensionapo-iaudioprocessingobjectrtqueueservice)


### Sample code - Threading Framework

This sample demonstrates the use of the method IAudioProcessingObjectRTQueueService::GetRealTimeWorkQueue and how the IAudioProcessingObjectRTQueueService interface pointer is obtained in IAudioProcessingObject::Initialize.

```cpp
#include <rtworkq.h>

class SampleApo3 :
    public winrt::implements<SampleApo3, IAudioProcessingObject, IAudioProcessingObjectConfiguration,
        IAudioSystemEffects, IAudioSystemEffects2, IAudioSystemEffects3>
{
private:
    DWORD m_queueId = 0;
    wil::com_ptr_nothrow<SampleApo3AsyncCallback> m_asyncCallback;

public:
    // IAudioProcessingObject
    STDMETHOD(Initialize)(UINT32 cbDataSize, BYTE* pbyData);

    // IAudioProcessingObjectConfiguration
    STDMETHOD(LockForProcess)(
        _In_ UINT32 u32NumInputConnections,
        _In_reads_(u32NumInputConnections) APO_CONNECTION_DESCRIPTOR** ppInputConnections,
        _In_ UINT32 u32NumOutputConnections,
        _In_reads_(u32NumOutputConnections) APO_CONNECTION_DESCRIPTOR** ppOutputConnections);

    // Non-interface methods called by the SampleApo3AsyncCallback helper class.
    HRESULT DoWorkOnRealTimeThread()
    {
        // Do the actual work here
        return S_OK;
    }
    void HandleWorkItemCompleted(_In_ IRtwqAsyncResult* asyncResult);

    // Implementation of IAudioProcessingObject, IAudioSystemEffects2, IAudioSystemEffects3   and IAudioProcessingObjectConfiguration is omitted
    // for brevity.
};

// Implementation of IAudioProcessingObject::Initialize
STDMETHODIMP SampleApo3::Initialize(UINT32 cbDataSize, BYTE* pbyData)
{
    if (cbDataSize == sizeof(APOInitSystemEffects3))
    {
        APOInitSystemEffects3* apoInitSystemEffects3 = reinterpret_cast<APOInitSystemEffects3*>(pbyData);

        wil::com_ptr_nothrow<IAudioProcessingObjectRTQueueService> apoRtQueueService;
        RETURN_IF_FAILED(apoInitSystemEffects3->pServiceProvider->QueryService(
            SID_AudioProcessingObjectRTQueue, IID_PPV_ARGS(&apoRtQueueService)));

        // Call the GetRealTimeWorkQueue to get the ID of a work queue that can be used for scheduling tasks
        // that need to run at a real-time priority. The work queue ID is used with the Rtwq APIs.
        RETURN_IF_FAILED(apoRtQueueService->GetRealTimeWorkQueue(&m_queueId));
    }

    // Do other initialization here
    return S_OK;
}

STDMETHODIMP SampleApo3::LockForProcess(
    _In_ UINT32 u32NumInputConnections,
    _In_reads_(u32NumInputConnections) APO_CONNECTION_DESCRIPTOR** ppInputConnections,
    _In_ UINT32 u32NumOutputConnections,
    _In_reads_(u32NumOutputConnections) APO_CONNECTION_DESCRIPTOR** ppOutputConnections)
{
    // Implementation details of LockForProcess omitted for brevity
    m_asyncCallback = winrt::make<SampleApo3AsyncCallback>(m_queueId).get();
    RETURN_IF_NULL_ALLOC(m_asyncCallback);

    wil::com_ptr_nothrow<IRtwqAsyncResult> asyncResult;	
    RETURN_IF_FAILED(RtwqCreateAsyncResult(this, m_asyncCallback.get(), nullptr, &asyncResult));

    RETURN_IF_FAILED(RtwqPutWorkItem(m_queueId, 0, asyncResult.get())); 
    return S_OK;
}

void SampleApo3::HandleWorkItemCompleted(_In_ IRtwqAsyncResult* asyncResult)
{
    // check the status of the result
    if (FAILED(asyncResult->GetStatus()))
    {
        // Handle failure
    }

    // Here the app could call RtwqPutWorkItem again with m_queueId if it has more work that needs to
    // execute on a real-time thread.
}


class SampleApo3AsyncCallback :
    public winrt::implements<SampleApo3AsyncCallback, IRtwqAsyncCallback>
{
private:
    DWORD m_queueId;

public:
    SampleApo3AsyncCallback(DWORD queueId) : m_queueId(queueId) {}

    // IRtwqAsyncCallback
    STDMETHOD(GetParameters)(_Out_ DWORD* pdwFlags, _Out_ DWORD* pdwQueue)
    {
        *pdwFlags = 0;
        *pdwQueue = m_queueId;
        return S_OK;
    }
    STDMETHOD(Invoke)(_In_ IRtwqAsyncResult* asyncResult);
};


STDMETHODIMP SampleApo3AsyncCallback::Invoke(_In_ IRtwqAsyncResult* asyncResult)
{
    // We are now executing on the real-time thread. Invoke the APO and let it execute the work.
    wil::com_ptr_nothrow<IUnknown> objectUnknown;
    RETURN_IF_FAILED(asyncResult->GetObject(objectUnknown.put_unknown()));

    wil::com_ptr_nothrow<SampleApo3> sampleApo3 = static_cast<SampleApo3*>(objectUnknown.get());
    HRESULT hr = sampleApo3->DoWorkOnRealTimeThread();
    RETURN_IF_FAILED(asyncResult->SetStatus(hr));

    sampleApo3->HandleWorkItemCompleted(asyncResult);
    return S_OK;
}
```

For more examples of how to utilize this interface, please see the following sample code:
- [SwapAPO SwapMFXApoAsyncCallback Class Definition - Example](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/SwapAPO/SwapAPO.h#L48-L75)
- [SwapAPO Invoke Function - Example](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/SwapAPO/swapapomfx.cpp#L124-L141)
- [SwapAPO Create Async Callback - Example](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/SwapAPO/swapapomfx.cpp#L347-L366)


## Audio Effects Discovery and Control for Effects

The discovery framework allows the OS to control audio effects on their stream. These APIs provide support for scenarios in which the user of an application needs to control certain effects on streams (e.g., deep noise suppression). To achieve this, this framework adds the following:

- A new API to query from an APO to determine whether an audio effect can be enabled or disabled.
- A new API to set the state of an audio effect to on/off.
- A notification when there is a change in the list of audio effects or when resources become available so that an audio effect can now be enabled/disabled.


### Implementation - Audio Effects Discovery

An APO needs to implement the [IAudioSystemEffects3](/windows/win32/api/audioengineextensionapo/nn-audioengineextensionapo-iaudiosystemeffects3) interface if it intends to expose effects that can be dynamically enabled and disabled. An APO exposes its audio effects through the [IAudioSystemEffects3::GetControllableSystemEffectsList](/windows/win32/api/audioengineextensionapo/nf-audioengineextensionapo-iaudiosystemeffects3-getcontrollablesystemeffectslist) function and enables and disables its audio effects through the [IAudioSystemEffects3::SetAudioSystemEffectState](/windows/win32/api/audioengineextensionapo/nf-audioengineextensionapo-iaudiosystemeffects3-setaudiosystemeffectstate) function.


### Sample code - Audio Effect Discovery

The Audio Effect Discovery sample code can be found within the [SwapAPOSFX sample - swapaposfx.cpp](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/SwapAPO/swapaposfx.cpp). 

The following sample code illustrates how to retrieve the list of configurable effects. [GetControllableSystemEffectsList sample - swapaposfx.cpp](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/SwapAPO/swapaposfx.cpp#L583-L625)

```cpp
HRESULT CSwapAPOSFX::GetControllableSystemEffectsList(_Outptr_result_buffer_maybenull_(*numEffects) AUDIO_SYSTEMEFFECT** effects, _Out_ UINT* numEffects, _In_opt_ HANDLE event)
{
    RETURN_HR_IF_NULL(E_POINTER, effects);
    RETURN_HR_IF_NULL(E_POINTER, numEffects);

    *effects = nullptr;
    *numEffects = 0;

    // Always close existing effects change event handle
    if (m_hEffectsChangedEvent != NULL)
    {
        CloseHandle(m_hEffectsChangedEvent);
        m_hEffectsChangedEvent = NULL;
    }

    // If an event handle was specified, save it here (duplicated to control lifetime)
    if (event != NULL)
    {
        if (!DuplicateHandle(GetCurrentProcess(), event, GetCurrentProcess(), &m_hEffectsChangedEvent, EVENT_MODIFY_STATE, FALSE, 0))
        {
            RETURN_IF_FAILED(HRESULT_FROM_WIN32(GetLastError()));
        }
    }

    if (!IsEqualGUID(m_AudioProcessingMode, AUDIO_SIGNALPROCESSINGMODE_RAW))
    {
        wil::unique_cotaskmem_array_ptr<AUDIO_SYSTEMEFFECT> audioEffects(
            static_cast<AUDIO_SYSTEMEFFECT*>(CoTaskMemAlloc(NUM_OF_EFFECTS * sizeof(AUDIO_SYSTEMEFFECT))), NUM_OF_EFFECTS);
        RETURN_IF_NULL_ALLOC(audioEffects.get());

        for (UINT i = 0; i < NUM_OF_EFFECTS; i++)
        {
            audioEffects[i].id = m_effectInfos[i].id;
            audioEffects[i].state = m_effectInfos[i].state;
            audioEffects[i].canSetState = m_effectInfos[i].canSetState;
        }

        *numEffects = (UINT)audioEffects.size();
        *effects = audioEffects.release();
    }

    return S_OK;
}
```

The following sample code illustrates how to enable and disable effects. [SetAudioSystemEffectState sample - swapaposfx.cpp](https://github.com/microsoft/Windows-driver-samples/blob/main/audio/sysvad/APO/SwapAPO/swapaposfx.cpp#L627-L653)

```cpp
HRESULT CSwapAPOSFX::SetAudioSystemEffectState(GUID effectId, AUDIO_SYSTEMEFFECT_STATE state)
{
    for (auto effectInfo : m_effectInfos)
    {
        if (effectId == effectInfo.id)
        {
            AUDIO_SYSTEMEFFECT_STATE oldState = effectInfo.state;
            effectInfo.state = state;

            // Synchronize access to the effects list and effects changed event
            m_EffectsLock.Enter();

            // If anything changed and a change event handle exists
            if (oldState != effectInfo.state)
            {
                SetEvent(m_hEffectsChangedEvent);
                m_apoLoggingService->ApoLog(APO_LOG_LEVEL_INFO, L"SetAudioSystemEffectState - effect: " GUID_FORMAT_STRING L", state: %i", effectInfo.id, effectInfo.state);
            }

            m_EffectsLock.Leave();
            
            return S_OK;
        }
    }

    return E_NOTFOUND;
}
```

## Reuse of the WM SFX and MFX APOs in Windows 11, version 22H2

Starting with Windows 11, version 22H2, the INF configuration files that that reuse the inbox WM SFX and MFX APOs, can now reuse the CAPX SFX and MFX APOs. This section describes the three ways to do this.

There are three insertion points for APOs: pre-mix render, post-mix render, and capture. Each logical device's audio engine supports one instance of a pre-mix render APO per stream (render SFX) and one post-mix render APO (MFX). The audio engine also supports one instance of a capture APO (capture SFX) that is inserted in each capture stream. For more information on how to reuse or wrap the inbox APOs, see [Combine custom and Windows APOs](combine-custom-and-windows-apos.md).

The CAPX SFX and MFX APOs can be reused in one of the following three ways. 

### Using INF DDInstall Section

Use mssysfx.CopyFilesAndRegisterCapX from wdmaudio.inf by adding the following entries.

```inf
   Include=wdmaudio.inf
   Needs=mssysfx.CopyFilesAndRegisterCapX
```

### Using an extension INF file

The wdmaudioapo.inf is the AudioProcessingObject class extension inf. It contains the device-specific registration of the SFX and MFX APOs. 

### Directly referencing the WM SFX and MFX APOs for stream and mode effects

To directly reference these APOs for stream and mode effects, use the following GUID values.

- Use `{C9453E73-8C5C-4463-9984-AF8BAB2F5447}` as the WM SFX APO 
- Use `{13AB3EBD-137E-4903-9D89-60BE8277FD17}` as the WM MFX APO.

SFX (Stream) and MFX (Mode) were referred in Windows 8.1 to LFX (local) and MFX was referred to as GFX (global). These registry entries continue to use the previous names.

Device-specific registration uses HKR instead of HKCR.
   
The INF file  will need to have the following enties added.

```inf
  HKR,"FX\\0\\%WMALFXGFXAPO_Context%",%PKEY_FX_Association%,,%KSNODETYPE_ANY%
  HKR,"FX\\0\\%WMALFXGFXAPO_Context%\\User",,,
  WMALFXGFXAPO_Context = "{B13412EE-07AF-4C57-B08B-E327F8DB085B}"
```

These INF file entries will create a property store that will be used by the Windows 11 APIs for the new APOs.

PKEY_FX_Association in the INF ex. `HKR,"FX\\0",%PKEY_FX_Association%,,%KSNODETYPE_ANY%`, should be replaced with `HKR,"FX\\0\\%WMALFXGFXAPO_Context%",%PKEY_FX_Association%,,%KSNODETYPE_ANY%`.

## See also

[Windows Audio Processing Objects](windows-audio-processing-objects.md).