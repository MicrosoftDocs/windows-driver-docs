---
title: About GPUView
description: About GPUView
ms.date: 12/06/2023
mscustom: contperf-fy22q4
---

# About GPUView

GPUView (*GPUView.exe*) is a development tool that reads logged video and kernel events from an [event trace log](/windows-hardware/drivers/devtest/trace-log) (.etl) file and presents the data graphically to the user.

* Video core developers can use GPUView to determine the performance of the GPU and CPU regarding DMA buffer processing, and all other video processing, on the video hardware.
* Developers and testers can use GPUView to show different kinds of events that might lead to unusual conditions like glitches, preparation delays, and poor synchronization.

## Quick start for using GPUView

To use GPUView, you first need to generate a trace. To do so:

* Open a command prompt with administrative privilege:
  * Find Start->All Programs->Accessories->Command Prompt
  * Right-click the command prompt icon and select Run as Administrator.

* Once at the command prompt, navigate to the GPUView directory and type the following command:

   ``` Log.cmd ```

* Reproduce the problem (no more than 30 seconds to 1 minute). Then retype the same command:

   ``` Log.cmd ```

   This command generates several Event Tracing for Windows (\*.ETL) files. These various streams are all merged together into a single file called *Merged.etl*, which is what GPUView reads.

* Use GPUView to view the resulting *Merged.ETL* file.

Some examples of logged events are:

* All CPU context switches, including the stack trace and the reason for switching.
* All kernel mode enters and exits and the stack trace.
* All GPU events as recorded by the DirectX Graphics Kernel, including all command buffer submissions, and resource creation, destruction, lock, and bind events.
* Events reported by the graphics driver, such as command buffer start and end times, and vertical synchronization intervals for each adapter.
* Many other system events that can affect performance, such as page faults.

You can also read ETL files with [XPerf](/windows-hardware/test/wpt/xperf-command-line-reference); however, it doesn't understand any of the GPU-specific events. Because these log files can be relatively large, you can use the `Log m` command instead, which skips many of the high frequency events.

More information, including how to download and use GPUView, can be found on Matthew Fisher's site, [Matt's Webcorner](https://graphics.stanford.edu/~mdfisher/GPUView.html), where he talks about creating GPUView.
