---
title: Porting NDIS Protocol Driver Receive Data Handling
description: Porting NDIS Protocol Driver Receive Data Handling
ms.assetid: e9b7e8ca-db64-4bce-ab34-5ba658111121
keywords:
- receive operation porting WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting NDIS Protocol Driver Receive Data Handling





NDIS 6.0 miniport drivers indicate to NDIS a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures instead of the NDIS 5.x [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures. NDIS forwards the **NET\_BUFFER\_LIST** structures to the appropriate overlying protocol drivers.

In NDIS 5.x, NDIS calls the [**ProtocolReceivePacket**](https://msdn.microsoft.com/library/windows/hardware/ff563251) function to indicate received data. In NDIS 6.0, NDIS calls the [*ProtocolReceiveNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff570267) function to indicate a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures.

NDIS 6.0 does not necessarily call the protocol driver's receive entry point at IRQL= DISPATCH level.

For an overview of receive operations, see [Receiving Network Data](receiving-network-data.md). For more information about protocol driver receive handling, see [Receiving Data in Protocol Drivers](receiving-data-in-protocol-drivers.md).

 

 





