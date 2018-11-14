---
title: Determining Whether a Leak Exists
description: Determining Whether a Leak Exists
ms.assetid: a29db56e-6507-48f4-ad30-eb0a849f8673
keywords: ["memory leak, detection"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
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

 

 





