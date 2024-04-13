---
title: Accepting SCO Connections in a Bluetooth Profile Driver
description: Accepting SCO connections in a Bluetooth profile driver
keywords:
- Synchronous Connection-Oriented WDK Bluetooth
- SCO profile drivers WDK Bluetooth
- incoming SCO connection requests WDK Bluetooth
- remote connection notifications WDK Bluetooth
ms.date: 01/10/2024
---

# Accepting SCO connections in a Bluetooth profile driver

A SCO profile driver can register itself to respond to incoming Synchronous Connection-Oriented (SCO) connection requests from remote devices. For example, a SCO profile driver for a cordless telephony profile (CTP) device responds to an incoming SCO connection request from the CTP device, either accepting or rejecting the request. If the server profile driver accepts the request, the server profile driver responds to input from the device and passes that input to the Bluetooth driver stack.

Server profile drivers must perform the following steps to accept incoming SCO connection requests from remote Bluetooth devices.

## To receive incoming SCO connection requests from remote devices

1. Profile drivers should [build and send](building-and-sending-a-brb.md) a [**BRB\_SCO\_REGISTER\_SERVER**](/previous-versions/ff536628(v=vs.85)) request to register a [*SCO Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnsco_indication_callback) with the Bluetooth driver stack so the stack can notify the profile driver of incoming SCO connection requests.

1. When the Bluetooth driver stack receives an incoming SCO connection request from a remote device, it calls the [*SCO Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnsco_indication_callback) registered earlier by the profile driver. The Bluetooth driver stack passes the value **ScoIndicationRemoteConnect** to the *Indication* parameter of the callback function.

1. To respond to incoming connection requests, profile drivers should build and send a [**BRB\_SCO\_OPEN\_CHANNEL\_RESPONSE**](/previous-versions/ff536627(v=vs.85)) request. Based on the value of the **Response** member of the [**\_BRB\_SCO\_OPEN\_CHANNEL**](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_sco_open_channel) structure passed with this request, the server profile driver accepts or rejects the connection request.

1. If the server profile driver accepts the connection, the Bluetooth driver stack can then call the [*SCO Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnsco_indication_callback) as specified in the **Callback** member of the [**\_BRB\_SCO\_OPEN\_CHANNEL**](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_sco_open_channel) structure to notify the server profile driver of any changes to the SCO connection.

After the profile driver accepts a connection request, it can use other BRBs to send and receive data over the newly established SCO connection.

To stop receiving notifications of remote device SCO connection attempts, profile drivers should [build and send](building-and-sending-a-brb.md) a [**BRB\_SCO\_UNREGISTER\_SERVER**](/previous-versions/ff536630(v=vs.85)) request to unregister a server when the profile driver processes [**IRP\_MN\_REMOVE\_DEVICE**](../kernel/irp-mn-remove-device.md) Plug and Play remove notifications.

For more information about notifications and callback functions, see [Supporting Bluetooth Event Notifications](supporting-bluetooth-event-notifications.md).
