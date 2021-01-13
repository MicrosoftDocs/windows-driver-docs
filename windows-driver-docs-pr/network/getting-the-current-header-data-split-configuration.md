---
title: Getting the Current Header-Data Split Configuration
description: Getting the Current Header-Data Split Configuration
keywords:
- header-data split WDK , configuration
- current header-data split configuration WDK networking
- status information WDK header-data split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Getting the Current Header-Data Split Configuration





To get the current header-data split settings of a miniport adapter, overlying drivers or user-mode applications can query the [OID\_GEN\_HD\_SPLIT\_CURRENT\_CONFIG](./oid-gen-hd-split-current-config.md) OID. However, overlying drivers should use the information that NDIS provides to them during initialization and with status indications.

A system administrator can use the GUID that is associated with the OID\_GEN\_HD\_SPLIT\_CURRENT\_CONFIG OID through the WMI interface. For more information about header-data split WMI GUIDs, see [WMI Support for Header-Data Split](wmi-support-for-header-data-split.md).

NDIS handles [OID\_GEN\_HD\_SPLIT\_CURRENT\_CONFIG](./oid-gen-hd-split-current-config.md) on behalf of the miniport driver. NDIS maintains the current header-data split configuration information based on the miniport driver initialization attributes and the [**NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG**](./ndis-status-hd-split-current-config.md) status indication.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains an [**NDIS\_HD\_SPLIT\_CURRENT\_CONFIG**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_hd_split_current_config) structure. NDIS also provides the NDIS\_HD\_SPLIT\_CURRENT\_CONFIG structure to overlying drivers during initialization and with the status indication.

When a miniport driver receives an [OID\_GEN\_HD\_SPLIT\_PARAMETERS](./oid-gen-hd-split-parameters.md) set request, the driver must use the contents of the [**NDIS\_HD\_SPLIT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_hd_split_parameters) structure to update the current configuration of the miniport adapter. After the update, the miniport driver must report the changes with the [**NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG**](./ndis-status-hd-split-current-config.md) status indication. The status indication ensures that all of the overlying drivers are updated with the new information.

When NDIS calls the [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function of NDIS 6.1 or later protocol drivers, NDIS provides an [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) structure with a pointer to an [**NDIS\_HD\_SPLIT\_CURRENT\_CONFIG**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_hd_split_current_config) structure.

When NDIS calls the [*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach) function of NDIS 6.1 or later filter drivers, NDIS provides an [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_attach_parameters) structure with a pointer to an NDIS\_HD\_SPLIT\_CURRENT\_CONFIG structure.

 

