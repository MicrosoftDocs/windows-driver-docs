---
title: Introduction to NDIS Selective Suspend
description: Introduction to NDIS Selective Suspend
ms.date: 03/02/2023
---

# Introduction to NDIS Selective Suspend


Starting with NDIS 6.30, the NDIS selective suspend interface allows NDIS to suspend an idle network adapter by transitioning the adapter to a low-power state. This enables the system to reduce the power overhead on the CPU and network adapter.

This section includes the following topics:

[Overview of NDIS Selective Suspend](overview-of-ndis-selective-suspend.md)

[Reporting NDIS Selective Suspend Capabilities](reporting-ndis-selective-suspend-capabilities.md)

[Registering NDIS Selective Suspend Handler Functions](registering-ndis-selective-suspend-handler-functions.md)

[NDIS Selective Suspend Idle Notifications](ndis-selective-suspend-idle-notifications.md)

[Standardized INF Keywords for NDIS Selective Suspend](standardized-inf-keywords-for-ndis-selective-suspend.md)

[NDIS Selective Suspend Implementation Guidelines](managing-irp-resources-for-ndis-selective-suspend.md)

**Note**  Although the NDIS selective suspend interface is especially useful for USB network adapters, the interface is bus-independent. As a result, miniport drivers can use the interface for network adapters on other bus types in order to reduce CPU and power overhead.

 

 

 





