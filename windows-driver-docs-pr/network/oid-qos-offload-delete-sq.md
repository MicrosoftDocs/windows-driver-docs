---
title: OID_QOS_OFFLOAD_DELETE_SQ
description: A driver issues OID_QOS_OFFLOAD_DELETE_SQ to delete a Scheduler Queue (SQ) on the miniport adapter.
ms.assetid:
ms.date: 10/30/2020
keywords: 
 -OID_QOS_OFFLOAD_DELETE_SQ Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_QOS_OFFLOAD_DELETE_SQ

Overlying drivers issue OID method requests of OID_QOS_OFFLOAD_DELETE_SQ to delete a Scheduler Queue (SQ) on the miniport adapter. The caller should set the **InformationBuffer** member of the [**NDIS_OID_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure to contain a pointer to an NDIS_QOS_SQ_ID type.

## Remarks

The caller must ensure there are no resources actively referencing this SQ before deleting it.

### Return Status Codes

NDIS handles the OID query request of OID_QOS_OFFLOAD_DELETE_SQ request for miniport drivers, and returns one of the following status codes.

|Status Code|Description|
|--- |--- |
|NDIS_STATUS_SUCCESS|The OID request completed successfully.|
|NDIS_STATUS_NOT_SUPPORTED|The miniport driver does not support the NDIS QoS interface.|
|NDIS_STATUS_FAILURE|The request failed for other reasons.|

 
## Requirements

|||
|--- |--- |
|Version|Supported in NDIS 6.84 and later.|
|Header|Ntddndis.h (include Ndis.h)|

## See also

[**NDIS\_OID\_REQUEST**](windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

[OID_QOS_OFFLOAD_CREATE_SQ](oid-qos-offload-create-sq.md)

[OID_QOS_OFFLOAD_UPDATE_SQ](oid-qos-offload-update-sq.md)

