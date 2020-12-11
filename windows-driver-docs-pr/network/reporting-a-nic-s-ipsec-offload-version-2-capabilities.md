---
title: Reporting a NIC's IPsec Offload Version 2 Capabilities
description: Reporting a NIC's IPsec Offload Version 2 Capabilities
keywords:
- IPsecOV2 WDK TCP/IP transport , capabilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting a NIC's IPsec Offload Version 2 Capabilities

\[The IPsec Task Offload feature is deprecated and should not be used.\]




To specify IPsec offload version 2 (IPsecOV2) capabilities, an NDIS 6.1 and later miniport driver specifies the current or default configuration of a NIC in an [**NDIS\_IPSEC\_OFFLOAD\_V2**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_ipsec_offload_v2) structure. Miniport drivers must include the default IPsecOV2 configuration in the [**NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_offload_attributes) structure. Miniport drivers call the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function from the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function and pass in the information in NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES.

Miniport drivers must report changes in the IPsecOV2 capabilities, if any, in the [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](./ndis-status-task-offload-current-config.md) status indication.

**Note**  NDIS provides a direct OID request interface for NDIS 6.1 and later drivers. The [direct OID request path](/windows-hardware/drivers/ddi/_netvista/) supports OID requests that are queried or set frequently.

 

In response to a query of [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](./oid-tcp-offload-current-config.md), NDIS includes the NDIS\_IPSEC\_OFFLOAD\_V2 structure in the [**NDIS\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure that NDIS returns in the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure. NDIS uses the information that the miniport driver provided.

 

