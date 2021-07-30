---
title: WDI_TLV_ADAPTER_NLO_SCAN_MODE (dot11wificxtypes.h)
description: WDI_TLV_ADAPTER_NLO_SCAN_MODE is a WiFiCx TLV that indicates whether scans should be performed in active or passive mode.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_ADAPTER_NLO_SCAN_MODE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ADAPTER\_NLO\_SCAN\_MODE (dot11wificxtypes.h)


WDI\_TLV\_ADAPTER\_NLO\_SCAN\_MODE is a TLV that indicates whether scans should be performed in active or passive mode.

## TLV Type


0x125

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                     |
|--------|---------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | [**WDI\_SCAN\_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_scan_type) value that indicates whether scans should be performed in active or passive mode. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

