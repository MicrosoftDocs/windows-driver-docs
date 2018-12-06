---
title: Address Families
description: Address Families
ms.assetid: d40df44e-f88b-4181-84ab-3fbf37172aaf
keywords:
- connection-oriented NDIS WDK , address families
- CoNDIS WDK networking , address families
- address families WDK networking
- AFs WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Address Families





An *address family* (AF) represents an association between one of the following sets of drivers:

-   A connection-oriented client, a call manager, and the underlying connection-oriented miniport driver.

-   A connection-oriented client and an MCM driver for a specific signaling protocol.

An address family also specifies a particular signaling protocol.

A call manager or MCM driver advertises its call manager services for a specific signaling protocol by registering the address family with NDIS. NDIS then notifies each client on the binding of the newly registered address family. Before it can use the call manager services provided by a call manager or MCM driver, a connection-oriented client must open the address family with the call manager or MCM driver that advertised it.

For more information about operations on address families, see [Registering and Opening an Address Family](registering-and-opening-an-address-family.md) and [Closing an Address Family](closing-an-address-family.md).

 

 





