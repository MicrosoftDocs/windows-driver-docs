---
title: WDI_TLV_INDICATION_WAKE_PACKET
ms.topic: reference
description: WDI_TLV_INDICATION_WAKE_PACKET is a TLV that contains a wake packet for NDIS_STATUS_WDI_INDICATION_WAKE_REASON. When the wake reason is WDI_WAKE_REASON_CODE PACKET, the status must include the wake packet encapsulated in a WDI_TLV_INDICATION_WAKE_PACKET.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_INDICATION_WAKE_PACKET Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_INDICATION\_WAKE\_PACKET


WDI\_TLV\_INDICATION\_WAKE\_PACKET is a TLV that contains a wake packet for [NDIS\_STATUS\_WDI\_INDICATION\_WAKE\_REASON](./ndis-status-wdi-indication-wake-reason.md). When the wake reason is WDI\_WAKE\_REASON\_CODE PACKET, the status must include the wake packet encapsulated in a WDI\_TLV\_INDICATION\_WAKE\_PACKET.

## TLV Type


0x9D

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | The wake packet. The size is the size of the flat memory version of the packet that will be indicated in the normal receive path. |

 

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

 

