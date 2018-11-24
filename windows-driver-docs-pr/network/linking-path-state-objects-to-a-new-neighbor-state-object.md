---
title: Linking Path State Objects to a New Neighbor State Object
description: Linking Path State Objects to a New Neighbor State Object
ms.assetid: 2e4096d9-59b7-438e-82c0-83fccefca450
keywords:
- updating offloaded TCP chimney state, relinking path state objects
- inking path state objects WDK TCP chimney offload
- reinking path state objects WDK TCP chimney offload
- path state object relinking WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Linking Path State Objects to a New Neighbor State Object


\[The TCP chimney offload feature is deprecated and should not be used.\]




When the next hop address changes--for example, because of a router failure that results in a failover to a new router with a new IP address--the host stack can relink the effected offloaded path state objects to a new neighbor state object that represents the new router. The sequence of relinking the effected offloaded path state objectsis as follows:

1.  The host stack might invalidate the neighbor state object that represents the failed router. For more information about this operation, see [Terminating Offload State](terminating-offload-state.md).

2.  If the neighbor state object that represents the new router has not yet been offloaded to the offload target, the host stack offloads the new neighbor state object.

3.  The host stack relinks the path state objects that depend on the old neighbor state object (which represents the failed router) to the new neighbor state object by using an update operation. In the update operation, the host stack passes an [offload state tree](offload-state-tree.md) to the offload target's [**MiniportUpdateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff560463) function. The root of the state tree is an [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure that references the neighbor state object that represents the new router. This root block list is linked to [dependent block lists](offload-block-lists.md) that reference the path state objects to be relinked. After receiving this state tree, the offload target updates its internal representation of offloaded state so that the referenced path objects are linked to the neighbor state object that represents the new router.

4.  The host stack terminates the offload of the old neighbor state object. For more information about this operation, see [Terminating Offload State](terminating-offload-state.md)

It is important that you distinguish between the following:

-   Updating a neighbor's *DestinationAddress* (medium access control (MAC) address) variable

-   Updating the next hop address, which involves relinking path state objects to a new neighbor

The host stack updates the cached *DestinationAddress* variable of an offloaded neighbor state object only in response to an ARP update or a neighbor discovery. An ARP update or neighbor discovery changes the mapping of a neighbor's IP address to a MAC address. Updating the *DestinationAddress* variable does not involve relinking path state objects to a different neighbor state object.

When the host is notified of a change in the neighbor's next hop address--for example through an Internet Control Message Protocol (ICMP) redirect or a Routing Information Protocol (RIP) update--the host stack ultimately relinks the effected path state objects to a different neighbor state object. Because the link between a path state object and a neighbor state object represents the IP address of the neighbor, relinking the paths to a new neighbor is equivalent to changing the next hop address.

 

 





