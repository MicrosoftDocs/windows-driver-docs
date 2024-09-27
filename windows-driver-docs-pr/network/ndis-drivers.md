---
title: Overview of NDIS Driver Types
description: Network Driver Interface Specification (NDIS) supports the following driver types.
ms.date: 09/27/2024
---

# Overview of NDIS driver types

The Network Driver Interface Specification (NDIS) library abstracts the network hardware from network drivers. NDIS also specifies a standard interface between layered network drivers, thereby abstracting lower-level drivers that manage hardware from upper-level drivers, such as network transports. NDIS also maintains state information and parameters for network drivers, including pointers to functions, handles, and parameter blocks for linkage, and other system values.

NDIS supports the following primary types of network drivers:

-   [Miniport drivers](ndis-miniport-drivers2.md)

-   [Protocol drivers](ndis-protocol-drivers2.md)

-   [Filter drivers](ndis-filter-drivers.md)

-   [Intermediate drivers](ndis-intermediate-drivers.md)

**Note**: These topics detail each type of NDIS driver individually. For more information about the NDIS driver stack and a diagram showing the relationship between all four NDIS driver types, see [NDIS Driver Stack](ndis-driver-stack.md).
