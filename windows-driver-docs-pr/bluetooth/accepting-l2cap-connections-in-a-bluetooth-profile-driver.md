---
title: Accepting L2CAP Connections in a Bluetooth Profile Driver
description: Accepting L2CAP connections in a Bluetooth profile driver
keywords:
- L2CAP profile drivers WDK Bluetooth
- Logical Link Controller and Adaptation Protocol WDK Bluetooth
- incoming L2CAP connection requests WDK Bluetooth
- connections WDK Bluetooth
- remote connection notifications WDK Bluetooth
- notifications WDK Bluetooth
ms.date: 01/10/2024
---

# Accepting L2CAP connections in a Bluetooth profile driver

An L2CAP server profile driver responds to incoming Logical Link Control and Adaptation Protocol (L2CAP) connection requests from remote devices. For example, an L2CAP server profile driver for a PDA would respond to an incoming connection request from the PDA.

## To receive incoming L2CAP connection requests

1. **To receive incoming L2CAP connection requests from*any*remote device for a particular PSM**, profile drivers should first [build and send](building-and-sending-a-brb.md) a [**BRB\_L2CA\_REGISTER\_SERVER**](/previous-versions/ff536618(v=vs.85)) request, specifying **NULL** in the **BtAddress** member and 0 in the **Psm** member of the request's \_BRB\_L2CA\_REGISTER\_SERVER structure. Profile drivers must also register an [*L2CAP Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbthport_indication_callback) with the Bluetooth driver stack when sending the **BRB\_L2CA\_REGISTER\_SERVER** request. This enables the Bluetooth driver stack to notify the profile driver of incoming L2CAP connection requests.

    Then, profile drivers should [build and send](building-and-sending-a-brb.md) a [**BRB\_REGISTER\_PSM**](/previous-versions/ff536621(v=vs.85)) request so the Bluetooth driver stack will accept connections from the PSM registered by the request. Otherwise, the Bluetooth driver stack rejects all connection requests that have unknown (unregistered) connection requests. For more information about PSMs, see the [**\_BRB\_PSM**](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_psm) structure.

1. **To receive incoming L2CAP connection requests from a*specific*remote device/PSM pair**, profile drivers should [build and send](building-and-sending-a-brb.md) a [**BRB\_L2CA\_REGISTER\_SERVER**](/previous-versions/ff536618(v=vs.85)) request, specifying the remote device's address in the **BtAddress** member, and PSM in the **Psm** member, of the request's accompanying \_BRB\_L2CA\_REGISTER\_SERVER structure. Profile drivers must also register an [*L2CAP Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbthport_indication_callback) with the Bluetooth driver stack when sending the **BRB\_L2CA\_REGISTER\_SERVER** request. This enables the Bluetooth driver stack to notify the profile driver of incoming L2CAP connection requests.

1. The profile driver should issue an [**IOCTL\_BTH\_SDP\_SUBMIT\_RECORD**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_bth_sdp_submit_record). The profile driver can then register an SDP record that describes the service that the profile driver supports, so that remote systems can discover the new service by using SDP.

1. When the Bluetooth driver stack receives an incoming L2CAP connection request from a remote device, the Bluetooth driver stack calls the [*L2CAP Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbthport_indication_callback) registered earlier by the profile driver. The Bluetooth driver stack passes the value **IndicationRemoteConnect** to the *Indication* parameter of the callback function.

1. To respond to incoming connection requests, profile drivers should [build and send](building-and-sending-a-brb.md) a [**BRB\_L2CA\_OPEN\_CHANNEL\_RESPONSE**](/previous-versions/ff536616(v=vs.85)) request. The server profile driver uses the value passed from the Bluetooth driver stack in the *Parameters* parameter of the callback function to negotiate the connection settings with the remote device. Based on the value of the **Response** member of the [**\_BRB\_L2CA\_OPEN\_CHANNEL**](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_l2ca_open_channel) structure passed with this request, the server profile driver accepts or rejects the connection request.

1. If the server profile driver accepts the connection, the Bluetooth driver stack can then call the [*L2CAP Callback Function*](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbthport_indication_callback) as specified in the **Callback** member of the [**\_BRB\_L2CA\_OPEN\_CHANNEL**](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_l2ca_open_channel) structure. The Bluetooth driver stack uses this function to notify the server profile driver of any changes to the L2CAP connection.

> [!NOTE]
>
> - A single profile driver can register to receive incoming L2CAP connection requests from multiple, different remote device/PSM pairs by building and sending multiple **BRB\_L2CA\_REGISTER\_SERVER** requests to register multiple L2CAP servers, specifying unique remote device address and PSM pairs in the **BtAddress** and **Psm** members of the requests.
> - A single profile driver can register to receive incoming L2CAP connection requests from *any* remote device for a particular PSM, as well as receive incoming L2CAP connection requests from multiple, different remote device/PSM pairs, by first registering to receive incoming L2CAP connection requests from any remote device for a particular PSM, and then registering to receive incoming L2CAP connection requests from a specific remote device/PSM pair as long as the particular PSM registered in the first step is not registered again.
> - Multiple profile drivers cannot register to receive incoming L2CAP connection requests from any remote device for the same PSM. The Bluetooth driver stack only permits one profile driver to receive incoming L2CAP connection requests from any remote device for a particular PSM.

After the profile driver accepts a connection request, it can use other BRBs to send and receive data over the newly established L2CAP connection.

To stop receiving notifications of remote device L2CAP connection attempts, profile drivers should [build and send](building-and-sending-a-brb.md) a [**BRB\_L2CA\_UNREGISTER\_SERVER**](/previous-versions/ff536619(v=vs.85)) request to unregister a server when the profile driver processes [**IRP\_MN\_REMOVE\_DEVICE**](../kernel/irp-mn-remove-device.md) Plug and Play remove notifications.

For more information about notifications and callback functions, see [Supporting Bluetooth Event Notifications](supporting-bluetooth-event-notifications.md).
