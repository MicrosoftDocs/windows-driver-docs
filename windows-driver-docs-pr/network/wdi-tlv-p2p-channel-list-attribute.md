---
title: WDI_TLV_P2P_CHANNEL_LIST_ATTRIBUTE
ms.topic: reference
description: WDI_TLV_P2P_CHANNEL_LIST_ATTRIBUTE is a TLV that contains channel list attributes.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_CHANNEL_LIST_ATTRIBUTE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_CHANNEL\_LIST\_ATTRIBUTE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_CHANNEL\_LIST\_ATTRIBUTE is a TLV that contains channel list attributes.

## TLV Type


0xD5

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                          | Multiple TLV instances allowed | Optional | Description              |
|-------------------------------------------------------------------------------|--------------------------------|----------|--------------------------|
| [**WDI\_TLV\_COUNTRY\_REGION\_LIST**](wdi-tlv-country-region-list.md)        |                                |          | The country/region list. |
| [**WDI\_TLV\_P2P\_CHANNEL\_ENTRY\_LIST**](wdi-tlv-p2p-channel-entry-list.md) | X                              |          | The list of channels.    |

 

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

 

 




