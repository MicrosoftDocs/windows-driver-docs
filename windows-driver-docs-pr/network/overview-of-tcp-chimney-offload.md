---
title: Overview of TCP Chimney Offload
description: Overview of TCP Chimney Offload
ms.assetid: d74095d8-cf7b-4259-ad07-1224d2ea20fc
keywords:
- TCP chimney offload WDK networking , about TCP chimney offload
- chimney offload WDK networking , about TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of TCP Chimney Offload


\[The TCP chimney offload feature is deprecated and should not be used.\]

The TCP chimney architecture offloads the data-transfer portion of TCP protocol processing for one or more TCP connections to a network interface card (NIC). This architecture provides a direct connection, called a *chimney*, between applications and an offload-capable NIC.

The chimney offload architecture reduces host network processing for network-intensive applications, so networked applications scale more efficiently and end-to-end latency is reduced. In addition, fewer servers are needed to host an application, and servers are able to use the full Ethernet bandwidth. The primary performance gains are obtained from:

-   Offloading segmentation and reassembly (SAR).

-   Offloading processing that ensures reliable connections (for example, acknowledgment (ACK) processing and TCP retransmission timers).

-   Reducing interrupt loading.

-   Zero-copy receive operations in many situations.

This section includes:

[TCP Chimney Architecture](tcp-chimney-architecture.md)

[Compliance with IETF RFCs](compliance-with-ietf-rfcs.md)

 

 





