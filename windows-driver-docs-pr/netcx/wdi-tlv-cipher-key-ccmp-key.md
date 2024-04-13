---
title: WDI_TLV_CIPHER_KEY_CCMP_KEY (dot11wificxtypes.hpp))
ms.topic: reference
description: WDI_TLV_CIPHER_KEY_CCMP_KEY is a WiFiCx TLV that contains CCMP cipher algorithm key data for OID_WDI_SET_ADD_CIPHER_KEY.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_CIPHER_KEY_CCMP_KEY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CIPHER\_KEY\_CCMP\_KEY (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_CIPHER\_KEY\_CCMP\_KEY is a TLV that contains CCMP cipher algorithm key data for [OID\_WDI\_SET\_ADD\_CIPHER\_KEY](./oid-wdi-set-add-cipher-keys.md).

## TLV Type


0x50

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                               |
|-----------|-------------------------------------------|
| UINT8\[\] | Specifies CCMP cipher algorithm key data. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

