---
title: WDI and WLAN Selective Suspend capability
description: This section describes how to enable USB Selective Suspend support for WDI drivers
ms.assetid: 4FCF726B-4CCF-4F0F-9088-2EABA0DA7D3C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI and WLAN Selective Suspend capability


To enable USB Selective Suspend support, the LE must report the capability. NDIS defines keywords for this feature. For more information, see [Standardized INF Keywords for NDIS Selective Suspend](standardized-inf-keywords-for-ndis-selective-suspend.md).

-   \*SelectiveSuspend : {Enable, Disable}

-   \*SSIdleTimeout : idle timeout in seconds

WDI enables support based on the following sources.

-   Device INF: This is written to the next item at device setup from the above keyword.
-   Registry settings: This is set from the INF or the Advanced property sheet for the device in Device Manager.
-   Power management capabilities in the return from [OID\_WDI\_GET\_ADAPTER\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/dn925838).
-   Idle handlers in [**NDIS\_MINIPORT\_DRIVER\_WDI\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/mt297617).
    -   [*MiniportWdiIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/mt297563)

    -   [*MiniportWdiCancelIdleNotification*](https://msdn.microsoft.com/library/windows/hardware/mt297560)

The WDI driver exposes two callback functions for the LE.

-   [**IdleNotificationComplete**](https://msdn.microsoft.com/library/windows/hardware/mt297600)

-   [**IdleNotificationConfirm**](https://msdn.microsoft.com/library/windows/hardware/mt297601)

 

 





