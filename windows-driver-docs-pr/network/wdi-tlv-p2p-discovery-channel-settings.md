---
title: WDI_TLV_P2P_DISCOVERY_CHANNEL_SETTINGS
ms.topic: reference
description: WDI_TLV_P2P_DISCOVERY_CHANNEL_SETTINGS is a TLV that contains Wi-Fi Direct discovery channel settings.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_DISCOVERY_CHANNEL_SETTINGS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_DISCOVERY\_CHANNEL\_SETTINGS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


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

 

 




