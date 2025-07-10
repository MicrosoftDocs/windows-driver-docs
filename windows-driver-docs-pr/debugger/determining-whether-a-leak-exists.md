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

Add memory and page file counters to the main Performance Monitor graph so you can monitor data changes. Under **Monitoring Tools**, right-click **Performance Monitor** and select **Properties**. In the **Properties** dialog > **Data** tab, add the following counters:

- **Memory** > **Pool Nonpaged Bytes**

- **Memory** > **Pool Paged Bytes**

- **Paging File** > **% Usage**

## Set duration to capture enough activity

Adjust the general time settings so you can capture a graph of any data leaks over time. In the **Properties** dialog > **General** tab, configure the following values:

- **Sample every**: Set the time to **600** seconds, which measures the value every 10 minutes.

- **Duration**: Set the time to capture enough activity. For example, to monitor the data over 24 hours, set the value to **86400** (60 x 60 x 24 = 86,400).

> [!TIP]
> Log the graph data to a file for later examination.

## Start application and monitor data 

After you configure the counters and time settings, start the application or test program that you want to check for leaks. Allow the program to run undisturbed for some time.

> [!IMPORTANT]
> Don't use the target computer while you're running the program to check for leaks. Leaks usually develop slowly. It can take hours for a data leak to accumulate to a detectable level.

Watch the Performance Monitor counters. When you start monitoring, the counter values change rapidly. It can take time for the memory pools values to reach a steady state. Wait several hours before you decide there's a leak.

### Investigate user-mode leaks

User-mode memory leaks are always located in _pageable_ pool. This type of leak causes the **Memory** > **Pool Paged Bytes** counter and the **Paging File** > **Usage** counter to increase steadily over time. For more information, see [Find user-mode memory leaks with PerfMon](./using-performance-monitor-to-find-a-user-mode-memory-leak.md).

### Investigate kernel-mode leaks

Kernel-mode memory leaks usually deplete _nonpaged_ pool. This type of leak causes the **Memory** > **Pool Nonpaged Bytes** counter to increase and potentially, pageable memory. Occasionally, Kernel-mode counters can show false positives because an application is caching data.