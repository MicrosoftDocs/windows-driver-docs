---
title: Testing DMA in KMDF Drivers
description: Testing DMA in KMDF Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Testing DMA in KMDF Drivers


\[Applies to KMDF only\]

The following tools can help debug framework-based drivers that support DMA:

-   [Driver Verifier](../devtest/driver-verifier.md) includes specific verification tests that detect improper use of various DMA operations. For more information about DMA-specific verification, see [DMA Verification](../devtest/dma-verification.md).

-   The [**!dma**](../debugger/-dma.md) kernel debugger extension displays information about the DMA subsystem and DMA device drivers that are being verified by [Driver Verifier](../devtest/driver-verifier.md).

-   The [Kernel-Mode Driver Framework Extensions](../debugger/kernel-mode-driver-framework-extensions--wdfkd-dll-.md) include the following DMA-specific commands:

    <a href="" id="-wdfcommonbuffer"></a>[**!wdfcommonbuffer**](../debugger/-wdfkd-wdfcommonbuffer.md)  
    Dumps information about a given common buffer object.

    <a href="" id="-wdfdmaenabler"></a>[**!wdfdmaenabler**](../debugger/-wdfkd-wdfdmaenabler.md)  
    Dumps information about a specific DMA enabler object and its transactions and common buffer objects.

    <a href="" id="-wdfdmaenablers"></a>[**!wdfdmaenablers**](../debugger/-wdfkd-wdfdmaenablers.md)  
    Lists all of the DMA enablers and their transactions and common buffer objects.

    <a href="" id="-wdfdmatransaction"></a>[**!wdfdmatransaction**](../debugger/-wdfkd-wdfdmatransaction.md)  
    Dumps information about a given transaction object.

 

