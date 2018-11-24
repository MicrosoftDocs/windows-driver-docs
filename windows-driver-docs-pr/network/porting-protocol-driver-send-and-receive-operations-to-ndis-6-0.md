---
title: Porting Protocol Driver Send and Receive Operations to NDIS 6.0
description: Porting Protocol Driver Send and Receive Operations to NDIS 6.0
ms.assetid: 22cb4ab3-fdd1-4d8c-a0e1-375afe476781
keywords:
- porting protocol drivers WDK networking , send and receive operations
- send operation porting WDK networking
- receive operation porting WDK networking
- data send/receive operation porting WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Protocol Driver Send and Receive Operations to NDIS 6.0





Data transfer code paths in NDIS 6.0 have changed as follows:

-   The [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) and [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures replace the [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure.

-   Drivers can send and receive multiple packets in a single call without determining the number of packets beforehand. This is true because the packets are provided in a linked list of NET\_BUFFER structures instead of an array of NDIS\_PACKET structures.

-   The completion status of a send or receive operation is indicated in the **Status** member of the NET\_BUFFER\_LIST structure. This completion status is not returned as a function return code or a parameter of the [**ProtocolSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570268) function.

-   The TCP/IP stack that is included in Windows Vista guarantees that all NET\_BUFFER structures in a NET\_BUFFER\_LIST structure are targeted for the same MAC address, IP address, and TCP port. Intermediate drivers are required to provide the same behavior for TCP/IP data sent to underlying drivers.

-   All send and receive operations are asynchronous.

For more information about NDIS 6.0 send and receive paths, see [NET\_BUFFER Architecture](net-buffer-architecture.md).

Additional information about porting send and receive operations is included in the following topics:

[Allocating Network Data Pools in an NDIS 6.0 Protocol Driver](allocating-network-data-pools-in-an-ndis-6-0-protocol-driver.md)

[Porting NDIS Protocol Driver Send Data Handling](porting-ndis-protocol-driver-send-data-handling.md)

[Porting NDIS Protocol Driver Receive Data Handling](porting-ndis-protocol-driver-receive-data-handling.md)

 

 





