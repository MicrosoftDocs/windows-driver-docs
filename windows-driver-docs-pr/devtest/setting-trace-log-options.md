---
title: Setting Trace Log Options
description: Setting Trace Log Options
ms.assetid: 3790a3af-69bd-4ccc-a116-0df6312f378a
keywords:
- summary message files WDK TraceView
- listing message files WDK
- trace logs WDK TraceView , setting options
- log files WDK TraceView , setting options
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Trace Log Options


When you display a trace log, you can also create a listing file or a summary file. These text files let you display and manipulate log data easily. To set the trace log options, use the following procedure:

1.  On the **File** menu, click **Open Existing Log File**.

2.  In the **Log File Selection** dialog box, in the **Log File Options** area, select trace log options.

The following list describes the trace log options:

<span id="Create_Listing_File"></span><span id="create_listing_file"></span><span id="CREATE_LISTING_FILE"></span>**Create Listing File**  
Creates a formatted, readable text file version of the trace messages from a real-time trace session or a [trace log](trace-log.md).

In the associated text box, type a path and file name for the listing file. The default is "LogSession*N*", where *N* is a zero-based integer that represents the order in which the session is created.

<span id="Create_Summary_File"></span><span id="create_summary_file"></span><span id="CREATE_SUMMARY_FILE"></span>**Create Summary File**  
Generates a text file of statistical information about a real-time trace session or a trace log.

In the associated text box, type a path and file name for the summary file. The default is "LogSession*N*", where *N* is a zero-based integer that represents the order in which the session is created.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

If you specify an existing listing or summary file, TraceView overwrites the file without warning.

TraceView creates the summary file when you stop the trace session. If you close the TraceView window before stopping the trace session, TraceView does not create a summary file for the session.

 

 





