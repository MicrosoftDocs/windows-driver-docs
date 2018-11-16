---
title: WDI_TLV_P2P_ACTION_FRAME_RESPONSE_PARAMETERS
description: WDI_TLV_P2P_ACTION_FRAME_RESPONSE_PARAMETERS is a TLV that contains Wi-Fi Direct Action Frame response parameters.
ms.assetid: 2DFF00A6-FDE2-43EF-93C2-EEA3DBC00D52
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_ACTION_FRAME_RESPONSE_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_ACTION\_FRAME\_RESPONSE\_PARAMETERS


WDI\_TLV\_P2P\_ACTION\_FRAME\_RESPONSE\_PARAMETERS is a TLV that contains Wi-Fi Direct Action Frame response parameters.

## TLV Type


0xAD

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                    | Description                                                                                                                          |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_P2P\_ACTION\_FRAME\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/dn926086) | The type of Response Frame to be sent.                                                                                               |
| [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071)                       | The device address of the target peer Wi-Fi Direct device.                                                                           |
| UINT8                                                                   | The Wi-Fi Direct Dialog Token for this transaction.                                                                                  |
| UINT32                                                                  | The send timeout. Specifies the maximum time, in milliseconds, to send this action frame.                                            |
| UINT32                                                                  | The post-ACK dwell time. Specifies the time to remain on listen channel, in milliseconds, after the incoming packet is acknowledged. |

 

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

 

 




