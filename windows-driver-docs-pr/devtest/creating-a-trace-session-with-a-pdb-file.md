---
title: Creating a Trace Session with a PDB File
description: Creating a Trace Session with a PDB File
ms.assetid: dae78674-3563-4fd5-869b-abd4c13aa202
keywords: ["program database symbol files WDK", "PDB symbol files WDK", "symbol files WDK software tracing"]
---

# Creating a Trace Session with a PDB File


## <span id="ddk_create_a_trace_session_with_a_pdb_file_tools"></span><span id="DDK_CREATE_A_TRACE_SESSION_WITH_A_PDB_FILE_TOOLS"></span>


The easiest way to specify a trace provider is to locate the [PDB symbol file](pdb-symbol-files.md) for the source code that includes the trace provider. TraceView can extract all of the information that it needs for the trace session from the PDB file.

### <span id="to_create_a_trace_session_with_a_pdb_file"></span><span id="TO_CREATE_A_TRACE_SESSION_WITH_A_PDB_FILE"></span>To create a trace session with a PDB file

1.  [Start TraceView](starting-and-exiting-traceview.md).

2.  On the **File** menu, click **Create New Log Session**.

3.  Click **Add Provider**.

4.  Click **PDB (Debug Information) File**, and then type the path to the [PDB symbol file](pdb-symbol-files.md) for the trace provider; or, click the ellipsis button (**...**) and navigate to the file.

5.  To add additional providers, click **Add Provider**. This step is optional.

6.  Click **Next**.

7.  [Select flags and a level](selecting-flags-and-levels.md), if desired.

8.  [Set basic trace session options](setting-basic-trace-session-options.md), if desired.

9.  [Set advanced trace session options](setting-advanced-trace-session-options.md), if desired.

10. Click **Finish**.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

If the PDB file that you specify does not include the required tracing elements, TraceView displays the "Cannot find PDB file" error message.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Creating%20a%20Trace%20Session%20with%20a%20PDB%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




