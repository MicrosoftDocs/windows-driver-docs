---
title: WDI_TLV_P2P_SEND_ACTION_FRAME_RESULT
description: WDI_TLV_P2P_SEND_ACTION_FRAME_RESULT is a TLV that contains information about an Action Frame that was sent to a peer.
ms.assetid: DA469DF2-4C59-495C-A4B5-DC7B3B157566
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_SEND_ACTION_FRAME_RESULT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT


WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT is a TLV that contains information about an Action Frame that was sent to a peer.

## TLV Type


0xAF

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                              | Multiple TLV instances allowed | Optional | Description                                           |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT\_PARAMETERS**](wdi-tlv-p2p-send-action-frame-result-parameters.md) |                                |          | The Wi-Fi Direct send Action Frame result parameters. |
| [**WDI\_TLV\_P2P\_ACTION\_FRAME\_IES**](wdi-tlv-p2p-action-frame-ies.md)                                         |                                |          | The set of IEs sent to the remote device.             |

 

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

 

 




