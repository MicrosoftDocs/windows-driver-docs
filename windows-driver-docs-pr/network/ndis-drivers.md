---
title: NDIS Drivers
description: NDIS Drivers
ms.assetid: ed7bd8b4-75d5-4ecd-beb2-df8ac1ce96b3
keywords: ["network drivers WDK , NDIS drivers", "NDIS WDK , driver types supported"]
---

# NDIS Drivers


## <a href="" id="ddk-ndis-drivers-ng"></a>


The Network Driver Interface Specification (NDIS) library abstracts the network hardware from network drivers. NDIS also specifies a standard interface between layered network drivers, thereby abstracting lower-level drivers that manage hardware from upper-level drivers, such as network transports. NDIS also maintains state information and parameters for network drivers, including pointers to functions, handles, and parameter blocks for linkage, and other system values.

NDIS supports the following primary types of network drivers:

-   [NDIS Miniport Drivers](ndis-miniport-drivers.md)

-   [NDIS Protocol Drivers](ndis-protocol-drivers.md)

-   [NDIS Filter Drivers](ndis-filter-drivers.md)

-   [NDIS Intermediate Drivers](ndis-intermediate-drivers.md)

 

 





