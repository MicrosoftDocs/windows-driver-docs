---
title: WDI_TLV_CHANNEL_WIDTH_LIST (dot11wificxtypes.hpp)
description: WDI_TLV_CHANNEL_WIDTH_LIST is a WiFiCx TLV that contains a list of channel widths.
ms.date: 09/30/2021
keywords:
 - WDI_TLV_CHANNEL_WIDTH_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CHANNEL\_WIDTH\_LIST (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_CHANNEL\_WIDTH\_LIST is a TLV that contains a list of channel widths.

## TLV Type


0xF5

## Length


The size (in bytes) of the array of UINT32 elements. The array must contain 1 or more elements.

## Values


| Type       | Description                                 |
|------------|---------------------------------------------|
| UINT32\[\] | A list of channel widths, specified in MHz. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




