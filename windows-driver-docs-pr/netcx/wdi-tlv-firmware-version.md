---
title: WDI_TLV_FIRMWARE_VERSION (dot11wificxtypes.hpp)
description: WDI_TLV_FIRMWARE_VERSION is a WiFiCx TLV that contains the firmware version.
ms.date: 09/30/2021
keywords:
 - WDI_TLV_FIRMWARE_VERSION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_FIRMWARE\_VERSION (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_FIRMWARE\_VERSION is a TLV that contains the firmware version.

## TLV Type


0xF4

## Length


The size (in bytes) of the array of char elements. The array must contain 1 or more elements.

## Values


| Type     | Description                                                     |
|----------|-----------------------------------------------------------------|
| char\[\] | The firmware version, stored as a null-terminated ASCII string. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

 




