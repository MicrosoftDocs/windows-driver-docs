---
title: NDIS driver types
description: NDIS driver types
ms.assetid: ed7bd8b4-75d5-4ecd-beb2-df8ac1ce96b3
keywords:
- network drivers WDK , NDIS drivers
- NDIS WDK , driver types supported
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS driver types





The Network Driver Interface Specification (NDIS) library abstracts the network hardware from network drivers. NDIS also specifies a standard interface between layered network drivers, thereby abstracting lower-level drivers that manage hardware from upper-level drivers, such as network transports. NDIS also maintains state information and parameters for network drivers, including pointers to functions, handles, and parameter blocks for linkage, and other system values.

NDIS supports the following primary types of network drivers:

-   [Miniport drivers](ndis-miniport-drivers2.md)

-   [Protocol drivers](ndis-protocol-drivers2.md)

-   [Filter drivers](ndis-filter-drivers.md)

-   [Intermediate drivers](ndis-intermediate-drivers.md)

 

 





