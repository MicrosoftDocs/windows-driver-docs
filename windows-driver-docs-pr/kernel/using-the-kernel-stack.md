---
title: Using the Kernel Stack
description: Using the Kernel Stack
keywords: ["memory management WDK kernel , kernel stack", "kernel-mode stack space WDK", "kernel stack space WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using the Kernel Stack





The size of the kernel-mode stack is limited to approximately three pages. Therefore, when passing data to internal routines, drivers cannot pass large amounts of data on the kernel stack.

To avoid running out of kernel-mode stack space, use the following design guidelines:

-   Avoid making deeply nested calls from one internal driver routine to another, if each routine passes data on the kernel stack.

-   Make sure that you limit the number of recursive calls that can occur, if you design a driver that has a recursive routine.

In other words, the call-tree structure of a driver should be relatively flat. You can call the [**IoGetStackLimits**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetstacklimits) and [**IoGetRemainingStackSize**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetremainingstacksize) routines to determine the kernel stack space that is available, or [**KeExpandKernelStackAndCallout**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keexpandkernelstackandcallout) to expand it. Note that the size of the kernel-mode stack can vary among different hardware platforms and different versions of the operating system.

Running out of kernel stack space causes a fatal system error. Therefore, it is better for a driver to [allocate system-space memory](allocating-system-space-memory.md) than to run out of kernel stack space. However, nonpaged pool is also a limited system resource.

Generally, the kernel-mode stack resides in memory, however it can occasionally be paged out if the thread enters a wait state that specifies user mode. See [**KeSetKernelStackSwapEnable**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-kesetkernelstackswapenable) for information on how to temporarily disable kernel stack paging for the current thread. For performance reasons, it is not recommended to disable kernel stack paging globally, but if you want to do so during a debugging session, see [Disable paging of kernel stacks](../debugger/disable-paging-of-kernel-stacks.md)

Because the kernel stack might be paged out, please be cautious about passing stack-based buffers (i.e. local variables) to DMA or any routine that runs at DISPATCH_LEVEL or above.
