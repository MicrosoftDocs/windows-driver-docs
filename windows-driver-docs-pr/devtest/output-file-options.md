---
title: Output File Options
description: Output File Options
ms.assetid: f53785d8-2a91-47da-945c-8c52d6345ae9
keywords:
- trace sessions WDK , advanced options
- summary message files WDK TraceView
- listing files WDK
- output files WDK TraceView
- files WDK TraceView
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Output File Options


In the **Output Files** tab, you can create text files for a [trace session](trace-session.md). You can set and change the following options only while creating the trace session. You cannot change these options after the session starts.

<span id="Create_Listing_File"></span><span id="create_listing_file"></span><span id="CREATE_LISTING_FILE"></span>**Create Listing File**  
Creates a formatted, readable text file version of the trace messages from a real-time trace session or a [trace log](trace-log.md).

In the associated text box, type a path and file name for the listing file. The default is LogSession*N*.out in the local directory, where *N* is a zero-based integer that represents the order in which the session is created.

<span id="Create_Summary_File"></span><span id="create_summary_file"></span><span id="CREATE_SUMMARY_FILE"></span>**Create Summary File**  
Generates a text file of statistical information about a real-time trace session or a trace log.

In the associated text box, type a path and file name for the summary file. The default is LogSession*N*.sum in the local directory, where *N* is a zero-based integer that represents the order in which the session is created.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

These options apply only to the trace session that you are creating, even if you include the trace session in a trace session group. Trace sessions in groups do not share their trace session options.

If you specify the path and file name of an existing output or summary file, TraceView overwrites that file without warning.

TraceView creates the summary file when you stop the trace session. If you close the TraceView window before stopping the trace session, TraceView does not create a summary file for the session.

 

 





