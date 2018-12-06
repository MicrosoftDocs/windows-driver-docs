---
title: WDI_TLV_CHANNEL_WIDTH_LIST
description: WDI_TLV_CHANNEL_WIDTH_LIST is a TLV that contains a list of channel widths.
ms.assetid: 9869157D-2E71-4F08-92D0-A4FFA085ACE7
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CHANNEL_WIDTH_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CHANNEL\_WIDTH\_LIST


WDI\_TLV\_CHANNEL\_WIDTH\_LIST is a TLV that contains a list of channel widths.

## TLV Type


0xF5

## Length


The size (in bytes) of the array of UINT32 elements. The array must contain 1 or more elements.

## Values


| Type       | Description                                 |
|------------|---------------------------------------------|
| UINT32\[\] | A list of channel widths, specified in MHz. |

 

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

 

 




