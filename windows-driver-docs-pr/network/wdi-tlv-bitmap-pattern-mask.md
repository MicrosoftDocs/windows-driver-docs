---
title: WDI_TLV_BITMAP_PATTERN_MASK
description: WDI_TLV_BITMAP_PATTERN_MASK is a TLV that contains the bitmap pattern mask.
ms.assetid: 251B3496-04CE-419B-BE5E-C46265F50B7A
ms.date: 07/18/2017
keywords:
 - WDI_TLV_BITMAP_PATTERN_MASK Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_BITMAP\_PATTERN\_MASK


WDI\_TLV\_BITMAP\_PATTERN\_MASK is a TLV that contains the bitmap pattern mask.

## TLV Type


0xE4

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                                                              |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that contains the byte array of the pattern mask. The mask must have 1 bit per pattern byte, therefore the mask length should equal (pattern length + 7) / 8. |

 

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

 

 




