---
title: WDI_TLV_BITMAP_PATTERN
description: WDI_TLV_BITMAP_PATTERN is a TLV that contains the byte array of a pattern.
ms.assetid: 44A18754-3D04-4B62-B8C2-861A47129F08
ms.date: 07/18/2017
keywords:
 - WDI_TLV_BITMAP_PATTERN Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_BITMAP\_PATTERN


WDI\_TLV\_BITMAP\_PATTERN is a TLV that contains the byte array of a pattern.

## TLV Type


0x68

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                              |
|-----------|----------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that contains the byte array of the pattern. Length = (Pattern length + 7)/8. |

 

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

 

 




