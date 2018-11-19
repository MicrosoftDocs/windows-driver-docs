---
title: WDI_TLV_UNREACHABLE_DETECTION_THRESHOLD
description: WDI_TLV_UNREACHABLE_DETECTION_THRESHOLD is a TLV that contains the unreachable detection threshold.
ms.assetid: D2C41B26-90EF-4A62-A105-DBEF3822BA6E
ms.date: 07/18/2017
keywords:
 - WDI_TLV_UNREACHABLE_DETECTION_THRESHOLD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_UNREACHABLE\_DETECTION\_THRESHOLD


WDI\_TLV\_UNREACHABLE\_DETECTION\_THRESHOLD is a TLV that contains the unreachable detection threshold.

## TLV Type


0xB1

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                                                                                                                                                                                                               |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The unreachable detection threshold. Specifies the maximum amount of time, in milliseconds, before the 802.11 station determines that it has lost connectivity to a peer device. The station must include missed beacons in making this connectivity loss determination but can also use any other heuristics it desires. |

 

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

 

 




