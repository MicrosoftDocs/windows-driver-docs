---
title: WDI_TLV_INDICATION_WAKE_PACKET_PATTERN_ID
ms.topic: reference
description: WDI_TLV_INDICATION_WAKE_PACKET_PATTERN_ID is a TLV that contains the ID of the pattern that matches a wake packet.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_INDICATION_WAKE_PACKET_PATTERN_ID Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_INDICATION\_WAKE\_PACKET\_PATTERN\_ID


WDI\_TLV\_INDICATION\_WAKE\_PACKET\_PATTERN\_ID is a TLV that contains the ID of the pattern that matches a wake packet.

## TLV Type


0xB0

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                                                                    |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The ID of the pattern that matches the wake packet. The ID is defined when the pattern is added with [OID\_WDI\_SET\_ADD\_WOL\_PATTERN](./oid-wdi-set-add-wol-pattern.md). |

 

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

 

