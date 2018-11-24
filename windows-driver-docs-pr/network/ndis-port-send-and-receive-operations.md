---
title: NDIS Port Send and Receive Operations
description: NDIS Port Send and Receive Operations
ms.assetid: f9a22b7b-5565-4d56-a9b9-22562b6bf0da
keywords:
- ports WDK NDIS , send and receive operations
- NDIS ports WDK , send and receive operations
- send operations WDK NDIS ports
- receive operations WDK NDIS ports
- target ports WDK NDIS
- source ports WDK NDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Port Send and Receive Operations





NDIS drivers can associate send and receive operations with NDIS ports.The port number in the *PortNumber* parameter of the NDIS send and receive functions identifies the target port of a send operation or the source port of a receive indication. If *PortNumber* is zero, the default port is used. When NDIS handles the default port and the miniport driver does not allocate any other ports, no NDIS drivers in the driver stack are required to do anything beyond always setting the *PortNumber* parameter to zero. For more information about allocating ports in a miniport driver, see [Allocating NDIS Ports](allocating-an-ndis-port.md).

If the miniport driver allocates ports, overlying drivers can use the ports to send and receive data on the appropriate subinterfaces of the associated miniport adapter. However, the overlying driver must ensure that the ports are active before sending any data. Miniport drivers activate ports when the associated subinterfaces become available. For more information about activating a port in a miniport driver, see [Activating NDIS Ports](activating-an-ndis-port.md).

When NDIS calls the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function of a protocol driver, NDIS provides a list of all currently active ports in the **ActivePorts** member of the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure that the *BindParameters* parameter points to. NDIS also informs protocol drivers with a PnP event when ports are activated and deactivated. For more information about PnP port activation and deactivation notifications, see [Handling NDIS Ports PnP Notifications](handling-ndis-ports-pnp-event-notifications.md). For more general information about send and receive operations, see [Send and Receive Operations](send-and-receive-operations.md).

 

 





