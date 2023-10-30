---
title: WDI_TLV_BAND_ID_LIST
ms.topic: reference
description: WDI_TLV_BAND_ID_LIST is a TLV that contains a list of band IDs.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_BAND_ID_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BAND\_ID\_LIST

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_BAND\_ID\_LIST is a TLV that contains a list of band IDs.

## TLV Type


0xB6

## Length


The size (in bytes) of the array of WDI\_BAND\_ID (UINT32) elements. The array must contain 1 or more elements.

## Values


| Type              | Description           |
|-------------------|-----------------------|
| WDI\_BAND\_ID\[\] | An array of band IDs. |

 

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

 

 




