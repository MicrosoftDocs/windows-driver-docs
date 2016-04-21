---
title: Introduction to DMA in Windows Driver Framework
author: windows-driver-content
description: Introduction to DMA in Windows Driver Framework
ms.assetid: 9bcd8ac1-f3dd-4bb3-a671-51c9465f8efa
keywords: ["DMA operations WDK KMDF , about DMA operations", "bus-master DMA WDK KMDF , about DMA operations"]
---

# Introduction to DMA in Windows Driver Framework


\[Applies to KMDF only\]

## <a href="" id="ddk-introduction-to-dma-in-windows-driver-framework-df"></a>


On Windows 7 and earlier, Kernel-Mode Driver Framework (KMDF) supports only bus-master direct memory access (DMA) devices. Such devices contain their own DMA controllers.

On System on a Chip (SoC)–based platforms running Windows 8 and later, the framework also supports system-mode DMA, in which multiple devices share a single multichannel DMA controller.

The framework's DMA support consists of:

-   A set of framework DMA objects and methods that drivers use to convert I/O requests into DMA operations.

-   A set of driver-supplied event callback functions that configure the device's DMA behavior as different events occur.

The framework supports both single packet and scatter/gather DMA transfers. It also supports the use of common buffers.

On SoC-based platforms running Windows 8 and later, the framework supports single-packet system-mode DMA transfers. For more information, see [Supporting System-Mode DMA](supporting-system-mode-dma.md).

The framework does not support system-mode DMA transfers on PC-based platforms.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Introduction%20to%20DMA%20in%20Windows%20Driver%20Framework%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




