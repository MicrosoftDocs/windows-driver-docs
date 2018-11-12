---
title: Asynchronous I/O and Completion Functions in Network Drivers
description: Asynchronous I/O and Completion Functions in Network Drivers
ms.assetid: fbb940d8-41ad-4f66-998b-f5dc829b54cc
keywords:
- network drivers WDK , asynchronous operations
- asynchronous I/O WDK networking
- completion function WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Asynchronous I/O and Completion Functions in Network Drivers





Latency is inherent in some network operations. Because of this latency, many of the upper-edge functions provided by a miniport driver and the lower-edge functions of a protocol driver are designed to support asynchronous operation. Rather than wasting CPU cycles waiting in a loop for some time-consuming task to finish or a hardware event to signal, network drivers rely on the ability to handle most operations asynchronously.

Asynchronous network I/O is supported by using a *completion* function. The following example illustrates using a completion function for a network *send* operation, but this same mechanism exists for many other operations that are performed by a protocol or miniport driver.

When a protocol driver calls NDIS to send a packet, resulting in a call to the miniport driver's [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function, the miniport driver can try to complete this request immediately and return an appropriate status value as a result. For synchronous operation, the possible responses are NDIS\_STATUS\_SUCCESS for successful completion of the send, NDIS\_STATUS\_RESOURCES, and NDIS\_STATUS\_FAILURE indicating a failure of some kind.

But a send operation can take some time to complete while the miniport driver (or NDIS) queues the packet and waits for the NIC to indicate the result of the send operation. The miniport driver *MiniportSendNetBufferLists* function can handle this operation asynchronously by returning a status value of NDIS\_STATUS\_PENDING. When the miniport driver completes the send operation, it calls the completion function, [**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668), passing a pointer to the packet descriptor that was sent. This information is passed to the protocol driver, signaling completion.

Most driver operations that can require an extended time to complete support asynchronous operation with a similar completion function. Such functions have names of the form **NdisM*Xxx*Complete**.

Completion functions are also provided to:

-   Set and querying configuration.

-   Reset hardware.

-   Indicate status.

-   Indicate received data.

-   Transfer received data.

 

 





