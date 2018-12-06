---
title: Joining a Trace Session
description: Joining a Trace Session
ms.assetid: 0fd065e4-004f-426a-bdb1-4b2e7d219e20
keywords:
- trace sessions WDK , joining
- tracing WDK , in-progress sessions
- in-progress tracing sessions WDK
- software tracing WDK , in-progress sessions
- stopping trace sessions
- canceling trace sessions
- restarting trace sessions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Joining a Trace Session


In rare situations, such as when you force TraceView to exit while it is controlling a running trace session, TraceView does not disable the session providers and stop the trace session. In this situation, when you try to start a trace session with the provider that is still enabled, TraceView displays a warning and offers to stop and restart the session or to let you join the trace session that is already in progress.

The options in the dialog box are as follows:

<span id="Yes_-_Stop_and_Restart_the_Log_Session"></span><span id="yes_-_stop_and_restart_the_log_session"></span><span id="YES_-_STOP_AND_RESTART_THE_LOG_SESSION"></span>**Yes - Stop and Restart the Log Session**  
TraceView stops the trace session and then starts a new trace session with the same providers and same properties.

<span id="No_-_Join_the_Log_Session_Without_Stopping"></span><span id="no_-_join_the_log_session_without_stopping"></span><span id="NO_-_JOIN_THE_LOG_SESSION_WITHOUT_STOPPING"></span>**No - Join the Log Session Without Stopping**  
TraceView retrieves and saves the session properties and joins the trace session. You can use TraceView to change the properties of the trace session, but TraceView cannot stop the trace session. To stop the trace session, [exit TraceView](starting-and-exiting-traceview.md).

<span id="Cancel_-_Abort_Start_Operation"></span><span id="cancel_-_abort_start_operation"></span><span id="CANCEL_-_ABORT_START_OPERATION"></span>**Cancel - Abort Start Operation**  
TraceView cancels the attempt to start the trace session.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The TraceView window displays only those running trace sessions that it started. To list all trace sessions that are running on the system, type **traceview -l** in a Command Prompt window. To stop trace sessions that TraceView did not start, type **traceview -stop***SessionName* in a Command Prompt window. For more information about these commands, see [TraceView Command-Line Interface](traceview-command-line-interface.md).

 

 





