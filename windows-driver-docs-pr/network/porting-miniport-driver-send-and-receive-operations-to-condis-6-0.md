---
title: Porting Miniport Driver Send and Receive Operations to CoNDIS 6.0
description: Porting Miniport Driver Send and Receive Operations to CoNDIS 6.0
ms.assetid: 2b1f7f31-2693-4ab5-bd30-b8a45dceb338
keywords:
- porting miniport drivers WDK networking , send and receive operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Driver Send and Receive Operations to CoNDIS 6.0





Data transfer code paths in NDIS 6.0 have changed as follows:

-   The [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures and [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures replace the [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure.

-   Drivers can send and receive multiple packets in a single call without previously determining the number of packets. This is possible because the packets are provided in a linked list of [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures instead of an array of [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures.

-   The completion status of a send operation is indicated in the **Status** member of the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure. This completion status is not returned as a function return value or a parameter of the [**NdisMCoSendComplete**](https://msdn.microsoft.com/library/windows/hardware/ff553475) function.

For more information about changes to send and receive paths, see [NET\_BUFFER Architecture](net-buffer-architecture.md).

You can also learn more about porting CoNDIS send and receive operations in the following topics:

[Porting CoNDIS Miniport Driver Send Data Handling](porting-condis-miniport-driver-send-data-handling.md)

[Porting CoNDIS Miniport Driver Receive Data Handling](porting-condis-miniport-driver-receive-data-handling.md)

 

 





