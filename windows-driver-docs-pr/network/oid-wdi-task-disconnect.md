---
title: OID_WDI_TASK_DISCONNECT
description: OID_WDI_TASK_DISCONNECT is used to terminate a connection with a peer.
ms.assetid: 03566fbd-5043-4166-bd33-0ed48f85f370
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_DISCONNECT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_DISCONNECT


OID\_WDI\_TASK\_DISCONNECT is used to terminate a connection with a peer.

| Object | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------|---------------------------------------|---------------------------------|
| Port   | No            | 2                                     | 1                               |

 

This command is used to disconnect from an Access Point or a Wi-Fi Direct GO, and also to disconnect clients of the port. When the disconnect is received, the port must disassociate and deauthenticate from the peer and clear the state associated with that peer. However, it must not reset any of the connection parameters that are not specific to this peer. The task must be completed only after the disconnect activity has been completed.

## Task parameters


| TLV                                                                            | Multiple TLV instances allowed | Optional | Description                |
|--------------------------------------------------------------------------------|--------------------------------|----------|----------------------------|
| [**WDI\_TLV\_DISCONNECT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn926300) |                                |          | The disconnect parameters. |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_DISCONNECT\_COMPLETE](ndis-status-wdi-indication-disconnect-complete.md)
## Unsolicited indication


[NDIS\_STATUS\_WDI\_INDICATION\_DISASSOCIATION](ndis-status-wdi-indication-disassociation.md)
When the port gets disconnected from the network, it sends the disassociation indication to the OS. The disconnect may be triggered by a command from the OS, or may be triggered from the network. Network triggered disconnects may be explicit from received disassociation or deauthentication packets, or may be implicit when the port cannot detect the presence of the peer it is connected to.

Before the disassociation indication is sent, the port must clear the state associated with the peer. This includes any keys and 802.1x port authorization information associated with the peer. The port must not trigger a roam on its own.

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

 

 




