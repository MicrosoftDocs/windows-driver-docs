---
title: Tracefmt Commands
description: To use Tracefmt, type the commands in a Command Prompt window.
ms.assetid: 79e56383-ce67-4716-98d6-4266b76a4b0a
keywords:
- Tracefmt Commands Driver Development Tools
topic_type:
- apiref
api_name:
- Tracefmt Commands
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tracefmt Commands


To use Tracefmt, type the commands in a Command Prompt window. The following syntax displays the elements of a Tracefmt command.

To display the trace messages in readable form, Tracefmt must apply the formatting instructions in a trace message format file to the trace messages. The syntax that you use depends on whether you have a TMF file for the trace provider, or whether you want Tracefmt to create a TMF file.

To provide a TMF file or a path to a directory of TMF files:

```
    tracefmt [EtlFile | -rt SessionName][-tmf TMFFile | -p TMFPath ] [Options]
```

To create a TMF file:

```
    tracefmt [EtlFile | -rt SessionName]-i ImageFiles [-r SymbolPath ] [-p TmfPath ] [Options]
```

To display the syntax at the command line.

```
    tracefmt -h | /?
```

## <span id="ddk_tracefmt_commands_tools"></span><span id="DDK_TRACEFMT_COMMANDS_TOOLS"></span>Parameters


<span id="_______EtlFile______"></span><span id="_______etlfile______"></span><span id="_______ETLFILE______"></span> *EtlFile*   
Specifies the event trace log (.etl) file that contains the trace messages. Enter the path (optional) and file name. The default is c:\\logfile.etl.

<span id="_______-rt________SessionName______"></span><span id="_______-rt________sessionname______"></span><span id="_______-RT________SESSIONNAME______"></span> **-rt** *SessionName*   
Real time. Formats trace messages from the specified real-time trace sessions, instead of from a [trace log](trace-log.md).

*SessionName* is the name of the trace session. The default is [NT Kernel Logger](nt-kernel-logger-trace-session.md).

<span id="_______-tmf_______TMFFile______"></span><span id="_______-tmf_______tmffile______"></span><span id="_______-TMF_______TMFFILE______"></span> **-tmf** *TMFFile*   
Specifies the path (optional) and file name of a [trace message format (.tmf) file](trace-message-format-file.md) for the trace messages. The default value is Default.tmf, a file included in the WDK.

<span id="_______-i_______ImageFiles______"></span><span id="_______-i_______imagefiles______"></span><span id="_______-I_______IMAGEFILES______"></span> **-i** *ImageFiles*   
Directs Tracefmt to find the PDB symbol files for the specified image files and to create a TMF file from the formatting instructions in the PDB files.

*ImageFiles* represents the path and file names of one or more binary files (.exe, .dll, or .sys) for [trace providers](trace-provider.md). Use a semicolon (;) to separate image file names.

<span id="_______-r_______SymbolPaths______"></span><span id="_______-r_______symbolpaths______"></span><span id="_______-R_______SYMBOLPATHS______"></span> **-r** *SymbolPaths*   
Specifies the location of the private PDB symbol files for the image files specified in **-i**.

*SymbolPaths* represents one or more paths to directories that store private symbols or symbol server paths. Use a semicolon (;) to separate path names. The path names in *SymbolPaths* can include wildcard characters, such as an asterisk (\*) to represent multiple characters and a question mark (?) to represent a single character.

If you include **-i** in a command, but omit **-r**, Tracepdb searches for the PDB files for the specified images in the paths specified by the %\_NT\_SYMBOL\_PATH% environment variable. If the environment variable is not set, Tracepdb searches in the default symbol path, **srv\*\\\\\\\\symbols\\\\symbols**.

<span id="_______-p_______TMFPath______"></span><span id="_______-p_______tmfpath______"></span><span id="_______-P_______TMFPATH______"></span> **-p** *TMFPath*   
Specifies the path to the directory that stores TMF files.

When **-p** is used without **-i**, Tracefmt searches in the path specified by **-p** for an existing TMF file. If **-p** is omitted Tracefmt looks for the TMF file in the value of the %TRACE\_FORMAT\_SEARCH\_PATH% environment variable, if it is set. Otherwise, Tracefmt tries to apply the formatting instructions in the Default.tmf file.

When **-p** is used with **-i**, Tracefmt places the TMF file that it creates in the directory specified by **-p**. If **-p** is omitted, Tracefmt places the TMF file in the directory specified by the value of the %TRACE\_FORMAT\_SEARCH\_PATH% environment variable, if it is set. Otherwise, Tracefmt places the file in the local directory.

<span id="_______-h_____"></span><span id="_______-H_____"></span> **-h** | **/?**  
Displays help.

<span id="_______-o_______OutputFile______"></span><span id="_______-o_______outputfile______"></span><span id="_______-O_______OUTPUTFILE______"></span> **-o** *OutputFile*   
Specifies alternate names for the [Tracefmt output file](tracefmt-output-file.md) and the [Tracefmt summary message file](summary-message-file.md). The default values are FmfFile.txt (for the output file) and FmtSum.txt.sum (for the summary file) in the local directory.

*OutputFile* is a path and file name with a .txt file name extension, such as c:\\traces\\trace.txt.

If you use this parameter with the **-displayonly** or **-summaryonly** options, it affects only the summary message file.

<span id="_______-csv______"></span><span id="_______-CSV______"></span> **-csv**   
Formats the [Tracefmt output file](tracefmt-output-file.md) as a comma-separated, variable length (.csv) file. This format adds a detailed, structured prefix to each message, in addition to the standard [trace message prefix](trace-message-prefix.md).

This option affects the output file and the display of trace messages in the Command Prompt window, if any.

<span id="_______-csvheader______"></span><span id="_______-CSVHEADER______"></span> **-csvheader**   
Adds a row of descriptive column headings to the CSV file. This header is especially useful for interpreting the structured prefix that Tracefmt adds to CSV files. By default, Tracefmt CSV files do not have column headings.

<span id="_______-csvquote______"></span><span id="_______-CSVQUOTE______"></span> **-csvquote**   
Doubles all quotations marks (") in the CSV file. This feature is designed for applications that display quotation marks only when they are enclosed in quotation marks.

<span id="_______-display______"></span><span id="_______-DISPLAY______"></span> **-display**   
Displays the trace messages in the Command Prompt window, in addition to writing them to the output file.

<span id="_______-displayonly______"></span><span id="_______-DISPLAYONLY______"></span> **-displayonly**   
Displays the trace messages only in the Command Prompt window, and does not create an output file.

<span id="_______-nosummary______"></span><span id="_______-NOSUMMARY______"></span> **-nosummary**   
Does not create a [summary message file](summary-message-file.md).

<span id="_______-summaryonly______"></span><span id="_______-SUMMARYONLY______"></span> **-summaryonly**   
Creates only a [summary message file](summary-message-file.md). Tracefmt does not create an [output file](tracefmt-output-file.md).

<span id="_______-noprefix______"></span><span id="_______-NOPREFIX______"></span> **-noprefix**   
Omits the [trace message prefix](trace-message-prefix.md). This option affects trace messages in the output file and the Tracefmt display.

<span id="_______-hires______"></span><span id="_______-HIRES______"></span> **-hires**   
High resolution. Displays the number of microseconds and nanoseconds in the trace message time stamp. By default, only milliseconds are displayed.

Use this option when a performance counter clock value is used for the trace message time stamp, instead of the system timer, such as when the **Tracelog -UsePerfCounter** parameter is used. For information about Tracelog commands, see [**Tracelog Command Syntax**](tracelog-command-syntax.md).

<span id="_______-seq______"></span><span id="_______-SEQ______"></span> **-seq**   
Displays the local or global sequence numbers in the [trace message prefix](trace-message-prefix.md). If sequence numbers were not recorded in the message, the field is uninitialized, or filled with zeros or "f"s.

<span id="_______-ods______"></span><span id="_______-ODS______"></span> **-ods**   
Sends the formatted trace messages to the debugger for display.

<span id="_______-gmt______"></span><span id="_______-GMT______"></span> **-gmt**   
Displays the time stamp on each trace message in Greenwich Mean Time (GMT).

This option affects only the Tracefmt output file. It does not convert the time stamps in the event trace log (.etl) file. The time zone of the trace log is displayed when you submit a Tracefmt command.

<span id="_______-utc______"></span><span id="_______-UTC______"></span> **-utc**   
Displays the time stamp on each trace message in Coordinated Universal Time (UTC). UTC is almost identical to GMT, but it represents midnight as zero.

This option affects only the Tracefmt output file. It does not convert the time stamps in the event trace log (.etl) file. The time zone of the trace log file is displayed when you submit a Tracefmt command.

<span id="_______-trace______"></span><span id="_______-TRACE______"></span> **-trace**   
Displays Tracefmt actions as they occur. This information is useful when the formatting is incorrect or when Tracefmt reports an error or exception.

The trace display can be extensive. Consider redirecting the Tracefmt output to a text file for later examination.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Verbose. Displays detailed information in the Command Prompt window as Tracefmt processes each block or buffer of trace messages. Use this option when you suspect file damage or inconsistencies.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

**Finding the TMF file**

If you omit the **-i** parameter, Tracefmt use the following methods to find the TMF file. The methods are listed in order that Tracefmt uses them.

-   The **-tmf** parameter.

-   The **-p** parameter.

-   The %TRACE\_FORMAT\_SEARCH\_PATH% environment variable.

-   Default.tmf, a file included in the WDK.

If Tracefmt cannot find a TMF file, or the TMF file does not include formatting information for the trace messages, Tracefmt cannot display the messages. Instead, it writes the following error message in place of the trace message

```
No Format Information found.
```

**Exception Raised**

If Tracefmt cannot format a trace message parameter, it raises an exception and displays a message such as:

```
*****FormatMessage Header(Header) of EventTrace, parameter 23 raised an exception*****
```

If you see a similar exception, review the message definition in the source code, with special attention to any user-specified variable types. For more information, see [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918).

**TMF files with non-GUID file names**

If the TMF file name is not a [message GUID](message-guid.md), you must use the -tmf parameter to identify the file and enter the fully qualified path to the file.

**Formatting NT Kernel Logger trace messages**

To format messages from the [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md) or a [Global Logger trace session](global-logger-trace-session.md), use the -tmf parameter to specify the system.tmf file, a [trace message format file](trace-message-format-file.md) included in the WDK..

**Formatting trace messages from real-time trace sessions**

When you use the **-rt** (real-time) parameter, Tracefmt displays a message confirming that it is in real-time mode, and then waits for trace messages from the specified trace provider. It does not return to the command prompt until the trace session stops.

**Formatting QPC time stamps**

Tracefmt does not format the values of the system performance counter clock (**QueryPerformanceCounter**) correctly. If you are using this high resolution time, use Tracerpt, a tool included in Windows XP and later versions of Windows, to format the trace messages. For more information, see the description of the **-UsePerfCounter** parameter in [**Tracelog Command Syntax**](tracelog-command-syntax.md).

**Out-of-sequence trace messages**

If you view a trace message file on a computer running Windows XP, the display might show trace messages that are out of sequence. To correct this problem, you can use the sequence number option when you start the trace session and view the trace using Tracefmt. You can then view the trace with Traceview and sort according to sequence number. You can also view the trace on a computer running Windows Server 2003 or later versions of Windows.









