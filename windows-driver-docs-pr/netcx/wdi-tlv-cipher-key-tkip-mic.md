---
title: WDI_TLV_CIPHER_KEY_TKIP_MIC (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_CIPHER_KEY_TKIP_MIC is a WiFiCx TLV that contains the TKIP MIC material.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_CIPHER_KEY_TKIP_MIC Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CIPHER\_KEY\_TKIP\_MIC (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_CIPHER\_KEY\_TKIP\_MIC is a TLV that contains the TKIP MIC material.

## TLV Type


0x4A

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                      |
|-----------|------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the TKIP MIC material. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




