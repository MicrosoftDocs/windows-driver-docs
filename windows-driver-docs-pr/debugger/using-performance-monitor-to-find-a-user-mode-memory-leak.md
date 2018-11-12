---
title: Using Performance Monitor to Find a User-Mode Memory Leak
description: Using Performance Monitor to Find a User-Mode Memory Leak
ms.assetid: 07ba4c55-299c-4558-b4c7-4ffe5c47f496
keywords: ["memory leak, user-mode, performance monitor"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Performance Monitor to Find a User-Mode Memory Leak


If you suspect there is a user-mode memory leak but are not sure which process is causing it, you can use Performance Monitor to measure the memory usage of individual processes.

Launch Performance Monitor. Add the following counters:

-   **Process**--&gt;**Private Bytes** (for each process you want to examine)

-   **Process**--&gt;**Virtual Bytes** (for each process you wish to examine)

Change the update time to 600 seconds to capture a graph of the leak over time. You might also want to log the data to a file for later examination.

The **Private Bytes** counter indicates the total amount of memory that a process has allocated, not including memory shared with other processes. The **Virtual Bytes** counter indicates the current size of the virtual address space that the process is using.

Some memory leaks appear in the data file as an increase in private bytes allocated. Other memory leaks show up as an increase in the virtual address space.

After you have determined which process is leaking memory, use the UMDH tool to determine the specific routine that is at fault. For details, see [Using UMDH to Find User-Mode Memory Leaks](using-umdh-to-find-a-user-mode-memory-leak.md).

 

 





