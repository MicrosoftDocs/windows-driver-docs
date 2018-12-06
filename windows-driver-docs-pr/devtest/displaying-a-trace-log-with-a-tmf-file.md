---
title: Displaying a Trace Log with a TMF File
description: Displaying a Trace Log with a TMF File
ms.assetid: 1d592ed3-44d2-4d12-9d31-19b07e6962ea
keywords:
- trace message format files WDK
- TMF files WDK , displaying trace logs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Displaying a Trace Log with a TMF File


## <span id="ddk_using_a_tmf_file_tools"></span><span id="DDK_USING_A_TMF_FILE_TOOLS"></span>


If you do not have the [PDB symbol file](pdb-symbol-files.md) for the trace provider, use the following procedure to display the contents of a trace log:

1.  [Start TraceView](starting-and-exiting-traceview.md).

2.  On the **File** menu, click **Open Existing Log File**.

3.  In the **Log File Name** box, type the path and name of an event trace log file (.etl). Or, click the ellipsis button (**...**) and navigate to the file.

4.  In the **Log File Selection** dialog box, you can also set select options to generate other output files from the log file. This step is optional. For more information, see [Setting Trace Log Options](setting-trace-log-options.md).

5.  Click **OK**.

6.  Click **TMF (Trace Format) Files** and then click **OK**.

7.  Do one of the following:
    -   To specify one or more TMF files , click **Select TMF Files**, click **OK**, click **Add**, and then browse to and select one or more TMF files from the directory. To select TMF files from another directory, click the **Add** button again. Otherwise, click **Done**.
    -   To direct TraceView to search for the TMF files in a specified directory, click **Set TMF Search Path**, click **OK**, browse to the directory, and then click **OK**.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

For more information about specifying TMF files, see Select TMF Files and Set TMF Search Path.

 

 





