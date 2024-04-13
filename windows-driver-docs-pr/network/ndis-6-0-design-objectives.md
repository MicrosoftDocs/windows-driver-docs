---
title: NDIS 6.0 Design Objectives
description: NDIS 6.0 Design Objectives
keywords:
- NDIS WDK , about NDIS
ms.date: 03/02/2023
---

# NDIS 6.0 Design Objectives





Two major objectives have guided the design and development of NDIS 6.0:

1.  Enhancing driver performance and scalability. (See [Enhanced Performance and Scalability](enhanced-performance-and-scalability.md) for more information.)

    Major improvements in the following provide significant performance gains for both clients and servers:

    -   Network data packaging
    -   Send and receive paths
    -   Run-time reconfiguration capabilities
    -   Scatter/gather DMA
    -   Filter drivers
    -   Multiprocessor scaling of received data handling
    -   Offloading TCP tasks to NICs

2.  Simplifying the NDIS driver model. (See [Simplified Driver Model](simplified-driver-model.md) for more information.)

    The following improvements simplify driver development:

    -   Streamlined driver initialization
    -   Versioning support for NDIS interfaces
    -   Simplified reset handling
    -   A standard interface for obtaining management information
    -   A filter driver model to replace filter intermediate drivers

 

 





