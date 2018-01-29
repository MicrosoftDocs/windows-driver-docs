---
title: Determining Whether a Leak Exists
description: Determining Whether a Leak Exists
ms.assetid: a29db56e-6507-48f4-ad30-eb0a849f8673
keywords: ["memory leak, detection"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Determining Whether a Leak Exists


If Windows performance is degrading over time and you suspect that a memory leak may be involved, the technique described in this section can indicate whether there is a memory leak. It will not tell you what the source of the leak is, nor whether it is user mode or kernel mode.

Begin by launching Performance Monitor. Add the following counters:

-   **Memory**--&gt;**Pool Nonpaged Bytes**

-   **Memory**--&gt;**Pool Paged Bytes**

-   **Paging File**--&gt;**% Usage**

Change the update time to 600 seconds to capture a graph of the leak over time. You might also want to log the data to a file for later examination.

Start the application or test that you believe is causing the leak. Allow the application or test to run undisturbed for some time; do not use the target computer during this time. Leaks are usually slow and may take hours to detect. Wait for a few hours before deciding whether a leak has occurred.

Monitor the Performance Monitor counters. After the test has started, the counter values will change rapidly, and it may take some time for the memory pools values to reach a steady state.

User-mode memory leaks are always located in pageable pool and cause both the **Pool Paged Bytes** counter and the page file **Usage** counter to increase steadily over time. Kernel-mode memory leaks usually deplete nonpaged pool, causing the **Pool Nonpaged Bytes** counter to increase, although pageable memory can be affected as well. Occasionally these counters may show false positives because an application is caching data.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Determining%20Whether%20a%20Leak%20Exists%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




