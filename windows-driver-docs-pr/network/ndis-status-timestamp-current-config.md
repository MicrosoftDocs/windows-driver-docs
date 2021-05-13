---
title: NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG
description: Miniport drivers use the NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG status indication to report the current timestamping configuration of the NIC hardware.
ms.date: 01/31/2021
keywords:
 - NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG

Miniport drivers use the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication to report the current timestamping configuration of the NIC hardware and miniport driver to NDIS and overlying drivers. 

This status indication represents which timestamping capabilities are currently enabled or disabled. For information about the status indication driver use to report the timestamping capabilities, see [**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md). 

## Remarks

During initialization, the miniport driver should indicate the current timestamping configuration from within its [**MiniportInitializeEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. The driver should:

1. Initialize an [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure with the current timestamping configuration.
The  driver sets the members of the **NDIS_TIMESTAMP_CAPABILITIES** structure  as follows:
   * The driver uses the **TimestampFlags** field to indicate its current timestamping configuration. Each flag in the [**NDIS_TIMESTAMP_CAPABILITY_FLAGS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capability_flags) structure should be set to **TRUE** if the corresponding timestamping capability is currently enabled or **FALSE** if it is not.

    > [!NOTE]
    > To determine which timestamping capabilities are currently enabled or disabled, the miniport reads the current values of the timestamping related keywords **\*PtpHardwareTimestamp** and **\*SoftwareTimestamp**. For more on using these keywords and determining which timestamping capabilities to enable, see [Standardized INF keywords for NDIS packet timestamping](standardized-inf-keywords-for-ndis-packet-timestamping.md).

    > [!NOTE] 
    > If an implementation finds both hardware and software timestamps enabled through the keywords, then the miniport should only enable hardware timestamps and should disable software timestamps.

    * The driver should set the **CrossTimestamp** field to **TRUE** if hardware cross timestamps are enabled in the current configuration or **FALSE** if they are not.

    * The **HardwareClockFrequencyHz** field must contain the current operating frequency of the NIC’s hardware clock.

    * The **Type** field in the **Header** field should be set to **NDIS_OBJECT_TYPE_DEFAULT** and the **Revision** to **NDIS_TIMESTAMP_CAPABILITIES_REVISION_1**.

1. Generate an [**NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG**](ndis-status-timestamp-capability.md) status indication by calling [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) to report the current configuration. The **StatusBuffer** field of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure should point to the initialized **NDIS_TIMESTAMP_CAPABILITIES** structure.

The miniport driver must generate an [**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md) indication at least once before indicating **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG**. Otherwise NDIS will reject the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication and it will not be indicated to overlying drivers.

If the miniport driver indicates a change in the NIC’s hardware timestamping *capability* using the [**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md) status indication (for example, a change in the **HardwareClockFrequencyHz** field in the **NDIS_TIMESTAMP_CAPABILITIES** structure because of an underlying change in the NIC hardware), then it must also report the corresponding change in the current configuration using the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication.

The miniport driver must also generate the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication whenever it detects a change in current timestamping configuration.

## Requirements

|Requirement|Value|
|-|-|
|Minimum supported server|Windows Server 2022|
|NDIS Version| NDIS 6.82 and later|
|Header|Ntddndis.h (include Ndis.h)|

## See also

[Reporting timestamping capabilities and current configuration](reporting-timestamping-capabilities.md)

[Standardized INF keywords for NDIS packet timestamping](standardized-inf-keywords-for-ndis-packet-timestamping.md)

[**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md)

[**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities)

[**NDIS_TIMESTAMP_CAPABILITY_FLAGS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capability_flags)

[**MiniportInitializeEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize)

[**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex)

[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)