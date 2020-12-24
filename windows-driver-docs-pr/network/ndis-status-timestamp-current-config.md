---
title: NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG
description: Miniport drivers use the NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG status indication to report the current timestamping configuration of the NIC hardware.
ms.date: 12/31/2020
keywords:
 - NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG

Miniport drivers use the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication to report the current timestamping configuration of the NIC hardware to NDIS and overlying drivers.

## Remarks

During initialization, the miniport driver should indicate its current timestamping configuration from within its [**MiniportInitializeEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

Miniport drivers generate **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indications by calling the [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) function. The **StatusBuffer** field of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure should point to an [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure.


Miniport drivers use the **TimestampFlags** field of the **NDIS_TIMESTAMP_CAPABILITIES** structure to indicate its current timestamping configuration.

The **CrossTimestamp** field of the **NDIS_TIMESTAMP_CAPABILITIES** structure should be set to **TRUE** if hardware cross timestamps are enabled in the current configuration, or **FALSE** if they are not.

To determine which timestamping capabilities are currently enabled or disabled, the miniport reads the current value of the timestamping related keywords during initialization. The timestamping related keywords are *PtpHardwareTimestamp and *SoftwareTimestamp and are described further below in the section called “Miniport driver inf changes”. That section also describes how the keywords should be used to enable the supported timestamping capabilities of the miniport and NIC hardware.

The **HardwareClockFrequencyHz** field of the **NDIS_TIMESTAMP_CAPABILITIES** structure must contain the current operating frequency of the NIC’s hardware clock.

The **Type** field in the **Header** field of the **NDIS_TIMESTAMP_CAPABILITIES** structure should be set to **NDIS_OBJECT_TYPE_DEFAULT** and the **Revision** to **NDIS_TIMESTAMP_CAPABILITIES_REVISION_1**.

The miniport driver must generate an [**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md) indication at least once before indicating **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG**. Otherwise NDIS will reject the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication and it will not be indicated to overlying drivers.

If the miniport driver indicates a change in the NIC’s hardware timestamping *capability* using the [**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md) status indication (for example, a change in the **HardwareClockFrequencyHz** field in the **NDIS_TIMESTAMP_CAPABILITIES** structure because of an underlying change in the NIC hardware), then it must also report the corresponding change in the current configuration using the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication.

The miniport driver must also generate the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication whenever it detects a change in current timestamping configuration.

## Requirements

**Version**: NDIS 6.82 and later

**Header**: Ntddndis.h (include Ndis.h)

## See also

[**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md)