---
title: WDI_TLV_P2P_GO_NEGOTIATION_REQUEST_INFO
description: WDI_TLV_P2P_GO_NEGOTIATION_REQUEST_INFO is a TLV that contains Wi-Fi Direct Group Owner negotiation request information.
ms.assetid: 4F505DF1-8D02-4421-956F-B7E1AF99D367
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_GO_NEGOTIATION_REQUEST_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_GO\_NEGOTIATION\_REQUEST\_INFO


WDI\_TLV\_P2P\_GO\_NEGOTIATION\_REQUEST\_INFO is a TLV that contains Wi-Fi Direct Group Owner negotiation request information.

## TLV Type


0x6D

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                         | Multiple TLV instances allowed | Optional | Description                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_GO\_NEGOTIATION\_REQUEST\_PARAMETERS**](wdi-tlv-p2p-go-negotiation-request-parameters.md) |                                |          | The Wi-Fi Direct Group Owner negotiation request parameters.                                                                        |
| [**WDI\_TLV\_P2P\_CHANNEL\_NUMBER**](wdi-tlv-p2p-channel-number.md)                                         |                                | X        | The listen channel of the remote device. Whenever this is specified, the GO negotiation request frame must be sent on this channel. |

 

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

 

 




