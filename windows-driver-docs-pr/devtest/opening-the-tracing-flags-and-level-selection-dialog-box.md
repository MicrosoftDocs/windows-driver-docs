---
title: Opening the Tracing Flags and Level Selection dialog box
description: Opening the Tracing Flags and Level Selection dialog box
ms.assetid: f6ee808e-ea29-492b-b161-0a3b57140214
keywords:
- trace flags WDK
- flags WDK software tracing
- trace levels WDK
- levels WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening the Tracing Flags and Level Selection dialog box


You can use the **Tracing Flags and Level Selection** dialog box to select and change the flags and level of providers when you create the session and while the session is running.

### <span id="while_creating_a_trace_session"></span><span id="WHILE_CREATING_A_TRACE_SESSION"></span>While creating a trace session

1.  [Start TraceView.](starting-and-exiting-traceview.md)

2.  On the **File** menu, click **Create New Log Session**.

3.  Click **Add Provider** and add a provider.

4.  Add additional providers, if desired..

5.  Click **Next**.

6.  On the **Log Session Options** page, click the **Set Flags and Level** button.

### <span id="while_a_trace_session_is_running"></span><span id="WHILE_A_TRACE_SESSION_IS_RUNNING"></span>While a trace session is running

1.  In the [Trace Session List](trace-session-list.md), locate the row for the trace session.

2.  Locate the **Flags** or **Level** column of that row and click the **SET** value. (The value is **SET** when you use a PDB file to identify the session provider.)

3.  Clicking **SET** opens the **Tracing Flags and Level Selection** dialog box.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **Set Flags and Level** option is enabled only when TraceView can find a [PDB symbol file](pdb-symbol-files.md) for the provider or when it can find a [trace message control (.tmc) file](trace-message-control-file.md) for the provider in the TMF path (specified by using the **Set TMF Search Path** option).

 

 





