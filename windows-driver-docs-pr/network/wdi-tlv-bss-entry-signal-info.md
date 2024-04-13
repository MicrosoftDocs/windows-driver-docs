---
title: WDI_TLV_BSS_ENTRY_SIGNAL_INFO
ms.topic: reference
description: WDI_TLV_BSS_ENTRY_SIGNAL_INFO is a TLV that contains signal information for a BSS entry.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_BSS_ENTRY_SIGNAL_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BSS\_ENTRY\_SIGNAL\_INFO

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_BSS\_ENTRY\_SIGNAL\_INFO is a TLV that contains signal information for a BSS entry.

## TLV Type


0xB

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                                                        |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INT32  | The received signal strength indicator (RSSI) value of the beacon or probe response from the peer. This value is specified in units of decibels referenced to 1.0 milliwatts (dBm) |
| UINT32 | The link quality specified by a value from 0 to 100. A value of 100 specifies the highest link quality.                                                                            |

 

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

 

 




