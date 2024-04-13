---
title: WDI_TLV_P2P_GROUP_ID
ms.topic: reference
description: WDI_TLV_P2P_GROUP_ID is a TLV that contains the Group ID for Wi-Fi Direct GO.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_GROUP_ID Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_GROUP\_ID

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_GROUP\_ID is a TLV that contains the Group ID for Wi-Fi Direct GO.

## TLV Type


0x75

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                 | Multiple TLV instances allowed | Optional | Description                                          |
|----------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------|
| [**WDI\_TLV\_P2P\_DEVICE\_ADDRESS**](wdi-tlv-p2p-device-address.md) |                                |          | Specifies the device address of the Wi-Fi Direct GO. |
| [**WDI\_TLV\_SSID**](wdi-tlv-ssid-list.md)                          |                                |          | Specifies the Group SSID.                            |

 

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

 

 




