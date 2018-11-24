---
title: Completing a DMA Transfer
description: Completing a DMA Transfer
ms.assetid: 3107c2e5-15a7-4399-b09d-b66a79cb5fab
keywords:
- memory-to-memory data transfers WDK NetDMA , completing
- data transfers WDK NetDMA , completing
- transferring data WDK NetDMA , completing
- DMA transfers WDK NetDMA , completing
- NetDMA WDK networking , completing transfers
- completing DMA transfers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Completing a DMA Transfer


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




The NetDMA interface provides two methods for a NetDMA provider to complete a dynamic memory access (DMA) transfer:

<a href="" id="completion-status-reporting"></a>Completion status reporting  
The DMA engine writes the physical address of the last descriptor that was processed and the status of the transfer operation to a memory location.

<a href="" id="interrupts"></a>Interrupts  
The DMA engine generates an interrupt when the processing is complete for a descriptor.

These two completion methods can be used together, separately, or there can be no completion action taken. Combinations of the NET\_DMA\_STATUS\_UPDATE\_ON\_COMPLETION and NET\_DMA\_INTERRUPT\_ON\_COMPLETION flags in the **ControlFlags** member of the [**NET\_DMA\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568734) structure specify the completion method for each DMA descriptor.

If the NET\_DMA\_STATUS\_UPDATE\_ON\_COMPLETION flag is set, the **CompletionVirtualAddress** and **CompletionPhysicalAddress** members in the [**NET\_DMA\_CHANNEL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff568732) structure reference a completion status value. The completion status value at the specified address is a 64-bit combination of the physical address of the most recent DMA descriptor that was processed and additional status information. If the NET\_DMA\_STATUS\_UPDATE\_ON\_COMPLETION flag is set, the DMA engine updates the completion status value when it completes the processing of each descriptor. If the NET\_DMA\_STATUS\_UPDATE\_ON\_COMPLETION flag is cleared, **CompletionVirtualAddress** and **CompletionPhysicalAddress** are not used.

The physical address of the DMA descriptor must be aligned to 64-bit boundaries. Therefore, the lower six bits of the physical address are available for other information. The DMA engine uses these bits to indicate status values, including **NetDmaTransferStatusActive**, **NetDmaTransferStatusIdle**, **NetDmaTransferStatusSuspend**, or **NetDmaTransferStatusHalted**.

If the NET\_DMA\_INTERRUPT\_ON\_COMPLETION flag is set, the DMA engine generates an interrupt for the DMA channel after it processes the DMA descriptor. When this flag is cleared, the DMA engine does not generate an interrupt.

If an interrupt is requested, the NetDMA provider driver calls the [**NetDmaIsr**](https://msdn.microsoft.com/library/windows/hardware/ff568331) function in its interrupt service routing (ISR) and provides the physical address of the last completed DMA descriptor. For more information about using interrupts, see [Managing NetDMA Interrupts](managing-netdma-interrupts.md).

 

 





