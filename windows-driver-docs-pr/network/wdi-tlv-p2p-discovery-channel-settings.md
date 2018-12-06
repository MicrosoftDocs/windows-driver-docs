---
title: WDI_TLV_P2P_DISCOVERY_CHANNEL_SETTINGS
description: WDI_TLV_P2P_DISCOVERY_CHANNEL_SETTINGS is a TLV that contains Wi-Fi Direct discovery channel settings.
ms.assetid: 50BD3F70-4C12-4984-8E3F-AEC9F5C3CDCA
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_DISCOVERY_CHANNEL_SETTINGS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_DISCOVERY\_CHANNEL\_SETTINGS


WDI\_TLV\_P2P\_DISCOVERY\_CHANNEL\_SETTINGS is a TLV that contains Wi-Fi Direct discovery channel settings.

## TLV Type


0xE8

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                   | Multiple TLV instances allowed | Optional | Description                         |
|------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------|
| [**WDI\_TLV\_P2P\_LISTEN\_DURATION**](wdi-tlv-p2p-listen-duration.md) |                                |          | The cycle duration and listen time. |
| [**WDI\_TLV\_BAND\_CHANNEL**](wdi-tlv-band-channel.md)                | X                              |          | The list of channels to scan.       |

 

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

 

 




