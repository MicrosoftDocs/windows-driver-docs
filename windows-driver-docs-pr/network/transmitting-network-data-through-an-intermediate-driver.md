---
title: Transmitting Network Data Through an Intermediate Driver
description: Transmitting Network Data Through an Intermediate Driver
keywords:
- intermediate drivers WDK networking , transmitting data
- NDIS intermediate drivers WDK , transmitting data
- transmitting network data
- data transfers WDK NDIS intermediate
- transferring data WDK NDIS intermediate
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Transmitting Network Data Through an Intermediate Driver





As discussed in [Registering an Intermediate Driver as a Miniport Driver](registering-an-intermediate-driver-as-a-miniport-driver.md), an intermediate driver must provide a [*MiniportSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists) function when it registers with [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver). The *MiniportSendNetBufferLists* function can forward incoming [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures by calling [**NdisSendNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissendnetbufferlists) if the driver has a connectionless lower edge . *MiniportSendNetBufferLists* can send the list of NET\_BUFFER\_LIST structures it receives with **NdisSendNetBufferLists** without regard to the capabilities of the underlying miniport driver.

*MiniportSendNetBufferLists* receives a list of NET\_BUFFER\_LIST structures arranged in an order determined by an overlying caller of **NdisSendNetBufferLists**. In most cases, the intermediate driver should maintain this ordering as it passes an incoming array of NET\_BUFFER\_LIST structures on to the underlying miniport driver. An intermediate driver that modifies data in network data before passing them on to the underlying driver can reorder a list.

NDIS always preserves the ordering of [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure pointers as passed as a linked list to **NdisSendNetBufferLists**. The underlying miniport driver also assumes that list that is passed in to its *MiniportSendNetBufferLists* function implies the network data should be transmitted in the same order.

 

