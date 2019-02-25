---
title: Creating a L2CAP Client Connection to a Remote Device
description: Creating a L2CAP Client Connection to a Remote Device
ms.assetid: b279db4b-3a4e-407e-ae9b-7330af1905b4
keywords:
- SDP WDK Bluetooth
- Service Discovery Protocol WDK Bluetooth
- Asynchronous Connection-Less WDK Bluetooth
- ACL WDK Bluetooth
- L2CAP profile drivers WDK Bluetooth
- Logical Link Controller and Adaptation Protocol WDK Bluetooth
- connections WDK Bluetooth
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a L2CAP Client Connection to a Remote Device


An L2CAP client profile driver is a profile driver that requests an Asynchronous Connectionless Link (ACL) connection to a remote device. If the device accepts the connection, the L2CAP client profile driver is notified of any changes to the connection. For example, a L2CAP client profile driver can request a connection to a remote printer, and after the printer accepts the request, the Bluetooth driver stack can notify the profile driver when the printer is turned off or removed.

The L2CAP client profile driver must have information about the remote device, such as the protocol/service multiplexer (PSM) that the device uses, in order to request a connection to the device. The client profile driver can obtain this information through the Service Discovery Protocol (SDP) DDIs, or through a service's fixed PSM. For more information about how to obtain this information, see [Accessing SDP Service Information](accessing-sdp-service-information.md).

To initiate a L2CAP connection to a remote device, after the client profile driver has the required information about the device, it should [build and send](building-and-sending-a-brb.md) a [**BRB\_L2CA\_OPEN\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff536615) request.

When the client profile driver builds the request, it supplies a pointer to a [**\_BRB\_L2CA\_OPEN\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff536860) structure in the **Parameters.Others.Argument1** member of the IRP associated with the request. This structure contains the Bluetooth address for the remote device, the PSM registered for the device, and additional configuration parameters.

If the remote device accepts the open channel request, the **OutResults** and **InResults** members of the \_BRB\_L2CA\_OPEN\_CHANNEL structure contain information about the newly created connection. The **OutResults** member specifies the parameters for the outbound half of the channel and the **InResults** member specifies the parameters for the inbound half of the channel.

Several of the configuration values passed in the \_BRB\_L2CA\_OPEN\_CHANNEL structure, such as the **Mtu** member, are used to negotiate the connection with the remote device. Client profile drivers should provide as wide a range as possible to increase the chances of successful channel negotiation. Specifying a minimum message transfer units (MTU) size greater than the basic Bluetooth minimum MTU size should only be done when absolutely necessary. If negotiation fails, the connection will fail.

The **IncomingQueueDepth** member of the \_BRB\_L2CA\_OPEN\_CHANNEL structure specifies the maximum number of MTUs that the Bluetooth driver stack will receive and queue on the connection before the Bluetooth driver stack begins to discard them. Setting this value to a very small number increases the chances of data loss, while setting it to a very large number increases memory requirements. Microsoft recommends setting this member to 10.

When the profile driver no longer requires the L2CAP connection to the remote device, it should [build and send](building-and-sending-a-brb.md) a [**BRB\_L2CA\_CLOSE\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff536614) request.

 

 





