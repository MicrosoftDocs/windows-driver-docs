---
title: WDI_TLV_SEND_ACTION_FRAME_REQUEST_PARAMETERS
description: WDI_TLV_SEND_ACTION_FRAME_REQUEST_PARAMETERS is a TLV that contains parameters for OID_WDI_TASK_SEND_REQUEST_ACTION_FRAME.
ms.assetid: 92629752-A94B-442A-97E9-D8E1C7924855
ms.date: 07/18/2017
keywords:
 - WDI_TLV_SEND_ACTION_FRAME_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_SEND\_ACTION\_FRAME\_REQUEST\_PARAMETERS


WDI\_TLV\_SEND\_ACTION\_FRAME\_REQUEST\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_TASK\_SEND\_REQUEST\_ACTION\_FRAME](https://msdn.microsoft.com/library/windows/hardware/dn925961).

## TLV Type


0xBF

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                     |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| WDI\_CHANNEL\_NUMBER (UINT32)                     | The channel on which to send the action frame and also to linger on as specified in the post-ACK dwell time.                                    |
| WDI\_BAND\_ID (UINT32)                            | The ID of the band on which to send the action frame.                                                                                           |
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) | The MAC address of the target access point or peer adapter.                                                                                     |
| UINT32                                            | The send timeout. Specifies the maximum time (in milliseconds) to send this Action Frame.                                                       |
| UINT32                                            | The post-acknowledgment dwell time. Specifies the time (in milliseconds) to remain on listen channel after the incoming packet is acknowledged. |

 

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

 

 




