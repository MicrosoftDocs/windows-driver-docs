---
title: Porting Protocol Driver Send and Receive Operations to CoNDIS 6.0
description: Porting Protocol Driver Send and Receive Operations to CoNDIS 6.0
ms.assetid: bfad982c-69a7-4bf0-beb9-6a5d2e65e770
keywords:
- porting protocol drivers WDK networking , send and receive operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Protocol Driver Send and Receive Operations to CoNDIS 6.0





Data transfer code paths in NDIS 6.0 have changed as follows:

-   The [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) and [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures replace the [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure.

-   Drivers can send and receive multiple packets in a single call without previously determining the number of packets. This is possible because the packets are provided in a linked list of NET\_BUFFER structures instead of an array of NDIS\_PACKET structures.

-   The completion status of a send operation is indicated in the **Status** member of the NET\_BUFFER\_LIST structure. This completion status is not returned as a function return value or a parameter of the [**ProtocolCoSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570257) function.

-   All send and receive operations are asynchronous.

For more information about NDIS 6.0 send and receive paths, see [NET\_BUFFER Architecture](net-buffer-architecture.md).

You can also learn more about porting send and receive operations in the following topics:

[Porting CoNDIS Protocol Driver Send Data Handling](porting-condis-protocol-driver-send-data-handling.md)

[Porting CoNDIS Protocol Driver Receive Data Handling](porting-condis-protocol-driver-receive-data-handling.md)

 

 





