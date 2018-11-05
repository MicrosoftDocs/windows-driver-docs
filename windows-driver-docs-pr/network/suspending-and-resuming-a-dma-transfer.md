---
title: Suspending and Resuming a DMA Transfer
description: Suspending and Resuming a DMA Transfer
ms.assetid: 0d46f60d-58a7-4108-b683-2f1322fa8211
keywords:
- memory-to-memory data transfers WDK NetDMA , suspending
- data transfers WDK NetDMA , suspending
- transferring data WDK NetDMA , suspending
- DMA transfers WDK NetDMA , suspending DMA transfers
- NetDMA WDK networking , suspending DMA transfers
- suspendi
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Suspending and Resuming a DMA Transfer


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




The NetDMA interface can call a NetDMA provider driver's [**ProviderSuspendDma**](https://msdn.microsoft.com/library/windows/hardware/ff570405) function, if any, to temporarily suspend any dynamic memory access (DMA) transfers that are in progress on a DMA channel. The NetDMA provider returns the physical address of the last DMA descriptor that it processed at the address that the *pLastDescriptor* parameter specifies in **ProviderSuspendDma**.

The NetDMA provider completes the transfer of the current DMA descriptor before it returns from [**ProviderSuspendDma**](https://msdn.microsoft.com/library/windows/hardware/ff570405) If completion status reporting is enabled, the DMA engine writes the **NetDmaTransferStatusSuspend** status in the address that is specified in the **CompletionVirtualAddress** and **CompletionPhysicalAddress** members in the [**NET\_DMA\_CHANNEL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff568732) structure.

While the DMA transfers are suspended, the NetDMA interface can modify the DMA descriptor linked list (for example, to insert or delete descriptors).

The NetDMA interface calls the [**ProviderResumeDma**](https://msdn.microsoft.com/library/windows/hardware/ff570401) function to resume DMA operations that the interface suspended by calling [**ProviderSuspendDma**](https://msdn.microsoft.com/library/windows/hardware/ff570405). If the NetDMA provider driver specifies an entry point for a **ProviderSuspendDma** function, it must also specify an entry point for a *ProviderResumeDma* function.

When the DMA engine resumes transfers, the hardware reloads the DMA descriptor that it processed last to get the new next descriptor.

 

 





