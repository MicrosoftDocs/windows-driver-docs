---
title: NDIS_STATUS_WDI_INDICATION_DISASSOCIATION
author: windows-driver-content
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_DISASSOCIATION to indicate that a port disconnected from the network.
ms.assetid: 4e3ed3ed-1b96-49ea-b60f-a36d2a3fc082
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WDI_INDICATION_DISASSOCIATION Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_DISASSOCIATION


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_DISASSOCIATION to indicate that a port disconnected from the network.

| Object |
|--------|
| Port   |

 

The disconnect may be triggered by a command from the operating system or triggered from the network. Network triggered disconnect may be explicit from received disassociation or deauthentication packets, or may be implicit when the port cannot detect the presence of the peer it is connected to.

Before the disassociation indication is sent, the port must clear the state associated with this peer. This includes any keys and 802.1x port authorization information associated with this peer. The port must not trigger a roam on its own.

## Payload data


Type
Multiple TLV instances allowed
Optional
Description
[**WDI\_TLV\_DISASSOCIATION\_INDICATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn926292)
The disassociation indication parameters.
[**WDI\_TLV\_DISCONNECT\_DEAUTH\_FRAME**](https://msdn.microsoft.com/library/windows/hardware/dn926296)
X
The deauthentication frame that was received. This does not include the 802.11 MAC header.
[**WDI\_TLV\_DISCONNECT\_DISASSOCIATION\_FRAME**](https://msdn.microsoft.com/library/windows/hardware/dn926298)
X
The disassociation frame that was received. This does not include the 802.11 MAC header.
 

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

## See also


[OID\_WDI\_TASK\_DISCONNECT](oid-wdi-task-disconnect.md)

[OID\_WDI\_TASK\_ROAM](oid-wdi-task-roam.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WDI_INDICATION_DISASSOCIATION%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


