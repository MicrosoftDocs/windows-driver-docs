---
title: WDI_TLV_WAKE_PACKET_IPv4_TCP_SYNC
description: WDI_TLV_WAKE_PACKET_IPv4_TCP_SYNC is a TLV that contains wake-on-LAN IPv4 TCP sync packet information.
ms.assetid: C1237747-721C-4E44-B2BA-1B93E81174A8
ms.date: 07/18/2017
keywords:
 - WDI_TLV_WAKE_PACKET_IPv4_TCP_SYNC Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_WAKE\_PACKET\_IPv4\_TCP\_SYNC


WDI\_TLV\_WAKE\_PACKET\_IPv4\_TCP\_SYNC is a TLV that contains wake-on-LAN IPv4 TCP sync packet information.

## TLV Type


0x5D

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type       | Description                                                      |
|------------|------------------------------------------------------------------|
| UINT32     | Specifies the wake-on-LAN pattern ID.                            |
| UINT8\[4\] | Specifies the IPv4 source address in the TCP SYN packet.         |
| UINT8\[4\] | Specifies the IPv4 destination address in the TCP SYN packet.    |
| UINT16     | Specifies the TCP source port number in the TCP SYN packet.      |
| UINT16     | Specifies the TCP destination port number in the TCP SYN packet. |

 

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

 

 




