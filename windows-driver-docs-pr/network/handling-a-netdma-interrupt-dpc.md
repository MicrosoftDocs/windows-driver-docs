---
title: Handling a NetDMA Interrupt DPC
description: Handling a NetDMA Interrupt DPC
ms.assetid: 92da9324-5bc2-4a19-9c27-811cd7ad4572
keywords: ["interrupts WDK NetDMA , DPC", "DPCs WDK NetDMA"]
---

# Handling a NetDMA Interrupt DPC


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 

## <a href="" id="ddk-handling-a-netdma-interrupt-dpc-ng"></a>


Dynamic memory access (DMA) providers call the [**NetDmaInterruptDpc**](https://msdn.microsoft.com/library/windows/hardware/ff568330) function in their interrupt deferred procedure call (DPC) handler. For more information about DPC handlers, see [DPC Objects and DPCs](https://msdn.microsoft.com/library/windows/hardware/ff544084).

The NetDMA provider driver passes the physical address of the last completed DMA descriptor at the *DmaDescriptor* parameter of **NetDmaInterruptDpc**. If the NetDMA provider calls **NetDmaInterruptDpc** when there is an error, the NetDMA provider sets*DmaDescriptor* to **NULL**.

 

 





