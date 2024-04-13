---
title: Packet Structures in Network Drivers
description: Packet Structures in Network Drivers
keywords:
- packets WDK networking
- network drivers WDK , packets
- network data WDK
- data WDK networking
- network packet structures WDK
- network data buffers WDK
- data buffers WDK networking
- network data WDK , structures
- data WDK networking , structures
ms.date: 04/20/2017
---

# Packet Structures in Network Drivers





In NDIS 6.0 and later versions, a higher layer driver allocates [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) and [**NET\_BUFFER LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures to hold network packet information, and sends the structures to the next lower NDIS driver so that the data can be sent on the network. Lower-level drivers allocate NET\_BUFFER and NET\_BUFFER\_LIST structures to hold received data and pass the structures up to interested higher-layer drivers. Sometimes, a higher layer driver allocates structures and passes them to a lower layer driver with a request for the lower layer driver to copy received data into the buffers provided. NDIS provides functions for allocating and manipulating the substructures that make up the NET\_BUFFER and NET\_BUFFER\_LIST structures.

For more information about the structure of network data buffers in NDIS drivers, see [NET\_BUFFER Architecture](net-buffer-architecture.md).

 

