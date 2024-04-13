---
title: Network Data Structures
description: Network Data Structures
keywords:
- NET_BUFFER
- NET_BUFFER_LIST
- NET_BUFFER_LIST_CONTEXT
- network data WDK , structures
- data WDK networking , structures
- packets WDK networking , data structures
ms.date: 04/20/2017
---

# Network Data Structures





Network data consists of packets of data that are sent or received over the network. NDIS provides data structures to describe and organize such data. The primary network data structures for NDIS 6.0 and later are:

-   [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer)
-   [**NET\_BUFFER LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list)
-   [**NET\_BUFFER\_LIST\_CONTEXT**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context)

The following figure illustrates the relationships between these structures.

:::image type="content" source="images/netbufferstructures.png" alt-text="Diagram illustrating NDIS 6.0 network data structures, including NET_BUFFER, NET_BUFFER_LIST, and NET_BUFFER_LIST_CONTEXT.":::

In NDIS 6.0 and later, the [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) is the basic building block for packaging network data. Each NET\_BUFFER structure has an MDL chain. The MDLs map the addresses of data buffers to the data space that the NET\_BUFFER structures specify. This data mapping is identical to the MDL chains that NDIS 5.*x* and earlier drivers use in the [**NDIS\_PACKET**](/previous-versions/windows/hardware/network/ff557086(v=vs.85)) structure. NDIS provides functions to manipulate the MDL chain.

Multiple NET\_BUFFER structures can be attached to a NET\_BUFFER\_LIST structure. The NET\_BUFFER structures are organized as a NULL-terminated singly linked list. Only the driver that originates a NET\_BUFFER\_LIST structure, or NDIS, should modify the linked list directly to insert and delete NET\_BUFFER structures.

[**NET\_BUFFER LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures contain information that describes all the [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structures that are attached to a list. If a driver requires additional space for context information, the driver can store such information in the NET\_BUFFER\_LIST\_CONTEXT structures. NDIS provides functions to allocate, free and access the data in the NET\_BUFFER\_LIST\_CONTEXT structures.

Multiple NET\_BUFFER\_LIST structures can be attached to form a list of NET\_BUFFER\_LIST structures. The NET\_BUFFER\_LIST structures are organized as a NULL-terminated singly linked list. Drivers can modify the linked list directly to insert and delete NET\_BUFFER\_LIST structures.

## Related topics


[**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer)

[NET\_BUFFER Structure](net-buffer-structure.md)

[**NET\_BUFFER LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list)

[NET\_BUFFER\_LIST Structure](net-buffer-list-structure.md)

[**NET\_BUFFER\_LIST\_CONTEXT**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context)

[NET\_BUFFER\_LIST\_CONTEXT Structure](net-buffer-list-context-structure.md)

 

