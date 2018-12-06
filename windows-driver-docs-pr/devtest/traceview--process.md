---
title: TraceView -process
description: Use a TraceView -process command to format the binary trace messages in a trace log or from a real-time trace seesion. The TraceView -process command creates a text file of a trace messages and a summary file that describes the input and output files.
ms.assetid: a0da5004-7a9f-4229-92c1-6264fcbf9b0d
keywords:
- TraceView -process Driver Development Tools
topic_type:
- apiref
api_name:
- TraceView -process
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TraceView -process


Use a **TraceView -process** command to format the binary trace messages in a [trace log](trace-log.md) or from a real-time trace seesion. The **TraceView -process** command creates a text file of a trace messages and a summary file that describes the input and output files.

```
    traceview -process [EtlFile | -rt SessionName][Parameters]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______EtlFile______"></span><span id="_______etlfile______"></span><span id="_______ETLFILE______"></span> *EtlFile*   
Specifies the event trace log (.etl) file that contains the trace messages. Enter the path (optional) and file name. The default is c:\\logfile.etl.

<span id="_______-rt_______SessionName______"></span><span id="_______-rt_______sessionname______"></span><span id="_______-RT_______SESSIONNAME______"></span> **-rt** *SessionName*   
Real time. Formats trace messages from the specified real-time trace sessions.

*SessionName* is the name of the trace session. If you omit the trace session name, Tracefmt formats messages from the [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md).

<span id="_______-tmf_______TMFFile______"></span><span id="_______-tmf_______tmffile______"></span><span id="_______-TMF_______TMFFILE______"></span> **-tmf** *TMFFile*   
Specifies the path (optional) and file name of the [trace message format (.tmf) file](trace-message-format-file.md) for the trace messages.

<span id="_______-p_______TMFPath______"></span><span id="_______-p_______tmfpath______"></span><span id="_______-P_______TMFPATH______"></span> **-p** *TMFPath*   
Specifies the path to the directory that contains the [trace message format (.tmf) file](trace-message-format-file.md) for the trace messages.

<span id="_______-o_______OutputFile______"></span><span id="_______-o_______outputfile______"></span><span id="_______-O_______OUTPUTFILE______"></span> **-o** *OutputFile*   
Specifies a name for the output files. This name applies to the text file of formatted trace messages and to a summary file.

*OutputFile* is a path and file name with a .txt file name extension, such as c:\\traces\\trace.txt. The default values are FmfFile.txt and FmtSum.txt in the local directory.

If you use this parameter with the **-displayonly** or **-summaryonly** parameter, it affects only the summary file.

<span id="_______-csv______"></span><span id="_______-CSV______"></span> **-csv**   
Formats the trace log as a comma-separated, variable length (.csv) file.

<span id="_______-display______"></span><span id="_______-DISPLAY______"></span> **-display**   
Displays the trace messages in the Command Prompt window, in addition to writing them to the output file.

<span id="_______-displayonly______"></span><span id="_______-DISPLAYONLY______"></span> **-displayonly**   
Displays the trace messages only in the Command Prompt window. TraceView does not create an text file of trace messages.

<span id="_______-nosummary______"></span><span id="_______-NOSUMMARY______"></span> **-nosummary**   
Does not create a [summary message file](summary-message-file.md).

<span id="_______-summaryonly______"></span><span id="_______-SUMMARYONLY______"></span> **-summaryonly**   
Creates only a [summary message file](summary-message-file.md). Tracefmt does not create an [output file](tracefmt-output-file.md).

<span id="_______-noprefix______"></span><span id="_______-NOPREFIX______"></span> **-noprefix**   
Omits the [trace message prefix](trace-message-prefix.md). This parameter affects trace messages in the output file and the Tracefmt display.

<span id="_______-ods______"></span><span id="_______-ODS______"></span> **-ods**   
Sends the formatted trace messages to the debugger for display.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Verbose. Displays detailed information in the Command Prompt window as Tracefmt processes each block or buffer of trace messages. Use this parameter when you suspect file damage or inconsistencies.

<span id="_______-h_____"></span><span id="_______-H_____"></span> **-h** | **/?**  
Displays help.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

```
traceview -process
traceview -process mytrace.etl -p c:\tracing -o mytrace.txt
traceview mytrace.etl -tmf c:\tracing\37753236-c81f-505e-d40a-128d3bb2b5ff.tmf
tracefmt -rt MyTrace -p c:\tracing -o mytrace.txt -display
```

### <span id="comments"></span><span id="COMMENTS"></span>Comments

To format trace messages, you must specify a trace message format file for the trace messages. The available methods are listed in order of precedence:

-   The **-tmf** parameter.

-   The **-p** parameter.

-   The %TRACE\_FORMAT\_SEARCH\_PATH% environment variable. Sets the value of the variable to the directory in which the TMF file is located.

If the TMF file name is not a [message GUID](message-guid.md), use the **-tmf** parameter and enter the fully qualified path to the file. Otherwise, TraceView will not find the TMF file.

If TraceView cannot find a TMF file, or the TMF file does not include formatting information for the trace messages, TraceView cannot format the messages. Instead, in place of the message text, TraceView writes: "No Format Information found."

If TraceView cannot format a trace message, it raises an exception and displays a message such as:

```
*****FormatMessage Header(Header) of EventTrace, parameter 23 raised an exception*****
```









