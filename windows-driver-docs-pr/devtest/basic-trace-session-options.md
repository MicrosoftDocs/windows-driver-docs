---
title: Basic Trace Session Options
description: Basic Trace Session Options
ms.assetid: c997310f-79dc-4c94-945e-13a0a7786928
keywords:
- trace sessions WDK , basic options
- tracing WDK , basic options
- software tracing WDK , basic options
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Basic Trace Session Options


The following list describes the basic trace session options that you can change on the **Log Session Options** page.

<span id="Real_Time_Display"></span><span id="real_time_display"></span><span id="REAL_TIME_DISPLAY"></span>**Real Time Display**  
Creates a [real-time trace session](trace-session.md#ddk_real_time_trace_sessions_tools).This option is selected by default.

You must select **Log Trace Event Data To File,Real Time Display**, or both.

<span id="Log_Session_Name"></span><span id="log_session_name"></span><span id="LOG_SESSION_NAME"></span>**Log Session Name**  
Specifies a name for the trace session. Select any name that meets the Windows naming standards.The default is "LogSession*N*", where *N* is a zero-based integer that represents the order in which the session is created.

After a trace session is named, you can refer to the session by its name (for example, when you are using the [TraceView command-line interface](traceview-command-line-interface.md)).

<span id="Log_Trace_Event_Data_To_File__"></span><span id="log_trace_event_data_to_file__"></span><span id="LOG_TRACE_EVENT_DATA_TO_FILE__"></span>**Log Trace Event Data To File**   
Creates a [trace log session](trace-session.md#ddk_trace_log_sessions_tools).

You must select **Log Trace Event Data To File**, **Real Time Display**, or both.

<span id="Log_File_Name"></span><span id="log_file_name"></span><span id="LOG_FILE_NAME"></span>**Log File Name**  
Specifies a path and file name for the [trace log](trace-log.md) (.etl). This option is enabled only when the **Log Trace Event Data To File** option is selected.

By default, the trace log is named "LogSession<em>\_date\_time</em>.etl" and it is saved in the local directory. To change the name or location, type a path and file name in the text box or, to navigate to a directory, click the ellipsis button (...).

**Caution**  If you select the path and name of an existing file, TraceView overwrites that file without warning.

 

<span id="Append_To_Existing_Log_File"></span><span id="append_to_existing_log_file"></span><span id="APPEND_TO_EXISTING_LOG_FILE"></span>**Append To Existing Log File**  
Adds the trace messages to the end of the trace log file that is specified in the **Log File Name** box, instead of overwriting the file.

This option is enabled only when **Log Trace Event Data To File** is enabled and **Real Time Display** is disabled. You cannot append real-time events to an existing trace log.

TraceView lets you select this option, even if the specified file does not yet exist.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The trace session name is not saved in the event trace log (.etl) file, the TraceView output file, or the TraceView summary file. When you use TraceView to display a trace log, it uses the default session name, "LogSession*N*" as the name of the trace session, where *N* is a zero-based integer that represents the order in which the session is created.

 

 





