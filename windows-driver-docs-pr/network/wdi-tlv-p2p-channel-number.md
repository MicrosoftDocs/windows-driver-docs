---
title: WDI_TLV_P2P_CHANNEL_NUMBER
description: WDI_TLV_P2P_CHANNEL_NUMBER is a TLV that contains Wi-Fi Direct channel number information.
ms.assetid: CE17143E-5DA1-4F5B-A2E0-2BD480030129
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_CHANNEL_NUMBER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_CHANNEL\_NUMBER


WDI\_TLV\_P2P\_CHANNEL\_NUMBER is a TLV that contains Wi-Fi Direct channel number information.

## TLV Type


0x82

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

 

 




