---
title: WDI_TLV_CIPHER_KEY_BIP_KEY
description: WDI_TLV_CIPHER_KEY_BIP_KEY is a TLV that contains BIP cipher algorithm key data for OID_WDI_SET_ADD_CIPHER_KEYS.
ms.assetid: 99630BDF-9845-4E3D-AB18-5F5BAFCF7198
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CIPHER_KEY_BIP_KEY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CIPHER\_KEY\_BIP\_KEY


WDI\_TLV\_CIPHER\_KEY\_BIP\_KEY is a TLV that contains BIP cipher algorithm key data for [OID\_WDI\_SET\_ADD\_CIPHER\_KEYS](https://msdn.microsoft.com/library/windows/hardware/dn925855).

## TLV Type


0x51

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                              |
|-----------|------------------------------------------|
| UINT8\[\] | Specifies BIP cipher algorithm key data. |

 

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

 

 




