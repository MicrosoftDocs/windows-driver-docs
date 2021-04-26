---
title: Registering NDIS Selective Suspend Handler Functions
description: Registering NDIS Selective Suspend Handler Functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering NDIS Selective Suspend Handler Functions


If a miniport driver supports NDIS selective suspend, NDIS notifies the driver that the underlying network adapter has become idle. The miniport driver must provide the following functions to handle these idle notifications:

<a href="" id="miniportidlenotification"></a>[*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification)  
NDIS calls the [*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification) handler function to notify the miniport driver that the network adapter has become idle. The miniport driver handles the idle notification by determining whether the network adapter can transition to a low-power state. The miniport driver performs this determination in a bus-specific manner.

For example, a USB miniport driver determines whether the network adapter can transition to a low-power state by issuing an I/O request packet (IRP) for a USB idle request ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)) to the underlying USB bus driver. Through the processing of this IRP, the miniport driver is notified that the adapter is idle and can be transitioned to a low-power state.

<a href="" id="miniportcancelidlenotification"></a>[*MiniportCancelIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_idle_notification)  
NDIS calls the [*MiniportCancelIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_idle_notification) handler function to cancel the outstanding idle notification. When this function is called, the miniport driver cancels any bus-specific IRPs that it may have previously issued for the idle notification.

For example, when [*MiniportCancelIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_idle_notification) is called, the USB miniport must cancel the previously-issued USB idle request IRP. When the IRP is canceled, the miniport driver is notified that the adapter can now be transitioned to a full-power state.

When the miniport driver's [**DriverEntry**](./initializing-a-miniport-driver.md) function is called, the driver registers its NDIS selective suspend handler functions by following these steps:

1.  The miniport driver must set the **SetOptionsHandler** member of the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) structure to the entry point for the driver's [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function. The driver calls [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) to register its **NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS** structure with NDIS.

2.  NDIS calls the [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function in the context of the call to [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver).

    When [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) is called, the miniport driver initializes an [**NDIS\_MINIPORT\_SS\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_ss_characteristics) structure with pointers to the handler functions. The miniport driver then calls [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) and sets the *OptionalHandlers* parameter to a pointer to the **NDIS\_MINIPORT\_SS\_CHARACTERISTICS** structure.

For more information on how to handle idle notifications for NDIS selective suspend, see [NDIS Selective Suspend Idle Notifications](ndis-selective-suspend-idle-notifications.md).

 

