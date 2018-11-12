---
title: Creating Text Versions of Trace Logs
description: Creating Text Versions of Trace Logs
ms.assetid: 15d15da3-e381-4b5f-81f2-300aa87e11db
keywords:
- TraceView WDK , text version trace logs
- trace logs WDK TraceView , text versions
- log files WDK TraceView , text versions
- Trace Message Lists WDK
- text format trace logs WDK
- listing files WDK software tracing
- .out files
- out files
- converting trace log format
- formats WDK audio , trace logs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Text Versions of Trace Logs


The trace messages that are generated during trace log sessions are saved in [trace logs](trace-log.md), which are binary files that are designed to store large volumes of trace messages efficiently. TraceView has several convenient methods for creating human-readable versions of these files.

### <span id="creating_a_listing_file_for_a_real_time_trace_session"></span><span id="CREATING_A_LISTING_FILE_FOR_A_REAL_TIME_TRACE_SESSION"></span>Creating a listing file for a real-time trace session

The **Create Listing File** option creates a *listing file* (.out), a text file of all trace messages that are generated during the session. You can use this option only while creating a trace session. To create a listing file for a real-time trace session, do the following:

1.  From the **File** menu, select **Create New Log Session**.

2.  Add providers, and then click **Next**.

3.  In the **Log Session Options** page, click **Advanced Log Session Options**.

4.  In the **Output Files** tab, click **Create Listing File**.

For more information, see [Setting Advanced Trace Session Options](setting-advanced-trace-session-options.md)

### <span id="creating_a_listing_file_for_an_existing_log_file"></span><span id="CREATING_A_LISTING_FILE_FOR_AN_EXISTING_LOG_FILE"></span>Creating a listing file for an existing log file

While starting a trace log session, you can use the **Create Listing File** option to create a text version of the trace log. To create a listing file for an existing log file, do the following:

1.  On the **File** menu, click **Open Existing Log File**.

2.  In the **Log File Selection** dialog box, select **Create Listing File**.

3.  In the **Log File Name** box, specify the name of the existing event trace log (.etl) file.

When you display the trace log, TraceView creates the listing file. For more information, see [Setting Trace Log Options](setting-trace-log-options.md).

### <span id="converting_a_trace_log_to_text_format"></span><span id="CONVERTING_A_TRACE_LOG_TO_TEXT_FORMAT"></span>Converting a trace log to text format

Use the [TraceView command-line interface](traceview-command-line-interface.md) to convert an event trace log (.etl) file to a text-formatted listing file by using the following command:

```
traceview -process ETLFile { -pdb PDBFile | -tmf TMFFile | -p TMFPath } [-o OutputFile] 
```

For example:

```
traceview -process mytrace.etl -p c:\tracetools -o mytrace.out
```

For more information, see [**TraceView -process**](traceview--process.md).

### <span id="copying_the_trace_message_list"></span><span id="COPYING_THE_TRACE_MESSAGE_LIST"></span> Copying the Trace Message List

You can copy trace messages directly from the Trace Message List for an existing trace log or running trace session.

This procedure gives you the most control over the display. You can copy the messages after [grouping trace sessions](grouping-trace-sessions.md), selecting the columns (that is, trace message properties) that you want to display, and sorting and filtering the trace messages. You can also select individual messages from the display. To copy trace messages from the Trace Message List, do the following:

1.  Select the trace messages that you want to copy. You can use SHIFT+Click to select consecutive messages or CTRL+Click to copy non-consecutive messages.

2.  Press CTRL+C. Or, right-click any cell of any selected messages and click **Copy**.

The messages are copied in a tab-delimited format. You can paste them into a text file or spreadsheet file for saving and analysis.

 

 





