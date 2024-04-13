---
title: NET_BUFFER_LIST Structure
description: NET_BUFFER_LIST Structure
keywords:
- NET_BUFFER_LIST
- network data WDK , structures
- data WDK networking , structures
- packets WDK networking , data structures
ms.date: 04/20/2017
---

# NET\_BUFFER\_LIST Structure





A [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure packages a linked list of NET\_BUFFER structures.

The following figure shows the fields in a NET\_BUFFER\_LIST structure.

:::image type="content" source="images/netbufferlist.png" alt-text="Diagram illustrating the fields in a NET_BUFFER_LIST structure.":::

The NET\_BUFFER\_LIST structure includes a [**NET\_BUFFER\_LIST\_HEADER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_header) structure in the **NetBufferListHeader** member. The NET\_BUFFER\_LIST\_HEADER structure includes a [**NET\_BUFFER\_LIST\_DATA**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_data) structure in the **NetBufferListData** member. You should use NDIS macros to access NET\_BUFFER\_LIST structure members. For more information about these macros, see the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure reference page.

Some of the members are only used by NDIS. The members that drivers are most likely to use are defined in the following list:

<a href="" id="parentnetbufferlist"></a>**ParentNetBufferList**  
If a NET\_BUFFER\_LIST structure is a child that was derived from a parent(cloned, fragmented, or reassembled), **ParentNetBufferList** specifies a pointer to the parent NET\_BUFFER\_LIST structure. Otherwise, this parameter is **NULL**.

<a href="" id="ndispoolhandle"></a>**NdisPoolHandle**  
Specifies a pool handle that identifies the NET\_BUFFER\_LIST pool from which the NET\_BUFFER\_LIST structure was allocated.

<a href="" id="protocolreserved"></a>**ProtocolReserved**  
Reserved for use by protocol drivers.

<a href="" id="miniportreserved"></a>**MiniportReserved**  
Reserved for use by miniport drivers.

<a href="" id="sourcehandle"></a>**SourceHandle**  
A handle that NDIS provided to the driver in a binding or attaching operation by using one of the following driver-supplied routines:

<a href="" id="miniport-driver"></a>Miniport Driver  
[*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize)

<a href="" id="protocol-driver"></a>Protocol Driver  
[*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex)

<a href="" id="filter-driver"></a>Filter Driver  
[*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach)

NDIS uses **SourceHandle** to return the NET\_BUFFER\_LIST structure to the driver that sent the NET\_BUFFER\_LIST structure. NDIS drivers should not read this handle.

<a href="" id="childrefcount"></a>**ChildRefCount**  
If a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure is a parent (has children derived by clone, fragment, or reassemble operations), **ChildRefCount** specifies the number of existing children. Otherwise, this parameter is zero.

<a href="" id="flags"></a>**Flags**  
Reserved for future specification of attributes for the NET\_BUFFER\_LIST structure. There are currently no flags available to drivers.

<a href="" id="status"></a>**Status**  
Specifies the final completion status of a network data operation for this NET\_BUFFER\_LIST structure. Miniport drivers write this value before completing a send operation.

<a href="" id="netbufferlistinfo"></a>**NetBufferListInfo**  
Specifies [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure information that is common to all [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structures in the list. This information is often referred to as "out-of-band (OOB) data."

<a href="" id="next"></a>**Next**  
Specifies a pointer to the next NET\_BUFFER\_LIST structure in a linked list of NET\_BUFFER\_LIST structures. If a NET\_BUFFER\_LIST structure is the last structure in the list, this member is **NULL**.

<a href="" id="firstnetbuffer"></a>**FirstNetBuffer**  
Specifies a pointer to the first NET\_BUFFER structure in a linked list of NET\_BUFFER structures that is associated with this NET\_BUFFER\_LIST structure.

**Note**  **Context** is a pointer to a [**NET\_BUFFER\_LIST\_CONTEXT**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list_context) structure. NDIS provides macros and functions to manipulate the data at **Context** . For more information about the NET\_BUFFER\_LIST\_CONTEXT structure, see [NET\_BUFFER\_LIST\_CONTEXT Structure](net-buffer-list-context-structure.md).

 

 

