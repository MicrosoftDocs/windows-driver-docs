---
title: Output File Options
description: Output File Options
ms.assetid: f53785d8-2a91-47da-945c-8c52d6345ae9
keywords: ["trace sessions WDK , advanced options", "summary message files WDK TraceView", "listing files WDK", "output files WDK TraceView", "files WDK TraceView"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Output%20File%20Options%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




