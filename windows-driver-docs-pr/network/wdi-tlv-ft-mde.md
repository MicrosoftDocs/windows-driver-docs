---
title: WDI_TLV_FT_MDE
ms.topic: reference
description: WDI_TLV_FT_MDE is a TLV that contains the MDIE of a BSS entry.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_FT_MDE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_FT\_MDE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_FT\_MDE is a TLV that contains the MDIE of a BSS entry.

## TLV Type


0x10D

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description              |
|-----------|--------------------------|
| UINT8\[\] | The MDIE of a BSS entry. |

 

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

 

 




