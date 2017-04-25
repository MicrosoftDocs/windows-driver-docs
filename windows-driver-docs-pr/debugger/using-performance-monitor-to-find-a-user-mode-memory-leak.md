---
title: Using Performance Monitor to Find a User-Mode Memory Leak
description: Using Performance Monitor to Find a User-Mode Memory Leak
ms.assetid: 07ba4c55-299c-4558-b4c7-4ffe5c47f496
keywords: ["memory leak, user-mode, performance monitor"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20Performance%20Monitor%20to%20Find%20a%20User-Mode%20Memory%20Leak%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




