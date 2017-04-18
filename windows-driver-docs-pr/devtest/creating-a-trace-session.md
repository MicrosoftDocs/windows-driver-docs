---
title: Creating a Trace Session
description: Creating a Trace Session
ms.assetid: 26f75b02-d830-4e3c-bbc9-03144d194e05
keywords: ["real-time trace sessions WDK", "trace log sessions WDK", "TraceView WDK , creating sessions", "trace sessions WDK , creating", "sessions WDK software tracing", "software tracing WDK , session creation", "tracing WDK , session creation", "trace logs WDK TraceView , sessions"]
---

# Creating a Trace Session


## <span id="ddk_creating_a_real_time_trace_session_tools"></span><span id="DDK_CREATING_A_REAL_TIME_TRACE_SESSION_TOOLS"></span>


This section explains how to use TraceView to create a real-time trace session or a trace log session.

When you *create* a [trace session](trace-session.md), TraceView configures and starts the trace session and enables the [trace providers](trace-provider.md) that you specify, such as the providers in a driver that is instrumented for event tracing.

TraceView uses wizard pages to guide you through the steps of creating the trace session.

TraceView requires that you specify at least one trace provider when creating a trace session. The provider type and the files that are available determine the method that you use to create the trace session.

This section includes:

[Creating a trace session with a PDB file](creating-a-trace-session-with-a-pdb-file.md)

[Creating a trace session with a CTL file](creating-a-trace-session-with-a-ctl-file.md)

[Creating a trace session with a Control GUID](creating-a-trace-session-with-a-control-guid.md)

[Creating a trace session for a registered provider](creating-a-trace-session-for-a-registered-provider.md)

[Creating an NT Kernel Logger trace session](creating-an-nt-kernel-logger-trace-session.md)

[Joining a Trace Session](joining-a-trace-session.md)

[Removing a Trace Provider](removing-a-trace-provider.md)

[Setting Basic Trace Session Options](setting-basic-trace-session-options.md)

[Selecting Flags and Levels](selecting-flags-and-levels.md)

[Setting Advanced Trace Session Options](setting-advanced-trace-session-options.md)

### <span id="comments"></span><span id="COMMENTS"></span>Comments

TraceView requires a [PDB symbol file](pdb-symbol-files.md), a [trace message format (TMF) file](trace-message-format-file.md), or a TMF directory when creating a trace session. TraceView does not use the %TRACE\_FORMAT\_SEARCH\_PATH% environment variable.

When you use the TraceView window to create a trace session, the trace session runs only as long as the window remains open. You cannot close the window and leave the session running. To start a trace session that runs independently of the TraceView window, use the [TraceView command-line interface](traceview-command-line-interface.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Creating%20a%20Trace%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




