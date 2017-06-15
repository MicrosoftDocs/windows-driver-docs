---
title: Using the Kernel Stack
author: windows-driver-content
description: Using the Kernel Stack
MS-HAID:
- 'MemMgmt\_25dfdb48-8ea6-4a52-a665-6be3a106b3dd.xml'
- 'kernel.using\_the\_kernel\_stack'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f1df01f4-f156-4267-a4a0-c548e16c02ea
keywords: ["memory management WDK kernel , kernel stack", "kernel-mode stack space WDK", "kernel stack space WDK"]
---

# Using the Kernel Stack


## <a href="" id="ddk-using-the-kernel-stack-kg"></a>


The size of the kernel-mode stack is limited to approximately three pages. Therefore, when passing data to internal routines, drivers cannot pass large amounts of data on the kernel stack.

To avoid running out of kernel-mode stack space, use the following design guidelines:

-   Avoid making deeply nested calls from one internal driver routine to another, if each routine passes data on the kernel stack.

-   Make sure that you limit the number of recursive calls that can occur, if you design a driver that has a recursive routine.

In other words, the call-tree structure of a driver should be relatively flat. You can call the [**IoGetStackLimits**](https://msdn.microsoft.com/library/windows/hardware/ff549299) and [**IoGetRemainingStackSize**](https://msdn.microsoft.com/library/windows/hardware/ff549286) routines to determine the kernel stack space that is available. Note that the size of the kernel-mode stack can vary among different hardware platforms and different versions of the operating system.

Running out of kernel stack space causes a fatal system error. Therefore, it is better for a driver to [allocate system-space memory](allocating-system-space-memory.md) than to run out of kernel stack space. However, nonpaged pool is also a limited system resource.

Drivers of devices that use DMA can buffer data to be transferred, if necessary, either by calling [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) for a **NonPagedPool**-type buffer or, for some drivers, by using common-buffer DMA. For more information, see [Using Common-Buffer System DMA](using-common-buffer-system-dma.md) and [Using Common-Buffer Bus-Master DMA](using-common-buffer-bus-master-dma.md).

Generally, the kernel-mode stack cannot be paged; it is guaranteed to be resident in memory. However, Windows occasionally pages the kernel stacks of inactive threads. For help in guaranteeing that these kernel stacks are not paged during a debugging session, see [Disable paging of kernel stacks](https://msdn.microsoft.com/library/windows/hardware/ff541920).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20the%20Kernel%20Stack%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


