---
title: WDI_TLV_CIPHER_KEY_ID
description: WDI_TLV_CIPHER_KEY_ID is a TLV that contains a cipher key ID for OID_WDI_SET_ADD_CIPHER_KEYS and OID_WDI_SET_DELETE_CIPHER_KEYS.
ms.assetid: 24076B2A-FAC2-4509-9F1C-7F2AF57883CF
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CIPHER_KEY_ID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CIPHER\_KEY\_ID


WDI\_TLV\_CIPHER\_KEY\_ID is a TLV that contains a cipher key ID for [OID\_WDI\_SET\_ADD\_CIPHER\_KEYS](https://msdn.microsoft.com/library/windows/hardware/dn925855) and [OID\_WDI\_SET\_DELETE\_CIPHER\_KEYS](https://msdn.microsoft.com/library/windows/hardware/dn925929).

## TLV Type


0x4D

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                  |
|--------|------------------------------|
| UINT32 | Specifies the cipher key ID. |

 

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

 

 




