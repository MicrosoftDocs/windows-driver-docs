---
title: WDI_TLV_P2P_GROUP_ID
description: WDI_TLV_P2P_GROUP_ID is a TLV that contains the Group ID for Wi-Fi Direct GO.
ms.assetid: 5DF5E7AA-4A5A-4AF5-90E6-40791C8DBB56
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_GROUP_ID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_GROUP\_ID


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

 

 




