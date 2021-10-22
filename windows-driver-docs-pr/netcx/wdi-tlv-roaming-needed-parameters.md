---
title: WDI_TLV_ROAMING_NEEDED_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_ROAMING_NEEDED_PARAMETERS is a WiFiCx TLV that contains the reason for a roam trigger. This is used in the NDIS_STATUS_WDI_INDICATION_ROAMING_NEEDED payload.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_ROAMING_NEEDED_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ROAMING\_NEEDED\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_ROAMING\_NEEDED\_PARAMETERS is a TLV that contains the reason for a roam trigger. This is used in the [NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED](./ndis-status-wdi-indication-roaming-needed.md) payload.

## TLV Type


0x55

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                | Description                                                                                                                                      |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_ASSOC\_STATUS**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_assoc_status) | Specifies the reason for a roam trigger. When a [OID\_WDI\_TASK\_ROAM](./oid-wdi-task-roam.md) is triggered, this reason is forwarded to it. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

