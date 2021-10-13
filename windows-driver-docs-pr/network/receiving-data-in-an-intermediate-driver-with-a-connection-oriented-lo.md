---
title: Connection-oriented lower edge intermediate driver data reception
description: Receiving Data in an Intermediate Driver with a Connection-Oriented Lower Edge
keywords:
- intermediate drivers WDK networking , receive operations
- NDIS intermediate drivers WDK , receive operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving Data in an Intermediate Driver with a Connection-Oriented Lower Edge





If an intermediate driver is layered above a connection-oriented miniport driver, NDIS then calls the intermediate driver's [**ProtocolCoReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_receive_net_buffer_lists) function to indicate received data.

An underlying connection-oriented miniport driver indicates network data by calling [**NdisMCoIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcoindicatereceivenetbufferlists), passing a linked list of one or more [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures.

For more information about receiving data in an intermediate driver with a connection-oriented lower edge, see [Connection-Oriented Operations](connection-oriented-operations-performed-by-clients.md).

 

