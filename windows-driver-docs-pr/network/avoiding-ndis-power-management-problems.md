---
title: Avoiding NDIS Power Management Problems
description: Avoiding NDIS Power Management Problems
keywords:
- power management WDK NDIS miniport , problems
- network interface cards WDK networking , power problems
- NICs WDK networking , power problems
ms.date: 03/02/2023
---

# Avoiding NDIS Power Management Problems





The following rules will help you avoid power-management problems with your network adapter:

-   A network adapter must always report its power management capabilities to the bus driver.

-   Do not try to enable or disable power management for a network adapter based on registry settings. NDIS obtains power management information about the network adapter from the bus driver before the network adapter's miniport driver is initialized. If the information obtained from the bus driver indicates that the network adapter is not power management-capable, NDIS treats the network adapter as an old network adapter and does not issue an [OID\_PNP\_CAPABILITIES](./oid-pnp-capabilities.md) request to the network adapter's miniport driver.

-   Do not attempt to provide custom power-management controls in the user interface.

 

