---
title: How NDIS Detects Idle Network Adapters
description: How NDIS Detects Idle Network Adapters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How NDIS Detects Idle Network Adapters


After the miniport driver has enabled NDIS selective suspend and registered its handler functions, NDIS monitors the I/O activity of the network adapter in the following way:

-   NDIS monitors the calls to the I/O handler functions that the miniport driver registers through the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics) and [**NDIS\_MINIPORT\_PNP\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_pnp_characteristics) structures. For example, NDIS monitors calls to the miniport driver's [*MiniportSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists) or [*MiniportReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_return_net_buffer_lists) to determine whether the driver is involved in any packet I/O activity.

-   NDIS also monitors the calls of [**NdisOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisoidrequest) and [**NdisDirectOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdirectoidrequest) made by overlying protocol drivers.

    **Note**  NDIS monitors only those object identifier (OID) requests to the underlying miniport driver that are not handled directly by NDIS.

     

NDIS determines that the network adapter is idle if it does not detect any activity on the adapter for an idle time-out period. The duration of this time-out period is specified by the value of the **\*SSIdleTimeout** standardized INF keyword. For more information about this keyword, see [Standardized INF Keywords for NDIS Selective Suspend](standardized-inf-keywords-for-ndis-selective-suspend.md).

After the network adapter has become idle, NDIS starts the selective suspend operation. Through this operation, the network adapter is suspended by transitioning it to a low-power state.

NDIS begins this selective suspend operation by issuing an idle notification to the miniport driver. NDIS does this by calling the driver's [*MiniportIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_idle_notification) handler function. For more information about how the miniport driver handles this notification, see [Handling the NDIS Selective Suspend Idle Notification](handling-the-ndis-selective-suspend-idle-notification.md).

If NDIS detects that I/O requests to the network adapter are issued from overlaying drivers or if the adapter signals a wake-up event, NDIS cancels the idle notification. NDIS does this by calling the miniport driver's [*MiniportCancelIdleNotification*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_cancel_idle_notification) handler function.

For more information about how NDIS cancels the idle notification, see [Canceling the NDIS Selective Suspend Idle Notification](canceling-the-ndis-selective-suspend-idle-notification.md).

For more information about how the miniport driver completes the idle notification, see [Completing the NDIS Selective Suspend Idle Notification](completing-the-ndis-selective-suspend-idle-notification.md).

 

