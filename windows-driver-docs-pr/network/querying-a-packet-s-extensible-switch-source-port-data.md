---
title: Querying a Packet's Extensible Switch Source Port Data
description: Querying a Packet's Extensible Switch Source Port Data
ms.date: 04/20/2017
---

# Querying a Packet's Extensible Switch Source Port Data


The Hyper-V extensible switch source port is specified by the **SourcePortId** member in the [**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_forwarding_detail_net_buffer_list_info) structure. This structure is contained in the out-of-band (OOB) forwarding context of the packet's [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure. For more information on this context, see [Hyper-V Extensible Switch Forwarding Context](hyper-v-extensible-switch-forwarding-context.md).

The extensible switch extension accesses the [**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_forwarding_detail_net_buffer_list_info) structure by using the [**NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL**](/windows-hardware/drivers/ddi/ndis/nf-ndis-net_buffer_list_switch_forwarding_detail) macro. The following example shows how the driver can obtain the source port identifier from the packet's **NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO** structure.

```C++
PNDIS_SWITCH_FORWARDING_DETAIL_NET_BUFFER_LIST_INFO fwdDetail;
NDIS_SWITCH_PORT_ID sourcePortId;

fwdDetail = NET_BUFFER_LIST_SWITCH_FORWARDING_DETAIL(NetBufferList);
sourcePortId = fwdDetail->SourcePortId;
```

 

