---
title: New Scatter/Gather DMA Support
description: New Scatter/Gather DMA Support
ms.assetid: ac7cd98b-1211-4538-a54b-7362fa1d81b0
keywords:
- scatter/gather DMA WDK networking
- miniport drivers WDK networking , scatter/gather DMA
- NDIS miniport drivers WDK , scatter/gather DMA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# New Scatter/Gather DMA Support





Unlike previous versions of NDIS, NDIS 6.0 passes a send packet to a miniport driver before the packet is mapped for a DMA transfer. After it has obtained the packet, the miniport driver can request NDIS to supply a scatter/gather list for the packet.

This provides the following benefits:

-   Because a miniport driver has access to the packet before it is mapped, any changes that the miniport driver makes to the packet are reflected in the associated scatter/gather list data.

-   A miniport driver can optimize the transmission of small or highly fragmented packets by copying them to a preallocated buffer, thereby eliminating the need for mapping. This eliminates unnecessary processing.

-   NDIS can safely pass multiple [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures to the miniport driver in one function call. This results in fewer calls to the miniport driver and thus improves system performance.

-   Because a miniport driver can preallocate memory for a scatter/gather list, NDIS does not have to allocate memory for the scatter/gather list at run time.

For more information about NDIS 6.0 scatter/gather DMA, see [NDIS 6.0 Scatter/Gather DMA](ndis-scatter-gather-dma.md).

 

 





