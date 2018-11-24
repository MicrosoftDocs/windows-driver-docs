---
title: Protocol Driver Send and Receive Operations
description: Protocol Driver Send and Receive Operations
ms.assetid: c621d673-167e-41e1-a121-68e0d0bc6f8a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Protocol Driver Send and Receive Operations





Protocol drivers originate send requests and handle the receive indications of underlying drivers. In a single function call, NDIS protocol drivers can send multiple [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures with multiple [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures on each NET\_BUFFER\_LIST structure. In the receive path, protocol drivers can receive a list of NET\_BUFFER\_LIST structures.

Protocol drivers must manage send buffer pools. Proper management of such pools requires preallocation of sufficient buffer space to optimize system performance.

The following topics provide more information about protocol driver buffer management, send operations, and receive operations:

[Protocol Driver Buffer Management](protocol-driver-buffer-management.md)

[Sending Data from a Protocol Driver](sending-data-from-a-protocol-driver.md)

[Receiving Data in Protocol Drivers](receiving-data-in-protocol-drivers.md)

 

 





