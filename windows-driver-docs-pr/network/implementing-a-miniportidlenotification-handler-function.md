---
title: Implementing a MiniportIdleNotification Handler Function
description: Implementing a MiniportIdleNotification Handler Function
ms.date: 04/20/2017
---

# Implementing a MiniportIdleNotification Handler Function


NDIS calls the miniport driver's [*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification) handler function in order to selectively suspend the network adapter. The adapter is suspended when NDIS transitions the adapter to a low-power state.

The miniport driver can veto the idle notification if the network adapter is still being used. The driver does this by returning NDIS\_STATUS\_BUSY from the [*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification) handler function.

**Note**  The miniport driver cannot veto the idle notification if the *ForceIdle* parameter of the [*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification) handler function is set to **TRUE**.

 

If the miniport driver does not veto the idle notification, it may have to issue bus-specific I/O request packets (IRPs) to the underlying bus driver. These IRPs notify the bus driver about the adapter's idle state and request confirmation that the adapter can transition to a low-power state.

For example, when [*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification) is called, the USB miniport driver prepares an I/O request packet (IRP) for a USB idle request ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)). When the miniport driver prepares the IRP, it must specify a callback function. The driver must also call either [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) or [**IoSetCompletionRoutineEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutineex) to specify a completion routine for the IRP. The miniport driver then calls [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) to issue the IRP to the USB bus driver.

**Note**  The USB bus driver does not immediately complete the IRP. The IRP is left in a pending state through the low-power transition. The bus driver completes the IRP only when it is canceled by the miniport driver or a hardware event occurs, such as the surprise removal of the network adapter from the USB hub.

 

The following is an example of a [*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification) handler function for a USB miniport driver. This example shows the steps that are involved with issuing a USB idle request IRP to the underlying USB driver. This example also shows how the IRP resources, which were previously allocated in [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize), can be reused for the IRP.

```C++
//
// MiniportIdleNotification()
//
// This routine is invoked by NDIS when it has detected that the miniport
// is idle.  The miniport must prepare to issue its selective suspend IRP
// to the USB stack.  The driver can return NDIS_STATUS_BUSY if it is
// unwilling to become idle at this moment; NDIS will then retry later.
// Otherwise, the miniport should return NDIS_STATUS_PENDING.
//
NDIS_STATUS MiniportIdleNotification(
    _In_ NDIS_HANDLE MiniportAdapterContext,
    _In_ BOOLEAN ForceIdle
    )
{
    PIO_STACK_LOCATION IoSp;

    IoReuseIrp(Adapter->UsbSsIrp, STATUS_NOT_SUPPORTED);

    IoSp = IoGetNextIrpStackLocation(Adapter->UsbSsIrp);
    IoSp->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;
    IoSp->Parameters.DeviceIoControl.IoControlCode 
            = IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION;
    IoSp->Parameters.DeviceIoControl.InputBufferLength 
            = sizeof(Adapter->UsbSsCallback);
    IoSp->Parameters.DeviceIoControl.Type3InputBuffer 
            = Adapter->UsbSsCallback;

    IoSetCompletionRoutine(
            Adapter->UsbSsIrp,
            MiniportUsbIdleRequestCompletion,
            Adapter,
            TRUE,
            TRUE,
            TRUE);

    NtStatus = IoCallDriver(Adapter->Fdo, Adapter->UsbSsIrp);
    if (!NT_SUCCESS(NtStatus))
    {
       return NDIS_STATUS_FAILURE;
    }

    return NDIS_STATUS_PENDING;
}
```

For guidelines on implementing a callback routine for a USB idle request IRP, see [Implementing a USB Idle Request IRP Callback Routine](implementing-a-usb-idle-request-irp-callback-routine.md).

 

