---
title: WDI_TLV_P2P_SEND_ACTION_FRAME_RESULT_PARAMETERS
description: WDI_TLV_P2P_SEND_ACTION_FRAME_RESULT_PARAMETERS is a TLV that contains Wi-Fi Direct send Action Frame result parameters.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_SEND_ACTION_FRAME_RESULT_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT\_PARAMETERS


WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT\_PARAMETERS is a TLV that contains Wi-Fi Direct send Action Frame result parameters.

## TLV Type


0xAE

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                           |
|---------------------------------------------------|-------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | The device address of the target Wi-Fi Direct device. |
| UINT8                                             | The Wi-Fi Direct Dialog Token for this transaction.   |

 

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

 

