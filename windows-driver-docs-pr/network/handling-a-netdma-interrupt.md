---
title: Handling a NetDMA Interrupt
description: Handling a NetDMA Interrupt
ms.assetid: 239eb7e3-9935-4281-9215-5b0b987f7d33
keywords:
- interrupts WDK NetDMA , generating
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling a NetDMA Interrupt


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




If the NET\_DMA\_INTERRUPT\_ON\_COMPLETION flag in the **ControlFlags** member of the [**NET\_DMA\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568734) structure is set, the dynamic memory access (DMA) engine generates an interrupt for the DMA channel after it processes the DMA descriptor. When this flag is cleared, the DMA engine does not generate an interrupt.

DMA provider drivers call the [**NetDmaIsr**](https://msdn.microsoft.com/library/windows/hardware/ff568331) function in their interrupt service routine (ISR). For more information about ISRs, see [Interrupt Service Routines](https://msdn.microsoft.com/library/windows/hardware/ff547974).

The NetDMA provider driver passes the physical address of the last completed DMA descriptor at the *DmaDescriptor* parameter of **NetDmaIsr**. The NetDMA interface writes the CPU number at the address that is provided in the *pCpuNumber* parameter of **NetDmaIsr** before **NetDmaIsr** returns. The NetDMA provider must use the CPU number that *pCpuNumber* specifies as the target CPU for the interrupt DPC.

**Note**  When the ISR is called, the current DMA descriptor might already be different from the descriptor that triggered the interrupt.

 

A NetDMA provider driver should do as little work as possible in its ISR handler. Instead, the driver should defer I/O operations to the interrupt DPC handler. For more information about DPCs, see [Handling a NetDMA Interrupt DPC](handling-a-netdma-interrupt-dpc.md).

 

 





