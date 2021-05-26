---
title: OID_QOS_OFFLOAD_HARDWARE_CAPABILITIES
description: An overlying driver issues OID_QOS_OFFLOAD_HARDWARE_CAPABILITIES to obtain the vmQoS offload hardware capabilities of a miniport adapter.
ms.assetid:
ms.date: 10/30/2020
keywords: 
 -OID_QOS_OFFLOAD_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_QOS_OFFLOAD_HARDWARE_CAPABILITIES


An overlying driver issues an OID query request of OID_QOS_OFFLOAD_HARDWARE_CAPABILITIES to obtain the Quality of Service (QoS) offload hardware capabilities of a miniport adapter.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS_OID_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS_QOS_OFFLOAD_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_offload_capabilities) structure.

## Remarks

The [**NDIS_QOS_OFFLOAD_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_offload_capabilities) structure specifies the hardware and current Hardware Quality of Service (QoS) offload capabilities of a miniport adapter.

### Return Status Codes

NDIS handles the OID query request of OID_QOS_OFFLOAD_HARDWARE_CAPABILITIES for miniport drivers and returns one of the following status codes.

|Status Code|Description|
|--- |--- |
|NDIS_STATUS_SUCCESS|The OID request completed successfully.|
|NDIS_STATUS_NOT_SUPPORTED|The miniport driver does not support the NDIS QoS interface.|
|NDIS_STATUS_BUFFER_TOO_SHORT|The length of the information buffer is not sufficient for the returned data.|
|NDIS_STATUS_Xxx|The request failed for other reasons.|

 

## Requirements

|Requirement|Value|
|--- |--- |
|Version|Supported in NDIS 6.85 and later.|
|Header|Ntddndis.h (include Ndis.h)|

## See also

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS_QOS_OFFLOAD_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_offload_capabilities)

[OID_QOS_OFFLOAD_CURRENT_CAPABILITIES](oid-qos-offload-current-capabilities.md)

 
