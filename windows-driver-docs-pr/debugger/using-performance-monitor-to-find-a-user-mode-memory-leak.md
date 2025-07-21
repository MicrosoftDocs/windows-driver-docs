---
title: Use Performance Monitor to Find a User-Mode Memory Leak
description: Learn how to use Performance Monitor to find a user-mode memory leak and to measure the memory usage of individual processes.
keywords: ["memory leak, user-mode, performance monitor"]
ms.date: 08/26/2024
ms.topic: how-to
---

# Use Performance Monitor to find a user-mode memory leak

If you suspect there's a user-mode memory leak but aren't sure which process causes it, use Performance Monitor to measure the memory usage of individual processes.

Run Performance Monitor as Administrator. Right click on the *Performance Monitor* under *Monitoring Tools* and select **Properties** to add the following counters:

- **Process** > **Private Bytes** (for each process you want to examine)

- **Process** > **Virtual Bytes** (for each process you wish to examine)

 Set the *Duration* to capture enough activity. For example, change the update time to 600 seconds to capture a graph of the leak over time. You might also want to log the data to a file for later examination.

The **Private Bytes** counter indicates the total amount of memory that a process has allocated, not including memory shared with other processes. 

The **Virtual Bytes** counter indicates the current size of the virtual address space that the process uses.

Some memory leaks appear in the data file in the form of an increase in private bytes allocated. Other memory leaks show up in the form of an increase in the virtual address space.

After you've determined which process is leaking memory, use the UMDH tool to determine the specific routine that's at fault. For details, see [Using UMDH to find user-mode memory leaks](using-umdh-to-find-a-user-mode-memory-leak.md).
