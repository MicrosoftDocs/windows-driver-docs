---
title: Transmitting Network Data Through an Intermediate Driver
description: Transmitting Network Data Through an Intermediate Driver
ms.assetid: 90759322-810b-47fd-896c-465c96be4cdd
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





As discussed in [Registering an Intermediate Driver as a Miniport Driver](registering-an-intermediate-driver-as-a-miniport-driver.md), an intermediate driver must provide a [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function when it registers with [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654). The *MiniportSendNetBufferLists* function can forward incoming [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures by calling [**NdisSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564535) if the driver has a connectionless lower edge . *MiniportSendNetBufferLists* can send the list of NET\_BUFFER\_LIST structures it receives with **NdisSendNetBufferLists** without regard to the capabilities of the underlying miniport driver.

*MiniportSendNetBufferLists* receives a list of NET\_BUFFER\_LIST structures arranged in an order determined by an overlying caller of **NdisSendNetBufferLists**. In most cases, the intermediate driver should maintain this ordering as it passes an incoming array of NET\_BUFFER\_LIST structures on to the underlying miniport driver. An intermediate driver that modifies data in network data before passing them on to the underlying driver can reorder a list.

NDIS always preserves the ordering of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure pointers as passed as a linked list to **NdisSendNetBufferLists**. The underlying miniport driver also assumes that list that is passed in to its *MiniportSendNetBufferLists* function implies the network data should be transmitted in the same order.

 

 





