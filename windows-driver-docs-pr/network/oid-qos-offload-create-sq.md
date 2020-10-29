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

Overlying drivers issue OID method requests of OID_QOS_OFFLOAD_CREATE_SQ to create a new Scheduler Queue (SQ) on the miniport adapter. The caller sets the **InformationBuffer** member of the [**NDIS_OID_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure to contain a pointer to an [**NDIS_QOS_SQ_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_sq_parameters) structure. **NDIS_QOS_SQ_PARAMETERS** contains the parameters of the new SQ.

After a successful return from the OID query request, the **InformationBuffer** member of the **NDIS_OID_REQUEST** structure contains a pointer to an **NDIS_QOS_SQ_PARAMETERS** structure that specifies the SQ ID (**NDIS_QOS_SQ_ID**) of the new SQ.

## Remarks

**NDIS_QOS_SQ_ID** is a ULONG value that NDIS allocates and assigns for an SQ. This identifier is unique per miniport adapter. The value **zero** is not a valid SQ ID, and means that no SQ is to be used.

### Return Status Codes

NDIS handles the OID query request of OID_QOS_OFFLOAD_CREATE_SQ request for miniport drivers and returns one of the following status codes.

|Status Code|Description|
|--- |--- |
|NDIS_STATUS_SUCCESS|The OID request completed successfully.|
|NDIS_STATUS_NOT_SUPPORTED|The miniport driver does not support the NDIS QoS interface.|
|NDIS_STATUS_INVALID_LENGTH|The length of the information buffer is less than sizeof([**NDIS_QOS_SQ_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_sq_parameters)). NDIS sets the **DATA.QUERY_INFORMATION.BytesNeeded** member in the [**NDIS_OID_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure to the minimum buffer size that is required.|
|NDIS_STATUS_BUFFER_TOO_SHORT|The length of the information buffer is not sufficient for the returned data.|
|NDIS_STATUS_FAILURE|The request failed for other reasons.|

 

## Requirements

|Requirement|Value|
|--- |--- |
|Version|Supported in NDIS 6.84 and later.|
|Header|Ntddndis.h (include Ndis.h)|

## See also

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

[**NDIS_QOS_SQ_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_sq_parameters)

[**NDIS_QOS_OFFLOAD_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_qos_offload_capabilities)

[OID_QOS_HARDWARE_CAPABILITIES](oid-qos-hardware-capabilities.md)

[OID_QOS_OFFLOAD_UPDATE_SQ](oid-qos-offload-update-sq.md)

 
