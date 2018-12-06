---
title: NET_BUFFER Data Packaging
description: NET_BUFFER Data Packaging
ms.assetid: f0d539ab-c6ed-4cd9-9891-ef4235016d50
keywords:
- NDIS WDK , sending and receiving data
- data packaging WDK networking
- sending data WDK networking
- receiving data WDK networking
- NDIS_PACKET
- NET_BUFFER data packaging WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NET\_BUFFER Data Packaging





Data packaging was redesigned in NDIS 6.0. The send and receive architecture that is based on the [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure has been replaced with an architecture that is based on [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) and [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures. A NET\_BUFFER structure is the functional equivalent of an NDIS\_PACKET structure. A NET\_BUFFER structure specifies a buffer (MDL chain) for network data, as well as reserved space for NDIS, protocol drivers, and miniport drivers. NET\_BUFFER structures can be linked together in a list that is described by a NET\_BUFFER\_LIST structure. A NET\_BUFFER\_LIST structure also provides storage for out-of-band (OOB) data that applies to all the NET\_BUFFER structures in the list.

All components in the Microsoft next generation network driver stack, including the TCP/IP transport and Winsock, use NET\_BUFFER data packaging. Uniform data packaging throughout the driver stack eliminates the need to repackage data, simplifies data handling, and reduces the number of function calls.

To accommodate older drivers that use NDIS\_PACKET structures, NDIS 6.0 translates NDIS\_PACKET structures to NET\_BUFFER structures and vice versa. This translation is transparent to NDIS drivers.

NDIS propagates a driver's data backfill requirements to higher-level drivers. When allocating NET\_BUFFER and NET\_BUFFER\_LIST structures for send data, a higher-level driver allocates enough data space to accommodate all lower-level drivers in the stack. As a result, lower-level drivers do not have to allocate additional buffer space to accommodate layer-specific headers. Instead, they can use the preallocated backfill space for this purpose.

For more information about the NET\_BUFFER architecture, see [NET\_BUFFER Architecture](net-buffer-architecture.md).

 

 





