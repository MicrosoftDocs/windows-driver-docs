---
title: Supporting Bluetooth Event Notifications
description: Supporting Bluetooth Event Notifications
keywords:
- Bluetooth WDK , event notifications
- event notifications WDK Bluetooth
- notifications WDK Bluetooth
- profile drivers WDK Bluetooth
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Bluetooth Event Notifications


When a profile driver opens a connection to a remote device, it should register itself to be notified when the connection is closed, or when any other changes to the connection occur. Additionally, when a profile driver registers itself to accept incoming connections, it must be able to be notified when a remote device attempts to connect to it.

Profile drivers that use Synchronous Connection-Oriented (SCO) connection implement and register a [*SCO Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnsco_indication_callback). A client profile driver registers the appropriate callback function when it requests a connection to a remote device.

When a SCO profile driver issues a **BRB\_SCO\_OPEN\_CHANNEL** BRB, it specifies a pointer to its [*SCO Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnsco_indication_callback) in the **Callback** member of the BRB's corresponding [**\_BRB\_SCO\_OPEN\_CHANNEL**](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_sco_open_channel) structure. If the remote device accepts the SCO connection request, the Bluetooth driver stack can then send notifications to the profile driver through the callback function when a change occurs to the SCO connection .

For more information about creating SCO connections, see [Creating a SCO Client Connection to a Remote Device](creating-a-sco-client-connection-to-a-remote-device.md).

Profile drivers that use Logical Link Controller and Adaptation Protocol (L2CAP) connections implement and register an [*L2CAP Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbthport_indication_callback).

When a L2CAP profile driver issues a **BRB\_L2CA\_OPEN\_CHANNEL** BRB, it specifies a pointer to its [*L2CAP Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbthport_indication_callback) in the **Callback** member of the BRB's corresponding [**\_BRB\_L2CA\_OPEN\_CHANNEL**](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_l2ca_open_channel) structure. If the remote device accepts the L2CAP connection request, the Bluetooth driver stack can then send notifications to the profile driver through the callback function when a change occurs to the L2CAP connection.

For more information about creating L2CAP connections, see [Creating a L2CAP Client Connection to a Remote Device](creating-a-l2cap-client-connection-to-a-remote-device.md).

Similarly, when a profile driver registers itself to accept incoming (L2CAP, SCO) connection requests, it must register a callback function to be notified when a remote device attempts to connect to it.

Profile drivers that use L2CAP specify their [*L2CAP Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbthport_indication_callback) in the **IndicationCallback** member of the [**\_BRB\_L2CA\_REGISTER\_SERVER**](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_l2ca_register_server) structure. The Bluetooth driver stack can then call the callback function to notify the profile driver when a remote device attempts to initiate a L2CAP connection to the profile driver.

Profile drivers that use SCO specify their [*SCO Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnsco_indication_callback) in the **IndicationCallback** member of the [**\_BRB\_SCO\_REGISTER\_SERVER**](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_sco_register_server) structure. The Bluetooth driver stack can then call the callback function to notify the profile driver when a remote device attempts to initiate a SCO connection to the profile driver.

After the profile driver registers the appropriate callback function, the Bluetooth driver stack can also notify the profile driver if and when an event occurs across the open connection.

**Note**  A profile driver can register the same callback function to send it change notifications about an open channel and about remote devices attempting to connect to it.

 

For L2CAP connections, the [*L2CAP callback function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbthport_indication_callback) accepts three parameters:

-   The context that is defined for the L2CAP connection. In the case of BRB\_L2CA\_REGISTER\_SERVER requests, this context is the value passed in the **IndicationCallbackContext** member of the \_BRB\_L2CA\_REGISTER\_SERVER structure passed with the request. In the case of **BRB\_L2CA\_OPEN\_CHANNEL** or **BRB\_L2CA\_OPEN\_CHANNEL\_RESPONSE** requests, this context is the value passed in the **CallbackContext** member of the \_BRB\_L2CA\_OPEN\_CHANNEL structure passed with the request.

-   A value from the [**INDICATION\_CODE**](/windows-hardware/drivers/ddi/bthddi/ne-bthddi-_indication_code) enumeration that indicates the type of the notification event of the incoming L2CAP connection or bonding state change.

-   A pointer to an [**INDICATION\_PARAMETERS**](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_indication_parameters) structure that contains the parameters associated with the notification event.

The value passed in the [*L2CAP callback function's*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbthport_indication_callback)*Indication* parameter specifies which union member in the **Parameters** union of the *Parameters* parameter that the profile driver should use.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">If the value of the <em>Indication</em> parameter equals...</th>
<th align="left">...use the following union member of the <em>Parameters</em> parameter</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>IndicationRemoteConnect</strong></p></td>
<td align="left"><p><strong>Connect</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IndicationRemoteConfigRequest</strong></p></td>
<td align="left"><p><strong>ConfigRequest</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IndicationRemoteConfigResponse</strong></p></td>
<td align="left"><p><strong>ConfigResponse</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IndicationFreeExtraOptions</strong></p></td>
<td align="left"><p><strong>FreeExtraOptions</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IndicationRemoteDisconnect</strong></p></td>
<td align="left"><p><strong>Disconnect</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IndicationRecvPacket</strong></p></td>
<td align="left"><p><strong>RecvPacket</strong></p></td>
</tr>
</tbody>
</table>

 

For SCO connections, the [*SCO callback function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnsco_indication_callback) accepts three arguments:

-   The context that is defined for the SCO connection. In the case of **BRB\_SCO\_REGISTER\_SERVER** requests, this context is the value passed in the **IndicationCallbackContext** member of the \_BRB\_SCO\_REGISTER\_SERVER structure passed with the request. In the case of **BRB\_SCO\_OPEN\_CHANNEL** or **BRB\_SCO\_OPEN\_CHANNEL\_RESPONSE** requests, this context is the value passed in the **CallbackContext** member of the \_BRB\_SCO\_OPEN\_CHANNEL structure passed with the request.

-   A value from the [**SCO\_INDICATION\_CODE**](/windows-hardware/drivers/ddi/bthddi/ne-bthddi-_sco_indication_code) enumeration that indicates the type of the notification of the incoming SCO connection or bonding state change.

-   A pointer to a [**SCO\_INDICATION\_PARAMETERS**](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_sco_indication_parameters) structure that contains the parameters associated with the notification event.

The value passed in the [*SCO callback function's*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnsco_indication_callback)*Indication* parameter specifies which union member in the **Parameters** union of the *Parameters* parameter that the profile driver should use.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">If the value of the <em>Indication</em> parameter equals...</th>
<th align="left">...use the following union member of the <em>Parameters</em> parameter</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>ScoIndicationRemoteConnect</strong></p></td>
<td align="left"><p><strong>Connect</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ScoIndicationRemoteDisconnect</strong></p></td>
<td align="left"><p><strong>Disconnect</strong></p></td>
</tr>
</tbody>
</table>

 

### <span id="handling_plug_and_play_removal_irps"></span><span id="HANDLING_PLUG_AND_PLAY_REMOVAL_IRPS"></span>Handling Plug and Play Removal IRPs

Profile drivers should pass all [**IRP\_MN\_SURPRISE\_REMOVAL**](../kernel/irp-mn-surprise-removal.md) IRPs down the stack immediately to be processed by the Bluetooth driver stack. Do not attempt to close any open channels as part of processing a surprise removal IRP. Do not build and send any further BRBs that send data to the underlying radio after receiving a surprise removal IRP. However, profile drivers can perform other cleanup while processing a surprise removal IRP.

After the Bluetooth driver stack receives the surprise removal IRP, it will pass *ScoIndicationRemoteDisconnect* to the [*SCO Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnsco_indication_callback) that was specified by the profile driver when the profile driver built and sent a [**BRB\_SCO\_OPEN\_CHANNEL**](/previous-versions/ff536626(v=vs.85)) or [**BRB\_SCO\_OPEN\_CHANNEL\_RESPONSE**](/previous-versions/ff536627(v=vs.85)) request, to close any SCO channels that are currently open. Likewise, the Bluetooth driver stack will pass *IndicationRemoteDisconnect* to the [*L2CAP Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbthport_indication_callback) that was specified by the profile driver when the profile driver built and sent a [**BRB\_L2CA\_OPEN\_CHANNEL**](/previous-versions/ff536615(v=vs.85)) or [**BRB\_L2CA\_OPEN\_CHANNEL\_RESPONSE**](/previous-versions/ff536616(v=vs.85)) request, to close any L2CAP channels that are currently open.

Profile drivers should unregister all servers when processing [**IRP\_MN\_REMOVE\_DEVICE**](../kernel/irp-mn-remove-device.md) IRPs. To unregister a SCO server, a profile driver should [build and send](building-and-sending-a-brb.md) a [**BRB\_SCO\_UNREGISTER\_SERVER**](/previous-versions/ff536630(v=vs.85)) request. To unregister an L2CAP server, a profile driver should build and send a [**BRB\_L2CA\_UNREGISTER\_SERVER**](/previous-versions/ff536619(v=vs.85)) request.

 

