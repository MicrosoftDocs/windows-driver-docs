---
title: Creating a Trace Session
description: Creating a Trace Session
ms.assetid: 26f75b02-d830-4e3c-bbc9-03144d194e05
keywords:
- real-time trace sessions WDK
- trace log sessions WDK
- TraceView WDK , creating sessions
- trace sessions WDK , creating
- sessions WDK software tracing
- software tracing WDK , session creation
- tracing WDK , session creation
- trace logs WDK TraceView , sessions
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





