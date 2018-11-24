---
title: Displaying a Trace Log with a PDB File
description: Displaying a Trace Log with a PDB File
ms.assetid: 267a5d34-6fd0-43b6-aa07-5154bdb2b9a7
keywords:
- program database symbol files WDK
- PDB symbol files WDK
- symbol files WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Displaying a Trace Log with a PDB File


## <span id="ddk_using_a_pdb_file_tools"></span><span id="DDK_USING_A_PDB_FILE_TOOLS"></span>


To display a trace log, you must tell TraceView how to format the trace messages that are stored in the log. This formatting information is included in the [PDB symbol file](pdb-symbol-files.md) for the provider.

If you have the PDB symbol file for the provider, use the following procedure to display a trace log. If you do not have the PDB symbol file, see [Displaying a trace log with a TMF file](displaying-a-trace-log-with-a-tmf-file.md).

1.  [Start TraceView](starting-and-exiting-traceview.md).

2.  On the **File** menu, click **Open Existing Log File**.

3.  In the **Log File Name** box, type the path and name of an event trace log file (.etl). Or, click the ellipsis button (**...**) and navigate to the file.

4.  In the **Log File Selection** dialog box, you can also set select options to generate other output files from the log file. This step is optional. For more information, see [Setting Trace Log Options](setting-trace-log-options.md)..

5.  Click **OK**.

6.  Click **PDB (Debug Information) File** and type the path to the [PDB symbol file](pdb-symbol-files.md) for the trace provider. Or, click the ellipsis button (**...**) and navigate to the file.

7.  Click **OK**.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

When you display the contents of a log file, the expected value in the **State** column of the Trace Session List is **EXISTING**. This value indicates that the trace messages come from a log, not a running trace session.

 

 





