---
title: WDI_TLV_CHANNEL_WIDTH_LIST
ms.topic: reference
description: WDI_TLV_CHANNEL_WIDTH_LIST is a TLV that contains a list of channel widths.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_CHANNEL_WIDTH_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CHANNEL\_WIDTH\_LIST

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_CHANNEL\_WIDTH\_LIST is a TLV that contains a list of channel widths.

## TLV Type


0xF5

## Length


The size (in bytes) of the array of UINT32 elements. The array must contain 1 or more elements.

## Values


| Type       | Description                                 |
|------------|---------------------------------------------|
| UINT32\[\] | A list of channel widths, specified in MHz. |

 

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

 

 




