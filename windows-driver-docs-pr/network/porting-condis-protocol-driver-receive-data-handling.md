---
title: Porting CoNDIS Protocol Driver Receive Data Handling
description: Porting CoNDIS Protocol Driver Receive Data Handling
ms.assetid: da180754-673a-428f-b6a1-eb66faa4e8d7
keywords:
- porting protocol drivers WDK networking , send and receive operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting CoNDIS Protocol Driver Receive Data Handling





CoNDIS 6.0 miniport drivers indicate a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures to NDIS instead of the NDIS 5.x [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures. NDIS then forwards the NET\_BUFFER\_LIST structures to the appropriate overlying protocol drivers.

In CoNDIS 5.x, NDIS calls the [**ProtocolCoReceivePacket**](https://msdn.microsoft.com/library/windows/hardware/ff563224) function to indicate received data. In CoNDIS 6.0, NDIS calls the [**ProtocolCoReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff570256) function to indicate a linked list of NET\_BUFFER\_LIST structures.

If the NDIS\_RECEIVE\_FLAG\_RESOURCES flag in the *CoReceiveFlags* parameterr that NDIS passes to a protocol driver's *ProtocolCoReceiveNetBufferLists* function is set, NDIS regains the ownership of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures immediately after the *ProtocolCoReceiveNetBufferLists* call returns.

If the NDIS\_RECEIVE\_FLAG\_RESOURCES flag is cleared in the *CoReceiveFlags* parameter that NDIS passes to a protocol driver's [**ProtocolCoReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff570256) function , the protocol driver can retain ownership of the NET\_BUFFER\_LIST structures. In this case, the protocol driver must return the NET\_BUFFER\_LIST structures by calling the [**NdisReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564534) function.

NDIS 6.0 can call the protocol driver's receive entry point at IRQL&lt;= DISPATCH level. In NDIS 5.x and earlier versions, NDIS calls the receive entry point at IRQL = DISPATCH level.

For an overview of receive operations, see [Receiving Network Data](receiving-network-data.md). For more information about CoNDIS protocol driver receive operations, see [Receiving NET\_BUFFER Structures in CoNDIS Drivers](receiving-net-buffer-structures-in-condis-drivers.md).

 

 





