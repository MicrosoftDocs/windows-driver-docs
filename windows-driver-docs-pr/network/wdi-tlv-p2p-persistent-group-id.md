---
title: WDI_TLV_P2P_PERSISTENT_GROUP_ID
ms.topic: reference
description: WDI_TLV_P2P_PERSISTENT_GROUP_ID is a TLV that contains a Group ID of a Persistent Group to be used for a connection.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_PERSISTENT_GROUP_ID Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_PERSISTENT\_GROUP\_ID

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_PERSISTENT\_GROUP\_ID is a TLV that contains a Group ID of a Persistent Group to be used for a connection.

## TLV Type


0xF1

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                 | Multiple TLV instances allowed | Optional | Description                            |
|----------------------------------------------------------------------|--------------------------------|----------|----------------------------------------|
| [**WDI\_TLV\_P2P\_DEVICE\_ADDRESS**](wdi-tlv-p2p-device-address.md) |                                |          | The device address of the Group Owner. |
| [**WDI\_TLV\_SSID**](wdi-tlv-ssid.md)                               |                                |          | The Group SSID.                        |

 

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

 

 




