---
title: Porting CoNDIS Miniport Driver Receive Data Handling
description: Porting CoNDIS Miniport Driver Receive Data Handling
ms.assetid: 9f540bd8-8cbf-4a7a-b4ac-83cd159f5e37
keywords:
- porting miniport drivers WDK networking , send and receive operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting CoNDIS Miniport Driver Receive Data Handling





CoNDIS 6.0 miniport drivers indicate a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures to NDIS instead of a linked list of [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structures. NDIS then forwards the NET\_BUFFER\_LIST structures to the appropriate overlying drivers.

The CoNDIS 6.0 interfaces for indicating received data are very similar to that of CoNDIS 5.*x*. For example, NDIS 5.*x* miniport drivers call the [**NdisMCoIndicateReceivePacket**](https://msdn.microsoft.com/library/windows/hardware/ff553455) function to indicate an NDIS\_PACKET and CoNDIS 6.0 miniport drivers call the [**NdisMCoIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563561) function to indicate a linked list of NET\_BUFFER\_LIST structures.

If a miniport driver sets the NDIS\_RECEIVE\_FLAG\_RESOURCES flag in the *CoReceiveFlags* parameter of **NdisMCoIndicateReceiveNetBufferLists**, the driver can reclaim ownership of the NET\_BUFFER\_LIST structures as soon as **NdisMCoIndicateReceiveNetBufferLists** returns. If the miniport driver clears the NDIS\_RECEIVE\_FLAG\_RESOURCES flag for the *CoReceiveFlags* parameter, NDIS returns ownership of the NET\_BUFFER\_LIST structure by calling the miniport driver's [*MiniportReturnNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559437) function. This call is analogous to calling an NDIS 5.*x* miniport driver's [**MiniportReturnPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550510) function.

For more information about how CoNDIS miniport drivers handle receive data, see [Receiving NET\_BUFFER Structures in CoNDIS Drivers](receiving-net-buffer-structures-in-condis-drivers.md).

 

 





