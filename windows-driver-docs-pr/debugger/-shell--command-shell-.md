---
title: .shell (Command Shell)
description: The .shell command launches a shell process and redirects its output to the debugger, or to a specified file.
ms.assetid: 351cbd54-6e1a-4dc1-b0d8-8e61294b0e86
keywords: ["Command Shell (.shell) command", "MS-DOS Shell (.shell) command", "DOS Shell (.shell) command", "shell commands, Command Shell (.shell) command", ".shell (Command Shell) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .shell (Command Shell)
api_type:
- NA
ms.localizationpriority: medium
---

# .shell (Command Shell)


The **.shell** command launches a shell process and redirects its output to the debugger, or to a specified file.

```dbgcmd
.shell [Options] [ShellCommand] 
.shell -i InFile [-o OutFile [-e ErrFile]] [Options] ShellCommand
```

## <span id="ddk_meta_command_shell_dbg"></span><span id="DDK_META_COMMAND_SHELL_DBG"></span>Parameters


<span id="_______InFile______"></span><span id="_______infile______"></span><span id="_______INFILE______"></span> *InFile*   
Specifies the path and file name of a file to be used for input. If you intend to offer no input after the initial command, you can specify a single hyphen (-) instead of *InFile*, with no space before the hyphen.

<span id="_______OutFile______"></span><span id="_______outfile______"></span><span id="_______OUTFILE______"></span> *OutFile*   
Specifies the path and file name of a file to be used for standard output. If **-o** **** *OutFile* is omitted, output is sent to the Debugger Command window. If you do not want this output displayed or saved in a file, you can specify a single hyphen (-) instead of *OutFile*, with no space before the hyphen.

<span id="_______ErrFile______"></span><span id="_______errfile______"></span><span id="_______ERRFILE______"></span> *ErrFile*   
Specifies the path and file name of a file to be used for error output. If -e ErrFile is omitted, error output is sent to the same place as standard output. If you do not want this output displayed or saved in a file, you can specify a single hyphen (-) instead of *ErrFile*, with no space before the hyphen.

<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Can be any number of the following options:

<span id="-ci__Commands_"></span><span id="-ci__commands_"></span><span id="-CI__COMMANDS_"></span>**-ci "**<em>Commands</em>**"**  
Processes the specified debugger commands, and then passes their output as an input file to the process being launched. *Commands* can be any number of debugger commands, separated by semicolons, and enclosed in quotation marks.

<span id="-x"></span><span id="-X"></span>**-x**  
Causes any process being spawned to be completely detached from the debugger. This allows you to create processes which will continue running even after the debugging session ends.

<span id="_______ShellCommand______"></span><span id="_______shellcommand______"></span><span id="_______SHELLCOMMAND______"></span> *ShellCommand*   
Specifies the application command line or Microsoft MS-DOS command to be executed.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For other ways of accessing the command shell, see [Using Shell Commands](using-shell-commands.md).

Remarks
-------

The **.shell** command is not supported when the output of a user-mode debugger is redirected to the kernel debugger. For more information about redirecting output to the kernel debugger (sometimes called NTSD over KD), see [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md).

The entire line after the **.shell** command will be interpreted as a Windows command (even if it contains a semicolon). This line should not be enclosed in quotation marks. There must be a space between **.shell** and the *ShellCommand* (additional leading spaces are ignored).

The output from the command will appear in the Debugger Command window, unless the **-o** **** *OutFile* parameter is used.

Issuing a **.shell** command with no parameters will activate the shell and leave it open. All subsequent commands will be interpreted as Windows commands. During this time, the debugger will display messages reading **&lt;.shell process may need input&gt;**, and the WinDbg prompt will be replaced with an **Input&gt;** prompt. Sometimes, a separate Command Prompt window will appear when the debugger leaves the shell open. This window should be ignored; all input and output will be done through the Debugger Command window.

To close this shell and return to the debugger itself, type **exit** or **.shell\_quit**. (The **.shell\_quit** command is more powerful, because it works even if the shell is frozen.)

This command cannot be used while debugging CSRSS, because new processes cannot be created without CSRSS being active.

You can use the -ci flag to run one or more debugger commands and then pass their output to a shell process. For example, you could pass the output from the [**!process 0 7**](-process.md) command to a Perl script by using the following command:

```dbgcmd
0:000> .shell -ci "!process 0 7" perl.exe parsemyoutput.pl 
```

 

 





