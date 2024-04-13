---
title: WDI_TLV_CIPHER_KEY_TKIP_KEY (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_CIPHER_KEY_TKIP_KEY is a WiFiCx TLV that contains TKIP key material.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_CIPHER_KEY_TKIP_KEY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CIPHER\_KEY\_TKIP\_KEY (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_CIPHER\_KEY\_TKIP\_KEY is a TLV that contains TKIP key material.

## TLV Type


0x49

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                      |
|-----------|------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the TKIP key material. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




