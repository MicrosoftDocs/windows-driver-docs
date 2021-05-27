---
title: OID_QOS_OFFLOAD_CREATE_SQ
description: A driver issues OID_QOS_OFFLOAD_CREATE_SQ to create a new Scheduler Queue (SQ) on the miniport adapter
ms.assetid:
ms.date: 10/30/2020
keywords: 
 -OID_QOS_OFFLOAD_CREATE_SQ Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_QOS_OFFLOAD_CREATE_SQ

Overlying drivers issue OID set requests of OID_QOS_OFFLOAD_CREATE_SQ to create a new Scheduler Queue (SQ) on the miniport adapter. The caller sets the **InformationBuffer** member of the [**NDIS_OID_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure to contain a pointer to an [**NDIS_QOS_SQ_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_sq_parameters) structure. **NDIS_QOS_SQ_PARAMETERS** contains the parameters of the new SQ.

## Remarks

**NDIS_QOS_SQ_ID** is a ULONG value that NDIS allocates and assigns for an SQ. This identifier is unique per miniport adapter. The value **NDIS_QOS_DEFAULT_SQ_ID** is not a valid SQ ID and means that no SQ is to be used.

### Return Status Codes

NDIS handles the OID set request of OID_QOS_OFFLOAD_CREATE_SQ for miniport drivers and returns one of the following status codes.

|Status Code|Description|
|--- |--- |
|NDIS_STATUS_SUCCESS|The OID request completed successfully.|
|NDIS_STATUS_INVALID_PARAMETER|The length of the **InformationBuffer** is less than NDIS_SIZEOF_QOS_SQ_PARAMETERS_REVISION_1 or the **SqId** field of [**NDIS_QOS_SQ_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_sq_parameters) in the **InformationBuffer** is **NDIS_QOS_DEFAULT_SQ_ID**. |
|NDIS_STATUS_Xxx|The request failed for other reasons.|

 

## Requirements

|Requirement|Value|
|--- |--- |
|Version|Supported in NDIS 6.85 and later.|
|Header|Ntddndis.h (include Ndis.h)|

## See also

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS_QOS_SQ_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_sq_parameters)

[**NDIS_QOS_OFFLOAD_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_offload_capabilities)

[OID_QOS_HARDWARE_CAPABILITIES](oid-qos-hardware-capabilities.md)

[OID_QOS_OFFLOAD_UPDATE_SQ](oid-qos-offload-update-sq.md)

 
