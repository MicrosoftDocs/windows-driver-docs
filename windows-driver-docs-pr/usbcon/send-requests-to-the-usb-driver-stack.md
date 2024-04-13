---
description: This topic describes the steps that are required to submit an initialized URB to the USB driver stack to process a particular request.
title: How to Submit an URB
ms.date: 04/20/2017
---

# How to Submit an URB

This topic describes the steps that are required to submit an initialized URB to the USB driver stack to process a particular request.

A client driver communicates with its device by using I/O control code (IOCTL) requests that are delivered to the device in I/O request packets (IRPs) of type [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](../kernel/irp-mj-internal-device-control.md). For a device specific request, such as a select-configuration request, the request is described in an USB Request Block (URB) that is associated with an IRP. The process of associating an URB with an IRP, and sending the request to the USB driver stack is referred to as submitting an URB. To submit an URB, the client driver must use [**IOCTL\_INTERNAL\_USB\_SUBMIT\_URB**](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_urb) as the device control code. The IOCTL is one of the "internal" control codes that provide an I/O interface that a client driver uses to manage its device and the port to which the device is connected. User-mode applications do not have access to those internal I/O interface. For more control codes for kernel mode drivers, see [Kernel-Mode IOCTLs for USB Client Drivers](/windows-hardware/drivers/ddi/_usbref/#km-ioctl).

## Prerequisites

Before sending a request to the Universal Serial Bus (USB) driver stack, the client driver must allocate an [**URB**](/windows-hardware/drivers/ddi/usb/ns-usb-_urb) structure and format that structure depending on the type of request. For more information, see [Allocating and Building URBs](how-to-add-xrb-support-for-client-drivers.md) and [Best Practices: Using URBs](usb-client-driver-contract-in-windows-8.md).

## Instructions

1. Allocate an IRP for the URB by calling the [**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp) routine. You must provide the stack size of the device object that receives the IRP. You received a pointer to that device object in a previous call to the [**IoAttachDeviceToDeviceStack**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack) routine. The stack size is stored in the **StackSize** member of the [**DEVICE\_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object) structure.
2. Get a pointer to the IRP's first stack location ([**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)) by calling [**IoGetNextIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetnextirpstacklocation).
3. Set the **MajorFunction** member of the [**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) structure to [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](../kernel/irp-mj-internal-device-control.md).
4. Set the **Parameters.DeviceIoControl.IoControlCode** member of the [**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) structure to [**IOCTL\_INTERNAL\_USB\_SUBMIT\_URB**](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_urb).
5. Set the **Parameters.Others.Argument1** member of the [**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) structure to the address of the initialized [**URB**](/windows-hardware/drivers/ddi/usb/ns-usb-_urb) structure. To associate the IRP to the URB, you can alternatively call [**USBD\_AssignUrbToIoStackLocation**](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_assignurbtoiostacklocation) only if the URB was allocated by [**USBD\_UrbAllocate**](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_urballocate), [**USBD\_SelectConfigUrbAllocateAndBuild**](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectconfigurballocateandbuild), or [**USBD\_SelectInterfaceUrbAllocateAndBuild**](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_selectinterfaceurballocateandbuild).
6. Set a completion routine by calling [**IoSetCompletionRoutineEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutineex).

    If you submit the URB asynchronously, pass a pointer to the caller-implemented completion routine and its context. The caller releases the IRP in its completion routine.

    If you are submitting the IRP synchronously, implement a completion routine and pass a pointer to that routine in the call to [**IoSetCompletionRoutineEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutineex). The call also requires an initialized KEVENT object in the *Context* parameter. In your completion routine, set the event to the signaled state.

7. Call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) to forward the populated IRP to the next lower device object in the device stack. For an synchronous call, after calling **IoCallDriver**, wait for the event object by calling [**KeWaitForSingleObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitforsingleobject) to get the event notification.
8. Upon completion of the IRP, check the **IoStatus.Status** member of IRP and evaluate the result. If the **IoStatus.Status** is STATUS\_SUCCESS, the request was successful.

## USB Synchronous Submission

The following example shows how to submit an URB synchronously.

```ManagedCPlusPlus
// The SubmitUrbSync routine submits an URB synchronously.
//
// Parameters:
//      DeviceExtension: Pointer to the caller's device extension. The
//                       device extension must have a pointer to
//                       the next lower device object in the device stacks.  
//
//      Irp: Pointer to an IRP allocated by the caller.
//
//      Urb: Pointer to an URB that is allocated by  USBD_UrbAllocate,
//           USBD_IsochUrbAllocate, USBD_SelectConfigUrbAllocateAndBuild,
//           or USBD_SelectInterfaceUrbAllocateAndBuild.

//      CompletionRoutine: Completion routine.
//
// Return Value:
//
//      NTSTATUS  

NTSTATUS SubmitUrbSync( PDEVICE_EXTENSION DeviceExtension,
                       PIRP Irp,
                       PURB Urb,  
                       PIO_COMPLETION_ROUTINE SyncCompletionRoutine)  

{

    NTSTATUS  ntStatus;  
    KEVENT    kEvent;

    PIO_STACK_LOCATION nextStack;

    // Get the next stack location.
    nextStack = IoGetNextIrpStackLocation(Irp);  

    // Set the major code.
    nextStack->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;  

    // Set the IOCTL code for URB submission.
    nextStack->Parameters.DeviceIoControl.IoControlCode = IOCTL_INTERNAL_USB_SUBMIT_URB;  

    // Attach the URB to this IRP.
    // The URB must be allocated by USBD_UrbAllocate, USBD_IsochUrbAllocate,
    // USBD_SelectConfigUrbAllocateAndBuild, or USBD_SelectInterfaceUrbAllocateAndBuild.
    USBD_AssignUrbToIoStackLocation (DeviceExtension->UsbdHandle, nextStack, Urb);

    KeInitializeEvent(&kEvent, NotificationEvent, FALSE);

    ntStatus = IoSetCompletionRoutineEx ( DeviceExtension->NextDeviceObject,  
        Irp,  
        SyncCompletionRoutine,  
        (PVOID) &kEvent,  
        TRUE,
        TRUE,
        TRUE);

    if (!NT_SUCCESS(ntStatus))
    {
        KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, "IoSetCompletionRoutineEx failed. \n" ));
        goto Exit;
    }

    ntStatus = IoCallDriver(DeviceExtension->NextDeviceObject, Irp);  

    if (ntStatus == STATUS_PENDING)
    {
        KeWaitForSingleObject ( &kEvent,
            Executive,
            KernelMode,
            FALSE,
            NULL);
    }

    ntStatus = Irp->IoStatus.Status;

Exit:

    if (!NT_SUCCESS(ntStatus))
    {
        // We hit a failure condition,
        // We will free the IRP

        IoFreeIrp(Irp);
        Irp = NULL;
    }


    return ntStatus;
}

// The SyncCompletionRoutine routine is the completion routine
// for the synchronous URB submit request.
//
// Parameters:
//
//      DeviceObject: Pointer to the device object.
//      Irp:          Pointer to an I/O Request Packet.
//      CompletionContext: Context for the completion routine.
//
// Return Value:
//
//      NTSTATUS  

NTSTATUS SyncCompletionRoutine ( PDEVICE_OBJECT DeviceObject,
                                PIRP           Irp,
                                PVOID          Context)
{
    PKEVENT kevent;

    kevent = (PKEVENT) Context;

    if (Irp->PendingReturned == TRUE)
    {
        KeSetEvent(kevent, IO_NO_INCREMENT, FALSE);
    }

    KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, "Request completed. \n" ));


    return STATUS_MORE_PROCESSING_REQUIRED;
}
```

## USB Asynchronous Submission

The following example shows how to submit an URB asynchronously.

```ManagedCPlusPlus
// The SubmitUrbASync routine submits an URB asynchronously.
//
// Parameters:
//
// Parameters:
//      DeviceExtension: Pointer to the caller's device extension. The
//                       device extension must have a pointer to
//                       the next lower device object in the device stacks.  
//
//      Irp: Pointer to an IRP allocated by the caller.
//
//      Urb: Pointer to an URB that is allocated by  USBD_UrbAllocate,
//           USBD_IsochUrbAllocate, USBD_SelectConfigUrbAllocateAndBuild,
//           or USBD_SelectInterfaceUrbAllocateAndBuild.

//      CompletionRoutine: Completion routine.
//
//      CompletionContext: Context for the completion routine.
//
//
// Return Value:
//
//      NTSTATUS

NTSTATUS SubmitUrbASync ( PDEVICE_EXTENSION DeviceExtension,
                         PIRP Irp,
                         PURB Urb,  
                         PIO_COMPLETION_ROUTINE CompletionRoutine,  
                         PVOID CompletionContext)  
{
    // Completion routine is required if the URB is submitted asynchronously.
    // The caller's completion routine releases the IRP when it completes.


    NTSTATUS ntStatus = -1;  

    PIO_STACK_LOCATION nextStack = IoGetNextIrpStackLocation(Irp);  

    // Attach the URB to this IRP.
    nextStack->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;  

    // Attach the URB to this IRP.
    nextStack->Parameters.DeviceIoControl.IoControlCode = IOCTL_INTERNAL_USB_SUBMIT_URB;  

    // Attach the URB to this IRP.
    (void) USBD_AssignUrbToIoStackLocation (DeviceExtension->UsbdHandle, nextStack, Urb);  

    // Caller's completion routine will free the irp when it completes.
    ntStatus = IoSetCompletionRoutineEx ( DeviceExtension->NextDeviceObject,
        Irp,  
        CompletionRoutine,  
        CompletionContext,  
        TRUE,
        TRUE,
        TRUE);

    if (!NT_SUCCESS(ntStatus))
    {
        goto Exit;
    }

    (void) IoCallDriver(DeviceExtension->NextDeviceObject, Irp);

Exit:
    if (!NT_SUCCESS(ntStatus))
    {
        // We hit a failure condition,
        // We will free the IRP

        IoFreeIrp(Irp);
        Irp = NULL;
    }

    return ntStatus;
}
```

## Related topics

[Sending Requests to a USB Device](communicating-with-a-usb-device.md)
