---
title: Implementing Audio Processing Objects
description: This topic describes how to implement an audio processing object (APO). For general information about APOs, see Audio Processing Object Architecture.
ms.date: 06/11/2021
ms.localizationpriority: medium
---

# Implementing Audio Processing Objects

This topic describes how to implement an audio processing object (APO). For general information about APOs, see [Audio Processing Object Architecture](audio-processing-object-architecture.md).

## Implementing Custom APOs

Custom APOs are implemented as in-process COM objects, so they run in user mode and are packaged in a dynamic-link library (DLL). There are three types of APO, based on where they are inserted in the signal processing graph.

- Stream effects (SFX)
- Mode effects (MFX)
- Endpoint effects (EFX)

Each logical device can be associated with one APO of each type. For more information on modes and effects, see [Audio Signal Processing Modes](audio-signal-processing-modes.md).

You can implement an APO by basing your custom class on the CBaseAudioProcessingObject base class, which is declared in the Baseaudioprocessingobject.h file. This approach involves adding new functionality into the CBaseAudioProcessingObject base class to create a customized APO. The CBaseAudioProcessingObject base class implements much of the functionality that an APO requires. It provides default implementations for most of the methods in the three required interfaces. The primary exception is the [**IAudioProcessingObjectRT::APOProcess**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-apoprocess) method.

Perform the following steps to implement your custom APOs.

1. Create custom APO com objects to provide the desired audio processing.
2. Optionally create a user interface for configuring the custom APOs using a.
3. Create an INF file to install and register the APOs and the custom user interface.

## Design Considerations for Custom APO Development

All custom APOs must have the following general characteristics:

- The APO must have one input and one output connection. These connections are audio buffers and can have multiple channels.
- An APO can modify only the audio data that is passed to it through its [**IAudioProcessingObjectRT::APOProcess**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-apoprocess) routine. The APO cannot change the settings of the underlying logical device, including its KS topology.
- In addition to IUnknown, APOs must expose the following interfaces:

  - [IAudioProcessingObject](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iaudioprocessingobject). An interface that handles setup tasks such as initialization and format negotiation.

  - [IAudioProcessingObjectConfiguration](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iaudioprocessingobjectconfiguration). The configuration interface.

  - [IAudioProcessingObjectRT](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iaudioprocessingobjectrt). A real-time interface that handles audio processing. It can be called from a real-time processing thread.

  - [IAudioSystemEffects](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iaudiosystemeffects). The interface that makes the audio engine recognize a DLL as a systems effects APO.

- All APOs must have real-time system compatibility. This means that:

  - All methods that are members of real-time interfaces must be implemented as nonblocking members. They must not block, use paged memory, or call any blocking system routines.

  - All buffers that are processed by the APO must be nonpageable. All code and data in the process path must be nonpageable.

  - APOs should not introduce significant latency into the audio processing chain.

- Custom APOs must not expose the IAudioProcessingObjectVBR interface.

>[!NOTE]
>For detailed information about the required interfaces, see the Audioenginebaseapo.h and Audioenginebaseapo.idl files in the Windows Kits\\&lt;build number&gt;\\Include\\um folder.

## Using Sample Code to Accelerate the Development Process

Using the SYSVAD Swap APO code sample as a template can accelerate the custom APO development process. The Swap sample is the sample that was developed to illustrate some features of audio processing objects. The Swap APO sample swaps the left channel with the right channel and implements both SFX and MFX effects. You can enable and disable the channel swap audio effects using the properties dialog.

The SYSVAD audio sample is available on the [Windows Driver Samples GitHub](https://github.com/Microsoft/Windows-driver-samples).

You can browse the Sysvad audio sample here:

<https://github.com/Microsoft/Windows-driver-samples/tree/master/audio/sysvad>

### Download and extract the Sysvad audio sample from GitHub

Follow these steps to download and open the SYSVAD sample.

a. You can use GitHub tools to work with the samples. You can also download the universal driver samples in one zip file.

<https://github.com/Microsoft/Windows-driver-samples/archive/master.zip>

b. Download the master.zip file to your local hard drive.

c. Selecct and hold (or right-click) *Windows-driver-samples-master.zip*, and choose **Extract All**. Specify a new folder, or browse to an existing one that will store the extracted files. For example, you could specify *C:\\DriverSamples\\* as the new folder into which the files will be extracted.

d. After the files are extracted, navigate to the following subfolder: *C:\\DriverSamples\\Audio\\Sysvad*

### Open the driver solution in Visual Studio

In Microsoft Visual Studio, Select **File** &gt; **Open** &gt; **Project/Solution...** and navigate to the folder that contains the extracted files (for example, *C:\\DriverSamples\\Audio\\Sysvad*). Double-click the *Sysvad* solution file to open it.

In Visual Studio locate the Solution Explorer. (If this is not already open, choose **Solution Explorer** from the **View** menu.) In Solution Explorer, you can see one solution that has six projects.

### SwapAPO Example Code

There are five projects in the SYSVAD sample, one of which is of primary interest to the APO developer.

|**Project**|**Description**|
|----|----|
|SwapAPO|Sample code for an example APO|

The other projects in the Sysvad sample are summarized below.

|**Project**|**Description**|
|----|----|
| TabletAudioSample      | Sample code for an alternate audio driver. |
| KeywordDetectorAdapter | Sample code for a keyword detector adapter |
| EndpointsCommon        | Sample code for common endpoints.          |

The primary header files for the SwapAPO sample is swapapo.h. The other primary code elements are summarized below.

|**File**|**Description**|
|----|----|
| Swap.cpp             | C++ code that contains the implementation of the Swap APO.        |
| SwapAPOMFX.cpp       | Implementation of CSwapAPOMFX                                     |
| SwapAPOSFX.cpp       | Implementation of CSwapAPOSFX                                     |
| SwapAPODll.cpp       | Implementation of DLL Exports.                                    |
| SwapAPODll.idl       | Definition of COM interfaces and coclasses for the DLL.           |
| SwapAPOInterface.idl | The interface and type definitions for Swap APO functionality.    |
| swapapodll.def       | COM exports definitions                                           |

## Implementing the COM Object Audio Processing Code

You can wrap a system-supplied APO by basing your custom class on the **CBaseAudioProcessingObject** base class, which is declared in the Baseaudioprocessingobject.h file. This approach involves introducing new functionality into the **CBaseAudioProcessingObject** base class to create a customized APO. The **CBaseAudioProcessingObject** base class implements much of the functionality that an APO requires. It provides default implementations for most of the methods in the three required interfaces. The primary exception is the [**IAudioProcessingObjectRT::APOProcess**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-apoprocess) method.

By using **CBaseAudioProcessingObject**, you can more easily implement an APO. If an APO has no special format requirements and operates on the required float32 format, the default implementations of the interface methods that are included in **CBaseAudioProcessingObject** should be sufficient. Given the default implementations, only three main methods must be implemented: [**IAudioProcessingObject::IsInputFormatSupported**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-isinputformatsupported), [**IAudioProcessingObjectRT::APOProcess**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-apoprocess), and **ValidateAndCacheConnectionInfo**.

To develop your APOs based on the **CBaseAudioProcessingObject** class, perform the following steps:

1. Create a class that inherits from **CBaseAudioProcessingObject**.

    The following C++ code example shows the creation of a class that inherits from **CBaseAudioProcessingObject**. For an actual implementation of this concept, follow instructions in the **Audio Processing Objects Driver Sample** section to go to the Swap sample, and then refer to the *Swapapo.h* file.

    ```cpp
    // Custom APO class - LFX
    Class MyCustomAPOLFX: public CBaseAudioProcessingObject
    {
     public:
    //Code for custom class goes here
    ...
    };
    ```

    **Note**   Because the signal processing that is performed by an SFX APO is different from the signal processing that is performed by an MFX or an EFX APO, you must create separate classes for each.

2. Implement the following three methods:

    - [**IAudioProcessingObject::IsInputFormatSupported**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-isinputformatsupported). This method handles format negotiation with the audio engine.

    - [**IAudioProcessingObjectRT::APOProcess**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-apoprocess). This method uses your custom algorithm to perform signal processing.

    - **ValidateAndCacheConnectionInfo**. This method allocates memory to store format details, for example, channel count, sampling rate, sample depth, and channel mask.

The following C++ code example shows an implementation of the [**APOProcess**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-apoprocess) method for the sample class that you created in step 1. For an actual implementation of this concept, follow instructions in the **Audio Processing Objects Driver Sample** section to go to the Swap sample, and then refer to the *Swapapolfx.cpp* file.

```cpp
// Custom implementation of APOProcess method
STDMETHODIMP_ (Void) MyCustomAPOLFX::APOProcess (...)
{
// Code for method goes here. This code is the algorithm that actually
// processes the digital audio signal.
...
}
```

The following code example shows an implementation of the **ValidateAndCacheConnectionInfo** method. For an actual implementation of this method, follow instructions in the **Audio Processing Objects Driver Sample** section to go to the Swap sample, and then refer to the *Swapapogfx.cpp* file.

```cpp
// Custom implementation of the ValidateAndCacheConnectionInfo method.
HRESULT CSwapAPOGFX::ValidateAndCacheConnectionInfo( ... )
{
// Code for method goes here.
// The code should validate the input/output format pair.
...
}
```

**Note**  The remaining interfaces and methods that your class inherits from **CBaseAudioProcessingObject** are described in detail in the Audioenginebaseapo.idl file.

## Replacing System-supplied APOs

When implementing the APO interfaces, there are two approaches: you can write your own implementation, or you can call into the inbox APOs.

This pseudocode illustrates wrapping a system APO.

```cpp
CMyWrapperAPO::CMyWrapperAPO {
    CoCreateInstance(CLSID_InboxAPO, m_inbox);
}

CMyWrapperAPO::IsInputFormatSupported {
    Return m_inbox->IsInputFormatSupported(…);
}
```

This pseudocode illustrates creating your own custom APO.

```cpp
CMyFromScratchAPO::IsInputFormatSupported {
    my custom logic
}
```

When you develop your APOs to replace the system-supplied ones, you must use the same names in the following list, for the interfaces and methods. Some of the interfaces have more methods in addition to the listed required methods. See the reference pages for those interfaces to determine if you want to implement all the methods or only the required ones.

The rest of the implementation steps are the same as a custom APO.

Implement the following interfaces and methods for the COM component:

- [IAudioProcessingObject](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iaudioprocessingobject). The required methods for this interface are: [**Initialize**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-initialize) and [**IsInputFormatSupported.**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-isinputformatsupported)
- [IAudioProcessingObjectConfiguration](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iaudioprocessingobjectconfiguration). The required methods for this interface are: [**LockForProcess**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectconfiguration-lockforprocess) and [**UnlockForProcess**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectconfiguration-unlockforprocess)
- [IAudioProcessingObjectRT](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iaudioprocessingobjectrt). The required method for this interface is [**APOProcess**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-apoprocess) and it is the method that implements the DSP algorithm.
- [IAudioSystemEffects](/windows/win32/api/audioenginebaseapo/nn-audioenginebaseapo-iaudiosystemeffects). This interface makes the audio engine recognize a DLL as an APO.

## Working with Visual Studio and APOs

When working with APOs in Visual Studio, perform these tasks for each APO project.

### Link to the CRT

Drivers that are targeting Windows 10 should dynamically link against the universal CRT.

If you need to support Windows 8,1, enable static linking by setting the project properties in C/C++, Code Generation. Set "Runtime Library" to */MT* for release builds or */MTd* for debug builds. This change is made, because for a driver it is difficult to redistribute the MSVCRT&lt;n&gt;.dll binary. The solution is to statically link libcmt.dll. For more information see [/MD, /MT, /LD (Use Run-Time Library)](/cpp/build/reference/md-mt-ld-use-run-time-library) .

### Disable Use of an Embedded Manifest

Disable Use of an Embedded Manifest by setting project properties for your APO project. Select **Manifest Tool**, **Input and Output**. Then change "Embed Manifest" from the default of *Yes* to *No*. If you have an embedded manifest, this triggers the use of certain APIs which are forbidden within a protected environment. This means that your APO will run with DisableProtectedAudioDG=1, but when this test key is removed, your APO will fail to load, even if it is WHQL-signed.

## Packaging your APO with a Driver

When you develop your own audio driver and wrap or replace the system-supplied APOs, you must provide a driver package for installing the driver and APOs. For Windows 10, please see [Universal Windows Drivers for Audio](audio-universal-drivers.md). Your audio related driver packages should follow the policies and packaging model detailed there.  

The custom APO is packaged as a DLL, and any configuration UI is packaged as a separate UWP or Desktop Bridge app. The APO device INF copies the DLLs to the system folders that are indicated in the associated INF CopyFile directive. The DLL that contains the APOs must register itself by including an AddReg section in the INF file.

The following paragraphs and INF file fragments show the modifications that are necessary to use the standard INF file to copy and register APOs.

The inf files included with the Sysvad sample illustrate how the SwapApo.dll APOs are registered.

## Registering APOs for Processing Modes and Effects in the INF File

You can register APOs for specific modes using certain allowable combinations of registry keys. For more information on which effects are available and general information about APOs, see [Audio Processing Object Architecture](audio-processing-object-architecture.md).

Refer to these reference topics for information on each of the APO INF file settings.

[PKEY\_FX\_StreamEffectClsid](./pkey-fx-streameffectclsid.md)

[PKEY\_FX\_ModeEffectClsid](./pkey-fx-modeeffectclsid.md)

[PKEY\_FX\_EndpointEffectClsid](./pkey-fx-endpointeffectclsid.md)

[PKEY\_SFX\_ProcessingModes\_Supported\_For\_Streaming](./pkey-sfx-processingmodes-supported-for-streaming.md)

[PKEY\_MFX\_ProcessingModes\_Supported\_For\_Streaming](./pkey-mfx-processingmodes-supported-for-streaming.md)

[PKEY\_EFX\_ProcessingModes\_Supported\_For\_Streaming](./pkey-efx-processingmodes-supported-for-streaming.md)

The following INF file samples show how to register audio processing objects (APOs) for specific modes. They illustrate the possible combinations available from this list.

- PKEY\_FX\_StreamEffectClsid with PKEY\_SFX\_ProcessingModes\_Supported\_For\_Streaming
- PKEY\_FX\_ModeEffectClsid with PKEY\_MFX\_ProcessingModes\_Suppoted\_For\_Streaming
- PKEY\_FX\_ModeEffectClsid without PKEY\_MFX\_ProcessingModes\_Suppoted\_For\_Streaming
- PKEY\_FX\_EndpointEffectClsid without PKEY\_EFX\_ProcessingModes\_Supported\_For\_Streaming

There is one additional valid combination that is not shown in these samples.

- PKEY\_FX\_EndpointEffectClsid with PKEY\_EFX\_ProcessingModes\_Supported\_For\_Streaming

### SYSVAD Tablet Multi-Mode Streaming Effect APO INF Sample

This sample shows a multi-mode streaming effect being registered using AddReg entries in the SYSVAD Tablet INF file.

This sample code is from the SYSVAD audio sample and is available on GitHub: <https://github.com/Microsoft/Windows-driver-samples/tree/master/audio/sysvad>.

This sample illustrates this combination of system effects:

- PKEY\_FX\_StreamEffectClsid with PKEY\_SFX\_ProcessingModes\_Supported\_For\_Streaming
- PKEY\_FX\_ModeEffectClsid with PKEY\_MFX\_ProcessingModes\_Suppoted\_For\_Streaming

```inf
[SWAPAPO.I.Association0.AddReg]
; Instruct audio endpoint builder to set CLSID for property page provider into the
; endpoint property store
HKR,EP\0,%PKEY_AudioEndpoint_ControlPanelPageProvider%,,%AUDIOENDPOINT_EXT_UI_CLSID%

; Instruct audio endpoint builder to set the CLSIDs for stream, mode, and endpoint APOs
; into the effects property store
HKR,FX\0,%PKEY_FX_StreamEffectClsid%,,%FX_STREAM_CLSID%
HKR,FX\0,%PKEY_FX_ModeEffectClsid%,,%FX_MODE_CLSID%
HKR,FX\0,%PKEY_FX_UserInterfaceClsid%,,%FX_UI_CLSID%

; Driver developer would replace the list of supported processing modes here
; Concatenate GUIDs for DEFAULT, MEDIA, MOVIE
HKR,FX\0,%PKEY_SFX_ProcessingModes_Supported_For_Streaming%,%REG_MULTI_SZ%,%AUDIO_SIGNALPROCESSINGMODE_DEFAULT%,%AUDIO_SIGNALPROCESSINGMODE_MEDIA%,%AUDIO_SIGNALPROCESSINGMODE_MOVIE%

; Concatenate GUIDs for DEFAULT, MEDIA, MOVIE
HKR,FX\0,%PKEY_MFX_ProcessingModes_Supported_For_Streaming%,%REG_MULTI_SZ%,%AUDIO_SIGNALPROCESSINGMODE_DEFAULT%,%AUDIO_SIGNALPROCESSINGMODE_MEDIA%,%AUDIO_SIGNALPROCESSINGMODE_MOVIE%

;HKR,FX\0,%PKEY_EFX_ProcessingModes_Supported_For_Streaming%,0x00010000,%AUDIO_SIGNALPROCESSINGMODE_DEFAULT%
```

Note that in the sample INF file, the EFX\_Streaming property is commented out because the audio processing has transitioned to kernel mode above that layer, so that streaming property is not necessary and would not be used. It would be valid to specify a PKEY\_FX\_EndpointEffectClsid for discovery purposes, but it would be an error to specify PKEY\_EFX\_ProcessingModes\_Supported\_For\_Streaming. This is because the mode mix / tee happens lower in the stack, where it is not possible to insert an endpoint APO.

### Componentized APO Installation

Starting with Windows 10, release 1809, APO registration with the audio engine uses the componentized audio driver model. Using audio componentization creates a smoother and more reliable install experience and better supports component servicing. For more information, see [Creating a componentized audio driver installation](./audio-universal-drivers.md#creating-a-componentized-audio-driver-installation).

The following example code is extracted from the public ComponentizedAudioSampleExtension.inf and ComponentizedApoSample.inf. Refer to the SYSVAD audio sample which is available on GitHub here: <https://github.com/Microsoft/Windows-driver-samples/tree/master/audio/sysvad>.

The registration of the APO with the audio engine is done using a newly created APO device. For the audio engine to make use of the new APO device it must be a PNP child of the audio device, sibling of the audio endpoints. The new componentized APO design does not allow for an APO to be registered globally and used by multiple different drivers. Each driver must register its own APO's.

The installation of the APO is done in two parts. First, the driver extension INF will add an APO component to the system:

```inf
[DeviceExtension_Install.Components]
AddComponent = SwapApo,,Apo_AddComponent

[Apo_AddComponent]
ComponentIDs = VEN_SMPL&CID_APO
Description = "Audio Proxy APO Sample"
```

This APO component triggers the second part, the installation of the APO INF, in the SYSVAD sample this is done in ComponentizedApoSample.inf. This INF file is dedicated to the APO component. It specifies the component class as AudioProcessingObject and adds all of the APO properties for CLSID registration and registering with the audio engine.

>[!NOTE]
> The INF file samples shown support driver package isolation by using in most cases the HKR registry key. Earlier samples used the HKCR to store persistent values. The exception is that registration of Component Object Model (COM) objects, a key may be written under HKCR.
 For more information, see [Using a Universal INF File](../install/using-a-universal-inf-file.md).

```inf
[Version]
Signature   = "$WINDOWS NT$"
Class       = AudioProcessingObject
ClassGuid   = {5989fce8-9cd0-467d-8a6a-5419e31529d4}

[ApoComponents.NT$ARCH$]
%Apo.ComponentDesc% = ApoComponent_Install,APO\VEN_SMPL&CID_APO

[Apo_AddReg]
; CLSID registration
HKCR,CLSID\%SWAP_FX_STREAM_CLSID%,,,%SFX_FriendlyName%
HKCR,CLSID\%SWAP_FX_STREAM_CLSID%\InProcServer32,,0x00020000,%%SystemRoot%%\System32\swapapo.dll
HKCR,CLSID\%SWAP_FX_STREAM_CLSID%\InProcServer32,ThreadingModel,,"Both"
…
;Audio engine registration
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"FriendlyName",,%SFX_FriendlyName%
...
```

When this INF installs the componentized APO, on a desktop system "Audio Processing Objects" will be shown in Windows Device Manager.

### Bluetooth Audio Sample APO INF Sample

This sample illustrates this combination of system effects:

- PKEY\_FX\_StreamEffectClsid with PKEY\_SFX\_ProcessingModes\_Supported\_For\_Streaming

- PKEY\_FX\_ModeEffectClsid with PKEY\_MFX\_ProcessingModes\_Suppoted\_For\_Streaming

This sample code supports Bluetooth hands-free and stereo devices.

```inf
; wdma_bt.inf – example usage
...
[BthA2DP]
Include=ks.inf, wdmaudio.inf, BtaMpm.inf
Needs=KS.Registration,WDMAUDIO.Registration,BtaMPM.CopyFilesOnly,mssysfx.CopyFilesAndRegister
...
[BTAudio.SysFx.Render]
HKR,"FX\\0",%PKEY_ItemNameDisplay%,,%FX_FriendlyName%
HKR,"FX\\0",%PKEY_FX_StreamEffectClsid%,,%FX_STREAM_CLSID%
HKR,"FX\\0",%PKEY_FX_ModeEffectClsid%,,%FX_MODE_CLSID%
HKR,"FX\\0",%PKEY_FX_UiClsid%,,%FX_UI_CLSID%
HKR,"FX\\0",%PKEY_FX_Association%,,%KSNODETYPE_ANY%
HKR,"FX\\0",%PKEY_SFX_ProcessingModes_Supported_For_Streaming%,0x00010000,%AUDIO_SIGNALPROCESSINGMODE_DEFAULT%
HKR,"FX\\0",%PKEY_MFX_ProcessingModes_Supported_For_Streaming%,0x00010000,%AUDIO_SIGNALPROCESSINGMODE_DEFAULT%
...
[Strings]
FX_UI_CLSID      = "{5860E1C5-F95C-4a7a-8EC8-8AEF24F379A1}"
FX_STREAM_CLSID  = "{62dc1a93-ae24-464c-a43e-452f824c4250}"
PKEY_FX_StreamEffectClsid   = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},5"
PKEY_FX_ModeEffectClsid     = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},6"
PKEY_SFX_ProcessingModes_Supported_For_Streaming = "{D3993A3F-99C2-4402-B5EC-A92A0367664B},5"
PKEY_MFX_ProcessingModes_Supported_For_Streaming = "{D3993A3F-99C2-4402-B5EC-A92A0367664B},6"
AUDIO_SIGNALPROCESSINGMODE_DEFAULT = "{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}"
```

### APO INF Audio Sample

This sample INF file illustrates the following combination of system effects:

- PKEY\_FX\_StreamEffectClsid with PKEY\_SFX\_ProcessingModes\_Supported\_For\_Streaming

- PKEY\_FX\_ModeEffectClsid with PKEY\_MFX\_ProcessingModes\_Suppoted\_For\_Streaming

- PKEY\_FX\_EndpointEffectClsid without PKEY\_EFX\_ProcessingModes\_Supported\_For\_Streaming

```inf
[MyDevice.Interfaces]
AddInterface=%KSCATEGORY_AUDIO%,%MyFilterName%,MyAudioInterface

[MyAudioInterface]
AddReg=MyAudioInterface.AddReg

[MyAudioInterface.AddReg]
;To register an APO for discovery, use the following property keys in the .inf (or at runtime when registering the KSCATEGORY_AUDIO device interface):
HKR,"FX\\0",%PKEY_FX_StreamEffectClsid%,,%FX_STREAM_CLSID%
HKR,"FX\\0",%PKEY_FX_ModeEffectClsid%,,%FX_MODE_CLSID%
HKR,"FX\\0",%PKEY_FX_EndpointEffectClsid%,,%FX_MODE_CLSID%

;To register an APO for streaming and discovery, add the following property keys as well (to the same section):
HKR,"FX\\0",%PKEY_SFX_ProcessingModes_For_Streaming%,%REG_MULTI_SZ%,%AUDIO_SIGNALPROCESSINGMODE_DEFAULT%,%AUDIO_SIGNALPROCESSINGMODE_MOVIE%,%AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS%

;To register an APO for streaming in multiple modes, use a REG_MULTI_SZ property and include all the modes:
HKR,"FX\\0",%PKEY_MFX_ProcessingModes_For_Streaming%,%REG_MULTI_SZ%,%AUDIO_SIGNALPROCESSINGMODE_DEFAULT%,%AUDIO_SIGNALPROCESSINGMODE_MOVIE%,%AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS%
```

### Define a custom APO and CLSID APO INF Sample

This sample shows how to define your own CLSID for a custom APO. This sample uses the MsApoFxProxy CLSID {889C03C8-ABAD-4004-BF0A-BC7BB825E166}. CoCreate-ing this GUID instantiates a class in MsApoFxProxy.dll which implements the IAudioProcessingObject interfaces and queries the underlying driver via the KSPROPSETID\_AudioEffectsDiscovery property set.

This INF file sample shows the \[BthHfAud\] section, which pulls in \[MsApoFxProxy.Registration\] from wdmaudio.inf \[BthHfAud.AnlgACapture.AddReg.Wave\], which then registers PKEY\_FX\_EndpointEffectClsid as the well-known CLSID for MsApoFxProxy.dll.

This INF file sample also illustrates the use of this combination of system effects:

- PKEY\_FX\_EndpointEffectClsid without PKEY\_EFX\_ProcessingModes\_Supported\_For\_Streaming

```inf
;wdma_bt.inf
[BthHfAud]
Include=ks.inf, wdmaudio.inf, BtaMpm.inf
Needs=KS.Registration, WDMAUDIO.Registration, BtaMPM.CopyFilesOnly, MsApoFxProxy.Registration
CopyFiles=BthHfAud.CopyList
AddReg=BthHfAud.AddReg

; Called by needs entry in oem inf
[BthHfAudOEM.CopyFiles]
CopyFiles=BthHfAud.CopyList

[BthHfAud.AnlgACapture.AddReg.Wave]
HKR,,CLSID,,%KSProxy.CLSID%
HKR,"FX\\0",%PKEY_FX_Association%,,%KSNODETYPE_ANY%
HKR,"FX\\0",%PKEY_FX_EndpointEffectClsid%,,%FX_DISCOVER_EFFECTS_APO_CLSID%
#endif
```

### Sample APO Effect Registration

This sample shows the \[Apo_AddReg\] section from the Sysvad ComponentizedApoSample.inx. This section registers the swap stream GUID with COM and registers the Swap Stream APO effect. The \[Apo_CopyFiles\] section copies the swapapo.dll into C:\\Windows\\system32.

```inf
; ComponentizedApoSample.inx

...

[ApoComponent_Install]
CopyFiles = Apo_CopyFiles
AddReg    = Apo_AddReg

[Apo_CopyFiles]
swapapo.dll

...

[Apo_AddReg]
; Swap Stream effect APO COM registration
HKCR,CLSID\%SWAP_FX_STREAM_CLSID%,,,%SFX_FriendlyName%
HKCR,CLSID\%SWAP_FX_STREAM_CLSID%\InProcServer32,,0x00020000,%13%\swapapo.dll
HKCR,CLSID\%SWAP_FX_STREAM_CLSID%\InProcServer32,ThreadingModel,,"Both"

'''
; Swap Stream effect APO registration
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"FriendlyName",,%SFX_FriendlyName%
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"Copyright",,%Copyright%
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"MajorVersion",0x00010001,1
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"MinorVersion",0x00010001,1
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"Flags",0x00010001,%APO_FLAG_DEFAULT%
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"MinInputConnections",0x00010001,1
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"MaxInputConnections",0x00010001,1
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"MinOutputConnections",0x00010001,1
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"MaxOutputConnections",0x00010001,1
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"MaxInstances",0x00010001,0xffffffff
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"NumAPOInterfaces",0x00010001,1
HKR,AudioEngine\AudioProcessingObjects\%SWAP_FX_STREAM_CLSID%,"APOInterface0",,"{FD7F2B29-24D0-4B5C-B177-592C39F9CA10}"
...

[Strings]
; Driver developers would replace these CLSIDs with those of their own APOs
SWAP_FX_STREAM_CLSID   = "{B48DEA3F-D962-425a-8D9A-9A5BB37A9904}"

...
```

## APO Registration

APO registration is used to support a process that dynamically matches the effects to endpoints using a weighted calculation. The weighted calculation uses the following property stores. Every audio interface has zero or more *endpoint property stores* and *effects property stores* registered either via the .inf or at runtime. The most specific endpoint property store and the most specific effects property store have the highest weights and are used. All other property stores are ignored.

Specificity is calculated as follows:

Endpoint property stores weighting

1. FX with specific KSNODETYPE
2. FX with KSNODETYPE\_ANY
3. MSFX with specific KSNODETYPE
4. MSFX with KSNODETYPE\_ANY

Effects property stores weighting

1. EP with specific KSNODETYPE
2. EP with KSNODETYPE\_ANY
3. MSEP with specific KSNODETYPE
4. MSEP with KSNODETYPE\_ANY

Numbers must start at 0 and increase sequentially: MSEP\\0, MSEP\\1, …, MSEP\\n If (for example) EP\\3 is missing, Windows will stop looking for EP\\n and will not see EP\\4, even if it exists

The value of PKEY\_FX\_Association (for effects property stores) or PKEY\_EP\_Association (for endpoint property stores) is compared against the KSPINDESCRIPTOR.Category value for the pin factory at the hardware end of the signal path, as exposed by Kernel Streaming.

Only Microsoft inbox class drivers (which can be wrapped by a third-party developer) should use MSEP and MSFX; all third-party drivers should use EP and FX.

### APO Node Type Compatibility

The following INF file sample illustrates setting the PKEY\_FX\_Association key to a GUID associated with the APO.

```inf
;; Property Keys
PKEY_FX_Association = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},0"
"
```

```inf
;; Key value pairs
HKR,"FX\\0",%PKEY_FX_Association%,,%KSNODETYPE_ANY%
```

Because an audio adapter is capable of supporting multiple inputs and outputs, you must explicitly indicate the type of kernel streaming (KS) node type that your custom APO is compatible with. In the preceding INF file fragment, the APO is shown to be associated with a KS node type of %KSNODETYPE\_ANY%. Later in this INF file, KSNODETYPE\_ANY is defined as follows:

```inf
[Strings]
;; Define the strings used in MyINF.inf
...
KSNODETYPE_ANY      = "{00000000-0000-0000-0000-000000000000}"
KSNODETYPE_SPEAKER  = "{DFF21CE1-F70F-11D0-B917-00A0C9223196}"
...
```

A value of **NULL** for KSNODETYPE\_ANY means that this APO is compatible with any type of KS node type. To indicate, for example, that your APO is only compatible with a KS node type of KSNODETYPE\_SPEAKER, the INF file would show the KS node type and APO association as follows:

```inf
;; Key value pairs
...
HKR,"FX\\0",%PKEY_FX_Association%,,%KSNODETYPE_SPEAKER%
...
```

For more information about the GUID values for the different KS node types, see the Ksmedia.h header file.

## Troubleshooting APO Load Failures

The following information is provided to help you understand how failure is monitored for APOs. You can use this information to troubleshoot APOs that fail to get incorporated into the audio graph.

The audio system monitors APO return codes to determine whether APOs are being successfully incorporated into the graph. It monitors the return codes by tracking the HRESULT values that are returned by any one of the designated methods. The system maintains a separate failure count value for each SFX, MFX and EFX APO that is being incorporated into the graph.

The audio system monitors the returned HRESULT values from the following four methods.

- CoCreateInstance

- IsInputFormatSupported

- IsOutputFormatSupported

- LockForProcess

The failure count value is incremented for an APO every time one of these methods returns a failure code. The failure count is reset to zero when an APO returns a code that indicates that it was successfully incorporated into the audio graph. A successful call to the [**LockForProcess**](/windows/win32/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectconfiguration-lockforprocess) method is a good indication that the APO was successfully incorporated.

For [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) in particular, there are a number of reasons why the returned HRESULT code could indicate a failure. The three primary reasons are as follows:

- The graph is running protected content, and the APO is not properly signed.

- The APO is not registered.

- The APO has been renamed or tampered with.

Also, if the failure count value for an SFX, MFX or EFX APO reaches a system-specified limit, the SFX, MFX and EFX APOs are disabled by setting the PKEY\_Endpoint\_Disable\_SysFx registry key to '1'. The system-specified limit is currently a value of 10.

## Related topics

[Windows Audio Processing Objects](windows-audio-processing-objects.md)

[Using a Universal INF File](../install/using-a-universal-inf-file.md)

[Creating a componentized audio driver installation](./audio-universal-drivers.md#creating-a-componentized-audio-driver-installation)
