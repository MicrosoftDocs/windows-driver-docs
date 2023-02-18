---
title: WDI_TLV_SSID (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_SSID is a WiFiCx TLV that contains an SSID.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SSID, WiFiCx
---

# WDI_TLV_SSID (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI_TLV_SSID is a TLV that contains an SSID.

## TLV Type

0x3B

## Length


The size (in bytes) of the array of UINT8 elements. An array length of 0 is allowed.

## Values


| Type      | Description                                        |
|-----------|----------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies an SSID. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




