---
title: Implementing a USB Idle Request IRP Completion Routine
description: Implementing a USB Idle Request IRP Completion Routine
ms.assetid: C9435A1D-031B-4F67-B968-66534C48A9BC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing a USB Idle Request IRP Completion Routine


When [*MiniportIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464092) is called, the USB miniport driver calls [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to issue an I/O request packet (IRP) for a USB idle request ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)) to the underlying USB bus driver. The miniport driver issues this IRP to inform the USB bus driver that the network adapter is idle and must be suspended.

The USB miniport driver must also call [**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686) in order to register a completion routine for the USB idle request IRP. The USB bus driver calls the completion routine when it completes the IRP after it is canceled by the USB miniport driver. The USB miniport driver cancels the IRP when NDIS cancels the idle notification by calling [*MiniportCancelIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464088).

The completion routine only has to call [**NdisMIdleNotificationComplete**](https://msdn.microsoft.com/library/windows/hardware/hh451492) in order to notify NDIS that it can continue with the full-power state transition of the network adapter.

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

 

 





