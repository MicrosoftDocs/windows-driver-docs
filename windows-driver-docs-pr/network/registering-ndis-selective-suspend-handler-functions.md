---
title: Registering NDIS Selective Suspend Handler Functions
description: Registering NDIS Selective Suspend Handler Functions
ms.assetid: D4125F14-8356-4D9E-A287-D35D3BF69182
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering NDIS Selective Suspend Handler Functions


If a miniport driver supports NDIS selective suspend, NDIS notifies the driver that the underlying network adapter has become idle. The miniport driver must provide the following functions to handle these idle notifications:

<a href="" id="miniportidlenotification"></a>[*MiniportIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464092)  
NDIS calls the [*MiniportIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464092) handler function to notify the miniport driver that the network adapter has become idle. The miniport driver handles the idle notification by determining whether the network adapter can transition to a low-power state. The miniport driver performs this determination in a bus-specific manner.

For example, a USB miniport driver determines whether the network adapter can transition to a low-power state by issuing an I/O request packet (IRP) for a USB idle request ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)) to the underlying USB bus driver. Through the processing of this IRP, the miniport driver is notified that the adapter is idle and can be transitioned to a low-power state.

<a href="" id="miniportcancelidlenotification"></a>[*MiniportCancelIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464088)  
NDIS calls the [*MiniportCancelIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464088) handler function to cancel the outstanding idle notification. When this function is called, the miniport driver cancels any bus-specific IRPs that it may have previously issued for the idle notification.

For example, when [*MiniportCancelIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/hh464088) is called, the USB miniport must cancel the previously-issued USB idle request IRP. When the IRP is canceled, the miniport driver is notified that the adapter can now be transitioned to a full-power state.

When the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548818) function is called, the driver registers its NDIS selective suspend handler functions by following these steps:

1.  The miniport driver must set the **SetOptionsHandler** member of the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure to the entry point for the driver's [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function. The driver calls [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) to register its **NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS** structure with NDIS.

2.  NDIS calls the [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function in the context of the call to [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654).

    When [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) is called, the miniport driver initializes an [**NDIS\_MINIPORT\_SS\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/hh451559) structure with pointers to the handler functions. The miniport driver then calls [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) and sets the *OptionalHandlers* parameter to a pointer to the **NDIS\_MINIPORT\_SS\_CHARACTERISTICS** structure.

For more information on how to handle idle notifications for NDIS selective suspend, see [NDIS Selective Suspend Idle Notifications](ndis-selective-suspend-idle-notifications.md).

 

 





