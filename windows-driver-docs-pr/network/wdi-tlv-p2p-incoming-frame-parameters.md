---
title: WDI_TLV_P2P_INCOMING_FRAME_PARAMETERS
description: WDI_TLV_P2P_INCOMING_FRAME_PARAMETERS is a TLV that contains incoming Wi-Fi Direct action frame parameters.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_INCOMING_FRAME_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_INCOMING\_FRAME\_PARAMETERS


WDI\_TLV\_P2P\_INCOMING\_FRAME\_PARAMETERS is a TLV that contains incoming Wi-Fi Direct action frame parameters.

## TLV Type


0x7A

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                    | Description                                        |
|-------------------------------------------------------------------------|----------------------------------------------------|
| [**WDI\_P2P\_ACTION\_FRAME\_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_action_frame_type) | The type of the incoming action frame.             |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address)                       | The MAC address of the remote peer.                |
| UINT8                                                                   | The Wi-Fi Direct Dialog Token for the transaction. |

 

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

 

