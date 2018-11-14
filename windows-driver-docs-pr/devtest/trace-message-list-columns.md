---
title: Trace Message List Columns
description: Trace Message List Columns
ms.assetid: d0f5873e-9b01-4a74-8448-90194545da1f
keywords:
- Trace Message Lists WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Trace Message List Columns


The columns in the Trace Message List represent properties of the trace message, similar to those that typically appear in the [trace message prefix](trace-message-prefix.md). You can display and hide the columns, but you cannot reorder them.

By default, the **ID** field and the first eight columns that are described in the following list appear in a Trace Message List. For more information about choosing which columns to display, see Displaying and Hiding Columns.

<span id="ID"></span><span id="id"></span>**ID**  
The **ID** appears in Trace Message List window frame. It displays the *Group ID* of the trace session, an identifier that TraceView assigns to trace sessions and trace session groups. The **Group ID** also appears in the first column of [Trace Session List](trace-session-list.md) to help you associate the trace session with its trace messages.

<span id="Msg_"></span><span id="msg_"></span><span id="MSG_"></span>**Msg\#**  
Displays the message number of the trace message. By default, the Trace Message List is sorted by the values in the **Msg\#** column.

<span id="Name"></span><span id="name"></span><span id="NAME"></span>**Name**  
Displays the friendly name of the [message GUID](message-guid.md) of the trace message. By default, the friendly name of the message GUID is the name of the directory in which the trace provider was built.

For the [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md), this column displays the name of the kernel tracing subcomponent that generated the message (for example, "FileIo").

You can use the **-p** parameter of RUN\_WPP or Tracewpp to specify an alternate value for the friendly name of the message GUID. For information, see Run\_WPP Options.

<span id="Process_ID"></span><span id="process_id"></span><span id="PROCESS_ID"></span>**Process ID**  
Identifies the process that generated the trace message.

<span id="Thread_ID"></span><span id="thread_id"></span><span id="THREAD_ID"></span>**Thread ID**  
Identifies the thread that generated the trace message.

<span id="CPU_"></span><span id="cpu_"></span>**CPU\#**  
Identifies the CPU on which the trace message was generated.

<span id="Sequence_"></span><span id="sequence_"></span><span id="SEQUENCE_"></span>**Sequence\#**  
Displays the local or global sequence number of the trace message. Local sequence numbers, which are unique only to this trace session, are the default value.

<span id="System_Time"></span><span id="system_time"></span><span id="SYSTEM_TIME"></span>**System Time**  
Displays the system timer value when the trace message was generated. Because the system timer has a resolution of 10 milliseconds, multiple events can have the same system time value.

<span id="Message"></span><span id="message"></span><span id="MESSAGE"></span>**Message**  
Displays the trace message.

<span id="File_Name"></span><span id="file_name"></span><span id="FILE_NAME"></span>**File Name**  
Displays the name of the source file that generated the trace message.

<span id="Line__"></span><span id="line__"></span><span id="LINE__"></span>**Line \#**  
Displays the line number of the code that generated the trace message.

<span id="Func_Name"></span><span id="func_name"></span><span id="FUNC_NAME"></span>**Func Name**  
Displays the name of the function that generated the trace message.

<span id="Kernel_Time"></span><span id="kernel_time"></span><span id="KERNEL_TIME"></span>**Kernel Time**  
Displays the elapsed execution time for kernel-mode instruction, in CPU ticks, at the time that the trace message was generated.

<span id="User_Time"></span><span id="user_time"></span><span id="USER_TIME"></span>**User Time**  
Displays the elapsed execution time for user-mode instruction, in CPU ticks, at the time that the trace message was generated.

<span id="Indent"></span><span id="indent"></span><span id="INDENT"></span>**Indent**  
Displays the number of spaces that the trace message is indented when it is written to a text log.

<span id="Flags_Name"></span><span id="flags_name"></span><span id="FLAGS_NAME"></span>**Flags Name**  
Displays the name of the [trace flags](trace-flags.md) that were enabled for the provider when the trace message was generated.

<span id="Level_Name"></span><span id="level_name"></span><span id="LEVEL_NAME"></span>**Level Name**  
Displays the value of the [trace level](trace-level.md) that was enabled for the provider when the trace message was generated.

<span id="Component_Name"></span><span id="component_name"></span><span id="COMPONENT_NAME"></span>**Component Name**  
Displays the name of the component of the provider that generated the trace message. The component name appears only if it is specified in the tracing code.

<span id="SubComponent_Name"></span><span id="subcomponent_name"></span><span id="SUBCOMPONENT_NAME"></span>**SubComponent Name**  
Displays the name of the subcomponent of the provider that generated the trace message. The subcomponent name appears only if it is specified in the tracing code.

<span id="Save_As_Default"></span><span id="save_as_default"></span><span id="SAVE_AS_DEFAULT"></span>**Save As Default**  
This option is not a column name. It is a command that saves the currently displayed column configuration as the default for future trace sessions. For more information, see "Saving the Column Configuration" in [Trace Message List Features](trace-message-list-features.md).

 

 





