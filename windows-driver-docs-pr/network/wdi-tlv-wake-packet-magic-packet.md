---
title: WDI_TLV_WAKE_PACKET_MAGIC_PACKET
ms.topic: reference
description: WDI_TLV_WAKE_PACKET_MAGIC_PACKET is a TLV that contains a pattern ID of a magic packet for OID_WDI_SET_ADD_WOL_PATTERN.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_WAKE_PACKET_MAGIC_PACKET Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_WAKE\_PACKET\_MAGIC\_PACKET


WDI\_TLV\_WAKE\_PACKET\_MAGIC\_PACKET is a TLV that contains a pattern ID of a magic packet for [OID\_WDI\_SET\_ADD\_WOL\_PATTERN](./oid-wdi-set-add-wol-pattern.md).

## TLV Type


0x5C

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                        |
|--------|----------------------------------------------------|
| UINT32 | Specifies the wake-on-LAN magic packet pattern ID. |

 

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

 

