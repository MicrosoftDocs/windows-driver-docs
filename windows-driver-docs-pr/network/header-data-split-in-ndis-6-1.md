---
title: Header-Data Split in NDIS 6.1
description: Header-Data Split in NDIS 6.1
keywords:
- header-data split WDK , about header-data split
ms.date: 03/02/2023
---

# Header-Data Split in NDIS 6.1





*Header-data split* services improve network performance by splitting the header and data in received Ethernet frames into separate buffers. By separating the headers and the data, these services enable the headers to be collected together into smaller regions of memory. Therefore, more headers fit into a single memory page and more headers fit into the system caches, so the overhead for memory accesses in the driver stack is reduced.

The header-data split interface is an optional service that is provided for header-data-split-capable network interface cards (NICs).

For more information about header-data split, see [Header-Data Split](header-data-split.md).

 

 





