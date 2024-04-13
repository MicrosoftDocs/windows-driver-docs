---
title: WDI_TLV_SEND_ACTION_FRAME_RESPONSE_PARAMETERS
ms.topic: reference
description: WDI_TLV_SEND_ACTION_FRAME_RESPONSE_PARAMETERS is a TLV that contains parameters for OID_WDI_TASK_SEND_RESPONSE_ACTION_FRAME.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_SEND_ACTION_FRAME_RESPONSE_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_SEND\_ACTION\_FRAME\_RESPONSE\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_SEND\_ACTION\_FRAME\_RESPONSE\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_TASK\_SEND\_RESPONSE\_ACTION\_FRAME](./oid-wdi-task-send-response-action-frame.md).

## TLV Type


0xE2

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                     |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| WDI\_CHANNEL\_NUMBER (UINT32)                     | The channel on which to send the action frame and also to linger on as specified in the post-ACK dwell time.                                    |
| WDI\_BAND\_ID (UINT32)                            | The ID of the band on which to send the action frame.                                                                                           |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | The MAC address of the target access point or peer adapter.                                                                                     |
| UINT32                                            | The send timeout. Specifies the maximum time (in milliseconds) to send this Action Frame.                                                       |
| UINT32                                            | The post-acknowledgment dwell time. Specifies the time (in milliseconds) to remain on listen channel after the incoming packet is acknowledged. |

 

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

 

