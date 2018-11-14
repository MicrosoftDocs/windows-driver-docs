---
title: Frame Server Custom Media Source
description: Provides information on implementation of a Custom Media Source within the Frame Server architecture. 
ms.date: 10/02/2018
ms.localizationpriority: medium
---

# Frame Server Custom Media Source 

This topic provides information on implementation of a Custom Media Source within the Frame Server architecture. 

## AV Stream and Custom Media Source options

When deciding how to provide video capture stream support within the Frame Server architecture, there are two main options: AV Stream and Custom Media Source.

The AV Stream model is the standard camera driver model using an AV Stream miniport driver (kernel mode driver). Typically AV Stream drivers fall into two main categories: MIPI based drivers and USB Video Class drivers.

For the Custom Media Source option, the driver model may be completely custom (proprietary) or may be based on a non-traditional camera source (such as file, or network sources).

### AV Stream Driver

The main benefit of an AV Stream Driver approach is that the PnP and Power Management/Device Management is already handled by the AV Stream framework.

However, it also means the underlying source must be a physical device with a kernel mode driver to interface with the hardware. For UVC devices, a Windows UVC 1.5 class driver is provided inbox so devices simply need to implement their firmware.

For MIPI based devices, the vendor will need to implement their own AV Stream miniport driver.

### Custom Media Source

For sources whose device driver is already available (but not an AV Stream miniport driver) or sources which use non-traditional camera capture, an AV Stream Driver may not be viable. For example, an IP Camera connected over the network would not fit into an AV Stream Driver model.

In such situations, a Custom Media Source using the Frame Server model would be an alternative.

| Features | Custom Media Source | AV Stream Driver |
|---|---|---|
| PnP and Power Management | Must be implemented by the source and/or stub driver | Provided by the AV Stream framework |
| User mode plugin       | Not available. Custom Media Source incorporates the OEM/IHV specific user mode logic. | DMFT, Platform DMFT, and MFT0 for legacy implementation |
| Sensor Group | Supported | Supported |
| Camera Profile V2 | Supported | Supported |
| Camera Profile V1 | Not supported | Supported |

## Custom Media Source Requirements

With the introduction of Windows Camera Frame Server (referred to as Frame Server) service, this can be accomplished through a Custom Media Source. This requires two main components:

-   A driver package with a stubbed driver designed to register/enable a camera device interface.

-   A COM DLL which hosts the Custom Media Source.

The first requirement is needed for two purposes:

-   A vetting process to ensure the Custom Media Source is installed through a trusted process (the driver package requires WHQL certification).

-   Support for the standard PnP enumeration and discovery of the "camera".

### Security

The Custom Media Source for Frame Server differs from the generic Custom Media Source in terms of security in the following manner:

-   Frame Server Custom Media Source runs as Local Service (not to be confused with Local System; Local Service is a very low privileged account on Windows machines).

-   Frame Server Custom Media Source runs in Session 0 (System Service session) and cannot interact with the user desktop.

Given these constraints, Frame Server Custom Media Sources must not attempt to access protected parts of the file system nor the registry. Generally, read access is permitted, but write access is not.

### Performance

As a part of the Frame Server model, there are two cases in how Custom Media Sources will be instantiated by the Frame Server:

-   During Sensor Group generation/publishing.

-   During "camera" activation

The Sensor Group generation is typically done during device installation and/or power cycle. Given this, we strongly recommended that Custom Media Sources avoid any significant processing during its creation and defer any such activity to the [IMFMediaSource::Start](https://docs.microsoft.com/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) function. The Sensor Group generation will not attempt to start the Custom Media Source, merely query the various available streams/media types and source/stream attribute information.

## Stub Driver

There are two minimum requirements for the driver package and the stub driver.

The stub driver can be written using either the WDF (UMDF or KMDF) or the WDM driver model.

The driver requirements are:

-   Register your "camera" (the Custom Media Source) device interface under the [KSCATEGORY_VIDEO_CAMERA](https://docs.microsoft.com/windows-hardware/drivers/install/kscategory-video-camera) category so it can be enumerated.

> [!NOTE]
> To allow enumeration by legacy DirectShow applications, your driver will need to also register under the [KSCATEGORY_VIDEO](https://docs.microsoft.com/windows-hardware/drivers/install/kscategory-video) and [KSCATEGORY_CAPTURE](https://docs.microsoft.com/windows-hardware/drivers/install/kscategory-capture).

-   Add a registry entry under the device interface node (use the **AddReg** directive in your driver INF **DDInstall.Interface** section) which declares the CoCreate-able CLSID of your Custom Media Source COM object. This must be added using the following registry value name: **CustomCaptureSourceClsid**.

This allows the "camera" source to be discovered by applications and when activated, informs the Frame Server service to intercept the activation call and re-route it to the CoCreated Custom Media Source.

### Sample INF

The following sample shows a typical INF for a Custom Media Source stub driver:

```INF
;/*++
;
;Module Name:
; SimpleMediaSourceDriver.INF
;
;Abstract:
; INF file for installing the Usermode SimpleMediaSourceDriver Driver
;
;Installation Notes:
; Using Devcon: Type "devcon install SimpleMediaSourceDriver.inf root\SimpleMediaSource" to install
;
;--*/

[Version]
Signature="$WINDOWS NT$"
Class=Sample
ClassGuid={5EF7C2A5-FF8F-4C1F-81A7-43D3CBADDC98}
Provider=%ProviderString%
DriverVer=01/28/2016,0.10.1234
CatalogFile=SimpleMediaSourceDriver.cat

[DestinationDirs]
DefaultDestDir = 12

; ================= Class section =====================

[ClassInstall32]
Addreg=SimpleMediaSourceClassReg

[SimpleMediaSourceClassReg]

HKR,,,0,%ClassName%
HKR,,Icon,,-24

[SourceDisksNames]
1 = %DiskId1%,,,""

[SourceDisksFiles]
SimpleMediaSourceDriver.dll = 1,,
SimpleMediaSource.dll = 1,,

;*****************************************
; SimpleMFSource Install Section
;*****************************************

[Manufacturer]
%StdMfg%=Standard,NT$ARCH$

[Standard.NT$ARCH$]
%SimpleMediaSource.DeviceDesc%=SimpleMediaSource, root\SimpleMediaSource

;---------------- copy files

[SimpleMediaSource.NT]
CopyFiles=UMDriverCopy, CustomCaptureSourceCopy
AddReg = CustomCaptureSource.ComRegistration

[SimpleMediaSource.NT.Interfaces]
AddInterface = %KSCATEGORY_VIDEO_CAMERA%, %CustomCaptureSource.ReferenceString%, CustomCaptureSourceInterface
AddInterface = %KSCATEGORY_VIDEO%, %CustomCaptureSource.ReferenceString%, CustomCaptureSourceInterface
AddInterface = %KSCATEGORY_CAPTURE%, %CustomCaptureSource.ReferenceString%, CustomCaptureSourceInterface

[CustomCaptureSourceInterface]
AddReg = CustomCaptureSourceInterface.AddReg, CustomCaptureSource.ComRegistration

[CustomCaptureSourceInterface.AddReg]
HKR,,CLSID,,%ProxyVCap.CLSID%
HKR,,CustomCaptureSourceClsid,,%CustomCaptureSource.CLSID%
HKR,,FriendlyName,,%CustomCaptureSource.Desc%

[CustomCaptureSource.ComRegistration]
HKCR,CLSID\%CustomCaptureSource.CLSID%,,,%CustomCaptureSource.Desc%
HKCR,CLSID\%CustomCaptureSource.CLSID%\InprocServer32,,%REG_EXPAND_SZ%,%CustomCaptureSource.Location%
HKCR,CLSID\%CustomCaptureSource.CLSID%\InprocServer32,ThreadingModel,,Both

[UMDriverCopy]
SimpleMediaSourceDriver.dll,,,0x00004000 ; COPYFLG_IN_USE_RENAME

[CustomCaptureSourceCopy]
SimpleMediaSource.dll,,,0x00004000 ; COPYFLG_IN_USE_RENAME

[DestinationDirs]
UMDriverCopy=12,UMDF ; copy to driversMdf
CustomCaptureSourceCopy=11

;-------------- Service installation
[SimpleMediaSource.NT.Services]
AddService=WUDFRd,0x000001fa,WUDFRD_ServiceInstall

[WUDFRD_ServiceInstall]
DisplayName = %WudfRdDisplayName%
ServiceType = 1
StartType = 3
ErrorControl = 1
ServiceBinary = %12%\WUDFRd.sys

;-------------- WDF specific section -------------
[SimpleMediaSource.NT.Wdf]
UmdfService=SimpleMediaSource, SimpleMediaSource_Install
UmdfServiceOrder=SimpleMediaSource

[SimpleMediaSource_Install]
UmdfLibraryVersion=$UMDFVERSION$
ServiceBinary=%12%\UMDF\SimpleMediaSourceDriver.dll

[Strings]
ProviderString = "Microsoft Corporation"
StdMfg = "(Standard system devices)"
DiskId1 = "SimpleMediaSource Disk \#1"
SimpleMediaSource.DeviceDesc = "SimpleMediaSource Capture Source" ; what you will see under SimpleMediaSource dummy devices
ClassName = "SimpleMediaSource dummy devices" ; device type this driver will install as in device manager
WudfRdDisplayName="Windows Driver Foundation - User-mode Driver Framework Reflector"
KSCATEGORY_VIDEO_CAMERA = "{E5323777-F976-4f5b-9B55-B94699C46E44}"
KSCATEGORY_CAPTURE="{65E8773D-8F56-11D0-A3B9-00A0C9223196}"
KSCATEGORY_VIDEO="{6994AD05-93EF-11D0-A3CC-00A0C9223196}"
ProxyVCap.CLSID="{17CCA71B-ECD7-11D0-B908-00A0C9223196}"
CustomCaptureSource.Desc = "SimpleMediaSource Source"
CustomCaptureSource.ReferenceString = "CustomCameraSource"
CustomCaptureSource.CLSID = "{9812588D-5CE9-4E4C-ABC1-049138D10DCE}"
CustomCaptureSource.Location = "%SystemRoot%\System32\SimpleMediaSource.dll"
CustomCaptureSource.Binary = "SimpleMediaSource.dll"
REG_EXPAND_SZ = 0x00020000
```

The above Custom Media Source registers under **KSCATEGORY\_VIDEO**, **KSCATEGORY\_CAPTURE**, and **KSCATEGORY\_VIDEO\_CAMERA** to ensure the "camera" is discoverable by any UWP and non-UWP apps searching for a standard RGB camera.

If the Custom Media Source also exposes non-RGB streams (IR, Depth, and so on) it may optionally also register under the [KSCATEGORY_SENSOR_CAMERA](https://docs.microsoft.com/windows-hardware/drivers/install/kscategory-sensor-camera).

> [!NOTE]
> Most USB based webcams will expose YUY2 and MJPG formats. Because of this behavior, many legacy DirectShow applications are written with the assumption that YUY2/MJPG is available. To ensure compatibility with such application, it is recommended that YUY2 media type is made available from your Custom Media Source if legacy app compatibility is desired.

### Stub Driver Implementation

In addition to the INF, the driver stub must also register and enable the camera device interfaces. This is typically done during the **DRIVER\_ADD\_DEVICE** operation.

See the [DRIVER_ADD_DEVICE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_add_device) callback function for WDM based drivers and the [WdfDriverCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nf-wdfdriver-wdfdrivercreate) function for UMDF/KMDF drivers.

The following is a code snip of a UMDF driver stub which handles this operation:

```cpp
NTSTATUS
DriverEntry(
    IN PDRIVER_OBJECT DriverObject,
    IN PUNICODE_STRING RegistryPath
    )
/*++

Routine Description:

    DriverEntry initializes the driver and is the first routine called by the
    system after the driver is loaded. DriverEntry specifies the other entry
    points in the function driver, such as EvtDevice and DriverUnload.

Parameters Description:

    DriverObject - represents the instance of the function driver that is loaded
    into memory. DriverEntry must initialize members of DriverObject before it
    returns to the caller. DriverObject is allocated by the system before the
    driver is loaded, and it is released by the system after the system unloads
    the function driver from memory.

RegistryPath - represents the driver specific path in the Registry.

    The function driver can use the path to store driver related data between
    reboots. The path does not store hardware instance specific data.

Return Value:

    STATUS_SUCCESS if successful,  
    STATUS_UNSUCCESSFUL otherwise.

--*/

{
    WDF_DRIVER_CONFIG config;
    NTSTATUS status;

    WDF_DRIVER_CONFIG_INIT(&config,
                    EchoEvtDeviceAdd
                    );

    status = WdfDriverCreate(DriverObject,
                            RegistryPath,
                            WDF_NO_OBJECT_ATTRIBUTES,
                            &config,
                            WDF_NO_HANDLE);

    if (!NT_SUCCESS(status)) {
        KdPrint(("Error: WdfDriverCreate failed 0x%x\n", status));
        return status;
    }

    // ...

    return status;
}

NTSTATUS
EchoEvtDeviceAdd(
    IN WDFDRIVER Driver,
    IN PWDFDEVICE_INIT DeviceInit
    )
/*++
Routine Description:

    EvtDeviceAdd is called by the framework in response to AddDevice
    call from the PnP manager. We create and initialize a device object to
    represent a new instance of the device.

Arguments:

    Driver - Handle to a framework driver object created in DriverEntry

    DeviceInit - Pointer to a framework-allocated WDFDEVICE_INIT structure.

Return Value:

    NTSTATUS

--*/
{
    NTSTATUS status;

    UNREFERENCED_PARAMETER(Driver);

    KdPrint(("Enter EchoEvtDeviceAdd\n"));

    status = EchoDeviceCreate(DeviceInit);

    return status;
}

NTSTATUS
EchoDeviceCreate(
    PWDFDEVICE_INIT DeviceInit  
/*++

Routine Description:

    Worker routine called to create a device and its software resources.

Arguments:

    DeviceInit - Pointer to an opaque init structure. Memory for this
                    structure will be freed by the framework when the WdfDeviceCreate
                    succeeds. Do not access the structure after that point.

Return Value:

    NTSTATUS

--*/  
{
    WDF_OBJECT_ATTRIBUTES deviceAttributes;
    PDEVICE_CONTEXT deviceContext;
    WDF_PNPPOWER_EVENT_CALLBACKS pnpPowerCallbacks;
    WDFDEVICE device;
    NTSTATUS status;
    UNICODE_STRING szReference;
    RtlInitUnicodeString(&szReference, L"CustomCameraSource");

    WDF_PNPPOWER_EVENT_CALLBACKS_INIT(&pnpPowerCallbacks);

    //
    // Register pnp/power callbacks so that we can start and stop the timer as the device
    // gets started and stopped.
    //
    pnpPowerCallbacks.EvtDeviceSelfManagedIoInit = EchoEvtDeviceSelfManagedIoStart;
    pnpPowerCallbacks.EvtDeviceSelfManagedIoSuspend = EchoEvtDeviceSelfManagedIoSuspend;

    #pragma prefast(suppress: 28024, "Function used for both Init and Restart Callbacks")
    pnpPowerCallbacks.EvtDeviceSelfManagedIoRestart = EchoEvtDeviceSelfManagedIoStart;

    //
    // Register the PnP and power callbacks. Power policy related callbacks will be registered
    // later in SotwareInit.
    //
    WdfDeviceInitSetPnpPowerEventCallbacks(DeviceInit, &pnpPowerCallbacks);

    {
        WDF_FILEOBJECT_CONFIG cameraFileObjectConfig;
        WDF_OBJECT_ATTRIBUTES cameraFileObjectAttributes;

        WDF_OBJECT_ATTRIBUTES_INIT(&cameraFileObjectAttributes);

        cameraFileObjectAttributes.SynchronizationScope = WdfSynchronizationScopeNone;

        WDF_FILEOBJECT_CONFIG_INIT(
            &cameraFileObjectConfig,
            EvtCameraDeviceFileCreate,
            EvtCameraDeviceFileClose,
            WDF_NO_EVENT_CALLBACK);

        WdfDeviceInitSetFileObjectConfig(
            DeviceInit,
            &cameraFileObjectConfig,
            &cameraFileObjectAttributes);
    }

    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&deviceAttributes, DEVICE_CONTEXT);

    status = WdfDeviceCreate(&DeviceInit, &deviceAttributes, &device);

    if (NT_SUCCESS(status)) {
        //
        // Get the device context and initialize it. WdfObjectGet_DEVICE_CONTEXT is an
        // inline function generated by WDF_DECLARE_CONTEXT_TYPE macro in the
        // device.h header file. This function will do the type checking and return
        // the device context. If you pass a wrong object handle
        // it will return NULL and assert if run under framework verifier mode.
        //
        deviceContext = WdfObjectGet_DEVICE_CONTEXT(device);
        deviceContext->PrivateDeviceData = 0;

        //
        // Create a device interface so that application can find and talk
        // to us.
        //
        status = WdfDeviceCreateDeviceInterface(
            device,
            &CAMERA_CATEGORY,
            &szReference // ReferenceString
            );

        if (NT_SUCCESS(status)) {
            //
            // Create a device interface so that application can find and talk
            // to us.
            //
            status = WdfDeviceCreateDeviceInterface(
            device,
            &CAPTURE_CATEGORY,
            &szReference // ReferenceString
            );
        }

        if (NT_SUCCESS(status)) {
            //
            // Create a device interface so that application can find and talk
            // to us.
            //
            status = WdfDeviceCreateDeviceInterface(
            device, 
            &VIDEO_CATEGORY,
            &szReference // ReferenceString
            );
        }

        if (NT_SUCCESS(status)) {
            //
            // Initialize the I/O Package and any Queues
            //
            status = EchoQueueInitialize(device);
        }       
    }

    return status;
}
```

### PnP Operation

Just like any other physical camera, it is recommended that your stub driver manage at least the PnP operations of enabling and disabling the device when the underlying source is removed/attached. For example, if your Custom Media Source is using a network source (such as an IP camera), you may want to trigger a device removal when that network source is no longer available.

This ensures that applications listen for device add/removal via the PnP APIs get the proper notifications. And ensures that a source that is no longer available cannot be enumerated.

For UMDF and KMDF drivers, see the [WdfDeviceSetDeviceState](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicesetdevicestate) function documentation.

For WMD drivers, see the [IoSetDeviceInterfaceState](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iosetdeviceinterfacestate) function documentation.

## Custom Media Source DLL

The Custom Media Source is a standard inproc COM server which must implement the following interfaces:

-   [IMFMediaEventGenerator](https://docs.microsoft.com/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator)

-   [IMFMediaSource](https://docs.microsoft.com/windows/desktop/api/mfidl/nn-mfidl-imfmediasource)

-   [IMFMediaSourceEx](https://docs.microsoft.com/windows/desktop/api/mfidl/nn-mfidl-imfmediasourceex)

-   [IKsControl](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/nn-ks-ikscontrol)

-   [IMFGetService](https://docs.microsoft.com/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)

> [!NOTE]
> **IMFMediaSourceEx** inherits from **IMFMediaSource** and **IMFMediaSource** inherits from **IMFMediaEventGenerator**.

Each supported stream within the Custom Media Source must support the following interfaces:

-   **IMFMediaEventGenerator**

-   [IMFMediaStream](https://docs.microsoft.com/windows/desktop/api/mfidl/nn-mfidl-imfmediastream)

-   **IMFMediaStream2**

> [!NOTE]
> **IMFMediaStream2** inherits from **IMFMediaStream** and **IMFMediaStream** inherits from **IMFMediaEventGenerator**.

Refer to the [Writing a Custom Media Source](https://docs.microsoft.com/windows/desktop/medfound/writing-a-custom-media-source) documentation on how to create a Custom Media Source. The rest of this section will explain the differences needed to support your Custom Media Source within the Frame Server framework.

### IMFGetService

**IMFGetService** is a mandatory interface for Frame Server Custom Media Source. **IMFGetService** may return **MF\_E\_UNSUPPORTED\_SERVICE** if your Custom Media Source does not need to expose any additional service interfaces.

The following example show an **IMFGetService** implementation with no support service interfaces:

```cpp
_Use_decl_annotations_
IFACEMETHODIMP
SimpleMediaSource::GetService(
    _In_ REFGUID guidService,
    _In_ REFIID riid,
    _Out_ LPVOID * ppvObject
    )
{
    HRESULT hr = S_OK;
    auto lock = _critSec.Lock();

    RETURN_IF_FAILED (_CheckShutdownRequiresLock());

    if (!ppvObject)
    {
        return E_POINTER;
    }
    *ppvObject = NULL;

    // We have no supported service, just return
    // MF_E_UNSUPPORTED_SERVICE for all calls.

    return MF_E_UNSUPPORTED_SERVICE;
}
```

### IMFMediaEventGenerator

As shown above, both the source and the individual streams within the source must support their own [IMFMediaEventGenerator](https://docs.microsoft.com/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface. The entire MF pipeline data and control flows from the source is managed through the event generator by sending specific [IMFMediaEvent](https://docs.microsoft.com/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaevent).

For implementing IMFMediaEventGenerator, the Custom Media Source must use the [MFCreateEventQueue](https://docs.microsoft.com/windows/desktop/api/mfapi/nf-mfapi-mfcreateeventqueue) API to create an [IMFMediaEventQueue](https://docs.microsoft.com/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventqueue) and route all methods for **IMFMediaEventGenerator** to the queue object:

**IMFMediaEventGenerator** has the following methods:

```cpp
// IMFMediaEventGenerator
IFACEMETHOD(BeginGetEvent)(_In_ IMFAsyncCallback *pCallback, _In_ IUnknown *punkState);
IFACEMETHOD(EndGetEvent)(_In_ IMFAsyncResult *pResult, _COM_Outptr_ IMFMediaEvent **ppEvent);
IFACEMETHOD(GetEvent)(DWORD dwFlags, _Out_ IMFMediaEvent **ppEvent);
IFACEMETHOD(QueueEvent)(MediaEventType met, REFGUID guidExtendedType, HRESULT hrStatus, _In_opt_ const PROPVARIANT *pvValue);
```

The following code shows the recommended implementation of the **IMFMediaEventGenerator** interface. The Custom Media Source implementation will expose the **IMFMediaEventGenerator** interface, and the methods for that interface will be routing the requests into the **IMFMediaEventQueue** object created during the media source creation/initialization.

In the code below, **\_spEventQueue** object is the **IMFMediaEventQueue** created using the **MFCreateEventQueue** function:

```cpp
// IMFMediaEventGenerator methods
IFACEMETHODIMP
SimpleMediaSource::BeginGetEvent(
    _In_ IMFAsyncCallback *pCallback,
    _In_ IUnknown *punkState
    )
{
    HRESULT hr = S_OK;
    auto lock = _critSec.Lock();

    RETURN_IF_FAILED (_CheckShutdownRequiresLock());
    RETURN_IF_FAILED (_spEventQueue->BeginGetEvent(pCallback, punkState));

    return hr;
}

IFACEMETHODIMP
SimpleMediaSource::EndGetEvent(
    _In_ IMFAsyncResult *pResult,
    _COM_Outptr_ IMFMediaEvent **ppEvent
    )
{
    HRESULT hr = S_OK;
    auto lock = _critSec.Lock();

    RETURN_IF_FAILED (_CheckShutdownRequiresLock());
    RETURN_IF_FAILED (_spEventQueue->EndGetEvent(pResult, ppEvent));

    return hr;
}

IFACEMETHODIMP
SimpleMediaSource::GetEvent(
    DWORD dwFlags,
    _COM_Outptr_ IMFMediaEvent **ppEvent
    )
{
    // NOTE:
    // GetEvent can block indefinitely, so we do not hold the lock.
    // This requires some juggling with the event queue pointer.

    HRESULT hr = S_OK;

    ComPtr<IMFMediaEventQueue> spQueue;

    {
        auto lock = _critSec.Lock();

        RETURN_IF_FAILED (_CheckShutdownRequiresLock());
        spQueue = _spEventQueue;
    }

    // Now get the event.
    RETURN_IF_FAILED (_spEventQueue->GetEvent(dwFlags, ppEvent));

    return hr;
}

IFACEMETHODIMP
SimpleMediaSource::QueueEvent(
    MediaEventType eventType,
    REFGUID guidExtendedType,
    HRESULT hrStatus,
    _In_opt_ PROPVARIANT const *pvValue
    )
{
    HRESULT hr = S_OK;
    auto lock = _critSec.Lock();

    RETURN_IF_FAILED (_CheckShutdownRequiresLock());
    RETURN_IF_FAILED (_spEventQueue->QueueEventParamVar(eventType, guidExtendedType, hrStatus, pvValue));

    return hr;
}
```

### Seeking and Pausing

Custom Media Sources supported through the Frame Server framework do not support Seek or Pause operations. Your Custom Media Source does not need to provide support for these operations and must not post either the **MFSourceSeeked** or **MEStreamSeeked** event.

[IMFMediaSource::Pause](https://docs.microsoft.com/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-pause) should return **MF\_E\_INVALID\_STATE\_TRANSITION** (or **MF\_E\_SHUTDOWN** if the source was already shutdown).

### IKsControl

[IKsControl](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/nn-ks-ikscontrol) is the standard control interface for all camera related controls. If your Custom Media Source implements any camera controls the **IKsControl** interface is how the pipeline will route the control I/O.

For more information, see the following Control Set documentation topics:

-   [PROPSETID_VIDCAP_CAMERACONTROL](https://docs.microsoft.com/windows-hardware/drivers/stream/propsetid-vidcap-cameracontrol)

-   [PROPSETID_VIDCAP_VIDEOPROCAMP](https://docs.microsoft.com/windows-hardware/drivers/stream/propsetid-vidcap-videoprocamp)

-   [KSPROPERTYSETID_ExtendedCameraControl](https://docs.microsoft.com/windows-hardware/drivers/stream/kspropertysetid-extendedcameracontrol)

The controls are optional and if not supported, the recommended error code to return is **HRESULT\_FROM\_WIN32(ERROR\_SET\_NOT\_FOUND)**.

The following code is an example **IKsControl** implementation with no supported controls:

```cpp
// IKsControl methods
_Use_decl_annotations_
IFACEMETHODIMP
SimpleMediaSource::KsProperty(
    _In_reads_bytes_(ulPropertyLength) PKSPROPERTY pProperty,
    _In_ ULONG ulPropertyLength,
    _Inout_updates_to_(ulDataLength, *pBytesReturned) LPVOID pPropertyData,
    _In_ ULONG ulDataLength,
    _Out_ ULONG* pBytesReturned
    )
{
    // ERROR_SET_NOT_FOUND is the standard error code returned
    // by the AV Stream driver framework when a miniport
    // driver does not register a handler for a KS operation.
    // We want to mimic the driver behavior here if we do not
    // support controls.
    return HRESULT_FROM_WIN32(ERROR_SET_NOT_FOUND);
}

_Use_decl_annotations_
IFACEMETHODIMP SimpleMediaSource::KsMethod(
    _In_reads_bytes_(ulMethodLength) PKSMETHOD pMethod,
    _In_ ULONG ulMethodLength,
    _Inout_updates_to_(ulDataLength, *pBytesReturned) LPVOID pMethodData,
    _In_ ULONG ulDataLength,
    _Out_ ULONG* pBytesReturned
    )
{
    return HRESULT_FROM_WIN32(ERROR_SET_NOT_FOUND);
}

_Use_decl_annotations_
IFACEMETHODIMP SimpleMediaSource::KsEvent(
    _In_reads_bytes_opt_(ulEventLength) PKSEVENT pEvent,
    _In_ ULONG ulEventLength,
    _Inout_updates_to_(ulDataLength, *pBytesReturned) LPVOID pEventData,
    _In_ ULONG ulDataLength,
    _Out_opt_ ULONG* pBytesReturned
    )
{
    return HRESULT_FROM_WIN32(ERROR_SET_NOT_FOUND);
}
```

### IMFMediaStream2

As explained in [Writing a Custom Media Source](https://docs.microsoft.com/windows/desktop/medfound/writing-a-custom-media-source), the **IMFMediaStream2** interface is provided to the frame work from your Custom Media Source via a [MENewStream](https://docs.microsoft.com/windows/desktop/medfound/menewstream) media event posted to the source event queue during the completion of the [IMFMediaSource::Start](https://docs.microsoft.com/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) method:

```cpp
IFACEMETHODIMP
SimpleMediaSource::Start(
    _In_ IMFPresentationDescriptor *pPresentationDescriptor,
    _In_opt_ const GUID *pguidTimeFormat,
    _In_ const PROPVARIANT *pvarStartPos
    )
{
    HRESULT hr = S_OK;
    auto lock = _critSec.Lock();
    DWORD count = 0;
    PROPVARIANT startTime;
    BOOL selected = false;
    ComPtr<IMFStreamDescriptor> streamDesc;
    DWORD streamIndex = 0;

    if (pPresentationDescriptor == nullptr || pvarStartPos == nullptr)
    {
        return E_INVALIDARG;
    }
    else if (pguidTimeFormat != nullptr && *pguidTimeFormat != GUID_NULL)
    {
        return MF_E_UNSUPPORTED_TIME_FORMAT;
    }

    RETURN_IF_FAILED (_CheckShutdownRequiresLock());

    if (_sourceState != SourceState::Stopped)
    {
        return MF_E_INVALID_STATE_TRANSITION;
    }

    _sourceState = SourceState::Started;

    // This checks the passed in PresentationDescriptor matches the member of streams we
    // have defined internally and that at least one stream is selected

    RETURN_IF_FAILED (_ValidatePresentationDescriptor(pPresentationDescriptor));
    RETURN_IF_FAILED (pPresentationDescriptor->GetStreamDescriptorCount(&count));
    RETURN_IF_FAILED (InitPropVariantFromInt64(MFGetSystemTime(), &startTime));

    // Send event that the source started. Include error code in case it failed.
    RETURN_IF_FAILED (_spEventQueue->QueueEventParamVar(MESourceStarted,
                                                            GUID_NULL,
                                                            hr,
                                                            &startTime));

    // We are hardcoding this to the first descriptor
    // since this sample is a single stream sample. For
    // multiple streams, we need to walk the list of streams
    // and for each selected stream, send the MEUpdatedStream
    // or MENewStream event along with the MEStreamStarted
    // event.
    RETURN_IF_FAILED (pPresentationDescriptor->GetStreamDescriptorByIndex(0,
                                                                            &selected,
                                                                            &streamDesc));

    RETURN_IF_FAILED (streamDesc->GetStreamIdentifier(&streamIndex));
    if (streamIndex >= NUM_STREAMS)
    {
        return MF_E_INVALIDSTREAMNUMBER;
    }

    if (selected)
    {
        ComPtr<IUnknown> spunkStream;
        MediaEventType met = (_wasStreamPreviouslySelected ? MEUpdatedStream : MENewStream);

        // Update our internal PresentationDescriptor
        RETURN_IF_FAILED (_spPresentationDescriptor->SelectStream(streamIndex));
        RETURN_IF_FAILED (_stream.Get()->SetStreamState(MF_STREAM_STATE_RUNNING));
        RETURN_IF_FAILED (_stream.As(&spunkStream));

        // Send the MEUpdatedStream/MENewStream to our source event
        // queue.

        RETURN_IF_FAILED (_spEventQueue->QueueEventParamUnk(met,
                                                                GUID_NULL,
                                                                S_OK,
                                                                spunkStream.Get()));

        // But for our stream started (MEStreamStarted), we post to our
        // stream event queue.
        RETURN_IF_FAILED (_stream.Get()->QueueEvent(MEStreamStarted,
                                                        GUID_NULL,
                                                        S_OK,
                                                        &startTime));
    }
    _wasStreamPreviouslySelected = selected;

    return hr;
}
```

This must be done for each stream selected via the [IMFPresentationDescriptor](https://docs.microsoft.com/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor).

For Custom Media Sources with video stream, [MEEndOfStream](https://docs.microsoft.com/windows/desktop/medfound/meendofstream) and [MEEndOfPresentation](https://docs.microsoft.com/windows/desktop/medfound/meendofpresentation) events should not be sent.

### Stream Attributes

All Custom Media Source streams must have the [MF_DEVICESTREAM_STREAM_CATEGORY](https://docs.microsoft.com/windows/desktop/medfound/mf-devicestream-stream-category) set to be **PINNAME\_VIDEO\_CAPTURE**. **PINNAME\_VIDEO\_PREVIEW** is not supported for Custom Media Sources.

> [!NOTE]
> **PINNAME\_IMAGE**, while supported, is not recommended. Exposing a stream with **PINNAME\_IMAGE** requires the Custom Media Source to support all the photo trigger controls. See the [Photo Stream Controls](#photo-stream-controls) section below for more details.

[MF_DEVICESTREAM_STREAM_ID](https://docs.microsoft.com/windows/desktop/medfound/mf-devicestream-stream-id) is a mandatory attribute for all streams. It should be a 0-based index. So the first stream has an ID of 0, second stream an ID of 1, and so on.

The following are a list of recommended attributes on the stream:

-   [MF_DEVICESTREAM_ATTRIBUTE_FRAMESOURCE_TYPES](https://docs.microsoft.com/windows/desktop/medfound/mf-devicestream-attribute-framesource-types)

-   [MF_DEVICESTREAM_FRAMESERVER_SHARED](https://docs.microsoft.com/windows/desktop/medfound/mf-devicestream-frameserver-shared)

#### MF\_DEVICESTREAM\_ATTRIBUTE\_FRAMESOURCE\_TYPES

**MF\_DEVICESTREAM\_ATTRIBUTE\_FRAMESOURCE\_TYPES** is a UINT32 attribute which is a bitmasked value of stream type. It may be set to any of the following (while these types are a bitmask flag, it is recommend that source types not be mixed if at all possible):

| Type                         | Flag   | Description                                      |
|------------------------------|--------|--------------------------------------------------|
| MFFrameSourceTypes\_Color    | 0x0001 | Standard RGB color stream                        |
| MFFrameSourceTypes\_Infrared | 0x0002 | IR stream                                        |
| MFFrameSourceTypes\_Depth    | 0x0004 | Depth stream                                     |
| MFFrameSourceTypes\_Image    | 0x0008 | Image stream (non-video subtype, typically JPEG) |
| MFFrameSourceTypes\_Custom   | 0x0080 | Custom stream type                               |

#### MF\_DEVICESTREAM\_FRAMESERVER\_SHARED

**MF\_DEVICESTREAM\_FRAMESERVER\_SHARED** is a UINT32 attribute which can be set to either 0 or 1. If set to 1, it marks the stream as being "shareable" by the Frame Server. This will allow applications to open the stream in a shared mode, even when used by another app.

If this attribute is not set, Frame Server will allow the first non-marked stream to be shared (if the Custom Media Source has only one stream, that stream will be marked as shared).

If this attribute is set to 0, Frame Server will block the stream from shared apps. If the Custom Media Source marks all streams with this attribute set to 0, no shared application will be able to initialize the source.

### Sample Allocation

All media frames must be produced as an [IMFSample](https://docs.microsoft.com/windows/desktop/api/mfobjects/nn-mfobjects-imfsample). Custom Media Sources must use the [MFCreateSample](https://docs.microsoft.com/windows/desktop/api/mfapi/nf-mfapi-mfcreatesample) function to allocate an instance of IMFSample and use the [AddBuffer](https://docs.microsoft.com/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-addbuffer) method to add media buffers.

Each **IMFSample** must have the sample time and sample duration set. All sample timestamps must be based on QPC time (QueryPerformanceCounter).

It is recommended that Custom Media Sources use the [MFGetSystemTime](https://docs.microsoft.com/windows/desktop/api/mfidl/nf-mfidl-mfgetsystemtime) function where possible. This function is a wrapper around **QueryPerformanceCounter** and converts the QPC ticks to 100 nanosecond units.

Custom Media Sources may use an internal clock, but all timestamps must be correlated to 100 nanosecond units based on the current QPC.

#### Media Buffer

All media buffers added to the **IMFSample** must use the standard MF buffer allocation functions. Custom Media Sources must not implement their own [IMFMediaBuffer](https://docs.microsoft.com/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer) interfaces or attempt to allocate media buffer directly (for example, new/malloc/VirtualAlloc, and so on, must not be used for frame data).

Use any of the following APIs to allocate media frames:

-   [MFCreateMemoryBuffer](https://docs.microsoft.com/windows/desktop/api/mfapi/nf-mfapi-mfcreatememorybuffer)

-   [MFCreateAlignedMemoryBuffer](https://docs.microsoft.com/windows/desktop/api/mfapi/nf-mfapi-mfcreatealignedmemorybuffer)

-   [MFCreate2DMediaBuffer](https://docs.microsoft.com/windows/desktop/api/mfapi/nf-mfapi-mfcreate2dmediabuffer)

-   [MFCreateDXGISurfaceBuffer](https://docs.microsoft.com/windows/desktop/api/mfapi/nf-mfapi-mfcreatedxgisurfacebuffer)

**MFCreateMemoryBuffer** and **MFCreateAlignedMemoryBuffer** should be used for non-stride aligned media data. Typically these would be custom subtypes or compressed subtypes (such as H264/HEVC/MJPG).

For known uncompressed media types (such as YUY2, NV12, and so on) using system memory, it is recommended to use **MFCreate2DMediaBuffer**.

For using DX surfaces (for GPU accelerated operations such as rendering and/or encoding), **MFCreateDXGISurfaceBuffer** should be used.

**MFCreateDXGISurfaceBuffer** does not create the DX surface. The surface is created using the DXGI Manager passed into the media source via the [IMFMediaSourceEx::SetD3DManager](https://docs.microsoft.com/windows/desktop/api/mfidl/nf-mfidl-imfmediasourceex-setd3dmanager) method.

The [IMFDXGIDeviceManager::OpenDeviceHandle](https://docs.microsoft.com/windows/desktop/api/mfobjects/nf-mfobjects-imfdxgidevicemanager-opendevicehandle) will provide the handle associated with the selected D3D device. The [ID3D11Device](https://docs.microsoft.com/windows/desktop/api/d3d11/nn-d3d11-id3d11device) interface can be then obtained using the [IMFDXGIDeviceManager::GetVideoService](https://docs.microsoft.com/windows/desktop/api/mfobjects/nf-mfobjects-imfdxgidevicemanager-getvideoservice) method.

Regardless of what type of buffer is used, the **IMFSample** created must be provided to the pipeline through the **MEMediaSample** event on the **IMFMediaEventGenerator** of the media stream.

While it is possible to use the same **IMFMediaEventQueue** for both the Custom Media Source and the underlying collection of **IMFMediaStream**, it should be noted that doing so will result in serialization of the media source events and stream events (which includes the media flow). For sources with multiple streams, this is not desirable.

The following code snip shows a sample implementation of the media stream:

```cpp
IFACEMETHODIMP
    SimpleMediaStream::RequestSample(
    _In_ IUnknown *pToken
    )
{
    HRESULT hr = S_OK;
    auto lock = _critSec.Lock();
    ComPtr<IMFSample> sample;
    ComPtr<IMFMediaBuffer> outputBuffer;
    LONG pitch = IMAGE_ROW_SIZE_BYTES;
    BYTE *bufferStart = nullptr; // not used
    DWORD bufferLength = 0;
    BYTE *pbuf = nullptr;
    ComPtr<IMF2DBuffer2> buffer2D;

    RETURN_IF_FAILED (_CheckShutdownRequiresLock());
    RETURN_IF_FAILED (MFCreateSample(&sample));
    RETURN_IF_FAILED (MFCreate2DMediaBuffer(NUM_IMAGE_COLS,
                                            NUM_IMAGE_ROWS,
                                            D3DFMT_X8R8G8B8,
                                            false,
                                            &outputBuffer));
    RETURN_IF_FAILED (outputBuffer.As(&buffer2D));
    RETURN_IF_FAILED (buffer2D->Lock2DSize(MF2DBuffer_LockFlags_Write,
                                                &pbuf,
                                                &pitch,
                                                &bufferStart,
                                                &bufferLength));
    RETURN_IF_FAILED (WriteSampleData(pbuf, pitch, bufferLength));
    RETURN_IF_FAILED (buffer2D->Unlock2D());
    RETURN_IF_FAILED (sample->AddBuffer(outputBuffer.Get()));
    RETURN_IF_FAILED (sample->SetSampleTime(MFGetSystemTime()));
    RETURN_IF_FAILED (sample->SetSampleDuration(333333));
    if (pToken != nullptr)
    {
        RETURN_IF_FAILED (sample->SetUnknown(MFSampleExtension_Token, pToken));
    }
    RETURN_IF_FAILED (_spEventQueue->QueueEventParamUnk(MEMediaSample,
                                                            GUID_NULL,
                                                            S_OK,
                                                            sample.Get()));

    return hr;
}
```

## Custom Media Source extension to expose IMFActivate (available in Windows 10, version 1809)

In addition to the above list of interfaces that must be supported for a Custom Media Source, one of the limitations imposed by Custom Media Source operation within the Frame Server architecture is that there can only be one instance of the UMDF driver "activated" through the pipeline.

For example, if you have a physical device which installs a UMDF stub driver in addition to its non-AV Stream driver package, and you attach more than one of those physical devices to a computer, while each instance of the UMDF driver will get a unique symbolic link name, the activation path for the Custom Media Source will not have a means to communicate the symbolic link name associated with the Custom Media Source at the time of creation.

Custom Media Source may look for the standard [MF_DEVSOURCE_ATTRIBUTE_SOURCE_TYPE_VIDCAP_SYMBOLIC_LINK](https://docs.microsoft.com/windows/desktop/medfound/mf-devsource-attribute-source-type-vidcap-symbolic-link) attribute in the Custom Media Source’s attribute store (the attribute store returned from the Custom Media Source through the [IMFMediaSourceEx::GetSourceAttributes](https://docs.microsoft.com/windows/desktop/api/mfidl/nf-mfidl-imfmediasourceex-getsourceattributes) method) at the time [IMFMediaSource::Start](https://docs.microsoft.com/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) is invoked.

However, this may result in a higher start up latency since this will defer in the HW resource acquisition to start time rather than creation/initialization time.

Because of this, in Windows 10, version 1809, Custom Media Sources may optionally expose an [IMFActivate](https://docs.microsoft.com/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) interface.

> [!NOTE] 
> **IMFActivate** inherits from [IMFAttributes](https://docs.microsoft.com/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes).

### IMFActivate

If the COM server for the Custom Media Source supports **IMFActivate** interface, the device initialization information will be provided to the COM server through the **IMFAttributes** inherited by the **IMFActivate**. So when the [IMFActivate::ActivateObject](https://docs.microsoft.com/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject) is invoked, the attribute store of the **IMFActivate** will contain the symbolic link name of the UMDF stub driver and any additional configuration settings provided by the pipeline/application at the time of the source creation/initialization.

The Custom Media Source should use this method invocation to acquire any hardware resources it needs.

> [!NOTE]
> If the hardware resource acquisition takes greater than 200 milliseconds, it is recommended hardware resource is asynchronously acquired. The activation of the Custom Media Source should not block on the hardware resource acquisition. Instead [IMFMediaSource::Start](https://docs.microsoft.com/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) operation should be serialized against the hardware resource acquisition.

The two additional methods exposed by **IMFActivate**, [DetachObject](https://docs.microsoft.com/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-detachobject) and [ShutdownObject](https://docs.microsoft.com/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-shutdownobject), must return **E\_NOTIMPL**.

The Custom Media Source may choose to implement the **IMFActivate** and **IMFAttributes** interface within the same COM object as the [IMFMediaSource](https://docs.microsoft.com/windows/desktop/api/mfidl/nn-mfidl-imfmediasource). If this is done, it is recommended the [IMFMediaSourceEx::GetSourceAttributes](https://docs.microsoft.com/windows/desktop/api/mfidl/nf-mfidl-imfmediasourceex-getsourceattributes) return the same **IMFAttributes** interface as those from the **IMFActivate**.

If the Custom Media Source does not implement the **IMFActivate** and **IMFAttributes** with the same object, the Custom Media Source must copy all the attributes set on the **IMFActivate** attribute store into the Custom Media Source's source attribute store.

## Encoded Camera Stream

A Custom Media Source may expose compressed media types (HEVC or H264 elementary streams) and the OS pipeline fully supports the source and configuration of the encoding parameters on the Custom Media Source (the encoding parameters are communicated through the [ICodecAPI](https://docs.microsoft.com/windows/desktop/api/strmif/nn-strmif-icodecapi), which is routed as an [IKsControl::KsProperty](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksproxy/nf-ksproxy-ikscontrol-ksproperty) call):

```cpp
// IKsControl methods
_Use_decl_annotations_
IFACEMETHODIMP
SimpleMediaSource::KsProperty(
    _In_reads_bytes_(ulPropertyLength) PKSPROPERTY pProperty,
    _In_ ULONG ulPropertyLength,
    _Inout_updates_to_(ulDataLength, *pBytesReturned) LPVOID pPropertyData,
    _In_ ULONG ulDataLength,
    _Out_ ULONG* pBytesReturned
    );
```

The **KSPROPERTY** structure passed into the **IKsControl::KsProperty** method will have the following information:

```cpp
KSPROPERTY.Set = Encoder Property GUID
KSPROPERTY.Id = 0
KSPROPERTY.Flags = (KSPROPERTY_TYPE_SET or KSPROPERTY_TYPE_GET)
```

Where Encoder Property GUID is the list of available properties defined in [Codec API Properties](https://docs.microsoft.com/windows/desktop/DirectShow/codec-api-properties).

The payload of the Encoder Property will be passed in through the *pPropertyData* field of the **KsProperty** method declared above.

### Capture Engine Requirements

While encoded sources are fully supported by Frame Server, the client side Capture Engine (**IMFCaptureEngine**) which is used by the [Windows.Media.Capture.MediaCapture](https://docs.microsoft.com/uwp/api/windows.media.capture.mediacapture) object imposes additional requirements:

-   Stream must either be all encoded (HEVC or H264) or all uncompressed (in this context MJPG is treated as uncompressed).

-   There must be at least one uncompressed stream available.

> [!NOTE]
> These requirements are in addition to the Custom Media Source requirements outlined in this topic. However, the Capture Engine Requirements are only enforced when the client application uses the Custom Media Source via the **IMFCaptureEngine** or **Windows.Media.Capture.MediaCapture** API.

## Camera Profiles (available in Windows 10, version 1803 and later)

Camera Profile support is available for Custom Media Sources. The recommended mechanism is to publish the profile through the **MF\_DEVICEMFT\_SENSORPROFILE\_COLLECTION** attribute off the source attribute ([IMFMediaSourceEx::GetSourceAttributes](https://docs.microsoft.com/windows/desktop/api/mfidl/nf-mfidl-imfmediasourceex-getsourceattributes)).

The **MF\_DEVICEMFT\_SENSORPROFILE\_COLLECTION** attribute is an **IUnknown** of the [IMFSensorProfileCollection](https://docs.microsoft.com/windows/desktop/api/mfidl/nn-mfidl-imfsensorprofilecollection) interface. **IMFSensorProfileCollection** can be obtained using the [MFCreateSensorProfileCollection](https://docs.microsoft.com/windows/desktop/api/mfidl/nf-mfidl-mfcreatesensorprofilecollection) function:

```cpp
IFACEMETHODIMP
SimpleMediaSource::GetSourceAttributes(
    _COM_Outptr_ IMFAttributes** sourceAttributes
    )
{
    HRESULT hr = S_OK;
    auto lock = _critSec.Lock();

    if (nullptr == sourceAttributes)
    {
        return E_POINTER;
    }

    RETURN_IF_FAILED (_CheckShutdownRequiresLock());

    *sourceAttributes = nullptr;
    if (_spAttributes.Get() == nullptr)
    {
        ComPtr<IMFSensorProfileCollection> profileCollection;
        ComPtr<IMFSensorProfile> profile;

        // Create our source attribute store
        RETURN_IF_FAILED (MFCreateAttributes(_spAttributes.GetAddressOf(), 1));

        // Create an empty profile collection
        RETURN_IF_FAILED (MFCreateSensorProfileCollection(&profileCollection));

        // In this example since we have just one stream, we only have one
        // pin to add: Pin0

        // Legacy profile is mandatory. This is to ensure non-profile
        // aware applications can still function, but with degraded
        // feature sets.
        RETURN_IF_FAILED (MFCreateSensorProfile(KSCAMERAPROFILE_Legacy, 0, nullptr,
                                                profile.ReleaseAndGetAddressOf()));
        RETURN_IF_FAILED (profile->AddProfileFilter(0, L"((RES==;FRT<=30,1;SUT==))"));
        RETURN_IF_FAILED (profileCollection->AddProfile(profile.Get()));

        // High Frame Rate profile will only allow >=60fps
        RETURN_IF_FAILED (MFCreateSensorProfile(KSCAMERAPROFILE_HighFrameRate, 0, nullptr,
                                                profile.ReleaseAndGetAddressOf()));
        RETURN_IF_FAILED (profile->AddProfileFilter(0, L"((RES==;FRT>=60,1;SUT==))"));
        RETURN_IF_FAILED (profileCollection->AddProfile(profile.Get()));

        // See the profile collection to the attribute store of the IMFTransform
        RETURN_IF_FAILED (_spAttributes->SetUnknown(MF_DEVICEMFT_SENSORPROFILE_COLLECTION,
                                                        profileCollection.Get()));
    }

    return _spAttributes.CopyTo(sourceAttributes);
}
```

### Face Authentication Profile

If the Custom Media Source is designed to support Windows Hello Facial Recognition, then it is recommended to publish a Face Authentication Profile. The requirements of a Face Authentication Profile are:

-   The Face Authentication DDI Control must be supported on a single IR stream. For more information, see [KSPROPERTY_CAMERACONTROL_EXTENDED_FACEAUTH_MODE](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-faceauth-mode).

-   The IR stream must be at least 340 x 340 at 15 fps. The format must be either L8, NV12 or MJPG marked with L8 compression.

-   The RGB stream must be at least 480 x 480 at 7.5 fps (this is only needed if Multispectrum authentication is enforced).

-   The Face Authentication Profile must have the Profile ID of: KSCAMERAPROFILE\_FaceAuth\_Mode,0.

We recommended that the Face Authentication Profile only advertise one media type for each of the IR and RGB streams.

## Photo Stream Controls

If independent photo streams are exposed by marking one of the stream’s[MF\_DEVICESTREAM\_STREAM\_CATEGORY](https://docs.microsoft.com/windows/desktop/medfound/mf-devicestream-stream-category) as **PINNAME\_IMAGE**, then a stream with stream category of **PINNAME\_VIDEO\_CAPTURE** is required (for example, a single stream exposing just the **PINNAME\_IMAGE** is not a valid media source).

Through **IKsControl**, the **PROPSETID\_VIDCAP\_VIDEOCONTROL** property set must be supported. For more information, see [Video Control Properties](https://docs.microsoft.com/windows-hardware/drivers/stream/video-control-properties).
