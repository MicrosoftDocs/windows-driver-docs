---
title: NET_LUID Values for Miniport Adapters and Filter Modules
description: NET_LUID Values for Miniport Adapters and Filter Modules
keywords:
- NDIS network interfaces WDK , NET_LUID
- network interfaces WDK , NET_LUID
- NET_LUID
- miniport adapters WDK networking , NET_LUID value
- filter modules WDK networking , NET_LUID value
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NET\_LUID Values for Miniport Adapters and Filter Modules





NDIS registers interfaces on behalf of miniport drivers (for each miniport adapter) and filter drivers (for each filter module). A protocol driver can query NDIS for the interface index and [**NET\_LUID**](/windows/win32/api/ifdef/ns-ifdef-net_luid_lh) value of a miniport adapter that the driver is bound to by using its binding handle. For example, the protocol-driver lower edge of a MUX intermediate driver might obtain the NET\_LUID values to specify the layering order of its internal interfaces.

A protocol driver passes a binding handle at the *NdisBindingHandle* parameter to the [**NdisIfQueryBindingIfIndex**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisifquerybindingifindex) function and receives interface indexes and NET\_LUID values for the interfaces at the top and bottom of a filter stack. Alternatively, the protocol driver can retrieve these values in the [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) structure.

A miniport driver can also query NDIS for the interface index of a miniport adapter by using the NDIS miniport adapter handle. A miniport driver receives an interface index and a NET\_LUID value in the [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_init_parameters) structure.

A filter driver gets an interface index and a NET\_LUID value for a filter module in the [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_attach_parameters) structure.

 

