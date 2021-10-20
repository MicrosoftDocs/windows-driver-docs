---
title: WDI_TLV_SCAN_DWELL_TIME (dot11wificxtypes.hpp)
description: WDI_TLV_SCAN_DWELL_TIME is a WiFiCx TLV that contains scanning dwell time settings.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_SCAN_DWELL_TIME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_SCAN\_DWELL\_TIME (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_SCAN\_DWELL\_TIME is a TLV that contains scanning dwell time settings.

## TLV Type


0x7

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                                                           |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | Specifies the maximum time in milliseconds to dwell on active channels. This is a hint and if the adapter decides to use its own dwell time, it must meet the Maximum Scan Time requirement. If overridden, the adapter must also meet the low latency connection quality parameters. |
| UINT32 | Specifies the maximum time in milliseconds to dwell on passive channels. This is a hint and if the adapter decides to use its own dwell time, it must meet the Maximum Scan Time requirement. If overridden, the adapter must also meet the low latency connection quality parameters.|
| UINT32 | Specifies the maximum time in milliseconds for total scan. If the adapter limits its dwell times to below the values specified above, it can ignore the Maximum Scan Time parameter.          |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 






