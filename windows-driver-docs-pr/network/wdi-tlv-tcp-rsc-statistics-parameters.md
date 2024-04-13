---
title: WDI_TLV_TCP_RSC_STATISTICS_PARAMETERS
ms.topic: reference
description: WDI_TLV_TCP_RSC_STATISTICS_PARAMETERS is a TLV that contains TCP RSC statistics for OID_WDI_TCP_RSC_STATISTICS.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_TCP_RSC_STATISTICS_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_TCP\_RSC\_STATISTICS\_PARAMETERS


WDI\_TLV\_TCP\_RSC\_STATISTICS\_PARAMETERS is a TLV that contains TCP RSC statistics for [OID\_WDI\_TCP\_RSC\_STATISTICS](./oid-wdi-tcp-rsc-statistics.md).

## TLV Type


0xF3

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                                                                                                               |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT64 | The total number of packets that were coalesced.                                                                                                                                                                                          |
| UINT64 | The total number of bytes that were coalesced.                                                                                                                                                                                            |
| UINT64 | The total number of coalescing events, which is the total number of packets that were formed from coalescing packets.                                                                                                                     |
| UINT64 | The total number of RSC abort events, which is the number of exceptions other than the IP datagram length being exceeded. This count should include the cases where a packet is not coalesced because of insufficient hardware resources. |

 

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

 

