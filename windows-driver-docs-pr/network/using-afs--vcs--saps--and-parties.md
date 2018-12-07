---
title: Using AFs, VCs, SAPs, and Parties
description: Using AFs, VCs, SAPs, and Parties
ms.assetid: 4bf736a9-1236-4322-85f0-5d3ab7b8c549
keywords:
- connection-oriented NDIS WDK , entities created
- CoNDIS WDK networking , entities created
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using AFs, VCs, SAPs, and Parties





Connection-oriented drivers create and use entities including address families (AFs), virtual connections (VCs), service access points (SAPs), and parties.

When a connection-oriented driver registers an AF or creates a VC, SAP, or party, it passes a pointer to its local context area for that entity to NDIS. NDIS then returns to the driver (as well as to other appropriate connection-oriented drivers) a handle that represents the newly registered AF or the newly created VC, SAP, or party.

The following topics describe the entities that connection-oriented drivers create and use:

[Address Families](address-families.md)

[Virtual Connections](virtual-connections.md)

[Service Access Points](service-access-points.md)

[Parties](parties.md)

 

 





