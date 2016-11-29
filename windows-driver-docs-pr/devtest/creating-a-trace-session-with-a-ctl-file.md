---
title: Creating a Trace Session with a CTL File
description: Creating a Trace Session with a CTL File
ms.assetid: aa9aee7b-d0d2-44fe-a124-3594078a8e6c
keywords: ["control GUIDs WDK", ".ctl files", "ctl files"]
---

# Creating a Trace Session with a CTL File


## <span id="ddk_create_a_trace_session_with_a_ctl_file_tools"></span><span id="DDK_CREATE_A_TRACE_SESSION_WITH_A_CTL_FILE_TOOLS"></span>


You can create a trace session by locating a [control GUID (.ctl) file](control-guid-file.md) for the trace providers and locating the [trace message format (.tmf) files](trace-message-format-file.md) for their messages.

### <span id="to_create_a_trace_session_with_a_ctl_file"></span><span id="TO_CREATE_A_TRACE_SESSION_WITH_A_CTL_FILE"></span>To create a trace session with a CTL file

1.  [Start TraceView](starting-and-exiting-traceview.md).

2.  On the **File** menu, click **Create New Log Session**.

3.  Click **Add Provider**.

4.  Click **CTL (Control GUID) File**, and then type the path to a [control GUID file](control-guid-file.md) for the trace provider; or, click the ellipsis button (**...**) and navigate to the file.

5.  Do one of the following:
    -   To specify one or more TMF files , click **Select TMF Files**, click **OK**, click **Add**, and then browse to and select one or more TMF files from the directory. To select TMF files from another directory, click the **Add** button again. Otherwise, click **Done**.
    -   To direct TraceView to search for the TMF files in a specified directory, click **Set TMF Search Path**, click **OK**, browse to the directory, and then click **OK**.

6.  To add additional providers, click **Add Provider**. This step is optional.

7.  Click **Next**.

8.  [Select flags and a level](selecting-flags-and-levels.md), if desired.

9.  [Set basic trace session options](setting-basic-trace-session-options.md), if desired.

10. [Set advanced trace session options](setting-advanced-trace-session-options.md), if desired.

11. Click **Finish**.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

If TraceView cannot find a TMF file for the trace provider, it does not add the trace provider to the provider list in the **Create New Log Session** dialog box and it does not display a message that explains why the provider was not added. If the provider does not appear in the provider list, restart the procedure and use the **Select TMF Files** method instead of **Set TMF Search Path**. If you cannot locate a PDB file or a TMF file for the provider, you cannot use TraceView to create a trace session with the provider.

You can use files with file name extensions other than ".ctl" with the **CTL (Control GUID) File** option. TraceView requires only that the file is a text file, that each control GUID appears on a separate line in the file, and that the control GUID is the first text on the line. If you submit a file with a different format, TraceView accepts the file but does not enable providers that are not specified correctly.

The control GUID file can contain multiple control GUIDs. TraceView enables all of the providers whose control GUIDs appear in the file.

When creating a trace session with a control GUID, you can use the **Tracing Flags and Levels Selection** dialog box (which is described in [Selecting Flags and Levels](selecting-flags-and-levels.md)) only when TraceView can find a PDB symbol file for the provider or when it can find a trace message control (.tmc) file for the provider in the TMF path (specified by using the Set TMF Search Path option).

If the TMC file is not available, you can set the trace flags and level for the provider manually in the **Advanced Trace Session Options** dialog box. For instructions, see [Setting Advanced Trace Session Options](setting-advanced-trace-session-options.md).

For information about specifying TMF files, see Select TMF Files and Set TMF Search Path.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Creating%20a%20Trace%20Session%20with%20a%20CTL%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




