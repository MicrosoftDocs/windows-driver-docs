---
title: WDI_TLV_CIPHER_KEY_BIP_GMAC_256_KEY
description: WDI_TLV_CIPHER_KEY_BIP_GMAC_256_KEY is a TLV that contains GMAC 256 cipher algorithm key data for OID_WDI_SET_ADD_CIPHER_KEYS.
ms.assetid: 
ms.date: 09/10/2020
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

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10, Version 2004</p></td>
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