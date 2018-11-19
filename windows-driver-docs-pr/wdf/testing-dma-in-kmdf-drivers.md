---
title: Testing DMA in KMDF Drivers
description: Testing DMA in KMDF Drivers
ms.assetid: 1D37F8B3-EAFC-4BB0-988D-64ADF30DBC40
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Testing DMA in KMDF Drivers


\[Applies to KMDF only\]

The following tools can help debug framework-based drivers that support DMA:

-   [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) includes specific verification tests that detect improper use of various DMA operations. For more information about DMA-specific verification, see [DMA Verification](https://msdn.microsoft.com/library/windows/hardware/ff544915).

-   The [**!dma**](https://msdn.microsoft.com/library/windows/hardware/ff562369) kernel debugger extension displays information about the DMA subsystem and DMA device drivers that are being verified by [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).

-   The [Kernel-Mode Driver Framework Extensions](https://msdn.microsoft.com/library/windows/hardware/ff551876) include the following DMA-specific commands:

    <a href="" id="-wdfcommonbuffer"></a>[**!wdfcommonbuffer**](https://msdn.microsoft.com/library/windows/hardware/ff565679)  
    Dumps information about a given common buffer object.

    <a href="" id="-wdfdmaenabler"></a>[**!wdfdmaenabler**](https://msdn.microsoft.com/library/windows/hardware/ff565717)  
    Dumps information about a specific DMA enabler object and its transactions and common buffer objects.

    <a href="" id="-wdfdmaenablers"></a>[**!wdfdmaenablers**](https://msdn.microsoft.com/library/windows/hardware/ff565719)  
    Lists all of the DMA enablers and their transactions and common buffer objects.

    <a href="" id="-wdfdmatransaction"></a>[**!wdfdmatransaction**](https://msdn.microsoft.com/library/windows/hardware/ff565721)  
    Dumps information about a given transaction object.

 

 





