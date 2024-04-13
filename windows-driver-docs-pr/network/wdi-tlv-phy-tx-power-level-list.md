---
title: WDI_TLV_PHY_TX_POWER_LEVEL_LIST
ms.topic: reference
description: WDI_TLV_PHY_TX_POWER_LEVEL_LIST is a TLV that contains a list of power levels.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_PHY_TX_POWER_LEVEL_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PHY\_TX\_POWER\_LEVEL\_LIST


WDI\_TLV\_PHY\_TX\_POWER\_LEVEL\_LIST is a TLV that contains a list of power levels.

## TLV Type


0x1C

## Length


The size (in bytes) of the array of UINT32 elements. The array must contain 1 or more elements.

## Values


| Type       | Description                                              |
|------------|----------------------------------------------------------|
| UINT32\[\] | An array of UINT32 elements that specifies power levels. |

 

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

 

 




