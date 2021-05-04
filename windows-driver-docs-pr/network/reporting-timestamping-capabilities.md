---
title: Reporting timestamping capabilities and current configuration
description: Miniport drivers use status indications to report the timestamping capabilities and their current configuration to the operating system.
ms.date: 01/31/2021
ms.localizationpriority: medium
---

# Reporting timestamping capabilities and current configuration

Miniport drivers need to indicate the NIC's hardware timestamping capabilities and the miniport driver's software timestamping capabilities to NDIS and overlying drivers. They also need to report which timestamping capabilities are currently enabled or disabled. Miniport drivers use status indications to report the timestamping capabilities and their current configuration to the operating system.

During initialization, the miniport driver should report the timestamping capabilities and their current configuration within the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. The driver should:

1. Generate an [**NDIS_STATUS_TIMESTAMP_CAPABILITY**](ndis-status-timestamp-capability.md) status indication to report the timestamping capabilities.

1.  Generate an [**NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG**](ndis-status-timestamp-current-config.md) status indication to report the current timestamping configuration.

> [!NOTE]
> Miniport drivers read the **\*PtpHardwareTimestamp** and **\*SoftwareTimestamp**  keywords values in the INF file to determine which timestamping capabilities are enabled or disabled. For more information, see [**Standardized INF keywords for NDIS packet timestamping**](standardized-inf-keywords-for-ndis-packet-timestamping.md). 

Any time that the miniport driver detects a change in underlying hardware capabilities it must generate the **NDIS_STATUS_TIMESTAMP_CAPABILITY** status indication. It must also report the corresponding change in the current configuration using the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication.

The miniport driver must also generate the **NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG** status indication whenever it detects a change in the current timestamping configuration.
