---
title: $ , $ , $$ , $$ , $$ a (Run Script File)
description: The $ , $ , $$ , $$ , and $$ a commands read the contents of the specified script file and use its contents as debugger command input.
ms.assetid: b3584680-765d-4aaf-ad43-c7d73552e5fb
keywords: ["$ (Run Script File) command", "$$ (Run Script File) command", "$$ (Run Script File) command", "Run Script File ($ ) command", "Run Script File ($ ) command", "Run Script File ($$ ) command", "Run Script File ($$ ) comm", "$ , $ , $$ , $$ , $$ a (Run Script File) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- $ , $ , $$ , $$ , $$ a (Run Script File)
api_type:
- NA
ms.localizationpriority: medium
---

# $<, $><, $$<, $$><, $$ >a< (Run Script File)


The **$&lt;**, **$&gt;&lt;**, **$$&lt;**, **$$&gt;&lt;**, and **$$&gt;a&lt;** commands read the contents of the specified script file and use its contents as debugger command input.

```dbgcmd
    $<Filename 
    $><Filename 
    $$<Filename 
    $$><Filename 
    $$>a<Filename [arg1 arg2 arg3 ...] 
```

## <span id="ddk_cmd_run_script_file_dbg"></span><span id="DDK_CMD_RUN_SCRIPT_FILE_DBG"></span>Parameters


<span id="_______Filename______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *Filename*   
Specifies a file that contains valid debugger command text. The file name must follow Microsoft Windows file name conventions. The file name may contain spaces.

<span id="_______argn______"></span><span id="_______ARGN______"></span> *argn*   
Specifies any number of string arguments for the debugger to pass to the script. The debugger will replace any string of the form ${$arg*n*} in the script file with the corresponding *argn* before executing the script. Arguments may not contain quotation marks or semicolons. Multiple arguments must be separated by spaces; if an argument contains a space it must be enclosed in quotation marks. All arguments are optional.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Modes</p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p>Targets</p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Platforms</p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **$$&lt;** and **$&lt;** tokens execute the commands that are found in the script file literally. However, with **$&lt;** you can specify any file name, including one that contains semicolons. Because **$&lt;** allows semicolons to be used in the file name, you cannot concatenate **$&lt;** with other debugger commands, because a semicolon cannot be used both as a command separator and as part of a file name.

The **$$&gt;&lt;** and **$&gt;&lt;** tokens execute the commands that are found in the script file literally, which means they open the script file, replace all carriage returns with semicolons, and execute the resulting text as a single command block. As with **$&lt;** discussed previously, the **$&gt;&lt;** variation permits file names that contains semicolons, which means you cannot concatenate **$&gt;&lt;** with other debugger commands.

The **$$&gt;&lt;** and **$&gt;&lt;** tokens are useful if you are running scripts that contain debugger command programs. For more information about these programs, see [Using Debugger Command Programs](using-debugger-command-programs.md).

Unless you have file names that contain semicolons, you do not need to use either **$&lt;** or **$&gt;&lt;**.

The **$$&gt;a&lt;** token allows the debugger to pass arguments to the script. If *Filename* contains spaces, it must be enclosed in quotation marks. If too many arguments are supplied, the excess arguments are ignored. If too few arguments are supplied, any token in the source file of the form ${$arg*n*} where *n* is larger than the number of supplied arguments will remain in its literal form and will not be replaced with anything. You can follow this command with a semicolon and additional commands; the presence of a semicolon terminates the argument list.

When the debugger executes a script file, the commands and their output are displayed in the [Debugger Command window](debugger-command-window.md). When the end of the script file is reached, control returns to the debugger.

The following table summarizes how you can use these tokens.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Token</th>
<th align="left">Allows file names that contain semicolons</th>
<th align="left">Allows concatenation of additional commands separated by semicolons</th>
<th align="left">Condenses to single command block</th>
<th align="left">Allows script arguments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>$&lt;</strong></p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$&gt;&lt;</strong></p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$$&lt;</strong></p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>$$&gt;&lt;</strong></p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>$$&gt;a&lt;</strong></p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
</tr>
</tbody>
</table>

 

The **$&lt;**, **$&gt;&lt;**, **$$&lt;**, and **$$&gt;&lt;** commands echo the commands contained in the script file and display the output of these commands. The **$$&gt;a&lt;** command does not echo the commands found in the script file, but merely displays their output.

Script files can be nested. If the debugger encounters one of these tokens in a script file, execution moves to the new script file and returns to the previous location when the new script file has been completed. Scripts can also be called recursively.

In WinDbg, you can paste the additional command text in the Debugger Command window.

Examples
--------

The following example demonstrates how to pass arguments to a script file, Myfile.txt. Assume that the file contains the following text:

```console
.echo The first argument is ${$arg1}.
.echo The second argument is ${$arg2}.
```

Then you can pass arguments to this file by using a command like this:

```console
0:000> $$>a<myfile.txt myFirstArg mySecondArg 
```

The result of this command would be:

```console
The first argument is myFirstArg.
The second argument is mySecondArg.
```

Here is an example of what happens when the wrong number of argument is supplied. Assume that the file My Script.txt contains the following text:

```console
.echo The first argument is ${$arg1}.
.echo The fifth argument is ${$arg5}.
.echo The fourth argument is ${$arg4}.
```

Then the following semicolon-delimited command line produces output thus:

```console
0:000> $$>a< "c:\binl\my script.txt" "First one" Two "Three More" Four; recx 
The first argument is First one.
The fifth argument is ${$arg5}.
The fourth argument is Four.
ecx=0021f4ac
```

In the preceding example, the file name is enclosed in quotation marks because it contains a space, and arguments that contain spaces are enclosed in quotation marks as well. Although a fifth argument seems to be expected by the script, the semicolon terminates the **$$&gt;a&lt;** command after the fourth argument.

 


