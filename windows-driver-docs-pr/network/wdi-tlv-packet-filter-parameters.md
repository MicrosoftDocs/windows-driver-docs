---
title: WDI_TLV_PACKET_FILTER_PARAMETERS
description: WDI_TLV_PACKET_FILTER_PARAMETERS is a TLV that contains packet filter parameters for OID_WDI_SET_RECEIVE_PACKET_FILTER.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_PACKET_FILTER_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_PACKET\_FILTER\_PARAMETERS


WDI\_TLV\_PACKET\_FILTER\_PARAMETERS is a TLV that contains packet filter parameters for [OID\_WDI\_SET\_RECEIVE\_PACKET\_FILTER](./oid-wdi-set-receive-packet-filter.md).

## TLV Type


0x47

## Length


The size (in bytes) of a UINT32.

## Values


| Type                                                                      | Description                                |
|---------------------------------------------------------------------------|--------------------------------------------|
| [**WDI\_PACKET\_FILTER\_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_packet_filter_type) (UINT32) | Specifies the desired Wi-Fi packet filter. |

 

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

 

