---
title: Look For User-Mode Memory Leak With PerfMon
description: Use Windows Performance Monitor (PerfMon) to find a user-mode memory leak and measure the memory usage of individual processes.
keywords: ["memory leak, user-mode, performance monitor"]
ms.date: 07/10/2025
ms.topic: how-to
---

# Find user-mode memory leaks with Performance Monitor (PerfMon)

If you suspect there's a user-mode memory leak, you can use Windows Performance Monitor (PerfMon) to measure the memory usage of individual processes. The tool can help you identify the specific process causing the leak.

Open Performance Monitor from Windows **Search**. Enter _perfmon_ (or _Performance Monitor_), then right-click the tool and select **Run as administrator**.

## Add data counters

Add process data counters to the main Performance Monitor graph so you can monitor data changes. Under **Monitoring Tools**, right-click **Performance Monitor** and select **Properties**. In the **Properties** dialog > **Data** tab, add the following counters:

- **Process** > **Private Bytes** > (for each process to examine): Set the total amount of memory allocated for the specific process, not including memory shared with other processes.

- **Process** > **Virtual Bytes** > (for each process to examine): Set the current size of the virtual address space for the specific process.

## Set duration to capture enough activity

Adjust the general time settings so you can capture a graph of any data leaks over time. In the **Properties** dialog > **General** tab, configure the following values:

- **Sample every**: Set the time to **600** seconds, which measures the value every 10 minutes.

- **Duration**: Set the time to capture enough activity. For example, to monitor the data over 24 hours, set the value to **86400** (60 x 60 x 24 = 86,400).

> [!TIP]
> Log the graph data to a file for later examination.

## Start application and monitor user-mode data 

After you configure the counters and time settings, start the application or test program that you want to check for leaks. Allow the program to run undisturbed for some time.

> [!IMPORTANT]
> Don't use the target computer while you're running the program to check for leaks. Leaks usually develop slowly. It can take hours for a data leak to accumulate to a detectable level.

Watch the Performance Monitor counters. When you start monitoring, the counter values change rapidly. It can take time for the memory pools values to reach a steady state.

- **Private Bytes**: Some memory leaks appear in the data file in the form of an increase in private bytes allocated.

- **Virtual Bytes**: Some memory leaks appear as an increase in the virtual address space.

## Find specific routine with leak

After you identify which process is leaking memory, use the user-mode dump heap (UMDH) utility to determine the specific routine with the memory issue. For for information, see [Use UMDH to find user-mode memory leaks](using-umdh-to-find-a-user-mode-memory-leak.md).