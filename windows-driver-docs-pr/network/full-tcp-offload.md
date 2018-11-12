---
title: Full TCP Offload
description: Full TCP Offload
ms.assetid: a940617a-b848-430d-8da1-acd946feba1b
keywords:
- TCP offload WDK networking
- chimney offload WDK networking , full
- offloading processing WDK networking
- full TCP offload WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Full TCP Offload





NDIS 6.0 introduced an architecture for full TCP offload. This architecture is called a "chimney offload" architecture because it provides a direct connection, called a "chimney," between applications and an offload-capable NIC. The chimney enables the NIC to perform TCP processing for offloaded connections, including maintaining the protocol state.

The chimney offload architecture reduces host network processing for network-intensive applications. This allows networked applications to scale more efficiently while also reducing end-to-end latency. Fewer servers are needed to host an application, and servers are able to use the full Ethernet bandwidth.

The TCP chimney offloads all TCP processing for one or more TCP connections. The primary performance gains are obtained from offloading segmentation and reassembly (SAR), offloading processing that ensures reliable connections (for example, ACK processing and TCP retransmission timers), and reducing interrupt loading.

**Note**  The Windows Vista operating system continues to support the individual TCP task offloads available in earlier versions of the operating system. These tasks can be offloaded on connections that have not been offloaded through a chimney. An offload-capable NIC should support both chimney offloads and task offloads. Such a NIC provides the highest degree of offload optimization.

 

For information on TCP chimney offload in NDIS 6.0 and later, see [NDIS TCP Chimney Offload](ndis-tcp-chimney-offload.md).

 

 





