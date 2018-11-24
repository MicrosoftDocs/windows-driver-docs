---
title: Send and Receive Operations
description: Send and Receive Operations
ms.assetid: 216bfed2-92f8-4480-95fc-9909d7c1f533
keywords:
- network data WDK , sending
- network data WDK , receiving
- data WDK networking , sending
- data WDK networking , receiving
- sending data WDK networking
- receiving data WDK networking
- NET_BUFFER_LIST
- multiple NET_BUFFER_LIST structures WDK networki
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Send and Receive Operations





In a single function call, NDIS 6.0 drivers can send multiple [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures with multiple [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures on each NET\_BUFFER\_LIST structure. Also, NDIS drivers can indicate completed send operations for multiple NET\_BUFFER\_LIST structures with multiple NET\_BUFFER structures on a NET\_BUFFER\_LIST structure.

In the receive path, miniport drivers can use a list of NET\_BUFFER\_LIST structures to indicate receives. Each NET\_BUFFER\_LIST indicated by a miniport driver contains one NET\_BUFFER structure. However, Native 802.11 drivers can have more than one NET\_BUFFER structure. Because a different protocol binding can process each NET\_BUFFER\_LIST structure, NDIS can return each NET\_BUFFER\_LIST structure to the miniport driver independently.

To support NDIS 5.*x* and earlier drivers, NDIS provides a translation layer between the [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086)-based and NET\_BUFFER-based interfaces. NDIS performs the necessary conversion between [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures and NDIS\_PACKET structures. To avoid performance degradation due to translation, NDIS drivers must be updated to use NET\_BUFFER structures and should support multiple [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures in all data paths.

This section includes the following topics:

[Sending Network Data](sending-network-data.md)

[Canceling a Send Operation](canceling-a-send-operation.md)

[Receiving Network Data](receiving-network-data.md)

[Looping Back NDIS Packets](looping-back-ndis-packets.md)

 

 





