---
title: Porting Send and Receive Operations to CoNDIS 6.0
description: Porting Send and Receive Operations to CoNDIS 6.0
ms.assetid: 63cfdaac-fd38-46b9-ac6a-7aec93709eb1
keywords:
- CoNDIS drivers WDK networking , send and receive operations
- connection-oriented drivers WDK networking , send and receive operations
- porting CoNDIS drivers WDK networking , send and receive operations
- send operation porting WDK networking
- receive
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Send and Receive Operations to CoNDIS 6.0





The CoNDIS send and receive functions are similar to the connectionless send and receive functions. The primary difference between the CoNDIS and connectionless interfaces is how they manage virtual connections (VCs). For more information about connectionless send and receive operations, see [Send and Receive Operations](send-and-receive-operations.md).

In a single function call, CoNDIS 6.0 drivers can send multiple [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures with multiple [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures on each NET\_BUFFER\_LIST structure. In addition, CoNDIS drivers can indicate completed send operations for multiple NET\_BUFFER\_LIST structures with multiple NET\_BUFFER structures on each NET\_BUFFER\_LIST structure.

In the receive path, CoNDIS miniport drivers can provide a list of NET\_BUFFER\_LIST structures to indicate receives. Each NET\_BUFFER\_LIST that a miniport driver provides contains one NET\_BUFFER structure. Because a different protocol binding can process each NET\_BUFFER\_LIST structure, NDIS can independently return each NET\_BUFFER\_LIST structure to the miniport driver.

To support NDIS 5.x and earlier drivers, NDIS provides a translation layer between the earlier [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures and the NET\_BUFFER-based structures. NDIS performs the necessary conversion between [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures and NDIS\_PACKET structures. To avoid degrading performance because of translation, CoNDIS drivers must be updated to support NET\_BUFFER structures and should support multiple [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures in all data paths.

This section includes the following topics:

[Porting Miniport Driver Send and Receive Operations to CoNDIS 6.0](porting-miniport-driver-send-and-receive-operations-to-condis-6-0.md)

[Porting Protocol Driver Send and Receive Operations to CoNDIS 6.0](porting-protocol-driver-send-and-receive-operations-to-condis-6-0.md)

 

 





