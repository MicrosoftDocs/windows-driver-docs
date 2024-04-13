---
title: WDI_TLV_P2P_INVITATION_RESPONSE_INFO
ms.topic: reference
description: WDI_TLV_P2P_INVITATION_RESPONSE_INFO is a TLV that contains Wi-Fi Direct Invitation Response information.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_INVITATION_RESPONSE_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_INVITATION\_RESPONSE\_INFO

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_INVITATION\_RESPONSE\_INFO is a TLV that contains Wi-Fi Direct Invitation Response information.

## TLV Type


0x7E

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                  | Multiple TLV instances allowed | Optional | Description                                      |
|-------------------------------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------|
| [**WDI\_TLV\_P2P\_INVITATION\_RESPONSE\_PARAMETERS**](wdi-tlv-p2p-invitation-response-parameters.md) |                                |          | The Wi-Fi Direct Invitation Response parameters. |
| [**WDI\_TLV\_P2P\_GROUP\_BSSID**](wdi-tlv-p2p-group-bssid.md)                                        |                                | X        | The Group BSSID for local Wi-Fi Direct GO.       |
| [**WDI\_TLV\_P2P\_CHANNEL\_NUMBER**](wdi-tlv-p2p-channel-number.md)                                  |                                | X        | The operating channel for Wi-Fi Direct GO.       |

 

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

 

 




