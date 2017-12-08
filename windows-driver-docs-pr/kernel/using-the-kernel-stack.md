---
title: Using the Kernel Stack
author: windows-driver-content
description: Using the Kernel Stack
ms.assetid: f1df01f4-f156-4267-a4a0-c548e16c02ea
keywords: ["memory management WDK kernel , kernel stack", "kernel-mode stack space WDK", "kernel stack space WDK"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using the Kernel Stack


## <a href="" id="ddk-using-the-kernel-stack-kg"></a>


The size of the kernel-mode stack is limited to approximately three pages. Therefore, when passing data to internal routines, drivers cannot pass large amounts of data on the kernel stack.

To avoid running out of kernel-mode stack space, use the following design guidelines:

-   Avoid making deeply nested calls from one internal driver routine to another, if each routine passes data on the kernel stack.

-   Make sure that you limit the number of recursive calls that can occur, if you design a driver that has a recursive routine.

In other words, the call-tree structure of a driver should be relatively flat. You can call the [**IoGetStackLimits**](https://msdn.microsoft.com/library/windows/hardware/ff549299) and [**IoGetRemainingStackSize**](https://msdn.microsoft.com/library/windows/hardware/ff549286) routines to determine the kernel stack space that is available, or [**KeExpandKernelStackAndCallout**](https://msdn.microsoft.com/en-us/library/windows/hardware/ff552030) to expand it. Note that the size of the kernel-mode stack can vary among different hardware platforms and different versions of the operating system.

Running out of kernel stack space causes a fatal system error. Therefore, it is better for a driver to [allocate system-space memory](allocating-system-space-memory.md) than to run out of kernel stack space. However, nonpaged pool is also a limited system resource.

Generally, the kernel-mode stack residents in memory, however it can occasionally be paged out if the thread enters a wait state that specifies user mode. See [**KeSetKernelStackSwapEnable**](https://msdn.microsoft.com/en-us/library/windows/hardware/ff553262) for more information on temporarily disable kernel stack paging for the current thread. For performance reason it is not recommended to disable kernel stack paging globally, but if you want to do so during a debugging session, see debugger document at [Disable paging of kernel stacks](https://msdn.microsoft.com/library/windows/hardware/ff541920)

Because kernel stack might be paged out, please be cautious about passing stack-based buffer (i.e. local variables) to DMA or any routine that runs at DISPATCH_LEVEL or above.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20the%20Kernel%20Stack%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


