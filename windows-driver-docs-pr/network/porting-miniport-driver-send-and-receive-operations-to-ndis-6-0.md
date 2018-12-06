---
title: Porting Miniport Driver Send and Receive Operations to NDIS 6.0
description: Porting Miniport Driver Send and Receive Operations to NDIS 6.0
ms.assetid: 9c50b01e-600a-48ac-ba1b-88156c3b235a
keywords:
- porting miniport drivers WDK networking , send and receive operations
- send operation porting WDK networking
- receive operation porting WDK networking
- data send/receive operation porting WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Driver Send and Receive Operations to NDIS 6.0





Data transfer code paths in NDIS 6.0 have changed as follows:

-   All NDIS 6.0 miniport drivers are deserialized.

-   The [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures and [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures replace the [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure.

-   Drivers can send and receive multiple packets in a single call without determining the number of packets beforehand. This is because the packets are provided in a linked list of NET\_BUFFER structures instead of an array of NDIS\_PACKET structures.

-   The completion status of a send or receive operation is indicated in the **Status** member of the NET\_BUFFER\_LIST structure. This completion status is not returned as a function return code or a parameter of the [**NdisMSendComplete**](https://msdn.microsoft.com/library/windows/hardware/ff553613) function.

For more information about these changes, see [NET\_BUFFER Architecture](net-buffer-architecture.md).

Additional information about porting send and receive operations is included in the following topics:

[Allocating Network Data Pools in an NDIS 6.0 Miniport Driver](allocating-network-data-pools-in-an-ndis-6-0-miniport-driver.md)

[Porting NDIS Miniport Driver Send Data Handling](porting-ndis-miniport-driver-send-data-handling.md)

[Porting NDIS Miniport Driver Receive Data Handling](porting-ndis-miniport-driver-receive-data-handling.md)

 

 





