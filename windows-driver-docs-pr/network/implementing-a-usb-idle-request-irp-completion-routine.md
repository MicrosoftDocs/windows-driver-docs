---
title: Implementing a USB Idle Request IRP Completion Routine
description: Implementing a USB Idle Request IRP Completion Routine
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing a USB Idle Request IRP Completion Routine


When [*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification) is called, the USB miniport driver calls [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) to issue an I/O request packet (IRP) for a USB idle request ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)) to the underlying USB bus driver. The miniport driver issues this IRP to inform the USB bus driver that the network adapter is idle and must be suspended.

The USB miniport driver must also call [**IoSetCompletionRoutineEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutineex) in order to register a completion routine for the USB idle request IRP. The USB bus driver calls the completion routine when it completes the IRP after it is canceled by the USB miniport driver. The USB miniport driver cancels the IRP when NDIS cancels the idle notification by calling [*MiniportCancelIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_idle_notification).

The completion routine only has to call [**NdisMIdleNotificationComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismidlenotificationconfirm) in order to notify NDIS that it can continue with the full-power state transition of the network adapter.

**Note**  The completion routine must return STATUS\_MORE\_PROCESSING\_REQUIRED if the USB miniport driver will reuse the IRP resources during another idle notification from NDIS.

 

The following is an example of a completion routine for the USB idle request IRP.

```C++
//
// MiniportUsbIdleRequestCompletion()
//
// This is the IO_COMPLETION_ROUTINE for the selective suspend IOCTL.
// All that is needed is to inform NDIS that the IdleNotification
// operation is complete.
//
VOID MiniportUsbIdleRequestCompletion(PVOID AdapterContext)
{
    NdisMIdleNotificationComplete(Adapter->MiniportAdapterHandle);

    // We will be reusing the IRP later, so do not let the IO manager delete it.
    return STATUS_MORE_PROCESSING_REQUIRED;
}
```

For more information about the USB idle request callback routine, see USB Idle Request IRP Completion Routine.

 

