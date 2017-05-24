---
title: User-Mode Dump Heap (UMDH) tool
description: The User-Mode Dump Heap (UMDH) tool, Umdh.exe, analyzes the Microsoft Windows heap memory allocations for a given process
ms.assetid: 112795a9-57c0-43a4-9f21-2a8655b65d1b
keywords: ["UMDH", "User-Mode Dump Heap", "User-Mode Dump Heap, See "UMDH""]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20UMDH%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




