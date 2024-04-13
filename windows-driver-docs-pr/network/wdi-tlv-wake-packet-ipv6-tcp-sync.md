---
title: WDI_TLV_WAKE_PACKET_IPv6_TCP_SYNC
ms.topic: reference
description: WDI_TLV_WAKE_PACKET_IPv6_TCP_SYNC is a TLV that contains wake-on-LAN IPv6 TCP sync packet information.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_WAKE_PACKET_IPv6_TCP_SYNC Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_WAKE\_PACKET\_IPv6\_TCP\_SYNC


WDI\_TLV\_WAKE\_PACKET\_IPv6\_TCP\_SYNC is a TLV that contains wake-on-LAN IPv6 TCP sync packet information.

## TLV Type


0x5E

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type        | Description                                                      |
|-------------|------------------------------------------------------------------|
| UINT32      | Specifies the WoL pattern ID.                                    |
| UINT8\[16\] | Specifies the IPv6 source address in the TCP SYN packet.         |
| UINT8\[16\] | Specifies the IPv6 destination address in the TCP SYN packet.    |
| UINT16      | Specifies the TCP source port number in the TCP SYN packet.      |
| UINT16      | Specifies the TCP destination port number in the TCP SYN packet. |

 

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

 

 




