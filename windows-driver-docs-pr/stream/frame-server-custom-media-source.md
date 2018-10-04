---


---


# Frame Server Custom Media Source 

## AV Stream vs. Custom Media Source

When deciding how to provide video capture stream support within the Frame Server architecture, there are two main options: AV Stream and Custom Media Source.

The AV Stream model is the standard camera driver model using an AV Stream miniport driver (kernel mode driver). Typically AV Stream drivers fall into two main categories: MIPI based drivers and USB Video Class drivers.

For the Custom Media Source option, the driver model may be completely custom (proprietary) or may be based on a non-traditional camera source (such as file, or network sources).

### AV Stream Driver

The main benefit of an AV Stream Driver approach is that the PnP and Power Management/Device Management is already handled by the AV Stream framework.

However, it also means the underlying source must be a physical device with a kernel mode driver to interface with the hardware. For UVC devices, a Windows UVC 1.5 class driver is provided in box so devices simply need to implement their firmware.

But for MIPI based devices, the vendor will need to implement their own AV Stream miniport driver.

### Custom Media Source

For sources whose device driver is already available (but not an AV Stream miniport driver) or sources which use non-traditional camera capture, an AV Stream Driver may not be viable. For example, an IP Camera connected over the network would not fit into an AV Stream Driver model.

In such situations, a Custom Media Source using the Frame Server model would be an alternative.

| Features | Custom Media Source | AV Stream Driver |
|---|---|---|
| PnP / Power Management | Must be implemented by the source and/or stub driver | Provided by the AV Stream framework |
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

The Sensor Group generation is typically done during device installation and/or power cycle. Given this, it is strongly recommended that Custom Media Sources avoid any significant processing during it’s creation and defer any such activity to the IMFMediaSource::Start function. The Sensor Group generation will not attempt to start the Custom Media Source, merely query the various available streams/media types and source/stream attribute information.

## Stub Driver

There are two minimum requirements for the driver package and the stub driver.

The stub driver can be written using either the WDF (UMDF or KMDF) or the WDM driver model.

The driver requirements are:

-   Register your "camera" (the Custom Media Source) device interface under the KSCATEGORY\_VIDEO\_CAMERA category so it can be enumerated.

> [!NOTE]
> To allow enumeration by legacy DirectShow applications, your driver will need to also register under the KCATEGORY\_VIDEO and KSCATEGORY\_CAPTURE.

-   Add a registry entry under the device interface node (use the AddReg directive in your driver INF's DDInstall.Interface section) which declares the CoCreate-able CLSID of your Custom Media Source's COM object. This must be added using the following registry value name: CustomCaptureSourceClsid.

This allows the "camera" source to be discovered by applications and when activated, informs the Frame Server service to intercept the activation call and re-route it to the CoCreated Custom Media Source.

### Sample INF

Here's a sample of how a typical INF would look for a Custom Media Source stub driver:

```INF
;/*++
;
;Copyright (c) 1990-2000 Microsoft Corporation
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
SimpleMediaSource.DeviceDesc = "SimpleMediaSource Capture Source" ; what you'll see under SimpleMediaSource dummy devices
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

The above Custom Media Source registers under KSCATEGORY\_VIDEO, KSCATEGORY\_CAPTURE and KSCATEGORY\_VIDEO\_CAMERA to ensure the "camera" is discoverable by any UWP and non-UWP apps searching for a standard RGB camera.

If the Custom Media Source also exposes non-RGB streams (IR, Depth, and so on) it may optionally also register under the KSCATEGORY\_SENSOR\_CAMERA.

> [!NOTE]
> Most USB based webcams will expose YUY2 and MJPG formats. Because of this behavior, many DirectShow/legacy applications are written with the assumption that YUY2/MJPG is available. To ensure compatibility with such application, it is recommended that YUY2 media type is made available from your Custom Media Source if legacy app compatibility is desired.

### Stub Driver Implementation

In addition to the INF, the driver stub must also register and enable the camera device interfaces. This is typically done during the DRIVER\_ADD\_DEVICE operation.

See the [DRIVER_ADD_DEVICE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_add_device) callback function for WDM based drivers and the [WdfDriverCreate](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nf-wdfdriver-wdfdrivercreate) function for UMDF/KMDF drivers.

The following is a code snip of a UMDF driver stub which handles this operation:

```C++
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
                    succeeds. So don't access the structure after that point.

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

deviceContext-&gt;PrivateDeviceData = 0;

//
// Create a device interface so that application can find and talk
// to us.
//

status = WdfDeviceCreateDeviceInterface(

device,

&CAMERA_CATEGORY,

&szReference // ReferenceString*

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

For UMDF/KMDF, see <https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicesetdevicestate>.

For WMD, see <https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iosetdeviceinterfacestate>.

## Custom Media Source DLL

The Custom Media Source is a standard inproc COM server which must implement the following interfaces:

-   IMFMediaEventGenerator

-   IMFMediaSource

-   IMFMediaSourceEx

-   IKsControl

-   IMFGetService

> [!NOTE]
> IMFMediaSourceEx inherits from IMFMediaSource and IMFMediaSource inherits from IMFMediaEventGenerator.

And each supported stream within the Custom Media Source must support the following interfaces:

-   IMFMediaEventGenerator

-   IMFMediaStream

-   IMFMediaStream2

> [!NOTE]
> IMFMediaStream2 inherits from IMFMediaStream. And IMFMediaStream inherits from IMFMediaEventGenerator.

Please refer to the MSDN documentation: <https://msdn.microsoft.com/en-us/library/windows/desktop/ms700134(v=vs.85).aspx> on how to create a Custom Media Source. The rest of this section will explain the differences needed to support your Custom Media Source with in the Frame Server framework.

### IMFGetService
-------------

IMFGetService is a mandatory interface for Frame Server Custom Media Source. IMFGetService may return MF\_E\_UNSUPPORTED\_SERVICE if your Custom Media Source do not need to expose any additional service interfaces.

Sample IMFGetService implementation with no support service interfaces:

\_Use\_decl\_annotations\_

IFACEMETHODIMP

SimpleMediaSource::GetService(

\_In\_ REFGUID guidService,

\_In\_ REFIID riid,

\_Out\_ LPVOID \* ppvObject

)

{

HRESULT hr = S\_OK;

auto lock = \_critSec.Lock();

RETURN\_IF\_FAILED (\_CheckShutdownRequiresLock());

if (!ppvObject)

{

return E\_POINTER;

}

\*ppvObject = NULL;

// We have no supported service, just return*

// MF\_E\_UNSUPPORTED\_SERVICE for all calls.*

return MF\_E\_UNSUPPORTED\_SERVICE;

}

### IMFMediaEventGenerator

As shown above, both the source and the individual streams within the source must support their own IMFMediaEventGenerator interface. The entire MF pipeline data and control flows from the source is managed through the event generator by sending specific IMFMediaEvent.

For implementing IMFMediaEventGenerator, the Custom Media Source must use the MFCreateEventQueue API to create an IMFMediaEventQueue and route all methods for IMFMediaEventGenerator to the queue object:

The IMFMediaEventGenerator has the following methods:

// IMFMediaEventGenerator

IFACEMETHOD(BeginGetEvent)(\_In\_ IMFAsyncCallback \*pCallback, \_In\_ IUnknown \*punkState);

IFACEMETHOD(EndGetEvent)(\_In\_ IMFAsyncResult \*pResult, \_COM\_Outptr\_ IMFMediaEvent \*\*ppEvent);

IFACEMETHOD(GetEvent)(DWORD dwFlags, \_Out\_ IMFMediaEvent \*\*ppEvent);

IFACEMETHOD(QueueEvent)(MediaEventType met, REFGUID guidExtendedType, HRESULT hrStatus, \_In\_opt\_ const PROPVARIANT \*pvValue);

The following code snip represents the recommended implementation of the IMFMediaEventGenerator interface. The Custom Media Source implementation will expose the IMFMediaEventGenerator interface, and the methods for that interface will be routing the requests into the IMFMediaEventQueue object created during the media source creation/initialization.

In the code snip below, \_spEventQueue object is the IMFMediaEventQueue created using the MFCreateEventQueue function:

// IMFMediaEventGenerator methods.

IFACEMETHODIMP

SimpleMediaSource::BeginGetEvent(

\_In\_ IMFAsyncCallback \*pCallback,

\_In\_ IUnknown \*punkState

)

{

HRESULT hr = S\_OK;

auto lock = \_critSec.Lock();

RETURN\_IF\_FAILED (\_CheckShutdownRequiresLock());

RETURN\_IF\_FAILED (\_spEventQueue-&gt;BeginGetEvent(pCallback, punkState));

return hr;

}

IFACEMETHODIMP

SimpleMediaSource::EndGetEvent(

\_In\_ IMFAsyncResult \*pResult,

\_COM\_Outptr\_ IMFMediaEvent \*\*ppEvent

)

{

HRESULT hr = S\_OK;

auto lock = \_critSec.Lock();

RETURN\_IF\_FAILED (\_CheckShutdownRequiresLock());

RETURN\_IF\_FAILED (\_spEventQueue-&gt;EndGetEvent(pResult, ppEvent));

return hr;

}

IFACEMETHODIMP

SimpleMediaSource::GetEvent(

DWORD dwFlags,

\_COM\_Outptr\_ IMFMediaEvent \*\*ppEvent

)

{

// NOTE:

// GetEvent can block indefinitely, so we don't hold the lock.

// This requires some juggling with the event queue pointer.

HRESULT hr = S\_OK;

ComPtr&lt;IMFMediaEventQueue&gt; spQueue;

{

auto lock = \_critSec.Lock();

RETURN\_IF\_FAILED (\_CheckShutdownRequiresLock());

spQueue = \_spEventQueue;

}

// Now get the event.

RETURN\_IF\_FAILED (\_spEventQueue-&gt;GetEvent(dwFlags, ppEvent));

return hr;

}

IFACEMETHODIMP

SimpleMediaSource::QueueEvent(

MediaEventType eventType,

REFGUID guidExtendedType,

HRESULT hrStatus,

\_In\_opt\_ PROPVARIANT const \*pvValue

)

{

HRESULT hr = S\_OK;

auto lock = \_critSec.Lock();

RETURN\_IF\_FAILED (\_CheckShutdownRequiresLock());

RETURN\_IF\_FAILED (\_spEventQueue-&gt;QueueEventParamVar(eventType, guidExtendedType, hrStatus, pvValue));

return hr;

}

### Seeking and Pausing
-----------------

Custom Media Sources supported through the Frame Server framework do not support Seek nor Pause operations. Your Custom Media Source does not need to provide support for these operations and must NOT post either the MFSourceSeeked nor MEStreamSeeked event.

IMFMediaSource::Pause should return MF\_E\_INVALID\_STATE\_TRANSITION (or MF\_E\_SHUTDOWN if the source was already shutdown).

### IKsControl

IKsControl is the standard control interface for all camera related controls. If your Custom Media Source implements any camera controls the IKsControl interface is how the pipeline will route the control I/O.

See the following MSDN documentation:

| Control Set                            | MSDN Link                                                                                                |
|----------------------------------------|----------------------------------------------------------------------------------------------------------|
| PROPSETID\_VIDCAP\_CAMERACONTROL       | <https://docs.microsoft.com/en-us/windows-hardware/drivers/stream/propsetid-vidcap-cameracontrol>        |
| PROPSETID\_VIDCAP\_VIDEOPROCAMP        | <https://docs.microsoft.com/en-us/windows-hardware/drivers/stream/propsetid-vidcap-videoprocamp>         |
| KSPROPERTYSETID\_ExtendedCameraControl | <https://docs.microsoft.com/en-us/windows-hardware/drivers/stream/kspropertysetid-extendedcameracontrol> |

The controls are optional and if not supported, the recommended error code to return is HRESULT\_FROM\_WIN32(ERROR\_SET\_NOT\_FOUND).

Sample IKsControl implementation with no supported controls:

// IKsControl methods

\_Use\_decl\_annotations\_

IFACEMETHODIMP

SimpleMediaSource::KsProperty(

\_In\_reads\_bytes\_(ulPropertyLength) PKSPROPERTY pProperty,

\_In\_ ULONG ulPropertyLength,

\_Inout\_updates\_to\_(ulDataLength, \*pBytesReturned) LPVOID pPropertyData,

\_In\_ ULONG ulDataLength,

\_Out\_ ULONG\* pBytesReturned

)

{

// ERROR\_SET\_NOT\_FOUND is the standard error code returned

// by the AV Stream driver framework when a miniport

// driver does not register a handler for a KS operation.

// We want to mimic the driver behavior here if we don't

// support controls.

return HRESULT\_FROM\_WIN32(ERROR\_SET\_NOT\_FOUND);

}

\_Use\_decl\_annotations\_

IFACEMETHODIMP SimpleMediaSource::KsMethod(

\_In\_reads\_bytes\_(ulMethodLength) PKSMETHOD pMethod,

\_In\_ ULONG ulMethodLength,

\_Inout\_updates\_to\_(ulDataLength, \*pBytesReturned) LPVOID pMethodData,

\_In\_ ULONG ulDataLength,

\_Out\_ ULONG\* pBytesReturned

)

{

return HRESULT\_FROM\_WIN32(ERROR\_SET\_NOT\_FOUND);

}

\_Use\_decl\_annotations\_

IFACEMETHODIMP SimpleMediaSource::KsEvent(

\_In\_reads\_bytes\_opt\_(ulEventLength) PKSEVENT pEvent,

\_In\_ ULONG ulEventLength,

\_Inout\_updates\_to\_(ulDataLength, \*pBytesReturned) LPVOID pEventData,

\_In\_ ULONG ulDataLength,

\_Out\_opt\_ ULONG\* pBytesReturned

)

{

return HRESULT\_FROM\_WIN32(ERROR\_SET\_NOT\_FOUND);

}

### IMFMediaStream2

As explained in the MSDN documentation on Writing a Custom Media Source, the IMFMediaStream2 interface is provided to the frame work from your Custom Media Source via an MENewStream media event posted to the source event queue during the completion of the IMFMediaSource::Start method:

IFACEMETHODIMP

SimpleMediaSource::Start(

\_In\_ IMFPresentationDescriptor \*pPresentationDescriptor,

\_In\_opt\_ const GUID \*pguidTimeFormat,

\_In\_ const PROPVARIANT \*pvarStartPos

)

{

HRESULT hr = S\_OK;

auto lock = \_critSec.Lock();

DWORD count = 0;

PROPVARIANT startTime;

BOOL selected = false;

ComPtr&lt;IMFStreamDescriptor&gt; streamDesc;

DWORD streamIndex = 0;

if (pPresentationDescriptor == nullptr || pvarStartPos == nullptr)

{

return E\_INVALIDARG;

}

else if (pguidTimeFormat != nullptr && \*pguidTimeFormat != GUID\_NULL)

{

return MF\_E\_UNSUPPORTED\_TIME\_FORMAT;

}

RETURN\_IF\_FAILED (\_CheckShutdownRequiresLock());

if (\_sourceState != SourceState::Stopped)

{

return MF\_E\_INVALID\_STATE\_TRANSITION;

}

\_sourceState = SourceState::Started;

// This checks the passed in PresentationDescriptor matches the member of streams we *

// have defined internally and that at least one stream is selected*

RETURN\_IF\_FAILED (\_ValidatePresentationDescriptor(pPresentationDescriptor));

RETURN\_IF\_FAILED (pPresentationDescriptor-&gt;GetStreamDescriptorCount(&count));

RETURN\_IF\_FAILED (InitPropVariantFromInt64(MFGetSystemTime(), &startTime));

// Send event that the source started. Include error code in case it failed.*

RETURN\_IF\_FAILED (\_spEventQueue-&gt;QueueEventParamVar(MESourceStarted,

GUID\_NULL,

hr,

&startTime));

// We're hardcoding this to the first descriptor*

// since this sample is a single stream sample. For*

// multiple streams, we need to walk the list of streams*

// and for each selected stream, send the MEUpdatedStream*

// or MENewStream event along with the MEStreamStarted*

// event.*

RETURN\_IF\_FAILED (pPresentationDescriptor-&gt;GetStreamDescriptorByIndex(0,

&selected,

&streamDesc));

RETURN\_IF\_FAILED (streamDesc-&gt;GetStreamIdentifier(&streamIndex));

if (streamIndex &gt;= NUM\_STREAMS)

{

return MF\_E\_INVALIDSTREAMNUMBER;

}

if (selected)

{

ComPtr&lt;IUnknown&gt; spunkStream;

MediaEventType met = (\_wasStreamPreviouslySelected ? MEUpdatedStream : MENewStream);

// Update our internal PresentationDescriptor*

RETURN\_IF\_FAILED (\_spPresentationDescriptor-&gt;SelectStream(streamIndex));

RETURN\_IF\_FAILED (\_stream.Get()-&gt;SetStreamState(MF\_STREAM\_STATE\_RUNNING));

RETURN\_IF\_FAILED (\_stream.As(&spunkStream));

// Send the MEUpdatedStream/MENewStream to our source event*

// queue.*

RETURN\_IF\_FAILED (\_spEventQueue-&gt;QueueEventParamUnk(met,

GUID\_NULL,

S\_OK,

spunkStream.Get()));

// But for our stream started (MEStreamStarted), we post to our*

// stream event queue.*

RETURN\_IF\_FAILED (\_stream.Get()-&gt;QueueEvent(MEStreamStarted,

GUID\_NULL,

S\_OK,

&startTime));

}

\_wasStreamPreviouslySelected = selected;

return hr;

}

This must be done for each stream selected via the IMFPresentationDescriptor.

For Custom Media Sources with video stream, MEEndOfStream and MEEndOfPresentation events should not be sent.

### Stream Attributes

All Custom Media Source streams must have the MF\_DEVICESTREAM\_STREAM\_CATEGORY set to be PINNAME\_VIDEO\_CAPTURE. PINNAME\_VIDEO\_PREVIEW is NOT supported for Custom Media Sources.

> [!NOTE]
> PINNAME\_IMAGE, while supported is not recommended. Exposing a stream with PINNAME\_IMAGE requires the Custom Media Source to support all the photo trigger controls. See the section Photo Stream Controls for more details.

MF\_DEVICESTREAM\_STREAM\_ID is a mandatory attribute for all streams. It should be a 0-based index. So the first stream has an ID of 0, second stream an ID of 1, etc…

The following are a list of recommended attributes on the stream:

-   MF\_DEVICESTREAM\_ATTRIBUTE\_FRAMESOURCE\_TYPES

-   MF\_DEVICESTREAM\_FRAMESERVER\_SHARED

#### MF\_DEVICESTREAM\_ATTRIBUTE\_FRAMESOURCE\_TYPES

MF\_DEVICESTREAM\_ATTRIBUTE\_FRAMESOURCE\_TYPES is a UINT32 attribute which is a bitmasked value of stream type. It may be set to any of the following (while these types are a bitmask flag, it is recommend that source types not be mixed if at all possible):

| Type                         | Flag   | Description                                      |
|------------------------------|--------|--------------------------------------------------|
| MFFrameSourceTypes\_Color    | 0x0001 | Standard RGB color stream                        |
| MFFrameSourceTypes\_Infrared | 0x0002 | IR stream                                        |
| MFFrameSourceTypes\_Depth    | 0x0004 | Depth stream                                     |
| MFFrameSourceTypes\_Image    | 0x0008 | Image stream (non-video subtype, typically JPEG) |
| MFFrameSourceTypes\_Custom   | 0x0080 | Custom stream type                               |

#### MF\_DEVICESTREAM\_FRAMESERVER\_SHARED

The MF\_DEVICESTREAM\_FRAMESERVER\_SHARED is a UINT32 attribute which can be set to either 0 or 1. If set to 1, it marks the stream as being "shareable" by the Frame Server. This will allow applications to open the stream in a shared mode, even when used by another app.

If this attribute is not set, Frame Server will allow the first non-marked stream to be shared (if the Custom Media Source has only one stream, that stream will be marked as shared).

If this attribute is set to 0, Frame Server will block the stream from shared apps. If the Custom Media Source marks all streams with this attribute set to 0, no shared application will be able to initialize the source.

### Sample Allocation

All media frames must be produced as an IMFSample. Custom Media Sources must use the MFCreateSample function to allocate an instance of IMFSample and use the AddBuffer method to add media buffers.

Each IMFSample must have the sample time and sample duration set. All sample timestamps must be based on QPC time (QueryPerformanceCounter).

It is recommended that Custom Media Sources use the MFGetSystemTime() function where possible. This function is a wrapper around QueryPerformanceCounter and converts the QPC ticks to 100ns units.

Custom Media Sources may use an internal clock, but all timestamps must be correlated to 100ns units based on the current QPC.

#### Media Buffer

All media buffers added to the IMFSample must use the standard MF buffer allocation functions. Custom Media Sources must not implement their own IMFMediaBuffer interfaces nor attempt to allocate media buffer directly (i.e., new/malloc/VirtualAlloc/et. al. must not be used for frame data).

Use any of the following APIs to allocate media frames:

-   MFCreateMemoryBuffer

-   MFCreateAlignedMemoryBuffer

-   MFCreate2DMediaBuffer

-   MFCreateDXGISurfaceBuffer

MFCreateMemoryBuffer and MFCreateAlignedMemoryBuffer should be used for non-stride aligned media data. Typically these would be custom subtypes or compressed subtypes (such as H264/HEVC/MJPG).

For known uncompressed media types (such as YUY2, NV12, etc…) using system memory, it is recommended to use MFCreate2DMediaBuffer.

For using DX surfaces (for GPU accelerated operations such as rendering and/or encoding), MFCreateDXGISurfaceBuffer should be used.

MFCreateDXGISurfaceBuffer does not create the DX surface. The surface is created using the DXGI Manager passed into the media source via the IMFMediaSourceEx::SetD3DManager method.

The IMFDXGIDeviceManager::OpenDeviceHandle() will provide the handle associated with the selected D3D device. The ID3D11Device interface can be then obtained using the IMFDXGIDeviceManager::GetVideoService method.

Regardless of what type of buffer is used, the IMFSample created must be provided to the pipeline through the MEMediaSample event on the IMFMediaEventGenerator of the media stream.

While it is possible to use the same IMFMediaEventQueue for both the Custom Media Source and the underlying collection of IMFMediaStream, it should be noted that doing so will result in serialization of the media source events and stream events (which includes the media flow). For sources with multiple streams, this is not desirable.

The following code snip shows a sample implementation of the media stream:

IFACEMETHODIMP

SimpleMediaStream::RequestSample(

\_In\_ IUnknown \*pToken

)

{

HRESULT hr = S\_OK;

auto lock = \_critSec.Lock();

ComPtr&lt;IMFSample&gt; sample;

ComPtr&lt;IMFMediaBuffer&gt; outputBuffer;

LONG pitch = IMAGE\_ROW\_SIZE\_BYTES;

BYTE \*bufferStart = nullptr; // not used*

DWORD bufferLength = 0;

BYTE \*pbuf = nullptr;

ComPtr&lt;IMF2DBuffer2&gt; buffer2D;

RETURN\_IF\_FAILED (\_CheckShutdownRequiresLock());

RETURN\_IF\_FAILED (MFCreateSample(&sample));

RETURN\_IF\_FAILED (MFCreate2DMediaBuffer(NUM\_IMAGE\_COLS,

NUM\_IMAGE\_ROWS,

D3DFMT\_X8R8G8B8,

false,

&outputBuffer));

RETURN\_IF\_FAILED (outputBuffer.As(&buffer2D));

RETURN\_IF\_FAILED (buffer2D-&gt;Lock2DSize(MF2DBuffer\_LockFlags\_Write,

&pbuf,

&pitch,

&bufferStart,

&bufferLength));

RETURN\_IF\_FAILED (WriteSampleData(pbuf, pitch, bufferLength));

RETURN\_IF\_FAILED (buffer2D-&gt;Unlock2D());

RETURN\_IF\_FAILED (sample-&gt;AddBuffer(outputBuffer.Get()));

RETURN\_IF\_FAILED (sample-&gt;SetSampleTime(MFGetSystemTime()));

RETURN\_IF\_FAILED (sample-&gt;SetSampleDuration(333333));

if (pToken != nullptr)

{

RETURN\_IF\_FAILED (sample-&gt;SetUnknown(MFSampleExtension\_Token, pToken));

}

RETURN\_IF\_FAILED (\_spEventQueue-&gt;QueueEventParamUnk(MEMediaSample,

GUID\_NULL,

S\_OK,

sample.Get()));

return hr;

}

## Windows 10, version 1809 Extension

In addition to the above list of interface that must be supported for a Custom Media Source, one of the limitations imposed by Custom Media Source operation within the Frame Server architecture is that there can only be one instance of the UMDF driver "activated" through the pipeline.

For example, if you have a physical device which installs a UMDF stub driver in addition to it’s non-AV Stream driver package, and you attach more than one of those physical devices to a computer, while each instance of the UMDF driver will get a unique symbolic link name, the activation path for the Custom Media Source will not have a means to communicate the symbolic link name associated with the Custom Media Source at the time of creation.

Custom Media Source may look for the standard MF\_DEVSOURCE\_ATTRIBUTE\_SOURCE\_TYPE\_VIDCAP\_SYMBOLIC\_LINK attribute in the Custom Media Source’s attribute store (the attribute store returned from the Custom Media Source through the IMFMediaSourceEx::GetSourceAttributes method) at the time IMFMediaSource::Start is invoked.

However, this may result in a higher start up latency since this will defer in the HW resource acquisition to start time rather than creation/initialization time.

Because of this, in Windows 10, version 1809, Custom Media Sources may optionally expose an IMFActivate interface.

> [!NOTE] 
> IMFActivate inherits from IMFAttributes.

### IMFActivate

If the COM server for the Custom Media Source supports IMFActivate interface, the device initialization information will be provided to the COM server through the IMFAttributes inherited by the IMFActivate. So when the IMFActivate::ActivateObject is invoked, the attribute store of the IMFActivate will contain the symbolic link name of the UMDF stub driver and any additional configuration settings provided by the pipeline/application at the time of the the source creation/initialization.

The Custom Media Source should use this method invocation to acquire any hardware resources it needs.

> [!NOTE]
> If the hardware resource acquisition takes greater than 200 milliseconds, it is recommended hardware resource is asynchronously acquired. The activation of the Custom Media Source should not block on the hardware resource acquisition. Instead IMFMediaSource::Start operation should be serialized against the hardware resource acquisition.

The two additional methods exposed by IMFActivate: DetachObject and ShutdownObject must return E\_NOTIMPL.

The Custom Media Source may choose to implement the IMFActivate and IMFAttributes interface within the same COM object as the IMFMediaSource. If this is done, it is recommended the IMFMediaSourceEx::GetSourceAttributes return the same IMFAttributes interface as those from the IMFActivate.

If the Custom Media Source does NOT implement the IMFActivate and IMFAttributes with the same object, the Custom Media Source must copy all the attributes set on the IMFActivate’s attribute store into the Custom Media Source’s source attribute store.

## Encoded Camera Stream

A Custom Media Source may expose compressed media types (HEVC or H264 elementary streams) and the OS pipeline fully supports the source and configuration of the encoding parameters on the Custom Media Source (the encoding parameters are communicated through the ICodecAPI, which is routed as an IKsControl::KsProperty call):

// IKsControl methods

\_Use\_decl\_annotations\_

IFACEMETHODIMP

SimpleMediaSource::KsProperty(

\_In\_reads\_bytes\_(ulPropertyLength) PKSPROPERTY pProperty,

\_In\_ ULONG ulPropertyLength,

\_Inout\_updates\_to\_(ulDataLength, \*pBytesReturned) LPVOID pPropertyData,

\_In\_ ULONG ulDataLength,

\_Out\_ ULONG\* pBytesReturned

);

The KSPROPERTY structure passed into the IKsControl::KsProperty method will have the following information:

KSPROPERTY.Set = Encoder Property GUID

KSPROPERTY.Id = 0

KSPROPERTY.Flags = (KSPROPERTY\_TYPE\_SET or KSPROPERTY\_TYPE\_GET).

Where Encoder Property GUID is the list of available properties defined in <https://msdn.microsoft.com/en-us/library/windows/desktop/dd387885(v=vs.85).aspx>.

The payload of the Encoder Property will be passed in through the *pPropertyData* field of the KsProperty method declared above.

### Capture Engine Requirements

While encoded sources are fully supported by Frame Server, the client side Capture Engine (IMFCaptureEngine) which is used by the Windows.Media.Capture.MediaCapture object imposes additional requirements:

-   Stream must either be all encoded (HEVC or H264) or all uncompressed (in this context MJPG is treated as uncompressed).

-   There must be at least one uncompressed stream available.

> [!NOTE]
> These requirements are in addition to the Custom Media Source requirements in this document. However, the Capture Engine Requirements are only enforced when the client application uses the Custom Media Source via the IMFCaptureEngine or Windows.Media.Capture.MediaCapture API.

## Camera Profiles (available in Windows 10, version 1803 and later)

Camera Profile support is available for Custom Media Sources. The recommended mechanism is to publish the profile through the MF\_DEVICEMFT\_SENSORPROFILE\_COLLECTION attribute off the source attribute (IMFMediaSourceEx::GetSourceAttributes).

The MF\_DEVICEMFT\_SENSORPROFILE\_COLLECTION attribute is an IUnknown of the IMFSensorProfileCollection interface. IMFSensorProfileCollection can be obtained using the MFCreateSensorProfileCollection function:

IFACEMETHODIMP

SimpleMediaSource::GetSourceAttributes(

\_COM\_Outptr\_ IMFAttributes\*\* sourceAttributes

)

{

HRESULT hr = S\_OK;

auto lock = \_critSec.Lock();

if (nullptr == sourceAttributes)

{

return E\_POINTER;

}

RETURN\_IF\_FAILED (\_CheckShutdownRequiresLock());

\*sourceAttributes = nullptr;

if (\_spAttributes.Get() == nullptr)

{

ComPtr&lt;IMFSensorProfileCollection&gt; profileCollection;

ComPtr&lt;IMFSensorProfile&gt; profile;

// Create our source attribute store.*

RETURN\_IF\_FAILED (MFCreateAttributes(\_spAttributes.GetAddressOf(), 1));

// Create an empty profile collection...*

RETURN\_IF\_FAILED (MFCreateSensorProfileCollection(&profileCollection));

// In this example since we have just one stream, we only have one*

// pin to add: Pin0.*

// Legacy profile is mandatory. This is to ensure non-profile*

// aware applications can still function, but with degraded*

// feature sets.*

RETURN\_IF\_FAILED (MFCreateSensorProfile(KSCAMERAPROFILE\_Legacy, 0, nullptr,

profile.ReleaseAndGetAddressOf()));

RETURN\_IF\_FAILED (profile-&gt;AddProfileFilter(0, L"((RES==;FRT&lt;=30,1;SUT==))"));

RETURN\_IF\_FAILED (profileCollection-&gt;AddProfile(profile.Get()));

// High Frame Rate profile will only allow &gt;=60fps.*

RETURN\_IF\_FAILED (MFCreateSensorProfile(KSCAMERAPROFILE\_HighFrameRate, 0, nullptr,

profile.ReleaseAndGetAddressOf()));

RETURN\_IF\_FAILED (profile-&gt;AddProfileFilter(0, L"((RES==;FRT&gt;=60,1;SUT==))"));

RETURN\_IF\_FAILED (profileCollection-&gt;AddProfile(profile.Get()));

// Se the profile collection to the attribute store of the IMFTransform.*

RETURN\_IF\_FAILED (\_spAttributes-&gt;SetUnknown(MF\_DEVICEMFT\_SENSORPROFILE\_COLLECTION,

profileCollection.Get()));

}

return \_spAttributes.CopyTo(sourceAttributes);

}

### Face Auth Profile

If the Custom Media Source is designed to support Windows Hello Facial Recognition, then it is recommended to publish a Face Auth Profile. The requirements of Face Auth Profile are:

-   Face Auth DDI Control must be supported on a single IR stream (see <https://docs.microsoft.com/en-us/windows-hardware/drivers/stream/ksproperty-cameracontrol-extended-faceauth-mode> for Face Auth DDI control)

-   IR stream must be at east 340x340 at 15fps. The format must be either L8, NV12 or MJPG marked with L8 compression.

-   RGB stream must be at least 480x480 at 7.5fps (this is only needed if Multispectrum authentication is enforced).

-   Face Auth Profile must have the Profile ID of: KSCAMERAPROFILE\_FaceAuth\_Mode,0.

It is recommended that the Face Auth Profile only advertise one media type for each of the IR and RGB streams.

## Photo Stream Controls

If independent photo streams are exposed by marking one of the stream’s MF\_DEVICESTREAM\_STREAM\_CATEGORY as PINNAME\_IMAGE, then a stream with stream category of PINNAME\_VIDEO\_CAPTURE is required (i.e., a single stream exposing just the PINNAME\_IMAGE is not a valid media source).

Through the IKsControl, the PROPSETID\_VIDCAP\_VIDEOCONTROL property set must be supported (see <https://docs.microsoft.com/en-us/windows-hardware/drivers/stream/video-control-properties> for details).
