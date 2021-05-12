---
title: WDI_TLV_STATION_ATTRIBUTES
description: WDI_TLV_STATION_ATTRIBUTES is a TLV that contains the attributes of a station.
ms.date: 02/14/2019
keywords:
 - WDI_TLV_STATION_ATTRIBUTES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI\_TLV\_STATION\_ATTRIBUTES


WDI\_TLV\_STATION\_ATTRIBUTES is a TLV that contains the attributes of a station.

## TLV Type

0x22

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type | Multiple TLV instances allowed | Optional | Description |
|--- | --- | --- | --- |
| [**WDI\_TLV\_STATION\_CAPABILITIES**](wdi-tlv-station-capabilities.md) |   |   | The station capabilities. |
| [**WDI\_TLV\_UNICAST\_ALGORITHM\_LIST**](wdi-tlv-unicast-algorithm-list.md) |   | X | The supported unicast algorithms. |
| [**WDI\_TLV\_MULTICAST\_DATA\_ALGORITHM\_LIST**](wdi-tlv-multicast-data-algorithm-list.md) |   | X  | The supported multicast data algorithms. |
| [**WDI\_TLV\_MULTICAST\_MGMT\_ALGORITHM\_LIST**](wdi-tlv-multicast-mgmt-algorithm-list.md) |   | X  | The supported multicast management algorithms. |

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

 

 




