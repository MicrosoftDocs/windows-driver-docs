---
title: OID_WDI_TASK_DISCONNECT
author: windows-driver-content
description: OID_WDI_TASK_DISCONNECT is used to terminate a connection with a peer.
ms.assetid: 03566fbd-5043-4166-bd33-0ed48f85f370
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_TASK_DISCONNECT Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_TASK_DISCONNECT%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


