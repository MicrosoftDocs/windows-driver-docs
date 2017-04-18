---
title: Displaying a Trace Log with a PDB File
description: Displaying a Trace Log with a PDB File
ms.assetid: 267a5d34-6fd0-43b6-aa07-5154bdb2b9a7
keywords: ["program database symbol files WDK", "PDB symbol files WDK", "symbol files WDK software tracing"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Displaying%20a%20Trace%20Log%20with%20a%20PDB%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




