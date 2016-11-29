---
title: Displaying a Trace Log with a TMF File
description: Displaying a Trace Log with a TMF File
ms.assetid: 1d592ed3-44d2-4d12-9d31-19b07e6962ea
keywords: ["trace message format files WDK", "TMF files WDK , displaying trace logs"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Displaying%20a%20Trace%20Log%20with%20a%20TMF%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




