---
title: Resolving TraceView Errors
description: Resolving TraceView Errors
ms.assetid: 4849e0b6-5dc9-4666-b1ca-ec89cb94bed0
keywords:
- TraceView WDK , errors
- errors WDK TraceView
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Resolving TraceView Errors


This topic describes errors that TraceView commonly reports and suggests solutions. It is not intended to be a complete troubleshooting guide.

### <span id="trace_provider_is_not_added"></span><span id="TRACE_PROVIDER_IS_NOT_ADDED"></span>Trace provider is not added

If TraceView cannot find a [PDB symbol file](pdb-symbol-files.md) or a [trace message format (.tmf) file](trace-message-format-file.md) for the trace provider, it does not add the trace provider to the provider list in the **Create New Log Session** dialog box, and it does not display a message that explains why the provider was not added.

If the provider does not appear in the provider list after you try to add it, restart the procedure and, in the **Format Information Source Select** dialog box, click **Select TMF Files** instead of **Set TMF Search Path**. If you cannot locate a PDB file or a TMF file for the provider, you cannot use TraceView to create a trace session with the provider.

### <span id="failed_to_enable_trace_for_control_guid__guid"></span><span id="FAILED_TO_ENABLE_TRACE_FOR_CONTROL_GUID__GUID"></span>Failed To Enable Trace For Control GUID: *guid*

This error typically occurs when more than one trace consumer is collecting events from a single trace provider on the system. To resolve this conflict, display all trace sessions that are running on the computer, and stop sessions that are conflicting.

To display all trace sessions on the computer, in a Command Prompt window, type **traceview -l**. (The TraceView window displays only the trace sessions that are running in TraceView.) The resulting display lists the active sessions.

To stop a trace session, in a Command Prompt window, type **traceview -stop***SessionName*.

For more information about these commands, see [**TraceView Control Commands**](traceview-control-commands.md).

### <span id="cannot_open_logfile_for_reading"></span><span id="CANNOT_OPEN_LOGFILE_FOR_READING"></span>Cannot open logfile for reading

This error occurs when you try to display an existing trace log for a trace provider that is providing events for a real-time trace session or another existing trace log in TraceView.

TraceView can create only one trace session or display one trace log for each trace provider.

### <span id="cannot_connect_to_any_trace_session_in_the_group"></span><span id="CANNOT_CONNECT_TO_ANY_TRACE_SESSION_IN_THE_GROUP"></span>Cannot connect to any trace session in the group

This error typically appears when you try to group trace sessions that cannot be grouped. For example, it appears when you try to include a real-time trace session in a group on a version of Windows earlier than Windows Server 2003.

To resolve this error, review the [Limitations of Grouping](limitations-of-grouping.md) topic and include only trace sessions that you can group on your system.

### <span id="internal_error__closetrace_error_170"></span><span id="INTERNAL_ERROR__CLOSETRACE_ERROR_170"></span>Internal error: CloseTrace error 170

This error occurs when you try to join an NT Kernel Logger trace session that is already in progress. You can use TraceView to create an NT Kernel Logger trace session, but you cannot join an NT Kernel Logger trace session that is started by a tool or method other than TraceView.

For more information, see [Joining a Trace Session](joining-a-trace-session.md) and [Creating an NT Kernel Logger trace session](creating-an-nt-kernel-logger-trace-session.md).

 

 





