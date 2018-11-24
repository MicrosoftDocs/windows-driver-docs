---
title: WDI_TLV_P2P_SEND_ACTION_REQUEST_FRAME_PARAMETERS
description: WDI_TLV_P2P_SEND_ACTION_REQUEST_FRAME_PARAMETERS is a TLV that contains parameters for sending a Wi-Fi Direct action request frame with OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME.
ms.assetid: 802654D0-CC8E-4808-8C1B-BAAF4C6E53F1
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_SEND_ACTION_REQUEST_FRAME_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_SEND\_ACTION\_REQUEST\_FRAME\_PARAMETERS


WDI\_TLV\_P2P\_SEND\_ACTION\_REQUEST\_FRAME\_PARAMETERS is a TLV that contains parameters for sending a Wi-Fi Direct action request frame with [OID\_WDI\_TASK\_P2P\_SEND\_REQUEST\_ACTION\_FRAME](https://msdn.microsoft.com/library/windows/hardware/dn925956).

## TLV Type


0x8B

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                    | Description                                                                                                                    |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_P2P\_ACTION\_FRAME\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn926086) | The type of request to send.                                                                                                   |
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071)                       | The MAC address of the target peer device.                                                                                     |
| UINT8                                                                   | The Direct Dialog Token for the transaction.                                                                                   |
| UINT32                                                                  | The send timeout. The maximum time, in milliseconds, to send the action frame.                                                 |
| UINT32                                                                  | The post-ACK dwell time. The time, in milliseconds, to remain on the listen channel after the incoming packet is acknowledged. |

 

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

 

 




