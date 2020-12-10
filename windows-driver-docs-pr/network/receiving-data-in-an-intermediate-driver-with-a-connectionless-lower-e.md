---
title: Connectionless lower edge intermediate driver data reception
description: Receiving Data in an Intermediate Driver with a Connectionless Lower Edge
keywords:
- intermediate drivers WDK networking , receive operations
- NDIS intermediate drivers WDK , receive operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving Data in an Intermediate Driver with a Connectionless Lower Edge





An intermediate driver with a connectionless lower edge must have a [**ProtocolReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_receive_net_buffer_lists) function to receive network data.

Underlying connectionless miniport drivers call the **NdisMIndicateReceiveNetBufferLists**, passing a linked list of one or more [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures, relinquishing ownership of the indicated structures to higher level drivers. When the higher level drivers have consumed the data, they return the NET\_BUFFER\_LIST structures (and the resources they specify) to the miniport driver.

For more information about receiving data in an intermediate driver with a connectionless lower edge, see [Protocol Driver Send and Receive Operations](protocol-driver-send-and-receive-operations.md).

 

