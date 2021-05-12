---
title: WDI_TLV_CIPHER_KEY_BIP_GMAC_256_KEY
description: WDI_TLV_CIPHER_KEY_BIP_GMAC_256_KEY is a TLV that contains GMAC 256 cipher algorithm key data for OID_WDI_SET_ADD_CIPHER_KEYS.
ms.date: 05/07/2021
keywords:
 - WDI_TLV_CIPHER_KEY_BIP_GMAC_256_KEY Network Drivers Starting with Windows 10, Version 2004
ms.localizationpriority: medium
---

# WDI\_TLV\_CIPHER\_KEY\_BIP\_GMAC\_256\_KEY

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

| &nbsp; | &nbsp; |
| ------ | ------ |
| **Minimum supported client** | Windows 10, version 2004 |
| **Minimum supported server** | Windows Server 2016 |
| **Header** | Wditypes.hpp |
