---
title: User-Mode Dump Heap (UMDH) tool
description: The User-Mode Dump Heap (UMDH) tool, Umdh.exe, analyzes the Microsoft Windows heap memory allocations for a given process
ms.assetid: 112795a9-57c0-43a4-9f21-2a8655b65d1b
keywords: UMDH, User-Mode Dump Heap
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# UMDH


## <span id="ddk_umdh_dtools"></span><span id="DDK_UMDH_DTOOLS"></span>


The User-Mode Dump Heap (UMDH) tool, Umdh.exe, analyzes the Microsoft Windows heap memory allocations for a given process. UMDH has the following modes.

-   **Analyze a running process** ("Mode 1"). UMDH captures and analyzes the heap memory allocations for a process. For each allocation, UMDH displays the size of the allocation, the size of the overhead, the pointer to the allocation and the allocation stack. If a process has more than one active memory heap, UMDH captures all heaps. This analysis can be displayed in realtime or saved in a log file.

-   **Analyze UMDH log files** ("Mode 2"). UMDH analyzes the log files it has previously created. UMDH can compare two logs created for the same process at different times, and display the calls in which the allocation size increased the most. This technique can be used to find memory leaks.

This section includes:

[Preparing to Use UMDH](preparing-to-use-umdh.md)

[UMDH Commands](umdh-commands.md)

[Interpreting a UMDH Log](interpreting-a-umdh-log.md)

[Interpreting a Log Comparison](interpreting-a-log-comparison.md)

 

 





