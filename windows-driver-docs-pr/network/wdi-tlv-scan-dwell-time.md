---
title: WDI_TLV_SCAN_DWELL_TIME
ms.topic: reference
description: WDI_TLV_SCAN_DWELL_TIME is a TLV that contains scanning dwell time settings.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_SCAN_DWELL_TIME Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_SCAN\_DWELL\_TIME

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_SCAN\_DWELL\_TIME is a TLV that contains scanning dwell time settings.

## TLV Type


0x7

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                                                           |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | Specifies the time in milliseconds to dwell on active channels. This is a hint and if the adapter decides to use its own dwell time, it must meet the Maximum Scan Time requirement.  |
| UINT32 | Specifies the time in milliseconds to dwell on passive channels. This is a hint and if the adapter decides to use its own dwell time, it must meet the Maximum Scan Time requirement. |
| UINT32 | Specifies the time in milliseconds for total scan. If the adapter limits its dwell times to below the values specified above, it can ignore the Maximum Scan Time parameter.          |

 

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

 

 




