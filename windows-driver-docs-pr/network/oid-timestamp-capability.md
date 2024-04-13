---
title: OID_TIMESTAMP_CAPABILITY
ms.topic: reference
description: An overlying driver issues an OID query request of OID_TIMESTAMP_CAPABILITY to obtain the timestamping capabilities of the NIC and the miniport driver.
ms.date: 01/31/2021
keywords: 
 -OID_TIMESTAMP_CAPABILITY Network Drivers Starting with Windows Vista
---

# OID_TIMESTAMP_CAPABILITY

An overlying driver issues an object identifier (OID) query request of OID_TIMESTAMP_CAPABILITY to obtain the hardware timestamping capabilities of the NIC and software timestamping capabilities of the miniport driver.

The **RequestType** member of the [**NDIS_OID_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure will be **NdisRequestQueryInformation**.

NDIS handles this OID for the miniport driver based on the information the miniport driver provided in the [**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md) status indication.

## Requirements

|Requirement|Value|
|-|-|
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|NDIS Version| NDIS 6.82 and later|
|Header|Ntddndis.h (include Ndis.h)|

## See also

[**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md)

[OID_TIMESTAMP_CURRENT_CONFIG](oid-timestamp-current-config.md)

[OID_TIMESTAMP_GET_CROSSTIMESTAMP](oid-timestamp-get-crosstimestamp.md)

[**NDIS_OID_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)
