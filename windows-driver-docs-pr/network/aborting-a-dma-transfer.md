---
title: Aborting a DMA Transfer
description: Aborting a DMA Transfer
ms.assetid: e63ccf75-b080-4268-b7af-03915c26a6ba
keywords:
- memory-to-memory data transfers WDK NetDMA , aborting
- data transfers WDK NetDMA , aborting
- transferring data WDK NetDMA , aborting
- DMA transfers WDK NetDMA , aborting
- NetDMA WDK networking , aborting transfers
- aborting DMA transfers WDK NetDMA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Aborting a DMA Transfer


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




The NetDMA interface can call a NetDMA provider driver's [**ProviderAbortDma**](https://msdn.microsoft.com/library/windows/hardware/ff570392) function, if any, to abort all dynamic memory access (DMA) transfers that have been scheduled on a DMA channel.

In *ProviderAbortDma*, the NetDMA provider should terminate the transfer immediately without completing the transfer of the data that is associated with the current DMA descriptor. If completion status reporting is enabled, the DMA engine writes the **NetDmaTransferStatusHalted** status in the address that is specified in the **CompletionVirtualAddress** and **CompletionPhysicalAddress** members in the [**NET\_DMA\_CHANNEL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff568732) structure.

After the abort operation completes, the DMA channel must be ready for the NetDMA interface to call the [**ProviderStartDma**](https://msdn.microsoft.com/library/windows/hardware/ff570404) function. The NetDMA interface will not call the [**ProviderAppendDma**](https://msdn.microsoft.com/library/windows/hardware/ff570394) function until after the transfer is restarted.

 

 





