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

-   [Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier) includes specific verification tests that detect improper use of various DMA operations. For more information about DMA-specific verification, see [DMA Verification](https://docs.microsoft.com/windows-hardware/drivers/devtest/dma-verification).

-   The [**!dma**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-dma) kernel debugger extension displays information about the DMA subsystem and DMA device drivers that are being verified by [Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier).

-   The [Kernel-Mode Driver Framework Extensions](https://docs.microsoft.com/windows-hardware/drivers/debugger/kernel-mode-driver-framework-extensions--wdfkd-dll-) include the following DMA-specific commands:

    <a href="" id="-wdfcommonbuffer"></a>[**!wdfcommonbuffer**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfcommonbuffer)  
    Dumps information about a given common buffer object.

    <a href="" id="-wdfdmaenabler"></a>[**!wdfdmaenabler**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfdmaenabler)  
    Dumps information about a specific DMA enabler object and its transactions and common buffer objects.

    <a href="" id="-wdfdmaenablers"></a>[**!wdfdmaenablers**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfdmaenablers)  
    Lists all of the DMA enablers and their transactions and common buffer objects.

    <a href="" id="-wdfdmatransaction"></a>[**!wdfdmatransaction**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfdmatransaction)  
    Dumps information about a given transaction object.

 

 





