---
title: WDI_TLV_CIPHER_KEY_ID (dot11wificxtypes.h)
description: WDI_TLV_CIPHER_KEY_ID is a WiFiCx TLV that contains a cipher key ID for OID_WDI_SET_ADD_CIPHER_KEYS and OID_WDI_SET_DELETE_CIPHER_KEYS.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_CIPHER_KEY_ID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CIPHER\_KEY\_ID (dot11wificxtypes.h)


WDI\_TLV\_CIPHER\_KEY\_ID is a TLV that contains a cipher key ID for [OID\_WDI\_SET\_ADD\_CIPHER\_KEYS](./oid-wdi-set-add-cipher-keys.md) and [OID\_WDI\_SET\_DELETE\_CIPHER\_KEYS](./oid-wdi-set-delete-cipher-keys.md).

## TLV Type


0x4D

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                  |
|--------|------------------------------|
| UINT32 | Specifies the cipher key ID. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

