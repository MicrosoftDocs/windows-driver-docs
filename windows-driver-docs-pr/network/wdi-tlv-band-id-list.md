---
title: WDI_TLV_BAND_ID_LIST
description: WDI_TLV_BAND_ID_LIST is a TLV that contains a list of band IDs.
ms.assetid: 415EF9E3-9441-420D-AC8A-0F819369E20E
ms.date: 07/18/2017
keywords:
 - WDI_TLV_BAND_ID_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_BAND\_ID\_LIST


WDI\_TLV\_BAND\_ID\_LIST is a TLV that contains a list of band IDs.

## TLV Type


0xB6

## Length


The size (in bytes) of the array of WDI\_BAND\_ID (UINT32) elements. The array must contain 1 or more elements.

## Values


| Type              | Description           |
|-------------------|-----------------------|
| WDI\_BAND\_ID\[\] | An array of band IDs. |

 

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

 

 




