---
title: Starting and Exiting TraceView
description: Starting and Exiting TraceView
ms.assetid: ebadf441-c28a-4d8e-ae83-444c8a68f62b
keywords:
- TraceView WDK , starting
- TraceView WDK , exiting
- TraceView WDK , command-line interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Starting and Exiting TraceView


## <span id="ddk_starting_traceview_tools"></span><span id="DDK_STARTING_TRACEVIEW_TOOLS"></span>


This topic explains how to open and close the TraceView window.

### <span id="starting_traceview"></span><span id="STARTING_TRACEVIEW"></span>Starting TraceView

To start TraceView, in Windows Explorer, navigate to the \\tools\\tracing\\i386 subdirectory of the WDK and double-click the **TraceView.exe** icon.

Or, in a Command Prompt window, navigate to the \\tools\\tracing\\i386 subdirectory of the WDK, and type **traceview**.

### <span id="exiting_traceview"></span><span id="EXITING_TRACEVIEW"></span>Exiting TraceView

To exit TraceView, on the **File** menu, click **Exit**, or click the Close button in the upper right corner of the TraceView window.

When you exit TraceView, it disables the trace providers that are running in the trace sessions that it started, stops all trace sessions that are running in the TraceView window, and then closes. This process might take a few seconds to complete, during which Windows might notify you that TraceView is not responding. Do not force TraceView to close before it is ready.

Exiting TraceView does not stop trace sessions that were started by other methods, including the [TraceView command-line interface](traceview-command-line-interface.md). Those sessions continue to run until you stop them or shut down Windows.

### <span id="starting_the_traceview_command_line_interface"></span><span id="STARTING_THE_TRACEVIEW_COMMAND_LINE_INTERFACE"></span>Starting the TraceView Command-Line Interface

To start the TraceView at the command line, open a Command Prompt window, navigate to the \\tools\\tracing\\i386 directory of the WDK, and then type a TraceView command, such as **traceview /?**. (If you type **traceview** with no parameters, the TraceView window opens.)

For information about the TraceView commands, see [TraceView Command-Line Interface](traceview-command-line-interface.md).

 

 





