---
title: Introduction to Header-Data Split
description: Introduction to Header-Data Split
keywords:
- header-data split WDK
- splitting header and data to separate buffers
- buffers WDK header-data split
- receiving data WDK networking
- frames WDK header-data split
- split frames WDK header-data split
- storage WDK header-data split
- space managemen
ms.date: 04/20/2017
---

# Introduction to Header-Data Split

This section describes header-data split services that are available in NDIS 6.1 and later versions. *Header-data split* improves network performance by splitting the header and data in received Ethernet frames into separate buffers. Separating the headers and the data enables the headers to be collected together into smaller regions of memory. As a result, more headers will fit into a single memory page and more headers will fit into the system caches, so the overhead for memory accesses in the driver stack is reduced.

This section includes:

[Header Data Split Overview](header-data-split-architecture.md)

[Initializing a Header-Data Split Provider](initializing-a-header-data-split-provider.md)

[Splitting Ethernet Frames](splitting-ethernet-frames.md)

[Receive Indications with Header-Data Split](receive-indications-with-header-data-split.md)

[Header-Data Split Administration and Configuration](setting-the-current-header-data-split-configuration.md)

[Supporting Header-Data Split in Protocol Driver and Filter Drivers](supporting-header-data-split-in-protocol-driver-and-filter-drivers.md)

 

 





