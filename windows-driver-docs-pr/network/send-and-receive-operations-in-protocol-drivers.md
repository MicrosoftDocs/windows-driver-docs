---
title: Send and Receive Operations in Protocol Drivers
description: Send and Receive Operations in Protocol Drivers
keywords:
- protocol drivers WDK networking , receive operations
- NDIS protocol drivers WDK , receive operations
- protocol drivers WDK networking , send operations
- NDIS protocol drivers WDK , send operations
- send operations WDK NDIS protocol
- receive operations WDK NDIS protocol
ms.date: 04/20/2017
---

# Send and Receive Operations in Protocol Drivers





There are two different interfaces for send and receive operations in NDIS protocol drivers. Protocol drivers with a connectionless lower edge call the [**NdisSendNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissendnetbufferlists) function to send network data. A connectionless protocol driver must supply a [**ProtocolReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_receive_net_buffer_lists) function. NDIS calls *ProtocolReceiveNetBufferLists* when an underlying connectionless miniport driver calls the [**NdisMIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatereceivenetbufferlists) function to indicate received network data. For more information about sending and receiving data in connectionless protocol drivers, see [Protocol Driver Send and Receive Operations](protocol-driver-send-and-receive-operations.md).

Connection-oriented NDIS (CoNDIS) protocol drivers call the [**NdisCoSendNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscosendnetbufferlists) function to send network data. A CoNDIS protocol driver must supply a [**ProtocolCoReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_receive_net_buffer_lists) function. NDIS calls *ProtocolCoReceiveNetBufferLists* when an underlying CoNDIS miniport driver calls the [**NdisMCoIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcoindicatereceivenetbufferlists) function to indicate received network data. For more information about send and operations in connection-oriented protocol drivers, see [Connection-Oriented Operations](connection-oriented-operations-performed-by-clients.md).

For an introduction to send and receive operations, see [Send and Receive Operations](send-and-receive-operations.md).

 

