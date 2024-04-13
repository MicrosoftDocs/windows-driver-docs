---
title: WDI_TLV_BEACON_FRAME
ms.topic: reference
description: WDI_TLV_BEACON_FRAME is a TLV that contains a beacon frame.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_BEACON_FRAME Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BEACON\_FRAME

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_BEACON\_FRAME is a TLV that contains a beacon frame.

## TLV Type


0xA

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                 |
|-----------|-------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the beacon frame. |

 

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

 

 




