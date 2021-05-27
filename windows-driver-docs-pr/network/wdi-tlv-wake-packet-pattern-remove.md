---
title: WDI_TLV_WAKE_PACKET_PATTERN_REMOVE
description: WDI_TLV_WAKE_PACKET_PATTERN_REMOVE is a TLV that contains the wake packet pattern ID to be removed with OID_WDI_SET_REMOVE_WOL_PATTERN.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_WAKE_PACKET_PATTERN_REMOVE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_WAKE\_PACKET\_PATTERN\_REMOVE


WDI\_TLV\_WAKE\_PACKET\_PATTERN\_REMOVE is a TLV that contains the wake packet pattern ID to be removed with [OID\_WDI\_SET\_REMOVE\_WOL\_PATTERN](./oid-wdi-set-remove-wol-pattern.md).

## TLV Type


0x6B

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                           |
|--------|---------------------------------------|
| UINT32 | Specifies the wake packet pattern ID. |

 

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

 

