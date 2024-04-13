---
title: Sending Data from a Miniport Driver
description: Sending Data from a Miniport Driver
keywords:
- sending data WDK networking
ms.date: 04/20/2017
---

# Sending Data from a Miniport Driver





The following figure illustrates a miniport driver send operation.

:::image type="content" source="images/miniportsend.png" alt-text="Diagram that shows a miniport driver send operation.":::

NDIS calls a miniport driver's [*MiniportSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists) function to transmit the network data that is described by a linked list of [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures.

Miniport drivers call the [**NdisMSendNetBufferListsComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsendnetbufferlistscomplete) function to return a linked list of NET\_BUFFER\_LIST structures to an overlying driver and to return the final status of a send request.

 

