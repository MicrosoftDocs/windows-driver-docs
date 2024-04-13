---
title: Receive Side Scaling Support
description: Receive Side Scaling Support
keywords:
- scalable networking WDK
- receive-side scaling WDK networking
- RSS WDK networking
- miniport drivers WDK networking , scaling receive-packet processing
- NDIS miniport drivers WDK , scaling receive-packet processing
ms.date: 04/20/2017
---

# Receive Side Scaling Support





NDIS 6.0 introduced support for the scaling of receive-packet processing across multiple processors. The receive side scaling (RSS) interface accommodates several levels of NIC hardware support.

Based upon its current RSS configuration, a miniport driver or a NIC determines the target processor to associate with the received data. The RSS configuration can be adjusted to make the most efficient use of available target processors.

The miniport driver or NIC assigns the received data to a receive queue that is associated with a target processor. The miniport driver requests NDIS to schedule deferred procedure calls (DPCs) for target processors with non-empty receive queues.

NDIS schedules a DPC on each of the specified target processors. Each DPC processes a particular receive queue on the specified target processor.

For more information about NDIS 6.0 receive side scaling, see [Receive Side Scaling](./receive-side-scaling-version-2-rssv2-.md).

 

