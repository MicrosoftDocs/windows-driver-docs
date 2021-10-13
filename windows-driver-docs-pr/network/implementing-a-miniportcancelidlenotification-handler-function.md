---
title: Implementing a MiniportCancelIdleNotification Handler Function
description: Implementing a MiniportCancelIdleNotification Handler Function
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing a MiniportCancelIdleNotification Handler Function


NDIS calls the miniport driver's [*MiniportCancelIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_idle_notification) handler function in order to cancel the idle notification process and transition the network adapter to a full-power state. When this function is called, the miniport driver must follow these steps:

1.  The miniport driver must cancel any bus-specific IRPs that it may have previously issued for the idle notification.

2.  The miniport driver calls [**NdisMIdleNotificationComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismidlenotificationcomplete). This call notifies NDIS that the idle notification has been completed. NDIS then comples the selective suspend operation by transitioning the network adapter to a full-power state.

For example, when [*MiniportCancelIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_idle_notification) is called, the USB miniport driver calls [**IoCancelIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocancelirp) to cancel the I/O request packet (IRP) for a USB idle request ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)). The USB miniport driver previously issued this IRP in its [*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification) handler function. As soon as the USB bus driver has canceled the IRP, it calls the IRP's completion routine. When the USB bus driver calls the completion routine, it confirms that the IRP is canceled and the device can resume to a full-power state. In the context of the completion routine, the miniport driver calls [**NdisMIdleNotificationComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismidlenotificationcomplete).

**Note**  The USB bus driver can call the completion routine either synchronously in the context of the call to [**IoCancelIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocancelirp) or asynchronously after [*MiniportCancelIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_idle_notification) returns.

 

The following is an example of a [*MiniportCancelIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_idle_notification) handler function for a USB miniport driver. This example shows the steps that are involved with canceling a USB idle request IRP.

```C++
//
// MiniportCancelIdleNotification()
//
// This routine is called if NDIS has to cancel an idle notification.
// All that is needed is to cancel the selective suspend IRP.
//
VOID MiniportCancelIdleNotification(
    _In_ NDIS_HANDLE MiniportAdapterContext
    )
{
    IoCancelIrp(Adapter->UsbSsIrp);
}
```

For guidelines on implementing a completion routine for a USB idle request IRP, see [Implementing a USB Idle Request IRP Completion Routine](implementing-a-usb-idle-request-irp-completion-routine.md).

 

