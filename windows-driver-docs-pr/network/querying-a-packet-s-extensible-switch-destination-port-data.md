---
title: Querying a Packet's Extensible Switch Destination Port Data
description: Querying a Packet's Extensible Switch Destination Port Data
ms.assetid: 57D82C5E-3758-492C-A1DA-B7BC3DBE2E7A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying a Packet's Extensible Switch Destination Port Data


Each Hyper-V extensible switch destination port is specified by an [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_switch_port_destination) element within the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_switch_forwarding_destination_array) structure. This array is contained in the out-of-band (OOB) forwarding context of the packet's [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer_list) structure. For more information on this context, see [Hyper-V Extensible Switch Forwarding Context](hyper-v-extensible-switch-forwarding-context.md).

The extensible switch extension calls the [*GetNetBufferListDestinations*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-ndis_switch_get_net_buffer_list_destinations) function to obtain a pointer to the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_switch_forwarding_destination_array) structure within a packet's [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer_list) structure. Individual [**NDIS\_SWITCH\_PORT\_DESTINATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_switch_port_destination) elements within this structure can be accessed by using the [**NDIS\_SWITCH\_PORT\_DESTINATION\_AT\_ARRAY\_INDEX**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-switch-port-destination-at-array-index) macro.

To improve performance, a forwarding extension can call the [*GrowNetBufferListDestinations*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-ndis_switch_grow_net_buffer_list_destinations) function instead of [*GetNetBufferListDestinations*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-ndis_switch_get_net_buffer_list_destinations) to obtain a pointer to the [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_switch_forwarding_destination_array) structure. The extension does this if it determines that it needs additional array elements in the packet's OOB data for destination ports. For more information, see [Adding Extensible Switch Destination Port Data to a Packet](adding-extensible-switch-destination-port-data-to-a-packet.md).

**Note**  Only packets obtained from the extensible switch egress data path will contain destination port information. For more information, see [Hyper-V Extensible Switch Data Path](hyper-v-extensible-switch-data-path.md).

 

 

 





