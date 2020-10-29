---
title: OID_QOS_OFFLOAD_ENUM_SQS
description: A driver issues OID_QOS_OFFLOAD_ENUM_SQS to obtain a list of all Scheduler Queues (SQs) currently on a miniport adapter.
ms.assetid:
ms.date: 10/30/2020
keywords: 
 -OID_QOS_OFFLOAD_ENUM_SQS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_QOS_OFFLOAD_ENUM_SQS

Overlying drivers issue OID query requests of OID_QOS_OFFLOAD_ENUM_SQS to obtain a list of all Scheduler Queues (SQs), with their parameters, that are currently present on a miniport adapter.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS_OID_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to an [**NDIS_QOS_SQ_PARAMETERS_ENUM_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_sq_parameters_enum_array) structure. Each element of the array is an [**NDIS_QOS_SQ_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_sq_parameters) structure.

## Remarks

### Return Status Codes

NDIS handles the OID query request of OID_QOS_OFFLOAD_ENUM_SQS request for miniport drivers and returns one of the following status codes.

|Status Code|Description|
|--- |--- |
|NDIS_STATUS_SUCCESS|The OID request completed successfully.|
|NDIS_STATUS_NOT_SUPPORTED|The miniport driver does not support the NDIS QoS interface.|
|NDIS_STATUS_INVALID_LENGTH|The length of the information buffer is less than sizeof([**NDIS_QOS_SQ_PARAMETERS_ENUM_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_sq_parameters_enum_array)). NDIS sets the **DATA.QUERY_INFORMATION.BytesNeeded** member in the [**NDIS_OID_REQUEST**](windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure to the minimum buffer size that is required.|
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

[**NDIS_QOS_SQ_PARAMETERS_ENUM_ARRAY**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-ndis_qos_sq_parameters_enum_array)

 
