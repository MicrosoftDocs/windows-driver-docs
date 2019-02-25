---
title: Indicating Received Data from a CoNDIS WAN Miniport Driver
description: Indicating Received Data from a CoNDIS WAN Miniport Driver
ms.assetid: d49ea741-df5c-4b65-b899-a751cb2b9929
keywords:
- CoNDIS WAN drivers WDK networking , receiving data
- receiving data WDK networking
- indications WDK CoNDIS WAN
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating Received Data from a CoNDIS WAN Miniport Driver





The following operations occur when a CoNDIS WAN miniport driver receives a network data packet:

1.  The driver removes driver-specific encapsulation from the network data packet, if necessary before calling [**NdisMCoIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563561) to indicate the received data in a NET\_BUFFER\_LIST structure. For example, the driver can remove PPPoE encapsulation. However, the miniport driver should leave encapsulated data, such as PPP header and payload, intact.

2.  The driver calls the **NdisMCoIndicateReceiveNetBufferLists** function to indicate to NDISWAN that a packet has arrived.

3.  NDISWAN processes the packet and calls [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) to indicate the arrival of the packet.

4.  To forward the packet, NDIS calls the [**ProtocolReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff570267) function of bound overlying protocol drivers.

 

 





