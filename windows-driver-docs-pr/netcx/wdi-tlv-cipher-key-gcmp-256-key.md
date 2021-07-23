---
title: WDI_TLV_CIPHER_KEY_GCMP_256_KEY (dot11wificxtypes.h)
description: WDI_TLV_CIPHER_KEY_GCMP_256_KEY is a WiFiCx TLV that contains GCMP 256 cipher algorithm key data for OID_WDI_SET_ADD_CIPHER_KEYS.
ms.assetid: 
ms.date: 07/31/2021
keywords:
 - WDI_TLV_CIPHER_KEY_GCMP_256_KEY Network Drivers Starting with Windows 10, Version 2004
ms.localizationpriority: medium
---

# WDI\_TLV\_CIPHER\_KEY\_GCMP\_256\_KEY (dot11wificxtypes.h)

WDI\_TLV\_CIPHER\_KEY\_GCMP\_256\_KEY is a TLV that contains GCMP 256 cipher algorithm key data for [OID\_WDI\_SET\_ADD\_CIPHER\_KEYS](./oid-wdi-set-add-cipher-keys.md).

## TLV Type

0x164

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8\[\] | Specifies GCMP 256 cipher algorithm key data. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|
