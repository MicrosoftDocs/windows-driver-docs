---
title: Determining Whether a Leak Exists
description: Determining Whether a Leak Exists
keywords: ["memory leak, detection"]
ms.date: 04/30/2021
ms.localizationpriority: medium
---

# Determining Whether a Leak Exists


If Windows performance is degrading over time and you suspect that a memory leak may be involved, use Windows Performance Monitor to investigate whether there is a memory leak. This process will not tell you what the source of the leak is, nor whether it is user mode or kernel mode. 

Begin by launching Performance Monitor. To open Performance Monitor, use one of the following procedures:

- Open Start Menu, search for Performance Monitor, and click the result 
- Use the ```Windows Key + R``` keyboard shortcut to open the _Run_ command, type ```perfmon```, and click OK to open.

After opening the Performance Monitor, add the following counters to the main Performance Monitor graph:

-   **Memory**--&gt;**Pool Nonpaged Bytes**

-   **Memory**--&gt;**Pool Paged Bytes**

-   **Paging File**--&gt;**% Usage**


Right click on the *Performance Monitor* under *Monitoring Tools* and select **Properties**. Change the update time to 600 seconds to capture a graph of the leak over time. You might also want to log the data to a file for later examination.

Start the application or test that you believe is causing the leak. Allow the application or test to run undisturbed for some time; do not use the target computer during this time. Leaks are usually slow and may take hours to detect. Wait for a few hours before deciding whether a leak has occurred.

Monitor the Performance Monitor counters. After the test has started, the counter values will change rapidly, and it may take some time for the memory pools values to reach a steady state.

User-mode memory leaks are always located in pageable pool and cause both the **Pool Paged Bytes** counter and the page file **Usage** counter to increase steadily over time. Kernel-mode memory leaks usually deplete nonpaged pool, causing the **Pool Nonpaged Bytes** counter to increase, although pageable memory can be affected as well. Occasionally these counters may show false positives because an application is caching data.

 

 





