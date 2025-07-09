---
title: Look For Potential Memory Leaks With PerfMon
description: Use Windows Performance Monitor (PerfMon) to determine if your system has memory leaks, and investigate memory issues related to degraded performance.
keywords: ["memory leak, detection"]
ms.date: 07/10/2025
ms.topic: how-to
---

# Look for memory leaks with Performance Monitor (PerfMon)

If Windows performance is degrading over time and you suspect a memory leak might be involved, use Windows Performance Monitor (PerfMon) to investigate for possible memory leaks. You can monitor data changes in memory over time for different aspects of your application or program. The tool doesn't identify the source of a leak, or confirm the presence of an issue in user mode or kernel mode. You can adjust settings in the tool to help locate the issue.

Open Performance Monitor with one of the following procedures:

- In Windows **Search**, enter _perfmon_ (or _Performance Monitor_), and select the tool.

- Use the **Windows Key** + **R** keyboard shortcut to open the **Run** command dialog. Enter _perfmon_ and select **OK**.

## Add data counters

Add memory and page file counters to the main Performance Monitor graph so you can monitor data changes.

1. In Performance Monitor, expand **Monitoring Tools**, and select **Performance Monitor**. The graph view displays.

1. Right-click **Performance Monitor** and select **Properties**. 

1. In the **Performance Monitor Properties** dialog, select the **Data** tab.

1. Select **Add**. The **Add Counters** dialog opens.

1. In the list of counters (sorted alphabetically), locate **Memory**. Select the dropdown arrow for **Memory** to see all memory-related counters. 

1. Add the following memory counters. Select a counter and then select **Add**.

   - **Pool Nonpaged Bytes**
   - **Pool Paged Bytes**

1. In the main list of counters, locate **Paging File**. Select the dropdown arrow for **Paging File** to see all page-related counters. 

1. Add the **% Usage** counter.

1. Select **OK**.

## Set duration to capture enough activity

Adjust the general time settings so you can capture a graph of any data leaks over time.

1. In the **Performance Monitor Properties** dialog, select the **General** tab.

1. Set the **Sample every** time to **600** seconds, which measures the value every 10 minutes.

1. Set the **Duration** time to capture enough activity.

   To monitor the data over 24 hours, the value is **86400** (60 x 60 x 24 = 86,400).
   
1. Select **OK**.

> [!TIP]
> Log the graph data to a file for later examination.

## Start application and monitor data 

After you configure the counters and time settings, run Performance Monitor to check for leaks:

1. Start the application or test program that you want to check for leaks.

1. Allow the program to run undisturbed for some time.

   > [!IMPORTANT]
   > Don't use the target computer while you're running the program to check for leaks.
   > Leaks usually develop slowly.
   > It can take hours for a data leak to accumulate to a detectable level.

1. Watch the Performance Monitor counters.

   When you start monitoring, the counter values change rapidly. It can take time for the memory pools values to reach a steady state.

1. Wait several hours before you decide there's a leak.

### Investigate user-mode leaks

User-mode memory leaks are always located in _pageable_ pool.

This type of leak causes the **Memory** > **Pool Paged Bytes** counter and the **Paging File** > **Usage** counter to increase steadily over time.

### Investigate kernel-mode leaks

Kernel-mode memory leaks usually deplete _nonpaged_ pool. This type of leak causes the **Memory** > **Pool Nonpaged Bytes** counter to increase and potentially, pageable memory.

Occasionally, Kernel-mode counters can show false positives because an application is caching data.
