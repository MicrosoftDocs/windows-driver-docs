---
title: Send and Receive Operations in Protocol Drivers
description: Send and Receive Operations in Protocol Drivers
ms.assetid: 4759725b-ed0b-4345-9cdc-9411ee29ebdb
keywords:
- protocol drivers WDK networking , receive operations
- NDIS protocol drivers WDK , receive operations
- protocol drivers WDK networking , send operations
- NDIS protocol drivers WDK , send operations
- send operations WDK NDIS protocol
- receive operations WDK NDIS protocol
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Send and Receive Operations in Protocol Drivers





There are two different interfaces for send and receive operations in NDIS protocol drivers. Protocol drivers with a connectionless lower edge call the [**NdisSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564535) function to send network data. A connectionless protocol driver must supply a [**ProtocolReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff570267) function. NDIS calls *ProtocolReceiveNetBufferLists* when an underlying connectionless miniport driver calls the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function to indicate received network data. For more information about sending and receiving data in connectionless protocol drivers, see [Protocol Driver Send and Receive Operations](protocol-driver-send-and-receive-operations.md).

Connection-oriented NDIS (CoNDIS) protocol drivers call the [**NdisCoSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561728) function to send network data. A CoNDIS protocol driver must supply a [**ProtocolCoReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff570256) function. NDIS calls *ProtocolCoReceiveNetBufferLists* when an underlying CoNDIS miniport driver calls the [**NdisMCoIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563561) function to indicate received network data. For more information about send and operations in connection-oriented protocol drivers, see [Connection-Oriented Operations](connection-oriented-operations.md).

For an introduction to send and receive operations, see [Send and Receive Operations](send-and-receive-operations.md).

 

 





