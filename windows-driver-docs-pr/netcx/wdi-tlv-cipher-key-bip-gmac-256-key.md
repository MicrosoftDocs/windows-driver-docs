---
title: WDI_TLV_CIPHER_KEY_BIP_GMAC_256_KEY (dot11wificxtypes.hpp)
description: WDI_TLV_CIPHER_KEY_BIP_GMAC_256_KEY is a WiFiCx TLV that contains GMAC 256 cipher algorithm key data for OID_WDI_SET_ADD_CIPHER_KEYS.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_CIPHER_KEY_BIP_GMAC_256_KEY Network Drivers Starting with Windows 10, Version 2004
ms.localizationpriority: medium
---

# WDI\_TLV\_CIPHER\_KEY\_BIP\_GMAC\_256\_KEY (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI\_TLV\_CIPHER\_KEY\_BIP\_GMAC\_256\_KEY is a TLV that contains BIP GMAC 256 cipher algorithm key data for [OID\_WDI\_SET\_ADD\_CIPHER\_KEYS](./oid-wdi-set-add-cipher-keys.md).

## TLV Type

0x165

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | ---|
| UINT8\[\] | Specifies BIP GMAC 256 cipher algorithm key data. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
