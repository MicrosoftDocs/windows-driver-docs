---
title: Joining a Trace Session
description: Joining a Trace Session
ms.assetid: 0fd065e4-004f-426a-bdb1-4b2e7d219e20
keywords: ["trace sessions WDK , joining", "tracing WDK , in-progress sessions", "in-progress tracing sessions WDK", "software tracing WDK , in-progress sessions", "stopping trace sessions", "canceling trace sessions", "restarting trace sessions"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Joining%20a%20Trace%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




