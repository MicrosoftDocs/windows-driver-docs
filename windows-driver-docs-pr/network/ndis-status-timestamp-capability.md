---
title: NDIS_STATUS_TIMESTAMP_CAPABILITY
description: Miniport drivers use the NDIS_STATUS_TIMESTAMP_CAPABILITY status indication to report the NIC and miniport driver timestamping capabilities.
ms.date: 01/31/2021
keywords:
 - NDIS_STATUS_TIMESTAMP_CAPABILITY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_TIMESTAMP_CAPABILITY

Miniport drivers use the **NDIS_STATUS_TIMESTAMP_CAPABILITY** status indication to report the NIC's hardware timestamping capabilities and the miniport driver's software timestamping capabilities to NDIS and overlying drivers.

This status indication represents the timestamping capabilities of the hardware and miniport driver, not which capability is currently enabled or disabled. For more information on reporting the current timestamping configuration, see [**NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG**](ndis-status-timestamp-current-config.md).

## Remarks

During initialization, the miniport driver should indicate its hardware and software timestamp capabilities from within its [**MiniportInitializeEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. The driver should:

1. Initialize an [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure with the NIC's hardware and software timestamp capabilities.
The  driver sets the members of the **NDIS_TIMESTAMP_CAPABILITIES** structure  as follows:
    * The  driver uses the **TimestampFlags** field to indicate the hardware and software timestamp capabilities.

    > [!NOTE]
    > An implementation must support hardware timestamps and cross timestamps. Supporting software timestamps is optional.

    * The driver must set the **CrossTimestamp** field to **TRUE**.

    * The **HardwareClockFrequencyHz** field should contain the nominal operating frequency of the hardware clock used for timestamping by the NIC. This data may be used to display the nominal clock frequency to end users for informational purposes.

    * The **Type** field in the **Header** field should be set to **NDIS_OBJECT_TYPE_DEFAULT** and the **Revision** to **NDIS_TIMESTAMP_CAPABILITIES_REVISION_1**.

1. Generate an **NDIS_STATUS_TIMESTAMP_CAPABILITY** status indication by calling [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) to report the timestamping capabilities. The **StatusBuffer** field of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure should point to the initialized **NDIS_TIMESTAMP_CAPABILITIES** structure.

The miniport driver must also generate the [**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md) status indication whenever it detects a change in underlying hardware capabilities.

Here's how a miniport driver might indicate its supported timestamping capabilities:

```C++
// From within its initialization routine, the miniport in this 
// example indicates that it supports the following capabilities:
// - PtpV2OverUdpIPv4EventMsgReceiveHw
// - PtpV2OverUdpIPv6EventMsgReceiveHw
// - TaggedTransmitHw
// - CrossTimestamp

NDIS_STATUS MiniportInitializeEx(
    _In_ NDIS_HANDLE MiniportAdapterHandle,
    _In_ NDIS_HANDLE MiniportDriverContext,
    _In_ PNDIS_MINIPORT_INIT_PARAMETERS MiniportInitParameters
)
{
. . .
    NDIS_TIMESTAMP_CAPABILITIES timeStampCapabilities;
    NDIS_STATUS_INDICATION timeStampStatus;
. . .

    // Initialize an NDIS_TIMESTAMP_CAPABILITIES structure

    RtlZeroMemory(&timeStampCapabilities, sizeof(timeStampCapabilities));
    RtlZeroMemory(&timeStampStatus, sizeof(timeStampStatus));

    timeStampCapabilities.Header.Type = NDIS_OBJECT_TYPE_DEFAULT;
    timeStampCapabilities.Header.Size = sizeof(timeStampCapabilities);
    timeStampCapabilities.Header.Revision = NDIS_TIMESTAMP_CAPABILITIES_REVISION_1;

    timeStampCapabilities.CrossTimestamp = TRUE;
    timeStampCapabilities.TimestampFlags.PtpV2OverUdpIPv4EventMsgReceiveHw = TRUE;
    timeStampCapabilities.TimestampFlags.PtpV2OverUdpIPv6EventMsgReceiveHw = TRUE;
    timeStampCapabilities.TimestampFlags.TaggedTransmitHw = TRUE;

    timeStampCapabilities.HardwareClockFrequencyHz = 150000;

    timeStampStatus.Header.Type = NDIS_OBJECT_TYPE_STATUS_INDICATION;
    timeStampStatus.Header.Revision = NDIS_STATUS_INDICATION_REVISION_1;
    timeStampStatus.Header.Size = NDIS_SIZEOF_STATUS_INDICATION_REVISION_1;

    timeStampStatus.SourceHandle = MiniportAdapterHandle;
    timeStampStatus.StatusBuffer = &timeStampCapabilities;
    timeStampStatus.StatusBufferSize = sizeof(timeStampCapabilities);
    timeStampStatus.StatusCode = NDIS_STATUS_TIMESTAMP_CAPABILITY;

    // Generate an NDIS_STATUS_TIMESTAMP_CAPABILITY status indication
    NdisMIndicateStatusEx(MiniportAdapterHandle, &timeStampStatus);
. . .
}
```

## Requirements

|Requirement|Value|
|-|-|
|Minimum supported server|Windows Server 2022|
|NDIS Version| NDIS 6.82 and later|
|Header|Ntddndis.h (include Ndis.h)|

## See also

[Reporting timestamping capabilities and current configuration](reporting-timestamping-capabilities.md)

[**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities)

[**NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG**](ndis-status-timestamp-current-config.md)

[**MiniportInitializeEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize)

[**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex)

[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)