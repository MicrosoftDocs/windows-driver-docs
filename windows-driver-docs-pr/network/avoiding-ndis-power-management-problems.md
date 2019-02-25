---
title: Avoiding NDIS Power Management Problems
description: Avoiding NDIS Power Management Problems
ms.assetid: 58bd91d5-68bd-471d-a961-6e0676d4a352
keywords:
- power management WDK NDIS miniport , problems
- network interface cards WDK networking , power problems
- NICs WDK networking , power problems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Avoiding NDIS Power Management Problems





The following rules will help you avoid power-management problems with your network adapter:

-   A network adapter must always report its power management capabilities to the bus driver.

-   Do not try to enable or disable power management for a network adapter based on registry settings. NDIS obtains power management information about the network adapter from the bus driver before the network adapter's miniport driver is initialized. If the information obtained from the bus driver indicates that the network adapter is not power management-capable, NDIS treats the network adapter as an old network adapter and does not issue an [OID\_PNP\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569774) request to the network adapter's miniport driver.

-   Do not attempt to provide custom power-management controls in the user interface.

 

 





