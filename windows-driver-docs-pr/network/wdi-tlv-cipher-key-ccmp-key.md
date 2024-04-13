---
title: WDI_TLV_CIPHER_KEY_CCMP_KEY
ms.topic: reference
description: WDI_TLV_CIPHER_KEY_CCMP_KEY is a TLV that contains CCMP cipher algorithm key data for OID_WDI_SET_ADD_CIPHER_KEY.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_CIPHER_KEY_CCMP_KEY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CIPHER\_KEY\_CCMP\_KEY

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


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

 

