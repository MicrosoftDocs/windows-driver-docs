---
title: OID_WDI_TASK_DOT11_RESET
author: windows-driver-content
description: OID_WDI_TASK_DOT11_RESET requests that the IHV component resets the MAC and PHY state on a specified port.
ms.assetid: 5fcac1da-0776-47a5-87b7-8e831f968f7c
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_TASK_DOT11_RESET Network Drivers Starting with Windows Vista
---

# OID\_WDI\_TASK\_DOT11\_RESET


OID\_WDI\_TASK\_DOT11\_RESET requests that the IHV component resets the MAC and PHY state on a specified port.

| Object | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------|---------------------------------------|---------------------------------|
| Port   | No            | 1                                     | 1                               |

 

Prior to issuing a dot11 reset command, the WDI driver stops issuing new commands to IHV component and aborts any task in progress on the port. It also flushes its Rx and TX queues.

The dot11 reset combines the semantics of the 802.11 MLME and PLME reset primitive. When the IHV component receives a dot11 reset request, it should perform the following tasks.

-   Reset the port’s MAC entity to its initial state.
-   Reset the port’s MIB attributes so they are set to their default values, if bSetDefaultMIB is true.
-   Reset the TX/Rx state machines for the PHY entity and set it to Rx state only to ensure no more frames are transmitted.
-   Flush the adapter’s Rx queue and complete the send for each packet in the TX queues.
-   If the MAC address parameter is present, reset the port’s MAC address to the specified value.
-   Set the port state to INIT before completing the dot11 reset operation.

If the port being reset was operating as a STA, AP, or a Wi-Fi Direct Client or GO, the host would have triggered the disconnect task to request the IHV component to send disassociation to the peers before the reset. As such, the IHV component does not need to do it again.

## Task parameters


| TLV                                                                               | Multiple TLV instances allowed | Optional | Description                                       |
|-----------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------|
| [**WDI\_TLV\_DOT11\_RESET\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn926302) |                                |          | Parameters for the dot11 reset.                   |
| [**WDI\_TLV\_CONFIGURED\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926257) |                                | X        | The MAC address that should be used for the port. |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_DOT11\_RESET\_COMPLETE](ndis-status-wdi-indication-dot11-reset-complete.md)
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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_TASK_DOT11_RESET%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


