---
title: WDI_TLV_BEACON_PROBE_RESPONSE
ms.topic: reference
description: WDI_TLV_BEACON_PROBE_RESPONSE is a TLV that contains the latest beacon or probe response frame received by the port.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_BEACON_PROBE_RESPONSE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BEACON\_PROBE\_RESPONSE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_BEACON\_PROBE\_RESPONSE is a TLV that contains the latest beacon or probe response frame received by the port.

## TLV Type


0x30

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the latest beacon or probe response frame received by the port. This does not include the 802.11 MAC header. |

 

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

 

 




