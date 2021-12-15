---
title: WDI_TLV_BEACON_IES (dot11wificxtypes.hpp)
description: WDI_TLV_BEACON_IES is a WiFiCx TLV that contains beacon IEs from an association.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_BEACON_IES Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BEACON\_IES (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_BEACON\_IES is a TLV that contains beacon IEs from an association.

## TLV Type


0x78

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                         |
|-----------|-------------------------------------|
| UINT8\[\] | The beacon IEs from an association. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




