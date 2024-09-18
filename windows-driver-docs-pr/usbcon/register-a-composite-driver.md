---
title: How to Register a Composite Device
description: How a USB multi-function device, called a composite driver, registers, and unregisters the composite device with the underlying USB driver stack.
ms.date: 09/18/2024
---

# How to register a composite device

This article describes how a driver of a USB multi-function device, called a composite driver, can register and unregister the composite device with the underlying USB driver stack. Windows loads the Microsoft-provided driver, Usbccgp.sys As the default composite driver. The procedure in this article applies to a custom Windows Driver Model (WDM)-based composite driver that replaces Usbccgp.sys.

A Universal Serial Bus (USB) device can provide multiple functions that are active simultaneously. Such multi-function devices are also known as composite devices. For example, a composite device might define a function for the keyboard functionality and another function for the mouse. The composite driver enumerates the functions of the device. The composite driver can manage those functions itself in a monolithic model or create physical device objects (PDOs) for each of the functions. USB function drivers, such as the keyboard driver and the mouse driver, manage their respective individual PDOs.

The USB 3.0 specification defines the function suspend and remote wake-up feature enabling individual functions to enter and exit low-power states without affecting the power state of other functions or the entire device. For more information about the feature, see [How to Implement Function Suspend in a Composite Driver](how-to--implement-remote-and-function-wake-support.md).

To use the feature, the composite driver needs to register the device with the underlying USB driver stack. Because the feature applies to USB 3.0 devices, the composite driver must make sure that the underlying stack supports version USBD_INTERFACE_VERSION_602. Through the registration request, the composite driver:

- Informs the underlying USB driver stack that the driver is responsible for sending a request to arm a function for remote wake-up. The USB driver stack processes the remote wake-up request, which sends the necessary protocol requests to the device.
- Obtains a list of function handles (one per function) assigned by the USB driver stack. The composite driver can then use a function handle in the driver's the request for remote wake-up of the function associated with the handle.

Typically a composite driver sends the registration request in the driver's AddDevice or the start-device routine to handle **[IRP_MN_START_DEVICE](../kernel/irp-mn-start-device.md)**. So, the composite driver releases the resources that are allocated for the registration in the driver's unload routines such as stop-device (**[IRP_MN_STOP_DEVICE](../kernel/irp-mn-stop-device.md)**) or remove-device routine (**[IRP_MN_REMOVE_DEVICE](../kernel/irp-mn-remove-device.md)**).

## Prerequisites

Before sending the registration request, make sure that:

- You have the number of functions in the device. That number can be derived the descriptors retrieved by the get-configuration request.
- You obtained a USBD handle in a previous call to **[USBD_CreateHandle](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_createhandle)**.
- The underlying USB driver stack supports USB 3.0 devices. To do so, call **[USBD_IsInterfaceVersionSupported](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_isinterfaceversionsupported)** and pass USBD_INTERFACE_VERSION_602 as the version to check.

For a code example, see [How to Implement Function Suspend in a Composite Driver](how-to--implement-remote-and-function-wake-support.md).

## Register a composite device

The following procedure describes how you should build and send a registration request to associate a composite driver with the USB driver stack.

1. Allocate a **[COMPOSITE_DEVICE_CAPABILITIES](/windows-hardware/drivers/ddi/usbdlib/ns-usbdlib-_composite_device_capabilities)** structure and initialize it by calling the **[COMPOSITE_DEVICE_CAPABILITIES_INIT](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-composite_device_capabilities_init)** macro.
1. Set the **CapabilityFunctionSuspend** member of **[COMPOSITE_DEVICE_CAPABILITIES](/windows-hardware/drivers/ddi/usbdlib/ns-usbdlib-_composite_device_capabilities)** to 1.
1. Allocate a **[REGISTER_COMPOSITE_DEVICE](/windows-hardware/drivers/ddi/usbdlib/ns-usbdlib-_register_composite_device)** structure and initialize the structure by calling the **[USBD_BuildRegisterCompositeDevice](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_buildregistercompositedevice)** routine. In the call, specify the USBD handle, the initialized **[COMPOSITE_DEVICE_CAPABILITIES](/windows-hardware/drivers/ddi/usbdlib/ns-usbdlib-_composite_device_capabilities)** structure, and the number of functions.
1. Allocate an I/O request packet (IRP) by calling **[IoAllocateIrp](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp)** and get a pointer to the IRP's first stack location (**[IO_STACK_LOCATION](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)**) by calling **[IoGetNextIrpStackLocation](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetnextirpstacklocation)**.
1. Allocate memory for a buffer that is large enough to hold an array of function handles (USBD_FUNCTION_HANDLE). The number of elements in the array must be the number of PDOs.
1. Build the request by setting the following members of the **[IO_STACK_LOCATION](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)**:
    - Specify the type of request by setting **Parameters.DeviceIoControl.IoControlCode** to **[IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_register_composite_device)**.
    - Specify the input parameter by setting **Parameters.Others.Argument1** to the address of the initialized **[REGISTER_COMPOSITE_DEVICE](/windows-hardware/drivers/ddi/usbdlib/ns-usbdlib-_register_composite_device)** structure.
    - Specify the output parameter by setting **AssociatedIrp.SystemBuffer** to the buffer that was allocated in step 5.

1. Call **[IoCallDriver](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)** to send the request by passing the IRP to the next stack location.

Upon completion, inspect the array of function handles returned by the USB driver stack. You can store the array in the driver's device context for future use.

The following code example shows how to build and send a registration request. The example assumes that the composite driver stores the previously obtained number of functions and the USBD handle in the driver's device context.

```cpp
VOID  RegisterCompositeDriver(PPARENT_FDO_EXT parentFdoExt)
{
    PIRP                            irp;
    REGISTER_COMPOSITE_DRIVER       registerInfo;
    COMPOSITE_DRIVER_CAPABILITIES   capabilities;
    NTSTATUS                        status;
    PVOID                           buffer;
    ULONG                           bufSize;
    PIO_STACK_LOCATION              nextSp;

    buffer = NULL;

    COMPOSITE_DRIVER_CAPABILITIES_INIT(&capabilities);
    capabilities.CapabilityFunctionSuspend = 1;

    USBD_BuildRegisterCompositeDriver(parentFdoExt->usbdHandle,
        capabilities,
        parentFdoExt->numFunctions,
        &registerInfo);

    irp = IoAllocateIrp(parentFdoExt->topDevObj->StackSize, FALSE);

    if (irp == NULL)
    {
        //IoAllocateIrp failed.
        status = STATUS_INSUFFICIENT_RESOURCES;
        goto ExitRegisterCompositeDriver;
    }

    nextSp = IoGetNextIrpStackLocation(irp);

    bufSize = parentFdoExt->numFunctions * sizeof(USBD_FUNCTION_HANDLE);

    buffer = ExAllocatePoolWithTag (NonPagedPool, bufSize, POOL_TAG);

    if (buffer == NULL)
    {
        // Memory alloc for function-handles failed.
        status = STATUS_INSUFFICIENT_RESOURCES;
        goto ExitRegisterCompositeDriver;
    }

    nextSp->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;
    nextSp->Parameters.DeviceIoControl.IoControlCode = IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DRIVER;

    //Set the input buffer in Argument1
    nextSp->Parameters.Others.Argument1 = &registerInfo;

    //Set the output buffer in SystemBuffer field for USBD_FUNCTION_HANDLE.
    irp->AssociatedIrp.SystemBuffer = buffer;

    // Pass the IRP down to the next device object in the stack. Not shown.
    status = CallNextDriverSync(parentFdoExt, irp, FALSE);

    if (!NT_SUCCESS(status))
    {
        //Failed to register the composite driver.
        goto ExitRegisterCompositeDriver;
    }

    parentFdoExt->compositeDriverRegistered = TRUE;

    parentFdoExt->functionHandleArray = (PUSBD_FUNCTION_HANDLE) buffer;

End:
    if (!NT_SUCCESS(status))
    {
        if (buffer != NULL)
        {
            ExFreePoolWithTag (buffer, POOL_TAG);
            buffer = NULL;
        }
    }

    if (irp != NULL)
    {
        IoFreeIrp(irp);
        irp = NULL;
    }

    return;
}
```

## Unregister a composite device

1. Allocate an IRP by calling **[IoAllocateIrp](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp)** and get a pointer to the IRP's first stack location (**[IO_STACK_LOCATION](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)**) by calling **[IoGetNextIrpStackLocation](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetnextirpstacklocation)**.
1. Build the request by setting the **Parameters.DeviceIoControl.IoControlCode** member of **[IO_STACK_LOCATION](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)** to **[IOCTL_INTERNAL_USB_UNREGISTER_COMPOSITE_DEVICE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_unregister_composite_device)**.
1. Call **[IoCallDriver](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)** to send the request by passing the IRP to the next stack location.

The **[IOCTL_INTERNAL_USB_UNREGISTER_COMPOSITE_DEVICE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_unregister_composite_device)** request is sent once by the composite driver in the context of remove-device routine. The purpose of the request is to remove the association between the USB driver stack and the composite driver and its enumerated function. The request also cleans up any resources that were created to maintain that association and all function handles that were returned in the previous registration request.

The following code example shows how to build and send a request to unregister the composite device. The example assumes that the composite driver was previously registered through a registration request as described earlier in this article.

```cpp
VOID  UnregisterCompositeDriver(
    PPARENT_FDO_EXT parentFdoExt )
{
    PIRP                irp;
    PIO_STACK_LOCATION  nextSp;
    NTSTATUS            status;

    PAGED_CODE();

    irp = IoAllocateIrp(parentFdoExt->topDevObj->StackSize, FALSE);

    if (irp == NULL)
    {
        //IoAllocateIrp failed.
        status = STATUS_INSUFFICIENT_RESOURCES;
        return;
    }

    nextSp = IoGetNextIrpStackLocation(irp);

    nextSp->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;
    nextSp->Parameters.DeviceIoControl.IoControlCode = IOCTL_INTERNAL_USB_UNREGISTER_COMPOSITE_DRIVER;

    // Pass the IRP down to the next device object in the stack. Not shown.
    status = CallNextDriverSync(parentFdoExt, irp, FALSE);

    if (NT_SUCCESS(status))
    {
        parentFdoExt->compositeDriverRegistered = FALSE;
    }

    IoFreeIrp(irp);

    return;
}
```

## Related topics

- **[IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_register_composite_device)**
- **[IOCTL_INTERNAL_USB_UNREGISTER_COMPOSITE_DEVICE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_unregister_composite_device)**
