---
title: WDI_TLV_PMKID
description: WDI_TLV_PMKID is a TLV that contains a PMKID value.
ms.assetid: 6873928B-7843-434F-AB80-6A7895D751A4
ms.date: 07/18/2017
keywords:
 - WDI_TLV_PMKID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_PMKID


WDI\_TLV\_PMKID is a TLV that contains a PMKID value.

## TLV Type


0x9F

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description            |
|-----------|------------------------|
| UINT8\[\] | A 16-byte PMKID value. |

 

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

 

 




