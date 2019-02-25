---
title: WDI_TLV_STATION_ATTRIBUTES
description: WDI_TLV_STATION_ATTRIBUTES is a TLV that contains the attributes of a station.
ms.assetid: CB15D3A4-5B42-44ED-A8A8-3E7F09B65F8B
ms.date: 07/18/2017
keywords:
 - WDI_TLV_STATION_ATTRIBUTES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_STATION\_ATTRIBUTES


WDI\_TLV\_STATION\_ATTRIBUTES is a TLV that contains the attributes of a station.

## TLV Type


0x22

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                        | Multiple TLV instances allowed | Optional | Description                                    |
|---------------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------|
| [**WDI\_TLV\_STATION\_CAPABILITIES**](wdi-tlv-station-capabilities.md)                     |                                |          | The station capabilities.                      |
| [**WDI\_TLV\_UNICAST\_ALGORITHM\_LIST**](wdi-tlv-unicast-algorithm-list.md)                |                                | X        | The supported unicast algorithms.              |
| [**WDI\_TLV\_MULTICAST\_DATA\_ALGORITHM\_LIST**](wdi-tlv-multicast-data-algorithm-list.md) |                                | X        | The supported multicast data algorithms.       |
| [**WDI\_TLV\_MULTICAST\_MGMT\_ALGORITHM\_LIST**](wdi-tlv-multicast-mgmt-algorithm-list.md) |                                | X        | The supported multicast management algorithms. |

 

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

 

 




