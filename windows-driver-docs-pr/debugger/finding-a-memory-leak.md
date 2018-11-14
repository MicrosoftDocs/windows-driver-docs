---
title: Finding a Memory Leak
description: Finding a Memory Leak
ms.assetid: 1227c5e8-d83b-4f27-aa69-6e54aebc3ad8
keywords: ["memory leak", "memory leak, debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Finding a Memory Leak


## <span id="ddk_finding_a_memory_leak_dbg"></span><span id="DDK_FINDING_A_MEMORY_LEAK_DBG"></span>


A memory leak occurs when a process allocates memory from the paged or nonpaged pools, but does not free the memory. As a result, these limited pools of memory are depleted over time, causing Windows to slow down. If memory is completely depleted, failures may result.

This section includes the following:

-   [Determining Whether a Leak Exists](determining-whether-a-leak-exists.md) describes a technique you can use if you are not sure whether there is a memory leak on your system.

-   [Finding a Kernel-Mode Memory Leak](finding-a-kernel-mode-memory-leak.md) describes how to find a leak that is caused by a kernel-mode driver or component.

-   [Finding a User-Mode Memory Leak](finding-a-user-mode-memory-leak.md) describes how to find a leak that is caused by a user-mode driver or application.

 

 





