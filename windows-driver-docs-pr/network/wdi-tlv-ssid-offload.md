---
title: WDI_TLV_SSID_OFFLOAD
ms.topic: reference
description: WDI_TLV_SSID_OFFLOAD is a TLV that contains an SSID and hints about the SSID.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_SSID_OFFLOAD Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_SSID\_OFFLOAD

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_SSID\_OFFLOAD is a TLV that contains an SSID and hints about the SSID.

## TLV Type


0x9E

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                         | Multiple TLV instances allowed | Optional | Description                 |
|------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------|
| [**WDI\_TLV\_SSID**](wdi-tlv-ssid.md)                                       |                                |          | The SSID.                   |
| [**WDI\_TLV\_UNICAST\_ALGORITHM\_LIST**](wdi-tlv-unicast-algorithm-list.md) |                                |          | The unicast algorithm list. |
| [**WDI\_TLV\_CHANNEL\_LIST**](wdi-tlv-channel-list.md)                      |                                |          | The channel list.           |

 

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

 

 




