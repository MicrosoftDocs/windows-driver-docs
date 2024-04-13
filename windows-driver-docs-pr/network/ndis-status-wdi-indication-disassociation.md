---
title: NDIS_STATUS_WDI_INDICATION_DISASSOCIATION
ms.topic: reference
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_DISASSOCIATION to indicate that a port disconnected from the network.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_DISASSOCIATION Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# NDIS\_STATUS\_WDI\_INDICATION\_DISASSOCIATION

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_DISASSOCIATION to indicate that a port disconnected from the network.

| Object |
|--------|
| Port   |

 

The disconnect may be triggered by a command from the operating system or triggered from the network. Network triggered disconnect may be explicit from received disassociation or deauthentication packets, or may be implicit when the port cannot detect the presence of the peer it is connected to.

Before the disassociation indication is sent, the port must clear the state associated with this peer. This includes any keys and 802.1x port authorization information associated with this peer. The port must not trigger a roam on its own.

## Payload data


| Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- |
| [**WDI\_TLV\_DISASSOCIATION\_INDICATION\_PARAMETERS**](./wdi-tlv-disassociation-indication-parameters.md) |   |   | The disassociation indication parameters. |
| [**WDI\_TLV\_DISCONNECT\_DEAUTH\_FRAME**](./wdi-tlv-disconnect-deauth-frame.md) |   | X | The deauthentication frame that was received. This does not include the 802.11 MAC header. |
| [**WDI\_TLV\_DISCONNECT\_DISASSOCIATION\_FRAME**](./wdi-tlv-disconnect-disassociation-frame.md) |   | X | The disassociation frame that was received. This does not include the 802.11 MAC header. | 

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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WDI\_TASK\_DISCONNECT](oid-wdi-task-disconnect.md)

[OID\_WDI\_TASK\_ROAM](oid-wdi-task-roam.md)

 

