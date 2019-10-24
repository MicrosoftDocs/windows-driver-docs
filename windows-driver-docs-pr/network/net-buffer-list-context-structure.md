---
title: NET_BUFFER_LIST_CONTEXT Structure
description: NET_BUFFER_LIST_CONTEXT Structure
ms.assetid: 45be8503-2c5f-46e6-9fc3-b1b3c42f0d91
keywords:
- NET_BUFFER_LIST_CONTEXT
- network data WDK , structures
- data WDK networking , structures
- packets WDK networking , data structures
- network data WDK , context data
- data WDK networking , context data
- packets WDK networking , context data
- context da
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NET\_BUFFER\_LIST\_CONTEXT Structure





NDIS drivers use [**NET\_BUFFER\_LIST\_CONTEXT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer_list_context) structures to store additional data that is associated with a [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer_list) structure. The **Context** member of the NET\_BUFFER\_LIST structure is a pointer to a NET\_BUFFER\_LIST\_CONTEXT structure. The information stored in the NET\_BUFFER\_LIST\_CONTEXT structures is opaque to NDIS and other drivers in the stack.

The following figure shows the fields in a NET\_BUFFER\_LIST\_CONTEXT structure.

![diagram illustrating the fields in a net\-buffer\-list\-context structure](images/netbufferlistcontext.png)

The [**NET\_BUFFER\_LIST\_CONTEXT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer_list_context) structure includes **ContextData** member that contains the context data. This data can be any context information that a driver requires for the [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer_list) structure.

Drivers should use the following NDIS macros and functions to access and manipulate members in a NET\_BUFFER\_LIST\_CONTEXT structure:

[**NdisAllocateNetBufferListContext**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatenetbufferlistcontext)

[**NdisFreeNetBufferListContext**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreenetbufferlistcontext)

[**NET\_BUFFER\_LIST\_CONTEXT\_DATA\_START**](https://docs.microsoft.com/windows-hardware/drivers/network/net-buffer-list-context-data-start)

[**NET\_BUFFER\_LIST\_CONTEXT\_DATA\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/network/net-buffer-list-context-data-size)

 

 





