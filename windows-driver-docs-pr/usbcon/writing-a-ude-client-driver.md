---
title: Write a UDE Client Driver
description: This article describes the behavior of USB device emulation(UDE) class extension and tasks that a client driver must perform for an emulated host controller and devices attached to it.
ms.date: 01/17/2024
---

# Write a UDE client driver

This article describes the behavior of USB device emulation(UDE) class extension and tasks that a client driver must perform for an emulated host controller and devices attached to it. It provides information about how the class driver and class extension communicate with each through a set of routines and callback functions. It also describes the features that the client driver is expected to implement.

## Summary

- UDE objects and handles used by the class extension and client driver.
- Creating an emulated host controller with features to query controller capabilities and reset the controller.
- Creating a virtual USB device, setting it up for power management and data transfers through endpoints.

## Important APIs

- [Emulated USB host controller driver programming reference](/windows-hardware/drivers/ddi/_usbref/#emulated-host-controller-driver-reference)

## Before you begin

- [Install](../download-the-wdk.md) the latest Windows Driver Kit (WDK) your development computer. The kit has the required header files and libraries for writing a UDE client driver, specifically, you'll need:
  - The stub library, (Udecxstub.lib). The library translates calls made by the client driver and pass them up to UdeCx.
  - The header file, Udecx.h.
- Install Windows 10 on your target computer.
- Familiarize yourself with UDE. See [Architecture: USB Device Emulation(UDE)](usb-emulated-device--ude--architecture.md).
- Familiarize yourself with Windows Driver Foundation (WDF). Recommended reading: [Developing Drivers with Windows Driver Foundation](/windows-hardware/drivers/wdf/developing-drivers-with-wdf), written by Penny Orwick and Guy Smith.

## UDE objects and handles

UDE class extension and the client driver use particular WDF objects that represent the emulated host controller and the virtual device, including its endpoints and URBs that are used to transfer data between the device and the host. The client driver requests the creation of the objects and lifetime of the object is managed by the class extension.

- **Emulated host controller object (WDFDEVICE)**

    Represents the emulated host controller and is the main handle between the UDE class extension and the client driver.

- **UDE device object (UDECXUSBDEVICE)**

    Represents a virtual USB device that is connected to a port on the emulated host controller.

- **UDE endpoint object (UDECXUSBENDPOINT)**

    Represent sequential data pipes of USB devices. Used to receive software requests to send or receive data on an endpoint.

## Initialize the emulated host controller

Here is the summary of the sequence in which the client driver retrieves a WDFDEVICE handle for the emulated host controller. We recommend that the driver perform these tasks in its *[EvtDriverDeviceAdd](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add)* callback function.

1. Call **[UdecxInitializeWdfDeviceInit](/windows-hardware/drivers/ddi/udecxwdfdevice/nf-udecxwdfdevice-udecxinitializewdfdeviceinit)** by passing the reference to [WDFDEVICE_INIT](../wdf/wdfdevice_init.md) passed by the framework.
1. Initialize the [WDFDEVICE_INIT](../wdf/wdfdevice_init.md) structure with setup information such that this device appears similar to other USB host controllers. For example assign an FDO name and a symbolic link, register a device interface with the Microsoft-provided GUID_DEVINTERFACE_USB_HOST_CONTROLLER GUID as the device interface GUID so that applications can open a handle to the device.
1. Call **[WdfDeviceCreate](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate)** to create the framework device object.
1. Call **[UdecxWdfDeviceAddUsbDeviceEmulation](/windows-hardware/drivers/ddi/udecxwdfdevice/nf-udecxwdfdevice-udecxwdfdeviceaddusbdeviceemulation)** and register the client driver's callback functions.

    Here are the callback functions associated with the host controller object, which are invoked by UDE class extension. These functions must be implemented by the client driver.

    - *[EVT_UDECX_WDF_DEVICE_QUERY_USB_CAPABILITY](/windows-hardware/drivers/ddi/udecxwdfdevice/nc-udecxwdfdevice-evt_udecx_wdf_device_query_usb_capability)*

      Determines the capabilities supported by the host controller that the client driver must report to the class extension.

    - *[EVT_UDECX_WDF_DEVICE_RESET](/windows-hardware/drivers/ddi/udecxwdfdevice/nc-udecxwdfdevice-evt_udecx_wdf_device_reset)*

      Optional. Resets the host controller and/or the connected devices.

    ```cpp

    EVT_WDF_DRIVER_DEVICE_ADD                 Controller_WdfEvtDeviceAdd;

    #define BASE_DEVICE_NAME                  L"\\Device\\USBFDO-"
    #define BASE_SYMBOLIC_LINK_NAME           L"\\DosDevices\\HCD"

    #define DeviceNameSize                    sizeof(BASE_DEVICE_NAME)+MAX_SUFFIX_SIZE
    #define SymLinkNameSize                   sizeof(BASE_SYMBOLIC_LINK_NAME)+MAX_SUFFIX_SIZE

    NTSTATUS
    Controller_WdfEvtDeviceAdd(
        _In_
            WDFDRIVER Driver,
        _Inout_
            PWDFDEVICE_INIT WdfDeviceInit
        )
    {
        NTSTATUS                            status;
        WDFDEVICE                           wdfDevice;
        WDF_PNPPOWER_EVENT_CALLBACKS        wdfPnpPowerCallbacks;
        WDF_OBJECT_ATTRIBUTES               wdfDeviceAttributes;
        WDF_OBJECT_ATTRIBUTES               wdfRequestAttributes;
        UDECX_WDF_DEVICE_CONFIG             controllerConfig;
        WDF_FILEOBJECT_CONFIG               fileConfig;
        PWDFDEVICE_CONTEXT                  pControllerContext;
        WDF_IO_QUEUE_CONFIG                 defaultQueueConfig;
        WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS
                                            idleSettings;
        UNICODE_STRING                      refString;
        ULONG instanceNumber;
        BOOLEAN isCreated;

        DECLARE_UNICODE_STRING_SIZE(uniDeviceName, DeviceNameSize);
        DECLARE_UNICODE_STRING_SIZE(uniSymLinkName, SymLinkNameSize);

        UNREFERENCED_PARAMETER(Driver);

        ...

        WdfDeviceInitSetPnpPowerEventCallbacks(WdfDeviceInit, &wdfPnpPowerCallbacks);

        WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&wdfRequestAttributes, REQUEST_CONTEXT);
        WdfDeviceInitSetRequestAttributes(WdfDeviceInit, &wdfRequestAttributes);

    // To distinguish I/O sent to GUID_DEVINTERFACE_USB_HOST_CONTROLLER, we will enable
    // enable interface reference strings by calling WdfDeviceInitSetFileObjectConfig
    // with FileObjectClass WdfFileObjectWdfXxx.

    WDF_FILEOBJECT_CONFIG_INIT(&fileConfig,
                                WDF_NO_EVENT_CALLBACK,
                                WDF_NO_EVENT_CALLBACK,
                                WDF_NO_EVENT_CALLBACK // No cleanup callback function
                                );

    ...

    WdfDeviceInitSetFileObjectConfig(WdfDeviceInit,
                                        &fileConfig,
                                        WDF_NO_OBJECT_ATTRIBUTES);

    ...

    // Do additional setup required for USB controllers.

    status = UdecxInitializeWdfDeviceInit(WdfDeviceInit);

    ...

    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&wdfDeviceAttributes, WDFDEVICE_CONTEXT);
    wdfDeviceAttributes.EvtCleanupCallback = _ControllerWdfEvtCleanupCallback;

    // Call WdfDeviceCreate with a few extra compatibility steps to ensure this device looks
    // exactly like other USB host controllers.

    isCreated = FALSE;

    for (instanceNumber = 0; instanceNumber < ULONG_MAX; instanceNumber++) {

        status = RtlUnicodeStringPrintf(&uniDeviceName,
                                        L"%ws%d",
                                        BASE_DEVICE_NAME,
                                        instanceNumber);

        ...

        status = WdfDeviceInitAssignName(*WdfDeviceInit, &uniDeviceName);

        ...

        status = WdfDeviceCreate(WdfDeviceInit, WdfDeviceAttributes, WdfDevice);

        if (status == STATUS_OBJECT_NAME_COLLISION) {

            // This is expected to happen at least once when another USB host controller
            // already exists on the system.

        ...

        } else if (!NT_SUCCESS(status)) {

        ...

        } else {

            isCreated = TRUE;
            break;
        }
    }

    if (!isCreated) {

        ...
    }

    // Create the symbolic link (also for compatibility).
    status = RtlUnicodeStringPrintf(&uniSymLinkName,
                                    L"%ws%d",
                                    BASE_SYMBOLIC_LINK_NAME,
                                    instanceNumber);
    ...

    status = WdfDeviceCreateSymbolicLink(*WdfDevice, &uniSymLinkName);

    ...

    // Create the device interface.

    RtlInitUnicodeString(&refString,
                         USB_HOST_DEVINTERFACE_REF_STRING);

    status = WdfDeviceCreateDeviceInterface(wdfDevice,
                                            (LPGUID)&GUID_DEVINTERFACE_USB_HOST_CONTROLLER,
                                            &refString);

    ...

    UDECX_WDF_DEVICE_CONFIG_INIT(&controllerConfig, Controller_EvtUdecxWdfDeviceQueryUsbCapability);

    status = UdecxWdfDeviceAddUsbDeviceEmulation(wdfDevice,
                                               &controllerConfig);

    // Create default queue. It only supports USB controller IOCTLs. (USB I/O will come through
    // in separate USB device queues.)
    // Shown later in this topic.

    WDF_IO_QUEUE_CONFIG_INIT_DEFAULT_QUEUE(&defaultQueueConfig, WdfIoQueueDispatchSequential);
    defaultQueueConfig.EvtIoDeviceControl = ControllerEvtIoDeviceControl;
    defaultQueueConfig.PowerManaged = WdfFalse;

    status = WdfIoQueueCreate(wdfDevice,
                              &defaultQueueConfig,
                              WDF_NO_OBJECT_ATTRIBUTES,
                              &pControllerContext->DefaultQueue);

    ...

    // Initialize virtual USB device software objects.
    // Shown later in this topic.

    status = Usb_Initialize(wdfDevice);

    ...

    exit:

        return status;
    }
    ```1.

## Handle user-mode IOCTL requests sent to the host controller

During initialization, the UDE client driver exposes the GUID_DEVINTERFACE_USB_HOST_CONTROLLER device interface GUID. This enables the driver to receive IOCTL requests from an application that opens a device handle by using that GUID. For a list of IOCTL control codes, see [USB IOCTLs](/windows-hardware/drivers/ddi/usbioctl/#ioctls) with Device interface GUID: GUID_DEVINTERFACE_USB_HOST_CONTROLLER.

To handle those requests, the client driver registers the *[EvtIoDeviceControl](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_device_control)* event callback. In the implementation, instead of handling the request, the driver can opt to forward the request to the UDE class extension for processing. To forward the request, the driver must call **[UdecxWdfDeviceTryHandleUserIoctl](/windows-hardware/drivers/ddi/udecxwdfdevice/nf-udecxwdfdevice-udecxwdfdevicetryhandleuserioctl)**. If the received IOCTL control code corresponds to a standard request, such as retrieving device descriptors, the class extension processes and completes the request successfully. In this case, **UdecxWdfDeviceTryHandleUserIoctl** completes with TRUE as the return value. Otherwise, the call returns FALSE and the driver must determine how to complete the request. In a simplest implementation, the driver can complete the request with an appropriate failure code by calling **[WdfRequestComplete](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete)**.

```cpp

EVT_WDF_IO_QUEUE_IO_DEVICE_CONTROL        Controller_EvtIoDeviceControl;

VOID
Controller_EvtIoDeviceControl(
    _In_
        WDFQUEUE Queue,
    _In_
        WDFREQUEST Request,
    _In_
        size_t OutputBufferLength,
    _In_
        size_t InputBufferLength,
    _In_
        ULONG IoControlCode
)
{
    BOOLEAN handled;
    NTSTATUS status;
    UNREFERENCED_PARAMETER(OutputBufferLength);
    UNREFERENCED_PARAMETER(InputBufferLength);

    handled = UdecxWdfDeviceTryHandleUserIoctl(WdfIoQueueGetDevice(Queue),
                                                Request);

    if (handled) {

        goto exit;
    }

    // Unexpected control code.
    // Fail the request.

    status = STATUS_INVALID_DEVICE_REQUEST;

    WdfRequestComplete(Request, status);

exit:

    return;
}
```

## Report the capabilities of the host controller

Before upper layer drivers can use the capabilities of a USB host controller, the drivers must determine whether those capabilities are supported by the controller. Drivers make such queries by calling **[WdfUsbTargetDeviceQueryUsbCapability](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability)** and **[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)**. Those calls are forwarded to the USB Device Emulation(UDE) class extension. Upon getting the request, the class extension invokes the client driver's *[EVT_UDECX_WDF_DEVICE_QUERY_USB_CAPABILITY](/windows-hardware/drivers/ddi/udecxwdfdevice/nc-udecxwdfdevice-evt_udecx_wdf_device_query_usb_capability)* implementation. This call is made only after *[EvtDriverDeviceAdd](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add)* completes, typically in *[EvtDevicePrepareHardware](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware)* and not after *[EvtDeviceReleaseHardware](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware)*. This is callback function is required.

In the implementation, the client driver must report whether it supports the requested capability. Certain capabilities are not supported by UDE such as static streams.

```cpp
NTSTATUS
Controller_EvtControllerQueryUsbCapability(
    WDFDEVICE     UdeWdfDevice,
    PGUID         CapabilityType,
    ULONG         OutputBufferLength,
    PVOID         OutputBuffer,
    PULONG        ResultLength
)

{
    NTSTATUS status;

    UNREFERENCED_PARAMETER(UdeWdfDevice);
    UNREFERENCED_PARAMETER(OutputBufferLength);
    UNREFERENCED_PARAMETER(OutputBuffer);

    *ResultLength = 0;

    if (RtlCompareMemory(CapabilityType,
                         &GUID_USB_CAPABILITY_CHAINED_MDLS,
                         sizeof(GUID)) == sizeof(GUID)) {

        //
        // TODO: Is GUID_USB_CAPABILITY_CHAINED_MDLS supported?
        // If supported, status = STATUS_SUCCESS
        // Otherwise, status = STATUS_NOT_SUPPORTED
    }

    else {

        status = STATUS_NOT_IMPLEMENTED;
    }

    return status;
}
```

## Create a virtual USB device

A virtual USB device behaves similar to a USB device. It supports a configuration with multiple interfaces and each interface supports alternate settings. Each setting can have one more endpoints that are used for data transfers. All descriptors (device, configuration, interface, endpoint) are set by the UDE client driver so that the device can report information much like a real USB device.

> [!NOTE]
> The UDE client driver does not support external hubs

Here is the summary of the sequence in which the client driver creates a UDECXUSBDEVICE handle for a UDE device object. The driver must perform these steps after it has retrieved the WDFDEVICE handle for the emulated host controller. We recommend that the driver perform these tasks in its *[EvtDriverDeviceAdd](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add)* callback function.

1. Call **[UdecxUsbDeviceInitAllocate](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdeviceinitallocate)** to get a pointer to the initialization parameters required to create the device. This structure is allocated by the UDE class extension.
1. Register event callback functions by setting members of **[UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS](/windows-hardware/drivers/ddi/udecxusbdevice/ns-udecxusbdevice-_udecx_usb_device_state_change_callbacks)** and then calling **[UdecxUsbDeviceInitSetStateChangeCallbacks](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdeviceinitsetstatechangecallbacks)**. Here are the callback functions associated with the UDE device object, which are invoked by the UDE class extension.

    These functions are implemented by the client driver to create or configure endpoints.

   - *[EVT_UDECX_USB_DEVICE_DEFAULT_ENDPOINT_ADD](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_default_endpoint_add)*
   - *[EVT_UDECX_USB_DEVICE_ENDPOINT_ADD](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_endpoint_add)*
   - *[EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_endpoints_configure)*
   - *[EVT_UDECX_USB_DEVICE_D0_ENTRY](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_d0_entry)*
   - *[EVT_UDECX_USB_DEVICE_D0_EXIT](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_d0_exit)*
   - *[EVT_UDECX_USB_DEVICE_SET_FUNCTION_SUSPEND_AND_WAKE](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_set_function_suspend_and_wake)*

1. Call **[UdecxUsbDeviceInitSetSpeed](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdeviceinitsetspeed)** to set the USB device speed and also the type of device, USB 2.0 or a SuperSpeed device.
1. Call **[UdecxUsbDeviceInitSetEndpointsType](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdeviceinitsetendpointstype)** to specify the type of endpoints the device supports: simple or dynamic. If the client driver chooses to create simple endpoints, the driver must create all endpoint objects before plugging in the device. The device must have only one configuration and only one interface setting per interface. In the case of dynamic endpoints, the driver can create endpoints at anytime after plugging in the device when it receives an *[EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_endpoints_configure)* event callback. See [Create dynamic endpoints](#create-dynamic-endpoints).
1. Call any of these methods to add necessary descriptors to the device.

   - **[UdecxUsbDeviceInitAddDescriptor](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdeviceinitadddescriptor)**
   - **[UdecxUsbDeviceInitAddDescriptorWithIndex](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdeviceinitadddescriptorwithindex)**
   - **[UdecxUsbDeviceInitAddStringDescriptor](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdeviceinitaddstringdescriptor)**
   - **[UdecxUsbDeviceInitAddStringDescriptorRaw](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdeviceinitaddstringdescriptorraw)**

     If the UDE class extension receives a request for a standard descriptor that the client driver has provided during initialization by using one of the preceding methods, the class extension automatically completes the request. The class extension does not forward that request to the client driver. This design reduces the number of requests that the driver needs to process for control requests. Additionally, it also eliminates the need for the driver to implement descriptor logic that requires extensive parsing of the setup packet and handling **wLength** and **TransferBufferLength** correctly. This list includes the standard requests. The client driver does not need to check for these requests (only if the preceding methods were called to add descriptor):

   - USB_REQUEST_GET_DESCRIPTOR
   - USB_REQUEST_SET_CONFIGURATION
   - USB_REQUEST_SET_INTERFACE
   - USB_REQUEST_SET_ADDRESS
   - USB_REQUEST_SET_FEATURE
   - USB_FEATURE_FUNCTION_SUSPEND
   - USB_FEATURE_REMOTE_WAKEUP
   - USB_REQUEST_CLEAR_FEATURE
   - USB_FEATURE_ENDPOINT_STALL
   - USB_REQUEST_SET_SEL
   - USB_REQUEST_ISOCH_DELAY

     However, requests for the interface, class-specific, or vendor-defined descriptor, the UDE class extension forwards them to the client driver. The driver must handle those GET_DESCRIPTOR requests.

1. Call **[UdecxUsbDeviceCreate](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdevicecreate)** to create the UDE device object and retrieve the UDECXUSBDEVICE handle.
1. Create static endpoints by calling **[UdecxUsbEndpointCreate](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointcreate)**. See [Create simple endpoints](#create-simple-endpoints).
1. Call **[UdecxUsbDevicePlugIn](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdeviceplugin)** to indicate to the UDE class extension that the device is attached and can receive I/O requests on endpoints. After this call, the class extension can also invoke callback functions on endpoints and the USB device.
    **Note**  If the USB device needs to be removed at runtime, the client driver can call **[UdecxUsbDevicePlugOutAndDelete](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdeviceplugoutanddelete)**. If the driver wants to use the device, it must create it by calling **[UdecxUsbDeviceCreate](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdevicecreate)**.

In this example, the descriptor declarations are assumed to be global variables, declared as shown here for a HID device just as an example:

```cpp
const UCHAR g_UsbDeviceDescriptor[] = {
    // Device Descriptor
    0x12, // Descriptor Size
    0x01, // Device Descriptor Type
    0x00, 0x03, // USB 3.0
    0x00, // Device class
    0x00, // Device sub-class
    0x00, // Device protocol
    0x09, // Maxpacket size for EP0 : 2^9
    0x5E, 0x04, // Vendor ID
    0x39, 0x00, // Product ID
    0x00, // LSB of firmware version
    0x03, // MSB of firmware version
    0x01, // Manufacture string index
    0x03, // Product string index
    0x00, // Serial number string index
    0x01 // Number of configurations
};
```

Here is an example in which the client driver specifies initialization parameters by registering callback functions, setting device speed, indicating the type of endpoints, and finally setting some device descriptors.

```cpp

NTSTATUS
Usb_Initialize(
    _In_
        WDFDEVICE WdfDevice
    )
{
    NTSTATUS                                status;
    PUSB_CONTEXT                            usbContext;    //Client driver declared context for the host controller object
    PUDECX_USBDEVICE_CONTEXT                deviceContext; //Client driver declared context for the UDE device object
    UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS callbacks;
    WDF_OBJECT_ATTRIBUTES                   attributes;

    UDECX_USB_DEVICE_PLUG_IN_OPTIONS        pluginOptions;

    usbContext = WdfDeviceGetUsbContext(WdfDevice);

    usbContext->UdecxUsbDeviceInit = UdecxUsbDeviceInitAllocate(WdfDevice);

    if (usbContext->UdecxUsbDeviceInit == NULL) {

        ...
        goto exit;
    }

    // State changed callbacks

    UDECX_USB_DEVICE_CALLBACKS_INIT(&callbacks);
#ifndef SIMPLEENDPOINTS
    callbacks.EvtUsbDeviceDefaultEndpointAdd = UsbDevice_EvtUsbDeviceDefaultEndpointAdd;
    callbacks.EvtUsbDeviceEndpointAdd = UsbDevice_EvtUsbDeviceEndpointAdd;
    callbacks.EvtUsbDeviceEndpointsConfigure = UsbDevice_EvtUsbDeviceEndpointsConfigure;
#endif
    callbacks.EvtUsbDeviceLinkPowerEntry = UsbDevice_EvtUsbDeviceLinkPowerEntry;
    callbacks.EvtUsbDeviceLinkPowerExit = UsbDevice_EvtUsbDeviceLinkPowerExit;
    callbacks.EvtUsbDeviceSetFunctionSuspendAndWake = UsbDevice_EvtUsbDeviceSetFunctionSuspendAndWake;

    UdecxUsbDeviceInitSetStateChangeCallbacks(usbContext->UdecxUsbDeviceInit, &callbacks);

    // Set required attributes.

    UdecxUsbDeviceInitSetSpeed(usbContext->UdecxUsbDeviceInit, UdecxUsbLowSpeed);

#ifdef SIMPLEENDPOINTS
    UdecxUsbDeviceInitSetEndpointsType(usbContext->UdecxUsbDeviceInit, UdecxEndpointTypeSimple);
#else
    UdecxUsbDeviceInitSetEndpointsType(usbContext->UdecxUsbDeviceInit, UdecxEndpointTypeDynamic);
#endif

    // Add device descriptor
    //
    status = UdecxUsbDeviceInitAddDescriptor(usbContext->UdecxUsbDeviceInit,
                                           (PUCHAR)g_UsbDeviceDescriptor,
                                           sizeof(g_UsbDeviceDescriptor));

    if (!NT_SUCCESS(status)) {

        goto exit;
    }

#ifdef USB30

    // Add BOS descriptor for a SuperSpeed device

    status = UdecxUsbDeviceInitAddDescriptor(pUsbContext->UdecxUsbDeviceInit,
                                           (PUCHAR)g_UsbBOSDescriptor,
                                           sizeof(g_UsbBOSDescriptor));

    if (!NT_SUCCESS(status)) {

        goto exit;
    }
#endif

    // String descriptors

    status = UdecxUsbDeviceInitAddDescriptorWithIndex(usbContext->UdecxUsbDeviceInit,
                                                    (PUCHAR)g_LanguageDescriptor,
                                                    sizeof(g_LanguageDescriptor),
                                                    0);

    if (!NT_SUCCESS(status)) {

        goto exit;
    }

    status = UdecxUsbDeviceInitAddStringDescriptor(usbContext->UdecxUsbDeviceInit,
                                                 &g_ManufacturerStringEnUs,
                                                 g_ManufacturerIndex,
                                                 US_ENGLISH);

    if (!NT_SUCCESS(status)) {

        goto exit;
    }

    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attributes, UDECX_USBDEVICE_CONTEXT);

    status = UdecxUsbDeviceCreate(&usbContext->UdecxUsbDeviceInit,
                                &attributes,
                                &usbContext->UdecxUsbDevice);

    if (!NT_SUCCESS(status)) {

        goto exit;
    }

#ifdef SIMPLEENDPOINTS
   // Create the default control endpoint
   // Shown later in this topic.

    status = UsbCreateControlEndpoint(WdfDevice);

    if (!NT_SUCCESS(status)) {

        goto exit;
    }

#endif

    UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT(&pluginOptions);
#ifdef USB30
    pluginOptions.Usb30PortNumber = 2;
#else
    pluginOptions.Usb20PortNumber = 1;
#endif
    status = UdecxUsbDevicePlugIn(usbContext->UdecxUsbDevice, &pluginOptions);

exit:

    if (!NT_SUCCESS(status)) {

        UdecxUsbDeviceInitFree(usbContext->UdecxUsbDeviceInit);
        usbContext->UdecxUsbDeviceInit = NULL;

    }

    return status;
}
```

## Power management of the USB device

The UDE class extension invokes client driver's callback functions when it receives a request to send the device to low power state or bring it back to working state. These callback functions are required for USB devices that support wake. The client driver registered its implementation by in the previous call to **[UdecxUsbDeviceInitSetStateChangeCallbacks](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdeviceinitsetstatechangecallbacks)**.

For more information, see [USB Device Power States](comparing-usb-device-states-to-wdm-device-states.md).

- *[EVT_UDECX_USB_DEVICE_D0_ENTRY](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_d0_entry)*: The client driver transitions the device from a Dx state to D0 state.

- *[EVT_UDECX_USB_DEVICE_D0_EXIT](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_d0_exit)*: The client driver transitions the device from D0 state to a Dx state.

- *[EVT_UDECX_USB_DEVICE_SET_FUNCTION_SUSPEND_AND_WAKE](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_set_function_suspend_and_wake)*: The client driver changes the function state of the specified interface of the virtual USB 3.0 device.

A USB 3.0 device allows individual functions to enter lower power state. Each function is also capable of send a wake signal. The UDE class extension notifies the client driver by invoking *[EVT_UDECX_USB_DEVICE_SET_FUNCTION_SUSPEND_AND_WAKE](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_set_function_suspend_and_wake)*. This event indicates a function power state change and informs the client driver of whether the function can wake from the new state. In the function, the class extension passes the interface number of the function that is waking up.

The client driver can simulate the action of a virtual USB device initiating its own wake up from a low link power state, function suspend, or both. For a USB 2.0 device, the driver must call **[UdecxUsbDeviceSignalWake](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdevicesignalwake)**, if the driver enabled wake on the device in the most recent *[EVT_UDECX_USB_DEVICE_D0_EXIT](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_d0_exit)*. For a USB 3.0 device, the driver must call **[UdecxUsbDeviceSignalFunctionWake](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdevicesignalfunctionwake)** because the USB 3.0 wake feature is per-function. If the entire device is in a low power state, or entering such a state, **UdecxUsbDeviceSignalFunctionWake** wakes up the device.

## Create simple endpoints

The client driver creates UDE endpoint objects to handle data transfers to and from the USB device. The driver creates simple endpoints after creating the UDE device and before reporting the device as plugged in.

Here is the summary of the sequence in which the client driver creates a UDECXUSBENDPOINT handle for a UDE endpoint object. The driver must perform these steps after it has retrieved the UDECXUSBDEVICE handle for the virtual USB device. We recommend that the driver perform these tasks in its *[EvtDriverDeviceAdd](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add)* callback function.

1. Call **[UdecxUsbSimpleEndpointInitAllocate](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbsimpleendpointinitallocate)** to get a pointer to the initialization parameters allocated by the class extension.
1. Call **[UdecxUsbEndpointInitSetEndpointAddress](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointinitsetendpointaddress)** to set the endpoint address in the initialization parameters.
1. Call **[UdecxUsbEndpointInitSetCallbacks](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointinitsetcallbacks)** to register the client driver-implemented callback functions.

    These functions are implemented by the client driver to handle queues and requests on an endpoint.

    - *[EVT_UDECX_USB_ENDPOINT_RESET](/windows-hardware/drivers/ddi/udecxusbendpoint/nc-udecxusbendpoint-evt_udecx_usb_endpoint_reset)*: Resets an endpoint of the virtual USB device.

    - *[EVT_UDECX_USB_ENDPOINT_START](/windows-hardware/drivers/ddi/udecxusbendpoint/nc-udecxusbendpoint-evt_udecx_usb_endpoint_start)*: Optional. Starts processing I/O requests

    - *[EVT_UDECX_USB_ENDPOINT_PURGE](/windows-hardware/drivers/ddi/udecxusbendpoint/nc-udecxusbendpoint-evt_udecx_usb_endpoint_purge)*: Optional. Stop queuing I/O requests to the endpoint's queue and cancel unprocessed requests.

1. Call **[UdecxUsbEndpointCreate](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointcreate)** to create the endpoint object and retrieve the UDECXUSBENDPOINT handle.
1. Call **[UdecxUsbEndpointSetWdfIoQueue](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointsetwdfioqueue)** to associate a framework queue object with the endpoint. If applicable, it can set the endpoint object to be the WDF parent object of the queue by setting appropriate attributes.

    Every endpoint object has a framework queue object in order to handle transfer requests. For each transfer request that the class extension receives, it queues a framework request object. The state of the queue (started, purged) is managed by the UDE class extension and the client driver must not change that state. Each request object contains an USB Request Block (**[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)**) that contains details of the transfer.

In this example, the client driver creates the default control endpoint.

```cpp
EVT_WDF_IO_QUEUE_IO_INTERNAL_DEVICE_CONTROL IoEvtControlUrb;
EVT_UDECX_USB_ENDPOINT_RESET UsbEndpointReset;
EVT_UDECX_USB_ENDPOINT_PURGE UsEndpointEvtPurge;
EVT_UDECX_USB_ENDPOINT_START UsbEndpointEvtStart;

NTSTATUS
UsbCreateControlEndpoint(
    _In_
        WDFDEVICE WdfDevice
    )
{
    NTSTATUS                      status;
    PUSB_CONTEXT                  pUsbContext;
    WDF_IO_QUEUE_CONFIG           queueConfig;
    WDFQUEUE                      controlQueue;
    UDECX_USB_ENDPOINT_CALLBACKS  callbacks;
    PUDECXUSBENDPOINT_INIT        endpointInit;

    pUsbContext = WdfDeviceGetUsbContext(WdfDevice);
    endpointInit = NULL;

    WDF_IO_QUEUE_CONFIG_INIT(&queueConfig, WdfIoQueueDispatchSequential);

    queueConfig.EvtIoInternalDeviceControl = IoEvtControlUrb;

    status = WdfIoQueueCreate (Device,
                               &queueConfig,
                               WDF_NO_OBJECT_ATTRIBUTES,
                               &controlQueue);

    if (!NT_SUCCESS(status)) {

        goto exit;
    }

    endpointInit = UdecxUsbSimpleEndpointInitAllocate(pUsbContext->UdecxUsbDevice);

    if (endpointInit == NULL) {

        status = STATUS_INSUFFICIENT_RESOURCES;
        goto exit;
    }

    UdecxUsbEndpointInitSetEndpointAddress(endpointInit, USB_DEFAULT_ENDPOINT_ADDRESS);

    UDECX_USB_ENDPOINT_CALLBACKS_INIT(&callbacks, UsbEndpointReset);
    UdecxUsbEndpointInitSetCallbacks(endpointInit, &callbacks);

    callbacks.EvtUsbEndpointStart = UsbEndpointEvtStart;
    callbacks.EvtUsbEndpointPurge = UsEndpointEvtPurge;

    status = UdecxUsbEndpointCreate(&endpointInit,
        WDF_NO_OBJECT_ATTRIBUTES,
        &pUsbContext->UdecxUsbControlEndpoint);

    if (!NT_SUCCESS(status)) {
        goto exit;
    }

    UdecxUsbEndpointSetWdfIoQueue(pUsbContext->UdecxUsbControlEndpoint,
        controlQueue);

exit:

    if (endpointInit != NULL) {

        NT_ASSERT(!NT_SUCCESS(status));
        UdecxUsbEndpointInitFree(endpointInit);
        endpointInit = NULL;
    }

    return status;
}
```

## Create dynamic endpoints

The client driver can create dynamic endpoints at the request of the UDE class extension (on behalf of the hub driver and client drivers). The class extension makes the request by invoking any of these callback functions:

*[EVT_UDECX_USB_DEVICE_DEFAULT_ENDPOINT_ADD](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_default_endpoint_add)
The client driver creates the default control endpoint (Endpoint 0)

*[EVT_UDECX_USB_DEVICE_ENDPOINT_ADD](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_endpoint_add)
The client driver creates a dynamic endpoint.

*[EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_endpoints_configure)
The client driver changes the configuration by selecting an alternate setting, disabling current endpoints, or adding dynamic endpoints.

The client driver registered the preceding callback during its call to **[UdecxUsbDeviceInitSetStateChangeCallbacks](/windows-hardware/drivers/ddi/udecxusbdevice/nf-udecxusbdevice-udecxusbdeviceinitsetstatechangecallbacks)**. See Create [virtual USB device](#create-a-virtual-usb-device).
This mechanism allows the client driver to dynamically change the USB configuration and interface settings on the device. For example, when a endpoint object is needed or an existing endpoint object must be released, the class extension calls the *[EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE](/windows-hardware/drivers/ddi/udecxusbdevice/nc-udecxusbdevice-evt_udecx_usb_device_endpoints_configure)*.

Here is the summary of the sequence in which the client driver creates a UDECXUSBENDPOINT handle for an endpoint object in its implementation of the callback function.

1. Call **[UdecxUsbEndpointInitSetEndpointAddress](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointinitsetendpointaddress)** to set the endpoint address in the initialization parameters.
1. Call **[UdecxUsbEndpointInitSetCallbacks](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointinitsetcallbacks)** to register the client driver-implemented callback functions. Similar to simple endpoints, the driver can register these callback functions:
    - *[EVT_UDECX_USB_ENDPOINT_RESET](/windows-hardware/drivers/ddi/udecxusbendpoint/nc-udecxusbendpoint-evt_udecx_usb_endpoint_reset)* (required).
    - *[EVT_UDECX_USB_ENDPOINT_START](/windows-hardware/drivers/ddi/udecxusbendpoint/nc-udecxusbendpoint-evt_udecx_usb_endpoint_start)*
    - *[EVT_UDECX_USB_ENDPOINT_PURGE](/windows-hardware/drivers/ddi/udecxusbendpoint/nc-udecxusbendpoint-evt_udecx_usb_endpoint_purge)*

1. Call **[UdecxUsbEndpointCreate](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointcreate)** to create the endpoint object and retrieve the UDECXUSBENDPOINT handle.
1. Call **[UdecxUsbEndpointSetWdfIoQueue](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointsetwdfioqueue)** to associate a framework queue object with the endpoint.

In this example implementation, the client driver creates a dynamic default control endpoint.

```cpp
NTSTATUS
UsbDevice_EvtUsbDeviceDefaultEndpointAdd(
    _In_
        UDECXUSBDEVICE            UdecxUsbDevice,
    _In_
        PUDECXUSBENDPOINT_INIT    UdecxUsbEndpointInit
)
{
    NTSTATUS                    status;
    PUDECX_USBDEVICE_CONTEXT    deviceContext;
    WDFQUEUE                    controlQueue;
    WDF_IO_QUEUE_CONFIG         queueConfig;
    UDECX_USB_ENDPOINT_CALLBACKS  callbacks;

    deviceContext = UdecxDeviceGetContext(UdecxUsbDevice);

    WDF_IO_QUEUE_CONFIG_INIT(&queueConfig, WdfIoQueueDispatchSequential);

    queueConfig.EvtIoInternalDeviceControl = IoEvtControlUrb;

    status = WdfIoQueueCreate (deviceContext->WdfDevice,
                               &queueConfig,
                               WDF_NO_OBJECT_ATTRIBUTES,
                               &controlQueue);

    if (!NT_SUCCESS(status)) {

        goto exit;
    }

    UdecxUsbEndpointInitSetEndpointAddress(UdecxUsbEndpointInit, USB_DEFAULT_DEVICE_ADDRESS);

    UDECX_USB_ENDPOINT_CALLBACKS_INIT(&callbacks, UsbEndpointReset);
    UdecxUsbEndpointInitSetCallbacks(UdecxUsbEndpointInit, &callbacks);

    status = UdecxUsbEndpointCreate(UdecxUsbEndpointInit,
        WDF_NO_OBJECT_ATTRIBUTES,
        &deviceContext->UdecxUsbControlEndpoint);

    if (!NT_SUCCESS(status)) {
        goto exit;
    }

    UdecxUsbEndpointSetWdfIoQueue(deviceContext->UdecxUsbControlEndpoint,
        controlQueue);

exit:

    return status;
}
```

## Perform error recovery by resetting an endpoint

At times, data transfers can fail due to various reasons, such as a stall condition in the endpoint. In the case of failed transfers, the endpoint cannot process requests until the error condition is cleared. When the UDE class extension experiences failed data transfers, it invokes the client driver's *[EVT_UDECX_USB_ENDPOINT_RESET](/windows-hardware/drivers/ddi/udecxusbendpoint/nc-udecxusbendpoint-evt_udecx_usb_endpoint_reset)* callback function, which the driver registered in the previous call to **[UdecxUsbEndpointInitSetCallbacks](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointinitsetcallbacks)**. In the implementation, the driver can choose to clear the HALT state of the pipe and take other necessary steps to clear the error condition.

This call is asynchronous. After the client is finished with the reset operation, driver must complete the request with an appropriate failure code by calling **[WdfRequestComplete](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete)**. That call notifies the UDE client extension about the completion of the reset operation with status.

**Note**  If a complex solution is required for error recovery, the client driver has the option of resetting the host controller. This logic can be implemented in the *[EVT_UDECX_WDF_DEVICE_RESET](/windows-hardware/drivers/ddi/udecxwdfdevice/nc-udecxwdfdevice-evt_udecx_wdf_device_reset)* callback function that the driver registered in its **[UdecxWdfDeviceAddUsbDeviceEmulation](/windows-hardware/drivers/ddi/udecxwdfdevice/nf-udecxwdfdevice-udecxwdfdeviceaddusbdeviceemulation)** call. If applicable, the driver can reset the host controller and all downstream devices. If the client driver does not need to reset the controller but reset all downstream devices, the driver must specify **UdeWdfDeviceResetActionResetEachUsbDevice** in the configuration parameters during registration. In that case, the class extension invokes *EVT_UDECX_WDF_DEVICE_RESET* for each connected device.

## Implement queue state management

The state of the framework queue object associated with a UDE endpoint object is managed by the UDE class extension. However, if the client driver forwards requests from endpoint queues to other internal queues, then the client must implement logic to handle changes in the endpoint's I/O flow. These callback functions are registered with **[UdecxUsbEndpointInitSetCallbacks](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointinitsetcallbacks)**.

### Endpoint purge operation

A UDE client driver with one queue per endpoint can implement *[EVT_UDECX_USB_ENDPOINT_PURGE](/windows-hardware/drivers/ddi/udecxusbendpoint/nc-udecxusbendpoint-evt_udecx_usb_endpoint_purge)* as shown in this example:

In the *[EVT_UDECX_USB_ENDPOINT_PURGE](/windows-hardware/drivers/ddi/udecxusbendpoint/nc-udecxusbendpoint-evt_udecx_usb_endpoint_purge)* implementation, the client driver is required to make sure all I/O forwarded from the endpoint's queue has been completed, and that newly forwarded I/O also fails until the client driver's *[EVT_UDECX_USB_ENDPOINT_START](/windows-hardware/drivers/ddi/udecxusbendpoint/nc-udecxusbendpoint-evt_udecx_usb_endpoint_start)* is invoked. These requirements are met by calling **[UdecxUsbEndpointPurgeComplete](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointpurgecomplete)**, which make sure that all forwarded I/O is completed and future forwarded I/O are failed.

### Endpoint start operation

In the *[EVT_UDECX_USB_ENDPOINT_START](/windows-hardware/drivers/ddi/udecxusbendpoint/nc-udecxusbendpoint-evt_udecx_usb_endpoint_start)* implementation, the client driver is required to begin processing I/O on the endpoint's queue, and on any queues that receive forwarded I/O for the endpoint. After an endpoint is created, it does not receive any I/O until after this callback function returns. This callback returns the endpoint to a state of processing I/O after *[EVT_UDECX_USB_ENDPOINT_PURGE](/windows-hardware/drivers/ddi/udecxusbendpoint/nc-udecxusbendpoint-evt_udecx_usb_endpoint_purge)* completes.

## Handling data transfer requests (URBs)

To process USB I/O requests sent to the client device's endpoints, intercept the [EVT_WDF_IO_QUEUE_IO_INTERNAL_DEVICE_CONTROL](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_internal_device_control) callback on the queue object used with **[UdecxUsbEndpointInitSetCallbacks](/windows-hardware/drivers/ddi/udecxusbendpoint/nf-udecxusbendpoint-udecxusbendpointinitsetcallbacks)** when associating the queue with the endpoint. In that callback, process I/O for the [IOCTL_INTERNAL_USB_SUBMIT_URB](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_urb) IoControlCode (see sample code under [URB handling methods](#urb-handling-methods)).

## URB handling methods

As part of processing URBs via [IOCTL_INTERNAL_USB_SUBMIT_URB](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_urb) of a queue associated with an endpoint on a virtual device, A UDE client driver can get a pointer to the transfer buffer of an I/O request by using these methods:

These functions are implemented by the client driver to handle queues and requests on an endpoint.

**[UdecxUrbRetrieveControlSetupPacket](/windows-hardware/drivers/ddi/udecxurb/nf-udecxurb-udecxurbretrievecontrolsetuppacket)**
Retrieves a USB control setup packet from a specified framework request object.

**[UdecxUrbRetrieveBuffer](/windows-hardware/drivers/ddi/udecxurb/nf-udecxurb-udecxurbretrievebuffer)**
Retrieves the transfer buffer of an URB from the specified framework request object sent to the endpoint queue.

**[UdecxUrbSetBytesCompleted](/windows-hardware/drivers/ddi/udecxurb/nf-udecxurb-udecxurbsetbytescompleted)**
Sets the number of bytes transferred for the URB contained within a framework request object.

**[UdecxUrbComplete](/windows-hardware/drivers/ddi/udecxurb/nf-udecxurb-udecxurbcomplete)**
Completes the URB request with a USB-specific completion status code.

**[UdecxUrbCompleteWithNtStatus](/windows-hardware/drivers/ddi/udecxurb/nf-udecxurb-udecxurbcompletewithntstatus)**
Completes the URB request with an NTSTATUS code.

Below is the flow of typical I/O processing for the URB of an USB OUT transfer.

```cpp
static VOID
IoEvtSampleOutUrb(
    _In_ WDFQUEUE Queue,
    _In_ WDFREQUEST Request,
    _In_ size_t OutputBufferLength,
    _In_ size_t InputBufferLength,
    _In_ ULONG IoControlCode
)
{
    PENDPOINTQUEUE_CONTEXT pEpQContext;
    NTSTATUS status = STATUS_SUCCESS;
    PUCHAR transferBuffer;
    ULONG transferBufferLength = 0;

    UNREFERENCED_PARAMETER(OutputBufferLength);
    UNREFERENCED_PARAMETER(InputBufferLength);

    // one possible way to get context info
    pEpQContext = GetEndpointQueueContext(Queue);

    if (IoControlCode != IOCTL_INTERNAL_USB_SUBMIT_URB)
    {
        LogError(TRACE_DEVICE, "WdfRequest %p Incorrect IOCTL %x, %!STATUS!",
            Request, IoControlCode, status);
        status = STATUS_INVALID_PARAMETER;
        goto exit;
    }

    status = UdecxUrbRetrieveBuffer(Request, &transferBuffer, &transferBufferLength);
    if (!NT_SUCCESS(status))
    {
        LogError(TRACE_DEVICE, "WdfRequest %p unable to retrieve buffer %!STATUS!",
            Request, status);
        goto exit;
    }

    if (transferBufferLength >= 1)
    {
        //consume one byte of output data
        pEpQContext->global_storage = transferBuffer[0];
    }

exit:
    // writes never pended, always completed
    UdecxUrbSetBytesCompleted(Request, transferBufferLength);
    UdecxUrbCompleteWithNtStatus(Request, status);
    return;
}
```

The client driver can complete an I/O request on a separate with a DPC. Follow these best practices:

- To ensure compatibility with existing USB drivers, the UDE client must call **[WdfRequestComplete](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete)** at DISPATCH_LEVEL.
- If the **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** was added to an endpoint's queue and the driver starts processing it synchronously on the calling driver's thread or DPC, the request must not be completed synchronously. A separate DPC is required for that purpose, which the driver queue by calling **[WdfDpcEnqueue](/windows-hardware/drivers/ddi/wdfdpc/nf-wdfdpc-wdfdpcenqueue)**.
- When the UDE class extension invokes *[EvtIoCanceledOnQueue](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_canceled_on_queue)* or *[EvtRequestCancel](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_cancel)*, the client driver must complete the received URB on a separate DPC from the caller's thread or DPC. To do this, the driver must provide an *EvtIoCanceledOnQueue* callback for its **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** queues.
