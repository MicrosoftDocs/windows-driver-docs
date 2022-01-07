---
title: WDI_TLV_PMKID (dot11wificxtypes.hpp)
description: WDI_TLV_PMKID is a WiFiCx TLV that contains a PMKID value.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_PMKID Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PMKID (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_PMKID is a TLV that contains a PMKID value.

## TLV Type


0x9F

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description            |
|-----------|------------------------|
| UINT8\[\] | A 16-byte PMKID value. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




