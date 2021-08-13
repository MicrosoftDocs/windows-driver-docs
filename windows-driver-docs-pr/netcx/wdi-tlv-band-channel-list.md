---
title: WDI_TLV_BAND_CHANNEL_LIST (dot11wificxtypes.h)
description: WDI_TLV_BAND_CHANNEL_LIST is a WiFiCx TLV that contains one or more channel numbers.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_BAND_CHANNEL_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_BAND_CHANNEL_LIST (dot11wificxtypes.h)


WDI_TLV_BAND_CHANNEL_LIST is a TLV that contains one or more channel numbers.

## TLV Type


0x16E

## Length


The size (in bytes) of the array of [**WDI\_CHANNEL\_MAPPING\_ENTRY**](/windows-hardware/drivers/ddi/dot11wificxtypes/ns-dot11wificxtypes-wdi_channel_mapping_entry) structures. The array must contain 1 or more structures.

## Values


| Type                                                                       | Description                          |
|----------------------------------------------------------------------------|--------------------------------------|
| [**WDI\_CHANNEL\_MAPPING\_ENTRY**](/windows-hardware/drivers/ddi/dot11wificxtypes/ns-dot11wificxtypes-wdi_channel_mapping_entry)\[\] | An array of channel mapping entries. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

