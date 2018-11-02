---
title: Survey of Software Tracing Tools
description: Survey of Software Tracing Tools
ms.assetid: d6b5d131-ed03-4961-9680-1c4ded35de96
keywords:
- software tracing WDK , tools listed
- tracing WDK , tools listed
- adding tracing
- software tracing WDK , adding
- tracing WDK , adding
- software tracing WDK , controlling sessions
- tracing WDK , controlling sessions
- software tracing WDK , TMF files
- tracing WDK , TMF files
- software tracing WDK , formatting messages
- tracing WDK , formatting messages
- software tracing WDK , displaying messages
- tracing WDK , displaying messages
- software tracing WDK , viewing events
- tracing WDK , viewing events
- trace consumers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Survey of Software Tracing Tools


## <span id="ddk_survey_of_software_tracing_tools_tools"></span><span id="DDK_SURVEY_OF_SOFTWARE_TRACING_TOOLS_TOOLS"></span>


The following software tracing tools are included in either the Windows Driver Kit (WDK) or the Windows operating system.

### <span id="enabling_wpp__tracing_in_a_trace_producer"></span><span id="ENABLING_WPP__TRACING_IN_A_TRACE_PRODUCER"></span>Enabling WPP tracing in a trace producer

-   TraceWPP (TraceWPP.exe) is a command-line tool that runs the Windows software trace preprocessor (WPP) on the source files of [trace providers](trace-provider.md), such as a kernel-mode driver or user-mode application.

    TraceWPP provides an alternative to setting the WPP options when you build your driver or application using the WDK and Visual Studio. This tool processes trace macros in a source file and creates a header file to enable WPP tracing.

    The command-line options for TraceWPP are the same as those used when the [TraceWPP task](tracewpp-task.md) is passed to MSBuild. For more information about these options, see [WPP Preprocessor](wpp-preprocessor.md).

    TraceWPP is located in the bin\\&lt;*Platform*&gt; directory of the WDK.

### <span id="controlling_trace_sessions__trace_controllers_"></span><span id="CONTROLLING_TRACE_SESSIONS__TRACE_CONTROLLERS_"></span>Controlling trace sessions (trace controllers)

-   [TraceView](traceview.md) (TraceView.exe) is a GUI-based [trace controller](trace-controller.md) and [trace consumer](trace-consumer.md), and is designed especially for the real-time display of trace messages. It enables, configures, starts, updates, and stops [trace session](trace-session.md). This tool also formats, filters, and displays trace messages from real-time trace sessions and [trace logs](trace-log.md).

    TraceView combines and extends the features of [Tracepdb](tracepdb.md), [Tracelog](tracelog.md), and [Tracefmt](tracefmt.md). For information, start TraceView and, from the **Help** menu, choose **Help Topics**.

    TraceView is located in the tools\\&lt;*Platform*&gt; subdirectory of the WDK, where &lt;*Platform*&gt; is either x86 or x64.

-   [Tracelog](tracelog.md) (Tracelog.exe) is a command-line [trace controller](trace-controller.md) that enables, configures, starts, updates, and stops real-time and log sessions. Tracelog supports user-mode and kernel-mode trace sessions, as well as [NT Kernel Logger trace sessions](nt-kernel-logger-trace-session.md) and the [Global Logger (boot) trace session](global-logger-trace-session.md). This tool also supports tracing to measure time spent in deferred procedure calls (DPCs) and interrupt service routines (ISRs).

    Tracelog is located in the tools\\&lt;*Platform*&gt; subdirectory of the WDK, where &lt;*Platform*&gt; is either x86 or x64.

-   Logman (Logman.exe) is a fully functional, GUI-based [trace controller](trace-controller.md) that is designed especially to control the logging of performance counters and event traces.

    Logman is included in Windows XP and later versions of Windows. For more information about how to use this tool, see the [Logman](http://go.microsoft.com/fwlink/p/?linkid=179385) topic on the TechNet website.

### <span id="creating_tmf_files"></span><span id="CREATING_TMF_FILES"></span>Creating TMF files

-   [Tracepdb](tracepdb.md) (Tracepdb.exe) is a command-line support tool that creates [trace message format (TMF) files](trace-message-format-file.md) from the trace message formatting instructions in [PDB symbol files](pdb-symbol-files.md).

    The tools that display trace messages, [Tracefmt](tracefmt.md)(Tracefmt.exe) and [TraceView](traceview.md)(TraceView.exe), can use the formatting instructions from the TMF files to format and display trace messages.

    Tracefmt can also create TMF files from [PDB symbol files](pdb-symbol-files.md).

    Tracepdb and Tracefmt are located in the tools\\tracing\\&lt;*Platform*&gt; subdirectory of the WDK, where &lt;*Platform*&gt; is either x86 or x64.

### <span id="formatting_and_displaying_trace_messages__trace_consumers_"></span><span id="FORMATTING_AND_DISPLAYING_TRACE_MESSAGES__TRACE_CONSUMERS_"></span>Formatting and displaying trace messages (trace consumers)

-   [Tracefmt](tracefmt.md) is a command-line [trace consumer](trace-consumer.md) that formats *trace messages* (**TraceMessage**) from real-time trace sessions or trace logs, and writes them to files or displays them in the Command Prompt window.

-   Tracerpt (Tracerpt.exe) is a command-line [trace consumer](trace-consumer.md) that formats *trace events* (**TraceEvent**) and performance counters and writes them to CSV or XML files. It also analyzes the events and generates summary reports.

    Tracerpt is included in Windows XP and later versions of Windows. For more information about how to use this tool, see [Tracerpt](http://go.microsoft.com/fwlink/p/?linkid=179389) topic on the TechNet website.

-   [TraceView](traceview.md), a GUI tool, that is a trace controller and a trace consumer, also formats and displays trace messages (**TraceMessage**) from real-time trace sessions or trace logs. It displays the trace messages in a tabular form, making them easier to filter and browse.

### <span id="viewing_trace_events_in_a_debugger"></span><span id="VIEWING_TRACE_EVENTS_IN_A_DEBUGGER"></span>Viewing trace events in a debugger

-   Debugging Tools for Windows includes **!wmitrace**, a specialized debugger extension that displays the trace messages in the trace session buffers before they are written to log files or delivered for display.

-   [Tracelog](tracelog.md) and [TraceView](traceview.md) can redirect trace messages to KD or Windbg, whichever is attached. For more information, see the Tracelog **-kd** parameter and the TraceView **Windbg** option.

### <span id="analyzing_dpc_and_isr_execution_times"></span><span id="ANALYZING_DPC_AND_ISR_EXECUTION_TIMES"></span>Analyzing DPC and ISR execution times

-   On Windows XP with Service Pack 2 (SP2) and later, you can use [Tracelog](tracelog.md) to log deferred procedure call (DPC) and interrupt service routine (ISR) events in the NT Kernel Logger trace session and then use Tracerpt to create summary reports from the logs. For more information about how to use this tool, including an example, see Tracelog.

 

 





