---
title: WDI and WLAN Selective Suspend capability
description: This section describes how to enable USB Selective Suspend support for WDI drivers
ms.date: 03/02/2023
---

# WDI and WLAN Selective Suspend capability


To enable USB Selective Suspend support, the LE must report the capability. NDIS defines keywords for this feature. For more information, see [Standardized INF Keywords for NDIS Selective Suspend](standardized-inf-keywords-for-ndis-selective-suspend.md).

-   \*SelectiveSuspend : {Enable, Disable}

-   \*SSIdleTimeout : idle timeout in seconds

WDI enables support based on the following sources.

-   Device INF: This is written to the next item at device setup from the above keyword.
-   Registry settings: This is set from the INF or the Advanced property sheet for the device in Device Manager.
-   Power management capabilities in the return from [OID\_WDI\_GET\_ADAPTER\_CAPABILITIES](./oid-wdi-get-adapter-capabilities.md).
-   Idle handlers in [**NDIS\_MINIPORT\_DRIVER\_WDI\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_ndis_miniport_driver_wdi_characteristics).
    -   [*MiniportWdiIdleNotification*](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_idle_notification)

    -   [*MiniportWdiCancelIdleNotification*](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_cancel_idle_notification)

The WDI driver exposes two callback functions for the LE.

-   [**IdleNotificationComplete**](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_idle_notification_complete)

-   [**IdleNotificationConfirm**](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-ndis_wdi_idle_notification_confirm)

 

