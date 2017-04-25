---
title: Using Driver Verifier to Find a Kernel-Mode Memory Leak
description: Using Driver Verifier to Find a Kernel-Mode Memory Leak
ms.assetid: d81a8b72-91d3-4132-9cc2-1cf1b597306a
---

# Using Driver Verifier to Find a Kernel-Mode Memory Leak


Driver Verifier determines whether a kernel-mode driver is leaking memory.

The Pool Tracking feature of Driver Verifier monitors the memory allocations made by a specified driver. At the time that the driver is unloaded, Driver Verifier verifies that all allocations made by the driver have been freed. If some of the driver's allocations have not been freed, a bug check is issued, and the parameters of the bug check indicate the nature of the problem.

While this feature is active, use the Driver Verifier Manager graphical interface to monitor pool allocation statistics. If a kernel debugger is attached to the driver, use the [**!verifier 0x3**](https://msdn.microsoft.com/library/windows/hardware/ff565591) extension to display allocation statistics.

If the driver uses Direct Memory Access (DMA), the DMA Verification feature of Driver Verifier is also helpful in finding memory leaks. DMA Verification tests for a number of common misuses of DMA routines, including failure to free common buffers and other errors that can lead to memory leaks. If a kernel debugger is attached while this option is active, use the [**!dma**](https://msdn.microsoft.com/library/windows/hardware/ff562369) extension to show allocation statistics.

For information about Driver Verifier, see [Driver Verifier](http://go.microsoft.com/fwlink/p/?linkid=120480) in the Windows Driver Kit (WDK) documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20Driver%20Verifier%20to%20Find%20a%20Kernel-Mode%20Memory%20Leak%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




