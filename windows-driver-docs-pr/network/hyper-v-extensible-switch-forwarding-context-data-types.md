---
title: Hyper-V Extensible Switch Forwarding Context Data Types
description: Hyper-V Extensible Switch Forwarding Context Data Types
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch Forwarding Context Data Types


The [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure for each packet that traverses the Hyper-V extensible switch data path contains out-of-band (OOB) data. This data specifies the source port from where the packet originated, as well as one or more destination ports for packet delivery. This OOB data is known as the *extensible switch forwarding context*.

The following data types have been declared to access the extensible switch forwarding context within a packet's [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure:

<a href="" id="ndis-switch-forwarding-detail-net-buffer-list-info"></a>[**NDIS\_SWITCH\_FORWARDING\_DETAIL\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_forwarding_detail_net_buffer_list_info)  
This is a 64-bit union that contains the forwarding characteristics of a packet. This data includes the identifiers for the source port and network adapter connection from which the packet originated. This data also includes the number of unused elements that are available in the destination port array.

The extensible switch extension can access this data by using the [**NET\_BUFFER\_LIST\_SWITCH\_FORWARDING\_DETAIL**](/windows-hardware/drivers/ddi/ndis/nf-ndis-net_buffer_list_switch_forwarding_detail) macro.

<a href="" id="ndis-switch-forwarding-destination-array"></a>[**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_forwarding_detail_net_buffer_list_info)  
This structure defines the destination port array for the packet. Each element in this array is formatted as an [**NDIS\_SWITCH\_PORT\_DESTINATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_port_destination) structure.

The [**NDIS\_SWITCH\_FORWARDING\_DESTINATION\_ARRAY**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_forwarding_detail_net_buffer_list_info) structure contains members that specify the current number of the total number of elements as well as the number of used elements in the array.

The extensible switch extension can obtain this array by calling the [*GetNetBufferListDestinations*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_get_net_buffer_list_destinations) function. If the driver adds or modifies elements in the array for a packet with multiple destination ports, it must call the [*UpdateNetBufferListDestinations*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_update_net_buffer_list_destinations) function. This function commits those changes to the destination port array in the packet's forwarding context.

**Note**  To commit changes to a packet with only one destination port, it is more efficient for the driver to call the [*AddNetBufferListDestination*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_add_net_buffer_list_destination) function.

 

<a href="" id="ndis-switch-port-destination"></a>[**NDIS\_SWITCH\_PORT\_DESTINATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_port_destination)  
This structure defines a destination port for the packet. For packets with a single destination port, there is only one [**NDIS\_SWITCH\_PORT\_DESTINATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_switch_port_destination) element in the destination port array. For packets with multiple destination ports, there are one or more of these elements in the array.

After the extensible switch extension has called [*GetNetBufferListDestinations*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_get_net_buffer_list_destinations) to obtain the packet's destination port array, it can access individual elements in the array by using the [**NDIS\_SWITCH\_PORT\_DESTINATION\_AT\_ARRAY\_INDEX**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndis_switch_port_destination_at_array_index) macro.

 

