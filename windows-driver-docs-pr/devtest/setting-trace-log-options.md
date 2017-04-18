---
title: Setting Trace Log Options
description: Setting Trace Log Options
ms.assetid: 3790a3af-69bd-4ccc-a116-0df6312f378a
keywords: ["summary message files WDK TraceView", "listing message files WDK", "trace logs WDK TraceView , setting options", "log files WDK TraceView , setting options"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Setting%20Trace%20Log%20Options%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




