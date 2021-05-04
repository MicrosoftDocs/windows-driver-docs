---
title: OID_TIMESTAMP_GET_CROSSTIMESTAMP
description: An overlying driver issues an OID query request of OID_TIMESTAMP_GET_CROSSTIMESTAMP to obtain the cross timestamp from the NIC hardware.
ms.date: 01/31/2021
keywords: 
 -OID_TIMESTAMP_GET_CROSSTIMESTAMP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_TIMESTAMP_GET_CROSSTIMESTAMP

An overlying driver issues an object identifier (OID) query request of OID_TIMESTAMP_GET_CROSSTIMESTAMP to obtain a cross timestamp from the NIC hardware. A cross timestamp is the set of a NIC hardware timestamp and system timestamp(s) obtained very close to each other. Precision Time Protocol (PTP) version 2 applications use the information provided in this OID to establish a relation between the NIC’s hardware clock and a system clock.

The miniport driver must support this OID if it sets the **CrossTimestamp** field to **TRUE** in the [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure as part of the current configuration. For more details on reporting the current configuration, see the [**NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG**](ndis-status-timestamp-current-config.md) status indication. If the cross timestamping ability is disabled, then the OID should be completed with an appropriate error code (for example, NDIS_STATUS_NOT_SUPPORTED).

The **RequestType** member of the [**NDIS_OID_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure will be **NdisRequestQueryInformation**.

When a miniport driver receives the OID request of OID_TIMESTAMP_GET_CROSSTIMESTAMP, the driver completes the OID by filling the **InformationBuffer** in the **QUERY_INFORMATION** with an [**NDIS_HARDWARE_CROSSTIMESTAMP**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_hardware_crosstimestamp) structure. The **Type** field in the **Header** field of the **NDIS_HARDWARE_CROSSTIMESTAMP** structure should be set to **NDIS_OBJECT_TYPE_DEFAULT** and the **Revision** field to **NDIS_HARDWARE_CROSSTIMESTAMP_REVISION_1**. The driver should fill the **SystemTimestamp1**, **HardwareClockTimestamp** and **SystemTimestamp2** fields with following timestamps taken as close to each other as possible and in the following order:

1. **SystemTimestamp1**: Performance counter value (QPC) obtained by calling [**KeQueryPerformanceCounter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-kequeryperformancecounter).

2. **HardwareClockTimestamp**: The NIC hardware clock’s current value. This should be the raw hardware clock value of the NIC.

3. **SystemTimestamp2**: Another performance counter value (QPC) obtained by calling **KeQueryPerformanceCounter**.

Here's an example of how a miniport driver handles OID_TIMESTAMP_GET_CROSSTIMESTAMP:

```C++
{
. . .
    NDIS_HARDWARE_CROSSTIMESTAMP crossTimestamp;
    LARGE_INTEGER timeStamp;

    RtlZeroMemory(&crossTimestamp, sizeof(crossTimestamp));

    timeStamp = KeQueryPerformanceCounter(NULL);
    crossTimestamp.SystemTimestamp1 = timeStamp.QuadPart;
    crossTimestamp.HardwareClockTimestamp = FunctionToRetrieveHardwareTimestampFromNetworkCard();
    timeStamp = KeQueryPerformanceCounter(NULL);
    crossTimestamp.SystemTimestamp2 = timeStamp.QuadPart;
    crossTimestamp.Header.Type = NDIS_OBJECT_TYPE_DEFAULT;
    crossTimestamp.Header.Size = NDIS_SIZEOF_HARDWARE_CROSSTIMESTAMP_REVISION_1;
    crossTimestamp.Header.Revision = NDIS_HARDWARE_CROSSTIMESTAMP_REVISION_1;

// Complete the OID by filling the query information buffer with the crossTimestamp
}
```
The **Flags** field in the **NDIS_HARDWARE_CROSSTIMESTAMP** structure is reserved for future use. The miniport driver must not change its value.

The miniport driver and hardware are free to optimize the collection of these timestamps depending on any advanced hardware capabilities. However, the **SystemTimestamp1** and **SystemTimestamp2** values returned on OID completion must accurately correspond to the performance counter (QPC) value at the time of capture. The **HardwareClockTimestamp** must correspond to the NIC’s hardware clock value at the point of capture. If a particular implementation can more accurately determine two timestamps rather than three (for example, one system timestamp and the corresponding NIC hardware clock timestamp), then it should set the **SystemTimestamp2** field to the same value as **SystemTimestamp1**.

The miniport driver should not set the **SystemTimestamp1**, **HardwareClockTimestamp**, or **SystemTimestamp2** values to **zero**.

### Return Status Codes

The miniport driver returns one of the following status codes for the OID query request of OID_TIMESTAMP_GET_CROSSTIMESTAMP.

|Status Code|Description|
|--- |--- |
|NDIS_STATUS_SUCCESS|The OID request completed successfully.|
|NDIS_STATUS_NOT_SUPPORTED|The miniport driver either does not support cross timestamping or the cross timestamping ability is disabled.|
|NDIS_STATUS_FAILURE|The request failed for other reasons.|


## Requirements

|Requirement|Value|
|-|-|
|Minimum supported server|Windows Server 2022|
|NDIS Version| NDIS 6.82 and later|
|Header|Ntddndis.h (include Ndis.h)|

## See also

[**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md)

[OID_TIMESTAMP_CURRENT_CONFIG](oid-timestamp-current-config.md)

[OID_TIMESTAMP_CAPABILITY](oid-timestamp-capability.md)

[**NDIS_OID_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)