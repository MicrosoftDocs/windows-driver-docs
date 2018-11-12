---
title: Porting CoNDIS Miniport Driver Send Data Handling
description: Porting CoNDIS Miniport Driver Send Data Handling
ms.assetid: 1d0f792f-0b84-4172-9876-8ed37fc7a9f7
keywords:
- porting miniport drivers WDK networking , send and receive operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting CoNDIS Miniport Driver Send Data Handling





In NDIS 6.0, the [**MiniportCoSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff559365) function replaces the NDIS 5.x [*MiniportCoSendPackets*](https://msdn.microsoft.com/library/windows/hardware/ff549426) function. *MiniportCoSendNetBufferLists* receives a pointer to a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures, each of which contains a linked list of [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures. *MiniportCoSendNetBufferLists* does not return a completion status, so a miniport driver should always complete a send operation asynchronously by calling the [**NdisMCoSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668) function.

CoNDIS 5.x miniport drivers specify the completion status of a send operation as a parameter for the [**NdisMCoSendComplete**](https://msdn.microsoft.com/library/windows/hardware/ff553475) function. CoNDIS 6.0 miniport drivers, however, specify the completion status in the NET\_BUFFER\_LIST structure by calling the [**NET\_BUFFER\_LIST\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff568411) macro, as the following example shows:

```C++
NET_BUFFER_LIST_STATUS(pNetBufferList) = NDIS_STATUS_SUCCESS
```

The completion status applies to all of the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures that are associated with the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. Therefore, a miniport driver should set the completion status to NDIS\_STATUS\_SUCCESS only if the data in all of the NET\_BUFFER structures that are associated with the NET\_BUFFER\_LIST structure was transmitted successfully.

If a miniport driver uses scatter/gather direct memory access (SGDMA), the driver must call the [**NdisMAllocateNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff562776) function once for each NET\_BUFFER structure for which it must obtain a scatter/gather DMA list. For more information about SGDMA, see [Porting Miniport Driver DMA Operations to NDIS 6.0](porting-miniport-driver-dma-operations-to-ndis-6-0.md).

For more information about how CoNDIS miniport drivers handle send data, see [Sending NET\_BUFFER Structures from CoNDIS Drivers](sending-net-buffer-structures-from-condis-drivers.md).

 

 





