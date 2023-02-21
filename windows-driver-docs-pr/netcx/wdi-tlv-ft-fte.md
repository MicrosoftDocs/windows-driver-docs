---
title: WDI_TLV_FT_FTE (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_FT_FTE is a WiFiCx TLV that contains a Fast Transition Element.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_FT_FTE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_FT\_FTE (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_FT\_FTE is a TLV that contains a Fast Transition Element.

## TLV Type


0x10B

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                    |
|-----------|----------------------------------------------------------------|
| UINT8\[\] | A Fast Transition Element that contains the R0KHID and SNonce. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

 




