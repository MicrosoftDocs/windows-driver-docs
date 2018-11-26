---
title: OID_WDI_TASK_DOT11_RESET
description: OID_WDI_TASK_DOT11_RESET requests that the IHV component resets the MAC and PHY state on a specified port.
ms.assetid: 5fcac1da-0776-47a5-87b7-8e831f968f7c
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_DOT11_RESET Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




