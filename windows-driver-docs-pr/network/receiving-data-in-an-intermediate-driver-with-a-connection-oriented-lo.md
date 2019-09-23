---
title: Connection-oriented lower edge intermediate driver data reception
description: Receiving Data in an Intermediate Driver with a Connection-Oriented Lower Edge
ms.assetid: c14b4e8a-cfa2-4771-83b2-aa20fda79d39
keywords:
- intermediate drivers WDK networking , receive operations
- NDIS intermediate drivers WDK , receive operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving Data in an Intermediate Driver with a Connection-Oriented Lower Edge





If an intermediate driver is layered above a connection-oriented miniport driver, NDIS then calls the intermediate driver's [**ProtocolCoReceiveNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-protocol_co_receive_net_buffer_lists) function to indicate received data.

An underlying connection-oriented miniport driver indicates network data by calling [**NdisMCoIndicateReceiveNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismcoindicatereceivenetbufferlists), passing a linked list of one or more [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer_list) structures.

For more information about receiving data in an intermediate driver with a connection-oriented lower edge, see [Connection-Oriented Operations](connection-oriented-operations.md).

 

 





