---
title: WDI_TLV_P2P_SEND_ACTION_REQUEST_FRAME_PARAMETERS
author: windows-driver-content
description: WDI_TLV_P2P_SEND_ACTION_REQUEST_FRAME_PARAMETERS is a TLV that contains parameters for sending a Wi-Fi Direct action request frame with OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME.
ms.assetid: 802654D0-CC8E-4808-8C1B-BAAF4C6E53F1
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_P2P_SEND_ACTION_REQUEST_FRAME_PARAMETERS Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WDI_TLV_P2P_SEND_ACTION_REQUEST_FRAME_PARAMETERS%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


