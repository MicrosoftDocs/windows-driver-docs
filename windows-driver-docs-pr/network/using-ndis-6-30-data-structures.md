---
title: Using NDIS 6.30 Data Structures
description: Using NDIS 6.30 Data Structures
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using NDIS 6.30 Data Structures


NDIS can support multiple versions of the same data structure. For the Windows 8 and Windows Server 2012 operating systems, miniport drivers that use an NDIS 6.30 version of a structure must initialize the **Header** member of the structure with the correct version and size values. The **Header** member is an [**NDIS\_OBJECT\_HEADER**](/windows-hardware/drivers/ddi/objectheader/ns-objectheader-ndis_object_header) structure, and the driver must initialize the **Revision** member and **Size** member value of the **Header** member to the NDIS 6.30 version and size values.

**Note**  To determine the correct version and size information see the reference pages for each structure that includes a **Header** member. The reference pages for structures that contain a **Header** member and that were updated for NDIS 6.30 include new information for NDIS 6.30 drivers. If there is no update to the structure for NDIS 6.30, the information that is provided for earlier versions of NDIS also applies to NDIS 6.30 drivers.

 

The following structures were updated for NDIS 6.30:

- [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters)
- [**NDIS\_MINIPORT\_ADAPTER\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_attributes)
- [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes)
- [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_hardware_assist_attributes)
- [**NDIS\_MINIPORT\_ADAPTER\_NATIVE\_802\_11\_ATTRIBUTES**](/previous-versions/windows/hardware/wireless/ff565926(v=vs.85))
- [**NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_net_buffer_list_filtering_info)
- [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities)
- [**NDIS\_OFFLOAD**](/windows-hardware/drivers/ddi/ndischimney/ns-ndischimney-_ndis_offload_handle)
- [**NDIS\_OFFLOAD\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload_parameters)
- [**NDIS\_PM\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_capabilities)
- [**NDIS\_PM\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_parameters)
- [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_capabilities)
- [**NDIS\_RECEIVE\_FILTER\_INFO\_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_info_array)
- [**NDIS\_RECEIVE\_FILTER\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_parameters)
- [**NDIS\_RECEIVE\_QUEUE\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_info)
- [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_queue_parameters)
- [**NDIS\_RECEIVE\_SCALE\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_capabilities)
- [**NDIS\_RSS\_PROCESSOR\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rss_processor_info)
- [**NDIS\_SHARED\_MEMORY\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_shared_memory_parameters)
 

