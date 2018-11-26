---
title: Connecting a KMDF Driver to GPIO I/O Pins
description: How a kernel-mode driver framework (KMDF) driver for a peripheral device can obtain a description of the GPIO I/O resource. 
ms.assetid: 02F6431C-7B55-4DFB-9792-4A72F0268C76
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Connecting a KMDF Driver to GPIO I/O Pins


A GPIO I/O resource is a set of one or more GPIO pins that are configured as data inputs or data outputs. The driver for a peripheral device that physically connects to these pins acquires the corresponding GPIO I/O resource from the operating system. The peripheral device driver opens a connection to the GPIO pins in this resource and sends I/O requests to the handle that represents this connection.

The following code example shows how the kernel-mode driver framework (KMDF) driver for a peripheral device can obtain a description of the GPIO I/O resource that the Plug and Play (PnP) manager has assigned to the driver.

```cpp
NTSTATUS
  EvtDevicePrepareHardware(
    _In_ WDFDEVICE Device,
    _In_ WDFCMRESLIST ResourcesRaw,
    _In_ WDFCMRESLIST ResourcesTranslated
    )
{
    int ResourceCount, Index;
    PCM_PARTIAL_RESOURCE_DESCRIPTOR Descriptor;
    XYZ_DEVICE_CONTEXT *DeviceExtension;

    ...

    DeviceExtension = XyzDrvGetDeviceExtension(Device);
    ResourceCount = WdfCmResourceListGetCount(ResourcesTranslated);
    for (Index = 0; Index < ResourceCount; Index += 1) {
        Descriptor = WdfCmResourceListGetDescriptor(ResourcesTranslated, Index);
        switch (Descriptor->Type) {

        //
        // GPIO I/O descriptors
        //

        case CmResourceTypeConnection:

            //
            // Check against expected connection type.
            //

            if ((Descriptor->u.Connection.Class == CM_RESOURCE_CONNECTION_CLASS_GPIO) &&
                (Descriptor->u.Connection.Type == CM_RESOURCE_CONNECTION_TYPE_GPIO_IO)) {

                DeviceExtension->ConnectionId.LowPart = Descriptor->u.Connection.IdLowPart;
                DeviceExtension->ConnectionId.HighPart = Descriptor->u.Connection.IdHighPart;

        ...

}
```

In the preceding code example, the `DeviceExtension` variable is a pointer to the device context for the peripheral device. The `XyzDrvGetDeviceExtension` function, which retrieves this device context, is implemented by the peripheral device driver. This driver previously registered its [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function by calling the [**WdfDeviceInitSetPnpPowerEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546135) method.

The following code example shows how the peripheral device driver can use the GPIO resource description that it obtained in the previous code example to open a WDFIOTARGET handle to the driver's GPIO I/O resource.

```cpp
NTSTATUS IoRoutine(WDFDEVICE Device, BOOLEAN ReadOperation) 
{
    WDFIOTARGET IoTarget;
    XYZ_DEVICE_CONTEXT *DeviceExtension;
    UNICODE_STRING ReadString;
    WCHAR ReadStringBuffer[100];;
    BOOL DesiredAccess;
    NTSTATUS Status;
    WDF_OBJECT_ATTRIBUTES ObjectAttributes;
    WDF_IO_TARGET_OPEN_PARAMS OpenParams

    DeviceExtension = XyzDrvGetDeviceExtension(Device);
    RtlInitEmptyUnicodeString(&ReadString,
                              ReadStringBuffer,
                              sizeof(ReadStringBuffer));

    Status = RESOURCE_HUB_CREATE_PATH_FROM_ID(&ReadString,
                                              DeviceExtension->ConnectionId.LowPart,
                                              DeviceExtension->ConnectionId.HighPart);

    NT_ASSERT(NT_SUCCESS(Status));

    WDF_OBJECT_ATTRIBUTES_INIT(&ObjectAttributes);
    ObjectAttributes.ParentObject = Device;

    Status = WdfIoTargetCreate(Device, &ObjectAttributes, &IoTarget);
    if (!NT_SUCCESS(Status)) {
        goto IoErrorEnd;
    }   

    if (ReadOperation != FALSE) {
        DesiredAccess = GENERIC_READ;
    } else {
        DesiredAccess = GENERIC_WRITE;
    }

    WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_NAME(&OpenParams, ReadString, DesiredAccess);

    Status = WdfIoTargetOpen(IoTarget, &OpenParams);
    if (!NT_SUCCESS(Status)) {
        goto IoErrorEnd;
    }
    ...
```

In the preceding code example, the `Device` variable is a WDFDEVICE handle to the framework device object for the peripheral device. The **RESOURCE\_HUB\_CREATE\_PATH\_FROM\_ID** function creates a string that contains the name of the GPIO I/O resource. The code example uses this string to open the GPIO I/O resource by name.

After the peripheral device driver has obtained a handle to a GPIO I/O resource, this driver can send I/O control requests to read data from or write data to the GPIO pins. A driver that opens a GPIO I/O resource for reads uses [**IOCTL\_GPIO\_READ\_PINS**](https://msdn.microsoft.com/library/windows/hardware/hh406483) I/O control requests to read data from the pins in the resource. A driver that opens a GPIO I/O resource for writes uses [**IOCTL\_GPIO\_WRITE\_PINS**](https://msdn.microsoft.com/library/windows/hardware/hh406487) I/O control requests to write data to the pins in the resource. The following code example shows how to perform a GPIO read or write operation.

```cpp
    WDF_OBJECT_ATTRIBUTES RequestAttributes;
    WDF_OBJECT_ATTRIBUTES Attributes;
    WDF_REQUEST_SEND_OPTIONS SendOptions;
    WDFREQUEST IoctlRequest;
    WDFIOTARGET IoTarget;
    WDFMEMORY WdfMemory;
    NTSTATUS Status;

    WDF_OBJECT_ATTRIBUTES_INIT(&RequestAttributes);
    Status = WdfRequestCreate(&RequestAttributes, IoTarget, &IoctlRequest);
    if (!NT_SUCCESS(Status)) {
        goto RwErrorExit;
    }

    //
    // Set up a WDF memory object for the IOCTL request.
    //

    WDF_OBJECT_ATTRIBUTES_INIT(&Attributes);
    Attributes.ParentObject = IoctlRequest;
    Status = WdfMemoryCreatePreallocated(&Attributes, Data, Size, &WdfMemory);
    if (!NT_SUCCESS(Status)) {
        goto RwErrorExit;
    }

    //
    // Format the request.
    //

    if (ReadOperation != FALSE) {
        Status = WdfIoTargetFormatRequestForIoctl(IoTarget,
                                                  IoctlRequest,
                                                  IOCTL_GPIO_READ_PINS,
                                                  NULL,
                                                  0,
                                                  WdfMemory,
                                                  0);

    } else {
        Status = WdfIoTargetFormatRequestForIoctl(IoTarget,
                                                  IoctlRequest,
                                                  IOCTL_GPIO_WRITE_PINS,
                                                  WdfMemory,
                                                  0,
                                                  WdfMemory,
                                                  0);
    }

    if (!NT_SUCCESS(Status)) {
        goto RwErrorExit;
    }

    //
    // Send the request synchronously (with a 60-second time-out).
    //

    WDF_REQUEST_SEND_OPTIONS_INIT(&SendOptions,
                                  WDF_REQUEST_SEND_OPTION_SYNCHRONOUS);
    WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT(&SendOptions,
                                         WDF_REL_TIMEOUT_IN_SEC(60));

    Status = WdfRequestAllocateTimer(IoctlRequest);
    if (!NT_SUCCESS(Status)) {
        goto RwErrorExit;
    }

    if (!WdfRequestSend(IoctlRequest, IoTarget, &SendOptions)) {
        Status = WdfRequestGetStatus(IoctlRequest);
    }

    ...
```

In the preceding code example, `Data` is a pointer to a data buffer, `Size` is the size, in bytes, of this data buffer, and `ReadOperation` indicates whether the requested operation is a read (**TRUE**) or a write (**FALSE**).

## For more information


For more information about **IOCTL\_GPIO\_READ\_PINS** requests, including the mapping of data input pins to the bits in the request output buffer, see [**IOCTL\_GPIO\_READ\_PINS**](https://msdn.microsoft.com/library/windows/hardware/hh406483). For more information about **IOCTL\_GPIO\_WRITE\_PINS** requests, including the mapping of the bits in the request input buffer to data output pins, see [**IOCTL\_GPIO\_WRITE\_PINS**](https://msdn.microsoft.com/library/windows/hardware/hh406487).

For a sample driver that shows how to write a GPIO peripheral driver that runs in kernel mode, see the SimDevice sample driver in the [GPIO sample drivers](http://go.microsoft.com/fwlink/p/?LinkId=616032) collection on GitHub.

 

 




