---
title: Creating a Trace Session with a PDB File
description: Creating a Trace Session with a PDB File
ms.assetid: dae78674-3563-4fd5-869b-abd4c13aa202
keywords:
- program database symbol files WDK
- PDB symbol files WDK
- symbol files WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
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

If you use TraceView to open a PDB file on a computer running Windows Server 2003, TraceView automatically exits.

 





