---
title: Reasons for Invalidating Offloaded State Objects
description: Reasons for Invalidating Offloaded State Objects
ms.assetid: 5abcf094-d361-4724-8bb7-c34dd7b2769d
keywords:
- invalidating offloaded state WDK TCP chimney offload , about invalidating offloaded state
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reasons for Invalidating Offloaded State Objects


\[The TCP chimney offload feature is deprecated and should not be used.\]




The host stack invalidates offloaded state to quickly stop data transmission on offloaded TCP connections that depend on that state. For example, when the host stack receives an Internet Control Message Protocol (ICMP) redirect to a new router, potentially thousands of offloaded TCP connections that depend on the old router can be affected at once. In this situation, the host stack invalidates the neighbor state that represents the old router. This invalidation causes the offload target to stop data transmission on all of the TCP connections that depend on the invalidated neighbor state object. The host stack then offloads a neighbor state object for the new router, if that state object has not already been offloaded, and issues an update to link the effected path state objects to the neighbor state object that represents the new router. For more information about this sequence of events, see [Linking Path State Objects to a New Neighbor State Object](linking-path-state-objects-to-a-new-neighbor-state-object.md).

The host stack typically does not invalidate the state for a single TCP connection. However, in this situation, it is faster for the host stack to terminate the offload of the connection and wait for the offload target's retransmit timer to time out. In the timeout interval, the host stack might find a new route, which would enable the host stack to offload a new neighbor state object to the offload target.

 

 





