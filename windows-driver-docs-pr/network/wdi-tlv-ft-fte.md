---
title: WDI_TLV_FT_FTE
ms.topic: reference
description: WDI_TLV_FT_FTE is a TLV that contains a Fast Transition Element.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_FT_FTE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_FT\_FTE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_FT\_FTE is a TLV that contains a Fast Transition Element.

## TLV Type


0x10B

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                    |
|-----------|----------------------------------------------------------------|
| UINT8\[\] | A Fast Transition Element that contains the R0KHID and SNonce. |

 

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

 

 




