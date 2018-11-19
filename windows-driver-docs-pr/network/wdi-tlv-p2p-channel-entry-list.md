---
title: WDI_TLV_P2P_CHANNEL_ENTRY_LIST
description: WDI_TLV_P2P_CHANNEL_ENTRY_LIST is a TLV that contains a channel number list.
ms.assetid: 10739684-C00C-4AE7-A3B2-D4A6F1E9829B
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_CHANNEL_ENTRY_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_CHANNEL\_ENTRY\_LIST


WDI\_TLV\_P2P\_CHANNEL\_ENTRY\_LIST is a TLV that contains a channel number list.

## TLV Type


0xF9

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                               | Multiple TLV instances allowed | Optional | Description                          |
|--------------------------------------------------------------------|--------------------------------|----------|--------------------------------------|
| [**WDI\_TLV\_OPERATING\_CLASS**](wdi-tlv-operating-class.md)      |                                |          | The frequency band for the channels. |
| [**WDI\_TLV\_CHANNEL\_INFO\_LIST**](wdi-tlv-channel-info-list.md) |                                |          | The channel number list.             |

 

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

 

 




