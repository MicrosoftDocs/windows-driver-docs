---
title: Starting and Exiting TraceView
description: Starting and Exiting TraceView
ms.assetid: ebadf441-c28a-4d8e-ae83-444c8a68f62b
keywords: ["TraceView WDK , starting", "TraceView WDK , exiting", "TraceView WDK , command-line interface"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Starting%20and%20Exiting%20TraceView%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




