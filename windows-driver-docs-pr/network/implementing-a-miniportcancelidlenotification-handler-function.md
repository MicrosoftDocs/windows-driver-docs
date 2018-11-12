---
title: Implementing a MiniportCancelIdleNotification Handler Function
description: Implementing a MiniportCancelIdleNotification Handler Function
ms.assetid: 51C25573-5723-44F9-B498-EBEF6756F3B0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing a MiniportCancelIdleNotification Handler Function


NDIS calls the miniport driver's [*MiniportCancelIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464088) handler function in order to cancel the idle notification process and transition the network adapter to a full-power state. When this function is called, the miniport driver must follow these steps:

1.  The miniport driver must cancel any bus-specific IRPs that it may have previously issued for the idle notification.

2.  The miniport driver calls [**NdisMIdleNotificationComplete**](https://msdn.microsoft.com/library/windows/hardware/hh451491). This call notifies NDIS that the idle notification has been completed. NDIS then comples the selective suspend operation by transitioning the network adapter to a full-power state.

For example, when [*MiniportCancelIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464088) is called, the USB miniport driver calls [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338) to cancel the I/O request packet (IRP) for a USB idle request ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)). The USB miniport driver previously issued this IRP in its [*MiniportIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464092) handler function. As soon as the USB bus driver has canceled the IRP, it calls the IRP's completion routine. When the USB bus driver calls the completion routine, it confirms that the IRP is canceled and the device can resume to a full-power state. In the context of the completion routine, the miniport driver calls [**NdisMIdleNotificationComplete**](https://msdn.microsoft.com/library/windows/hardware/hh451491).

**Note**  The USB bus driver can call the completion routine either synchronously in the context of the call to [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338) or asynchronously after [*MiniportCancelIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464088) returns.

 

The following is an example of a [*MiniportCancelIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464088) handler function for a USB miniport driver. This example shows the steps that are involved with canceling a USB idle request IRP.

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

 

 





