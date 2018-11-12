---
title: Configuring tools.ini
description: Configuring tools.ini
ms.assetid: 4f0d9f48-99d5-4180-b25d-70fd8de6f20e
keywords: ["tools.ini file", "ntsd.ini file"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Configuring tools.ini


## <span id="ddk_configuring_tools_ini_dbg"></span><span id="DDK_CONFIGURING_TOOLS_INI_DBG"></span>


The file tools.ini contains information to initialize the command-line debuggers. On startup, the debugger searches for the appropriate section header in the tools.ini file and extracts initialization information from the entries under the header. Each command-line debugger has its own section header - \[CDB\], \[NTSD\], and \[KD\]. The environment variable INIT must point to the directory containing the tools.ini file.

WinDbg does not use the tools.ini file. Instead, WinDbg saves initialization settings in [workspaces](using-workspaces.md).

The tools.ini entries are shown in the following table.

Keywords must be separated from the values by white space or a colon. Keywords are not case-sensitive.

For **TRUE** or **FALSE** values, "FALSE" is the only false value. Anything else is **TRUE**.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Entry</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>$u0:</strong> <em>value</em> ... <strong>$u9:</strong> <em>value</em></p></td>
<td align="left"><p>Assign values to fixed-name aliases. You can specify numeric values <em>n</em> or <em>0xn</em> or any other string. See <a href="using-aliases.md" data-raw-source="[Using Aliases](using-aliases.md)">Using Aliases</a> for details. No command-line equivalent.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>DebugChildren:</strong> <em>flag</em></p></td>
<td align="left"><p><strong>TRUE</strong> or <strong>FALSE</strong>. If <strong>TRUE</strong>, CDB debugs the specified application as well as any child processes that it might spawn. Command-line equivalent is <strong>-o</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>DebugOutput:</strong> <em>flag</em></p></td>
<td align="left"><p><strong>TRUE</strong> or <strong>FALSE</strong>. If <strong>TRUE</strong>, CDB sends output and receives input through a terminal. If <strong>FALSE</strong>, output goes to the user screen. The command-line option <strong>-d</strong> is similar but not identical.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IniFile:</strong> <em>file</em></p></td>
<td align="left"><p>Specifies the name of the script file that CDB or KD takes commands from at startup. The default is the ntsd.ini file in the current directory. Command-line equivalent is <strong>-cf</strong>. For details, see <a href="using-script-files.md" data-raw-source="[Using Script Files](using-script-files.md)">Using Script Files</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>LazyLoad:</strong> <em>flag</em></p></td>
<td align="left"><p><strong>TRUE</strong> or <strong>FALSE</strong>. If <strong>TRUE</strong>, CDB performs lazy symbol loading; that is, symbols are not loaded until required. Command-line equivalent is <strong>-s</strong>.</p>
<p>For details, and other methods of setting this option, see <a href="deferred-symbol-loading.md" data-raw-source="[Deferred Symbol Loading](deferred-symbol-loading.md)">Deferred Symbol Loading</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>SetDll:</strong> <em>filename</em></p></td>
<td align="left"><p>Set extension DLL. The .dll filename extension should be omitted. Default is userexts.dll. Command-line equivalent is <strong>-a</strong>.</p>
<p>For details, and other methods of setting this default, see <a href="loading-debugger-extension-dlls.md" data-raw-source="[Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md)">Loading Debugger Extension DLLs</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>StopFirst:</strong> <em>flag</em></p></td>
<td align="left"><p><strong>TRUE</strong> or <strong>FALSE</strong>. If <strong>true</strong>, CDB stops on the breakpoint at the end of the image-loading process. Command-line equivalent is <strong>-g</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>StopOnProcessExit:</strong> <em>flag</em></p></td>
<td align="left"><p><strong>TRUE</strong> or <strong>FALSE</strong>. If <strong>TRUE</strong>, CDB stops when it receives a process termination notification. Command-line equivalent is <strong>-G</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<strong>sxd:</strong> <em>event</em>
<strong>sxe:</strong> <em>event</em></td>
<td align="left"><p>Sets the debugger response and the handling status for the specified exception or event.</p>
<p>Exceptions and events may be specified in the following ways:</p>
<p></p>
<strong>*</strong>: Default exception
<em>n</em>: Exception <em>n</em> (decimal)
<em>0xn</em>: Exception <em>0xn</em> (hexadecimal)
(other): Event code
<p>See <a href="controlling-exceptions-and-events.md" data-raw-source="[Controlling Exceptions and Events](controlling-exceptions-and-events.md)">Controlling Exceptions and Events</a> for details of this process and for other methods of controlling these settings.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>VerboseOutput:</strong> <em>flag</em></p></td>
<td align="left"><p><strong>TRUE</strong> or <strong>FALSE</strong>. If <strong>TRUE</strong>, CDB will display detailed information about symbol handling, event notification, and other run-time occurrences. Command-line equivalent is <strong>-v</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>lines:</strong> <em>flag</em></p></td>
<td align="left"><p><strong>TRUE</strong> or <strong>FALSE</strong>. The lines flag enables or disables support for source-line information.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>srcopt:</strong> <em>options</em></p></td>
<td align="left"><p>Sets the source line options that control source display and program stepping options. For more information see <strong><a href="l---l---set-source-options-.md" data-raw-source="[l+, l- (Set Source Options)](l---l---set-source-options-.md)">l+, l- (Set Source Options)</a></strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>srcpath:</strong> <em>directory</em></p></td>
<td align="left"><p>Sets the source file search path. For more information see <strong><a href="-srcpath---lsrcpath--set-source-path-.md" data-raw-source="[.srcpath, .lsrcpath (Set Source Path)](-srcpath---lsrcpath--set-source-path-.md)">.srcpath, .lsrcpath (Set Source Path)</a></strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>enable_unicode:</strong> <em>flag</em></p></td>
<td align="left"><p><strong>TRUE</strong> or <strong>FALSE</strong>. The enable_unicode flag specifies whether the debugger displays USHORT pointers and arrays as Unicode strings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>force_radix_output:</strong> <em>flag</em></p></td>
<td align="left"><p><strong>TRUE</strong> or <strong>FALSE</strong>. The force_radix_output flag specifies whether integers are displayed in decimal format or in the default radix.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>col_mode:</strong> <em>flag</em></p></td>
<td align="left"><p><strong>TRUE</strong> or <strong>FALSE</strong>. The col_mode flag controls the color mode setting. When color mode is enabled the debugger can produce colored output. By default, most colors are not set and instead default to the current console colors.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>col:</strong> <em>name</em> <em>colspec</em></p></td>
<td align="left"><p>The <em>name</em> indicates the element that you are coloring. The <em>colspec</em> is a three-letter RGB indicator of the form [rR-][gG-][bB-]. A lower-case letter indicates darker, an upper-case letter indicates brighter and a dash indicates no color component contribution. Due to console color limitations, bright is not actually per-component, but applies to all components if any request bright. In other words, rgB is the same as RGB. For this reason, it is recommended that all caps be used if any caps are going to be used.</p>
<p>Example usage:</p>
<p>col: emphfg R--</p></td>
</tr>
</tbody>
</table>

 

A sample \[NTSD\] section in the tools.ini file follows:

```inf
[NTSD]
sxe: 3c
sxe: cc
$u0: VeryLongName
VerboseOutput:true
```

 

 





