---
title: Layers of Offload State
description: Layers of Offload State
ms.assetid: 50f5d8f7-4d32-4cf9-84a3-20523f0c6946
keywords:
- offload state WDK TCP chimney offload , layers
- neighbor state WDK TCP chimney offload
- path state WDK TCP chimney offload
- TCP connection state WDK TCP chimney offload
- layers of offload state WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Layers of Offload State


\[The TCP chimney offload feature is deprecated and should not be used.\]




As the following figure shows, the host stack offloads three layers of protocol state to an offload target.

![diagram illustrating how the host stack offloads three layers of protocol state to an offload target](images/offload-layers.png)

<a href="" id="neighbor-state"></a>Neighbor state  
The neighbor state is supplied by the framing layer (OSI layer 2) of the host stack. This state contains the destination medium access control (MAC) address of the next hop (neighbor) and information that the offload target uses to maintain the neighbor state.

<a href="" id="path-state"></a>Path state  
The path state is supplied by the network layer (OSI layer 3) of the host stack. This state is essentially a route (destination) cache entry that contains the source and destination IP addresses of an Internet path and the path maximum transmission unit (MTU).

<a href="" id="tcp-connection-state"></a>TCP connection state  
The TCP state is supplied by the transport layer (OSI layer 4) of the host stack. This state contains all of the necessary TCP parameters for a specific TCP connection.

 

 





