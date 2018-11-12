---
title: Implementing a USB Idle Request IRP Callback Routine
description: Implementing a USB Idle Request IRP Callback Routine
ms.assetid: B3F843CD-E9D8-4ABD-9BC9-08C5AB7CDB98
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing a USB Idle Request IRP Callback Routine


When [*MiniportIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464092) is called, the USB miniport driver calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to issue an I/O request packet (IRP) for a USB idle request ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)) to the underlying USB bus driver. The miniport driver issues this IRP to inform the USB bus driver that the network adapter is idle and must be suspended.

The USB miniport driver must provide an IRP callback routine for the USB idle request IRP. The USB bus driver calls this routine when it determines that the network adapter can be suspended and transitioned to a low-power state.

**Note**  After the USB bus driver handles the USB idle request IRP, it calls the callback routine either synchronously in the context of the call to [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) or asynchronously after [*MiniportIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464092) returns.

 

The callback routine only has to call [**NdisMIdleNotificationConfirm**](https://msdn.microsoft.com/library/windows/hardware/hh451492) in order to notify NDIS that it can continue with the low-power state transition of the network adapter. When the driver calls **NdisMIdleNotificationConfirm**, it must also specify the lowest device power state that the network adapter can transition to.

Within the context of the call to [**NdisMIdleNotificationConfirm**](https://msdn.microsoft.com/library/windows/hardware/hh451492), NDIS performs the steps that are required to transition the network adapter to a low-power state. For more information, see [Handling the NDIS Selective Suspend Idle Notification](handling-the-ndis-selective-suspend-idle-notification.md).

The following is an example of a callback routine for a USB idle request IRP.

```C++
//
// MiniportUsbIdleRequestCallback()
//
// This is the USB selective suspend idle notification.  All that is 
// needed is to inform NDIS that the USB stack is ready to go to a 
// low-power state.  Be aware that USB devices will always be requested
// to transition to a power state of NdisDeviceStateD2.
//
VOID MiniportUsbIdleRequestCallback(PVOID AdapterContext)
{
    NdisMIdleNotificationConfirm(
        AdapterContext->MiniportAdapterHandle,
        NdisDeviceStateD2
        );

    return;
}
```

For more information about the USB idle request callback routine, see USB Idle Request IRP Callback Routine.

 

 





