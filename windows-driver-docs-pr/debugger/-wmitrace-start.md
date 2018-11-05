---
title: wmitrace.start
description: The wmitrace.start extension starts the Event Tracing for Windows (ETW) logger on the target computer.
ms.assetid: 52ed0c5a-6ca9-4890-bae5-54394bc43d51
keywords: ["wmitrace.start Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wmitrace.start
api_type:
- NA
ms.localizationpriority: medium
---

# !wmitrace.start


The **!wmitrace.start** extension starts the Event Tracing for Windows (ETW) logger on the target computer.

```dbgcmd
!wmitrace.start LoggerName [-cir Size | -seq Size] [-f File] [-b Size] [-max Num] [-min Num] [-kd] [-ft Time] 
```

## <span id="ddk__wmitrace_strdump_dbg"></span><span id="DDK__WMITRACE_STRDUMP_DBG"></span>Parameters


<span id="_______LoggerName______"></span><span id="_______loggername______"></span><span id="_______LOGGERNAME______"></span> *LoggerName*   
Supplies a name to be used for the trace session. *LoggerName* cannot contain spaces or quotation marks.

<span id="_______-cir_______Size______"></span><span id="_______-cir_______size______"></span><span id="_______-CIR_______SIZE______"></span> **-cir** *Size*   
Causes the log file to be written in a circular manner. *Size* specifies the maximum file size, in bytes. When the file reaches this length, new data will be written to the file in a circular manner, overwriting the file from beginning to end. This cannot be combined with the **-seq** parameter. If neither **-cir** nor **-seq** is specified, the file is written in buffered mode.

<span id="_______-seq_______Num______"></span><span id="_______-seq_______num______"></span><span id="_______-SEQ_______NUM______"></span> **-seq** *Num*   
Causes the log file to be written in a sequential manner. *Size* specifies the maximum file size, in bytes. When the file reaches this length, the oldest data will be deleted from the beginning of the file whenever new data is appended to the end. This cannot be combined with the **-cir** parameter. If neither **-cir** nor **-seq** is specified, the file is written in buffered mode.

<span id="_______-f_______File______"></span><span id="_______-f_______file______"></span><span id="_______-F_______FILE______"></span> **-f** *File*   
Specifies the name of the log file to be created on the target computer. *File* must include an absolute directory path, and cannot contain spaces or quotation marks.

<span id="_______-b_______Size______"></span><span id="_______-b_______size______"></span><span id="_______-B_______SIZE______"></span> **-b** *Size*   
Specifies the size of each buffer, in kilobytes. The permissible range of *Size* is between 1 and 2048, inclusive.

<span id="_______-max_______Num______"></span><span id="_______-max_______num______"></span><span id="_______-MAX_______NUM______"></span> **-max** *Num*   
Specifies the maximum number of buffers to use. *Num* can be any positive integer.

<span id="_______-min_______Num______"></span><span id="_______-min_______num______"></span><span id="_______-MIN_______NUM______"></span> **-min** *Num*   
Specifies the minimum number of buffers to use. *Num* can be any positive integer.

<span id="_______-kd______"></span><span id="_______-KD______"></span> **-kd**   
Enables KD filter mode. Messages will be sent to the kernel debugger and displayed on the screen.

<span id="_______-ft_______Time______"></span><span id="_______-ft_______time______"></span><span id="_______-FT_______TIME______"></span> **-ft** *Time*   
Specifies the duration of the flush timer, in seconds. Starting in Windows 8, you can specify the flush timer duration in milliseconds by appending **ms** to the *Time* value. For example, **-ft 100ms**.

**Note**  If you start a tracing session in KD filter mode (**-kd**), trace buffers on the target computer are sent to the debugger on the host computer for display. This parameter specifies how often the buffers on the target computer are flushed and sent to the host computer.

 

### <span id="DLL"></span><span id="dll"></span>DLL

This extension is exported by Wmitrace.dll.

This extension is available in Windows 7 and later versions of Windows.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more details on the parameters of this extension, see [StartTrace Function](https://go.microsoft.com/fwlink/p/?linkid=139652) and [EVENT\_TRACE\_PROPERTIES](https://go.microsoft.com/fwlink/p/?linkid=139653). For a conceptual overview of event tracing, see the Microsoft Windows SDK. For information about tracing tools, see the Windows Driver Kit (WDK).

Remarks
-------

After using this extension, you must resume program execution (for example, by using the [**g (Go)**](g--go-.md) command) in order for it to take effect. After a brief time, the target computer automatically breaks into the debugger again.

When the trace session is started, the system assigns it an ordinal number (the *logger ID*). The session can then be referred to either by the logger name or the logger ID.

To stop the ETW logger, use [**!wmitrace.stop**](-wmitrace-stop.md).

 

 





