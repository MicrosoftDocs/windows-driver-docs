---
title: Porting NDIS Miniport Driver Send Data Handling
description: Porting NDIS Miniport Driver Send Data Handling
ms.assetid: 0179ca24-f736-4937-b8ab-42e364d2c63b
keywords:
- send operation porting WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting NDIS Miniport Driver Send Data Handling





The [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function replaces the [**MiniportSendPackets**](https://msdn.microsoft.com/library/windows/hardware/ff550524) function. *MiniportSendNetBufferLists* receives a pointer to a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures, each of which contains a linked list of [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures. *MiniportSendNetBufferLists* does not return a completion status. A miniport driver should therefore always complete a send operation asynchronously by calling the [**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668) function.

NDIS 5.*x* miniport drivers specify the completion status of a send operation as a parameter to the [**NdisMSendComplete**](https://msdn.microsoft.com/library/windows/hardware/ff553613) function. NDIS 6.0 miniport drivers, however, specify the completion status in the NET\_BUFFER\_LIST structure by calling the [**NET\_BUFFER\_LIST\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff568411) macro, as in the following example:

```C++
NET_BUFFER_LIST_STATUS(pNetBufferList) = NDIS_STATUS_SUCCESS
```

The completion status applies to all the NET\_BUFFER structures associated with the NET\_BUFFER\_LIST structure. Therefore, a miniport driver should set the completion status to NDIS\_STATUS\_SUCCESS only if the data in all the NET\_BUFFER structures associated with the NET\_BUFFER\_LIST structure was transmitted successfully.

If a miniport driver uses scatter gather DMA, it must call the [**NdisMAllocateNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff562776) function once for each NET\_BUFFER structure for which it must obtain a scatter gather DMA list. For more information about scatter gather DMA, see [Porting Miniport Driver DMA Operations to NDIS 6.0](porting-miniport-driver-dma-operations-to-ndis-6-0.md).

For more information about miniport driver send handling, see [Sending Data from a Miniport Driver](sending-data-from-a-miniport-driver.md).

 

 





