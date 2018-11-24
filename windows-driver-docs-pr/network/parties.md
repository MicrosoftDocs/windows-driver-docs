---
title: Parties
description: Parties
ms.assetid: ca60ee28-53a4-40ec-956c-d7d3e866f681
keywords:
- point-to-multipoint connections WDK CoNDIS
- parties WDK CoNDIS
- connection-oriented NDIS WDK , parties
- CoNDIS WDK networking , parties
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Parties





A *party* represents one of possibly many leaves of a *point-to-multipoint connection*. When making an outgoing call, a connection-oriented client can specify a party. This makes the call a multipoint call, with the client acting as the *root* of the call and the remote party as a *leaf*. The client can then request that additional remote parties be added as *leaf nodes* to the call.

For more information about adding parties to a point-to-multipoint call, see [Adding a Party to a Multipoint Call](adding-a-party-to-a-multipoint-call.md). For information about deleting parties from a point-to-multipoint call, see [Dropping a Party from a Multipoint Call](dropping-a-party-from-a-multipoint-call.md).

 

 





