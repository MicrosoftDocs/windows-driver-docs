---
title: WDI_TLV_LOW_LATENCY_CONNECTION_QUALITY_PARAMETERS
description: WDI_TLV_LOW_LATENCY_CONNECTION_QUALITY_PARAMETERS is a TLV that contains low latency connection quality parameters.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_LOW_LATENCY_CONNECTION_QUALITY_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_LOW\_LATENCY\_CONNECTION\_QUALITY\_PARAMETERS


WDI\_TLV\_LOW\_LATENCY\_CONNECTION\_QUALITY\_PARAMETERS is a TLV that contains low latency connection quality parameters.

## TLV Type


0xF6

## Length


The size (in bytes) of the array of all contained elements.

## Values


| Type  | Description                                                                                                                                                                                                                                                                            |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | Specifies the maximum number of milliseconds that the port can be on a different channel during Active Scan or other multi-channel operations. The only instance in which this off-channel can be higher is if the adapter needs to do a passive scan.                                 |
| UINT8 | Specifies the link quality threshold for [NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED](./ndis-status-wdi-indication-roaming-needed.md). When the link quality is below this threshold, it is acceptable for the adapter to send NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED. |

 

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

## See also


[OID\_WDI\_SET\_CONNECTION\_QUALITY](./oid-wdi-set-connection-quality.md)

[NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED](./ndis-status-wdi-indication-roaming-needed.md)

 

