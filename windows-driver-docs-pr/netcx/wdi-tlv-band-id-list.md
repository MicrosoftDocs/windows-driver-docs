---
title: WDI_TLV_BAND_ID_LIST (dot11wificxtypes.hpp)
description: WDI_TLV_BAND_ID_LIST is a WiFiCx TLV that contains a list of band IDs.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_BAND_ID_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BAND\_ID\_LIST (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_BAND\_ID\_LIST is a TLV that contains a list of band IDs.

## TLV Type


0xB6

## Length


The size (in bytes) of the array of WDI\_BAND\_ID (UINT32) elements. The array must contain 1 or more elements.

## Values


| Type              | Description           |
|-------------------|-----------------------|
| WDI\_BAND\_ID\[\] | An array of band IDs. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




