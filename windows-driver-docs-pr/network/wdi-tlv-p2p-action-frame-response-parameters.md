---
title: WDI_TLV_P2P_ACTION_FRAME_RESPONSE_PARAMETERS
ms.topic: reference
description: WDI_TLV_P2P_ACTION_FRAME_RESPONSE_PARAMETERS is a TLV that contains Wi-Fi Direct Action Frame response parameters.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_ACTION_FRAME_RESPONSE_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_ACTION\_FRAME\_RESPONSE\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_ACTION\_FRAME\_RESPONSE\_PARAMETERS is a TLV that contains Wi-Fi Direct Action Frame response parameters.

## TLV Type


0xAD

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                    | Description                                                                                                                          |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_P2P\_ACTION\_FRAME\_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_action_frame_type) | The type of Response Frame to be sent.                                                                                               |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address)                       | The device address of the target peer Wi-Fi Direct device.                                                                           |
| UINT8                                                                   | The Wi-Fi Direct Dialog Token for this transaction.                                                                                  |
| UINT32                                                                  | The send timeout. Specifies the maximum time, in milliseconds, to send this action frame.                                            |
| UINT32                                                                  | The post-ACK dwell time. Specifies the time to remain on listen channel, in milliseconds, after the incoming packet is acknowledged. |

 

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

 

