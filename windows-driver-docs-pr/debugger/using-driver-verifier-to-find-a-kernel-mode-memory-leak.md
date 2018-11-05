---
title: Using Driver Verifier to Find a Kernel-Mode Memory Leak
description: Using Driver Verifier to Find a Kernel-Mode Memory Leak
ms.assetid: d81a8b72-91d3-4132-9cc2-1cf1b597306a
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Using Driver Verifier to Find a Kernel-Mode Memory Leak


Driver Verifier determines whether a kernel-mode driver is leaking memory.

The Pool Tracking feature of Driver Verifier monitors the memory allocations made by a specified driver. At the time that the driver is unloaded, Driver Verifier verifies that all allocations made by the driver have been freed. If some of the driver's allocations have not been freed, a bug check is issued, and the parameters of the bug check indicate the nature of the problem.

While this feature is active, use the Driver Verifier Manager graphical interface to monitor pool allocation statistics. If a kernel debugger is attached to the driver, use the [**!verifier 0x3**](-verifier.md) extension to display allocation statistics.

If the driver uses Direct Memory Access (DMA), the DMA Verification feature of Driver Verifier is also helpful in finding memory leaks. DMA Verification tests for a number of common misuses of DMA routines, including failure to free common buffers and other errors that can lead to memory leaks. If a kernel debugger is attached while this option is active, use the [**!dma**](-dma.md) extension to show allocation statistics.

For information about Driver Verifier, see [Driver Verifier](https://go.microsoft.com/fwlink/p/?linkid=120480) in the Windows Driver Kit (WDK) documentation.

 

 





