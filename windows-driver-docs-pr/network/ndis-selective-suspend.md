---
title: NDIS Selective Suspend
description: NDIS Selective Suspend
ms.assetid: B0D44AE3-5197-4264-9838-83FB5EFEB0B0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Selective Suspend


Starting with NDIS 6.30, the NDIS selective suspend interface allows NDIS to suspend an idle network adapter by transitioning the adapter to a low-power state. This enables the system to reduce the power overhead on the CPU and network adapter.

This section includes the following topics:

[Overview of NDIS Selective Suspend](overview-of-ndis-selective-suspend.md)

[Reporting NDIS Selective Suspend Capabilities](reporting-ndis-selective-suspend-capabilities.md)

[Registering NDIS Selective Suspend Handler Functions](registering-ndis-selective-suspend-handler-functions.md)

[NDIS Selective Suspend Idle Notifications](ndis-selective-suspend-idle-notifications.md)

[Standardized INF Keywords for NDIS Selective Suspend](standardized-inf-keywords-for-ndis-selective-suspend.md)

[NDIS Selective Suspend Implementation Guidelines](ndis-selective-suspend-implementation-guidelines.md)

**Note**  Although the NDIS selective suspend interface is especially useful for USB network adapters, the interface is bus-independent. As a result, miniport drivers can use the interface for network adapters on other bus types in order to reduce CPU and power overhead.

 

 

 





