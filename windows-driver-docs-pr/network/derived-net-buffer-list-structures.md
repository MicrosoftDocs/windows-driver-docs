---
title: Derived NET_BUFFER_LIST Structures
description: Derived NET_BUFFER_LIST Structures
keywords:
- NET_BUFFER_LIST
- network data WDK , structures
- data WDK networking , structures
- packets WDK networking , data structures
- derived structures WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Derived NET\_BUFFER\_LIST Structures





NDIS provides functions that drivers can use to manage [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures that are derived from other NET\_BUFFER\_LIST structures. These functions are typically used by intermediate drivers.

The following NDIS functions can create derived NET\_BUFFER\_LIST structures from an existing NET\_BUFFER\_LIST structure:

[**NdisAllocateCloneNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocateclonenetbufferlist)

[**NdisAllocateFragmentNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatefragmentnetbufferlist)

[**NdisAllocateReassembledNetBufferList**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatereassemblednetbufferlist)

These functions improve system performance because NDIS creates the derived structures without copying the network data. There are three types of [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures that can be derived from an existing NET\_BUFFER\_LIST structure:

<a href="" id="clone"></a>Clone  
A cloned NET\_BUFFER\_LIST structure is a duplicate that references the original data. Drivers can use this type of structure to efficiently transfer the same data to multiple paths.

<a href="" id="fragment"></a>Fragment  
A fragment [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure includes a set of [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structures that reference the original data; however, the data is divided into units that do not exceed a maximum size. Drivers can use this type of structure to efficiently break up large buffers into smaller buffers.

<a href="" id="reassembled"></a>Reassembled  
A reassembled NET\_BUFFER\_LIST structure contains a NET\_BUFFER structure that references the original data from multiple source NET\_BUFFER structures. Drivers can use this type of structure to efficiently combine many smaller buffers into a single large buffer.

This following topics provide more information about derived NET\_BUFFER\_LIST structures:

-   [Relationships Between NET\_BUFFER\_LIST Generations](relationships-between-net-buffer-list-generations.md)
-   [Cloned NET\_BUFFER\_LIST Structures](cloned-net-buffer-list-structures.md)
-   [Fragmented NET\_BUFFER\_LIST Structures](fragmented-net-buffer-list-structures.md)
-   [Reassembled NET\_BUFFER\_LIST Structures](reassembled-net-buffer-list-structures.md)

 

