---
title: WDI_TLV_P2P_GO_NEGOTIATION_RESPONSE_INFO
ms.topic: reference
description: WDI_TLV_P2P_GO_NEGOTIATION_RESPONSE_INFO is a TLV that contains Wi-Fi Direct Group Owner negotiation response information.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_GO_NEGOTIATION_RESPONSE_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_GO\_NEGOTIATION\_RESPONSE\_INFO

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_GO\_NEGOTIATION\_RESPONSE\_INFO is a TLV that contains Wi-Fi Direct Group Owner negotiation response information.

## TLV Type


0x6F

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                           | Multiple TLV instances allowed | Optional | Description                                                             |
|----------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_GO\_NEGOTIATION\_RESPONSE\_PARAMETERS**](wdi-tlv-p2p-go-negotiation-response-parameters.md) |                                |          | Specifies the Wi-Fi Direct Group Owner negotiation response parameters. |
| [**WDI\_TLV\_P2P\_GROUP\_ID**](wdi-tlv-p2p-group-id.md)                                                       |                                | X        | Specifies the Group ID for local Wi-Fi Direct GO.                       |

 

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

 

 




