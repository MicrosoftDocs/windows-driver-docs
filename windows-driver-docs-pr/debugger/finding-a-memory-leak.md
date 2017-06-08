---
title: Finding a Memory Leak
description: Finding a Memory Leak
ms.assetid: 1227c5e8-d83b-4f27-aa69-6e54aebc3ad8
keywords: ["memory leak", "memory leak, debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Finding a Memory Leak


## <span id="ddk_finding_a_memory_leak_dbg"></span><span id="DDK_FINDING_A_MEMORY_LEAK_DBG"></span>


A memory leak occurs when a process allocates memory from the paged or nonpaged pools, but does not free the memory. As a result, these limited pools of memory are depleted over time, causing Windows to slow down. If memory is completely depleted, failures may result.

This section includes the following:

-   [Determining Whether a Leak Exists](determining-whether-a-leak-exists.md) describes a technique you can use if you are not sure whether there is a memory leak on your system.

-   [Finding a Kernel-Mode Memory Leak](finding-a-kernel-mode-memory-leak.md) describes how to find a leak that is caused by a kernel-mode driver or component.

-   [Finding a User-Mode Memory Leak](finding-a-user-mode-memory-leak.md) describes how to find a leak that is caused by a user-mode driver or application.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Finding%20a%20Memory%20Leak%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




