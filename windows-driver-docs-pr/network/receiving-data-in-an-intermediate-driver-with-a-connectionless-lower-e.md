---
title: Connectionless lower edge intermediate driver data reception
description: Receiving Data in an Intermediate Driver with a Connectionless Lower Edge
ms.assetid: 73143c2f-4127-41fc-b916-eac87521440a
keywords:
- intermediate drivers WDK networking , receive operations
- NDIS intermediate drivers WDK , receive operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving Data in an Intermediate Driver with a Connectionless Lower Edge





An intermediate driver with a connectionless lower edge must have a [**ProtocolReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff570267) function to receive network data.

Underlying connectionless miniport drivers call the **NdisMIndicateReceiveNetBufferLists**, passing a linked list of one or more [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures, relinquishing ownership of the indicated structures to higher level drivers. When the higher level drivers have consumed the data, they return the NET\_BUFFER\_LIST structures (and the resources they specify) to the miniport driver.

For more information about receiving data in an intermediate driver with a connectionless lower edge, see [Protocol Driver Send and Receive Operations](protocol-driver-send-and-receive-operations.md).

 

 





