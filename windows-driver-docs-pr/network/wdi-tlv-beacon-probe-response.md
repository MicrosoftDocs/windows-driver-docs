---
title: WDI_TLV_BEACON_PROBE_RESPONSE
description: WDI_TLV_BEACON_PROBE_RESPONSE is a TLV that contains the latest beacon or probe response frame received by the port.
ms.assetid: D1148F9B-D25F-4AF0-8C55-43453441C667
ms.date: 07/18/2017
keywords:
 - WDI_TLV_BEACON_PROBE_RESPONSE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_BEACON\_PROBE\_RESPONSE


WDI\_TLV\_BEACON\_PROBE\_RESPONSE is a TLV that contains the latest beacon or probe response frame received by the port.

## TLV Type


0x30

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the latest beacon or probe response frame received by the port. This does not include the 802.11 MAC header. |

 

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

 

 




