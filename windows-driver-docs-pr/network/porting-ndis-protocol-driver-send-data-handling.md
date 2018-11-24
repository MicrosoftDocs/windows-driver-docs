---
title: Porting NDIS Protocol Driver Send Data Handling
description: Porting NDIS Protocol Driver Send Data Handling
ms.assetid: 0d0a071d-5d4c-46c1-8b4f-b8bff9e3d465
keywords:
- send operation porting WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting NDIS Protocol Driver Send Data Handling





In NDIS 6.0. the [**NdisSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564535) function replaces the [**NdisSendPackets**](https://msdn.microsoft.com/library/windows/hardware/ff554715) function. **NdisSendNetBufferLists** sends a pointer to a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures, each of which contains a linked list of [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures. **NdisSendNetBufferLists** does not return a completion status. NDIS always completes a send operation asynchronously by calling the [**ProtocolSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570268) function.

NDIS 5.*x* miniport drivers specify the completion status of a send operation as a parameter to the [**NdisMSendComplete**](https://msdn.microsoft.com/library/windows/hardware/ff553613) function. NDIS 6.0 miniport drivers, however, specify the completion status in the NET\_BUFFER\_LIST structure's **Status** member: The completion status applies to all the NET\_BUFFER structures associated with the NET\_BUFFER\_LIST structure.

NDIS 6.0 does not provide loopback of send data by default. NDIS 6.0 protocol driver must explicitly request NDIS to check NET\_BUFFER structures for required loopback.

NDIS 6.0 protocol drivers can cancel send operations. For more information about canceling send operations, see [Canceling a Send Operation](canceling-a-send-operation.md). For an overview of send operations, see [Sending Network Data](sending-network-data.md). For more information about protocol driver send operations, see [Sending Data from a Protocol Driver](sending-data-from-a-protocol-driver.md).

 

 





