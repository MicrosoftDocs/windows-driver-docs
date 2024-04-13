---
title: WDI_TLV_P2P_ACTION_FRAME_IES
ms.topic: reference
description: WDI_TLV_P2P_ACTION_FRAME_IES is a TLV that contains action frame IEs.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_ACTION_FRAME_IES Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_ACTION\_FRAME\_IES

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_ACTION\_FRAME\_IES is a TLV that contains action frame IEs.

## TLV Type


0x90

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                  |
|-----------|----------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the set of IEs that are sent to the remote device. |

 

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

 

 




