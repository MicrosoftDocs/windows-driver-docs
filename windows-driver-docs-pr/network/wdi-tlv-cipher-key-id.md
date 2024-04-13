---
title: WDI_TLV_CIPHER_KEY_ID
ms.topic: reference
description: WDI_TLV_CIPHER_KEY_ID is a TLV that contains a cipher key ID for OID_WDI_SET_ADD_CIPHER_KEYS and OID_WDI_SET_DELETE_CIPHER_KEYS.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_CIPHER_KEY_ID Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CIPHER\_KEY\_ID

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


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

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

