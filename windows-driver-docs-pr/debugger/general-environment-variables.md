---
title: General Environment Variables
description: General Environment Variables
ms.assetid: 1f37de92-0c62-4317-b3c6-24b3efd9b3b3
keywords: ["environment variables, general", "_NO_DEBUG_HEAP environment variable", "_NT_ALT_SYMBOL_PATH environment variable", "_NT_DEBUG_HISTORY_SIZE environment variable", "_NT_DEBUG_LOG_FILE_APPEND environment variable", "_NT_DEBUG_LOG_FILE_OPEN environment variable", "_NT_DEBUGGER_EXTENSION_PATH environment variable", "_NT_EXECUTABLE_IMAGE_PATH environment variable", "_NT_SOURCE_PATH environment variable"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# General Environment Variables


## <span id="ddk_general_environment_variables_dbg"></span><span id="DDK_GENERAL_ENVIRONMENT_VARIABLES_DBG"></span>


The following table lists the environment variables that can be used in both user-mode and kernel-mode debugging.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Variable</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>_NT_DEBUGGER_EXTENSION_PATH = <em>Path</em></p></td>
<td align="left"><p>Specifies the path that the debugger will first search for extension DLLs. <em>Path</em> can contain a drive letter followed by a colon (<strong>:</strong>). Separate multiple directories with semicolons (<strong>;</strong>). For details, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>_NT_EXECUTABLE_IMAGE_PATH = <em>Path</em></p></td>
<td align="left"><p>Specifies the path containing the binary executable files. <em>Path</em> can contain a drive letter followed by a colon (<strong>:</strong>). Separate multiple directories with semicolons (<strong>;</strong>).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>_NT_SOURCE_PATH = <em>Path</em></p></td>
<td align="left"><p>Specifies the path containing the source files for the target. <em>Path</em> can contain a drive letter followed by a colon (<strong>:</strong>). Separate multiple directories with semicolons (<strong>;</strong>). For details, and for other ways to change this path, see [Source Path](source-path.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>_NT_SYMBOL_PATH = <em>Path</em></p></td>
<td align="left"><p>Specifies the root of a directory tree containing the symbol files. <em>Path</em> can contain a drive letter followed by a colon (<strong>:</strong>). Separate multiple directories with semicolons (<strong>;</strong>). For details, and for other ways to change this path, see [Symbol Path](symbol-path.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>_NT_ALT_SYMBOL_PATH = <em>Path</em></p></td>
<td align="left"><p>Specifies an alternate symbol path searched before _NT_SYMBOL_PATH. This is useful for keeping private versions of symbol files. <em>Path</em> can contain a drive letter followed by a colon (<strong>:</strong>). Separate multiple directories with semicolons (<strong>;</strong>). For details, see [Symbol Path](symbol-path.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>_NT_SYMBOL_PROXY = <em>Proxy</em><strong>:</strong><em>Port</em></p></td>
<td align="left"><p>Specifies the proxy server to be used by SymSrv. For details, see [Firewalls and Proxy Servers](firewalls-and-proxy-servers.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>_NT_DEBUG_HISTORY_SIZE = <em>Number</em></p></td>
<td align="left"><p>Specifies the number of commands in the command history that can be accessed during remote debugging. Because commands vary in length, the number of lines available may not exactly match <em>Number</em>. For details, and for other ways to change this number, see [Using Debugger Commands](using-debugger-commands.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>_NT_DEBUG_LOG_FILE_OPEN = <em>Filename</em></p></td>
<td align="left"><p>(CDB and KD only) Specifies the log file to which the debugger should send output.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>_NT_DEBUG_LOG_FILE_APPEND = <em>Filename</em></p></td>
<td align="left"><p>(CDB and KD only) Specifies the log file to which the debugger should append output.</p></td>
</tr>
<tr class="even">
<td align="left"><p>_NT_EXPR_EVAL = {<strong>masm</strong> | <strong>c++</strong>}</p></td>
<td align="left"><p>Specifies the default expression evaluator. If <strong>masm</strong> is specified, MASM expression syntax will be used. If <strong>c++</strong> is specified, C++ expression syntax will be used. MASM expression syntax is the default. See [Evaluating Expressions](evaluating-expressions.md) for details.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>_NO_DEBUG_HEAP</p></td>
<td align="left"><p>(Windows XP and later) Specifies that the debug heap should not be used for user-mode debugging.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBGENG_NO_DEBUG_PRIVILEGE</p></td>
<td align="left"><p>Prevents processes spawned by the debugger from inheriting SeDebugPrivilege.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBGENG_NO_BUGCHECK_ANALYSIS</p></td>
<td align="left"><p>Prevents automated bugcheck analysis.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBGHELP_HOMEDIR</p></td>
<td align="left"><p>Specifies the path for the root of the default downstream store used by SymSrv and SrcSrv. <em>Path</em> can contain a drive letter followed by a colon (<strong>:</strong>). Separate multiple directories with semicolons (<strong>;</strong>).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SRCSRV_INI_FILE</p></td>
<td align="left"><p>Specifies the path and name of the configuration file used by [SrcSrv](srcsrv.md). By default, the path is the srcsrv subdirectory of the Debugging Tools for Windows installation directory, and the file name is Srcsrv.ini. See [Source Indexing](source-indexing.md) for details.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20General%20Environment%20Variables%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




