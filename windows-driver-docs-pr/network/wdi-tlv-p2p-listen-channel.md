---
title: WDI_TLV_P2P_LISTEN_CHANNEL
ms.topic: reference
description: WDI_TLV_P2P_LISTEN_CHANNEL is a TLV that contains Wi-Fi Direct channel information.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_LISTEN_CHANNEL Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_LISTEN\_CHANNEL

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


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

 

 




