---
title: Porting CoNDIS Protocol Driver Send Data Handling
description: Porting CoNDIS Protocol Driver Send Data Handling
ms.assetid: 67f5a530-1971-4c77-ae54-8f6468dfa49f
keywords:
- porting protocol drivers WDK networking , send and receive operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting CoNDIS Protocol Driver Send Data Handling





In CoNDIS 6.0, the [**NdisCoSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561728) function replaces the CoNDIS 5.x [**NdisCoSendPackets**](https://msdn.microsoft.com/library/windows/hardware/ff551890) function. **NdisCoSendNetBufferLists** sends a pointer to a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures, each of which contains a linked list of [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures. **NdisCoSendNetBufferLists** does not return a completion status. In CoNDIS 6.0, NDIS always completes a send operation asynchronously by calling the [**ProtocolCoSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570257) function.

CoNDIS 5.x miniport drivers specify the completion status of a send operation as a parameter to the [**NdisMCoSendComplete**](https://msdn.microsoft.com/library/windows/hardware/ff553475) function. CoNDIS 6.0 miniport drivers, however, specify the completion status in the NET\_BUFFER\_LIST structure's **Status** member: The completion status applies to all of the NET\_BUFFER structures that are associated with the NET\_BUFFER\_LIST structure.

NDIS 6.0 does not provide loopback of send data by default. NDIS 6.0 protocol drivers must explicitly request for NDIS to check [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures for required loopback. To request loopback, set the NDIS\_SEND\_FLAGS\_CHECK\_FOR\_LOOPBACK flag in the *SendFlags* parameter of the [**NdisCoSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561728) function.

CoNDIS 6.0 protocol drivers can cancel send operations. For more information about canceling send operations, see [Canceling a Send Operation](canceling-a-send-operation.md). For an overview of send operations, see [Sending Network Data](sending-network-data.md). For more information about CoNDIS protocol driver send operations, see [Sending NET\_BUFFER Structures from CoNDIS Drivers](sending-net-buffer-structures-from-condis-drivers.md).

 

 





