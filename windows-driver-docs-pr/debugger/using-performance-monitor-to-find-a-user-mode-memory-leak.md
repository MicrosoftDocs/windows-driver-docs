---
title: Look For User-Mode Memory Leak With PerfMon
description: Use Windows Performance Monitor (PerfMon) to find a user-mode memory leak and measure the memory usage of individual processes.
keywords: ["memory leak, user-mode, performance monitor"]
ms.date: 07/10/2025
---

# Find user-mode memory leaks with Performance Monitor (PerfMon)

If you suspect there's a user-mode memory leak, you can use Windows Performance Monitor (PerfMon) to measure the memory usage of individual processes. The tool can help you identify the specific process causing the leak.

Open Performance Monitor from Windows **Search**. Enter _perfmon_ (or _Performance Monitor_), then right-click the tool and select **Run as administrator**.

## Add data counters

Add process data counters to the main Performance Monitor graph so you can monitor data changes.

1. In Performance Monitor, expand **Monitoring Tools**, and select **Performance Monitor**. The graph view displays.

1. Right-click **Performance Monitor** and select **Properties**. 

1. In the **Performance Monitor Properties** dialog, select the **Data** tab.

1. Select **Add**. The **Add Counters** dialog opens.

1. In the list of counters (sorted alphabetically), locate **Process**. Select the dropdown arrow for **Process** to see all memory-related counters. 

1. Add the following memory counters. Select a counter and then select **Add**.

   - **Private Bytes** (for each process to examine): Indicates the total amount of memory allocated for the process, not including memory shared with other processes.

   - **Virtual Bytes** (for each process to examine): Indicates the current size of the virtual address space that the process uses.

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

## Start application and check user-mode data 

After you configure the counters and time settings, check for leaks with Performance Monitor:

1. Start the application or test program that you want to check for leaks.

1. Allow the program to run undisturbed for some time.

   > [!IMPORTANT]
   > Don't use the target computer while you're running the program to check for leaks.
   > Leaks usually develop slowly.
   > It can take hours for a data leak to accumulate to a detectable level.

1. Watch the Performance Monitor counters.

   When you start monitoring, the counter values change rapidly. It can take time for the memory pools values to reach a steady state.

   - **Private Bytes**: Some memory leaks appear in the data file in the form of an increase in private bytes allocated.

   - **Virtual Bytes**: Some memory leaks appear as an increase in the virtual address space.

## Find specific routine with leak

After you identify which process is leaking memory, use the user-mode dump heap (UMDH) utility to determine the specific routine with the memory issue. For for information, see [Use UMDH to find user-mode memory leaks](using-umdh-to-find-a-user-mode-memory-leak.md).
