---
title: WDI_TLV_INDICATION_STOP_AP (dot11wificxtypes.h)
description: WDI_TLV_INDICATION_STOP_AP is a WiFiCx TLV that contains the reason for a Stop AP indication.
ms.date: 08/31/2021
keywords:
 - WDI_TLV_INDICATION_STOP_AP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_INDICATION\_STOP\_AP (dot11wificxtypes.h)


WDI\_TLV\_INDICATION\_STOP\_AP is a TLV that contains the reason for a Stop AP indication.

## TLV Type


0xE6

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------|
| UINT32 | The Stop AP reason. See [**WDI\_STOP\_AP\_REASON**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_stop_ap_reason) for possible reason values. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

## See also


[NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP](./ndis-status-wdi-indication-stop-ap.md)

 

