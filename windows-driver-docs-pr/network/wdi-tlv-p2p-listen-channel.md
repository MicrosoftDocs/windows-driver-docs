---
title: WDI_TLV_P2P_LISTEN_CHANNEL
description: WDI_TLV_P2P_LISTEN_CHANNEL is a TLV that contains Wi-Fi Direct channel information.
ms.assetid: 45D1B507-C02B-432B-A552-78F2539ECE68
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_LISTEN_CHANNEL Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_LISTEN\_CHANNEL


WDI\_TLV\_P2P\_LISTEN\_CHANNEL is a TLV that contains Wi-Fi Direct channel information.

## TLV Type


0x114

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                          | Description                                                                        |
|-------------------------------|------------------------------------------------------------------------------------|
| UINT8\[3\]                    | The country or region code where the operating class and channel number are valid. |
| UINT8                         | The operating class/frequency band for the channel number.                         |
| WDI\_CHANNEL\_NUMBER (UINT32) | The channel number for the Wi-Fi Direct Device or Group.                           |

 

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

 

 




