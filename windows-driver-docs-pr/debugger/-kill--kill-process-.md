---
title: .kill (Kill Process)
description: In user mode, the .kill command ends a process that is being debugged.
ms.assetid: e4bc13e4-2566-4438-9ae7-a5ba05b727de
keywords: [".kill (Kill Process) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .kill (Kill Process)
api_type:
- NA
ms.localizationpriority: medium
---

# .kill (Kill Process)


In user mode, the **.kill** command ends a process that is being debugged.

In kernel mode, the **.kill** command ends a process on the target computer.

User-Mode Syntax

```dbgcmd
.kill [ /h | /n ]
```

Kernel-Mode Syntax

```dbgcmd
.kill Process 
```

## <span id="ddk_meta_kill_process_dbg"></span><span id="DDK_META_KILL_PROCESS_DBG"></span>Parameters


<span id="________h______"></span><span id="________H______"></span> **/h**   
(User mode only) Any outstanding debug event will be continued and marked as handled. This is the default.

<span id="________n______"></span><span id="________N______"></span> **/n**   
(User mode only) Any outstanding debug event will be continued without being marked as handled.

<span id="_______Process______"></span><span id="_______process______"></span><span id="_______PROCESS______"></span> *Process*   
Specifies the address of the process to be terminated. If *Process* is omitted or zero, the default process for the current system state will be terminated.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

In kernel mode, this command is supported on Microsoft Windows Server 2003 and later versions of Windows.

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
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

In user mode, this command ends a process that is being debugged. If the debugger is attached to a child process, you can use **.kill** to end the child process without ending the parent process. For more information, see Examples.

In kernel mode, this command schedules the selected process on the target computer for termination. The next time that the target can run (for example, by using a [**g (Go)**](g--go-.md) command), the specified process is ended.

You cannot use this command during local kernel debugging.

Examples
--------

**Using .childdbg**

Suppose you attach a debugger to parent process (Parent.exe) before it creates a child process. You can enter the command [**.childdbg 1**](-childdbg--debug-child-processes-.md) to tell the debugger to attach to any child process that the parent creates.

```dbgcmd
1:001> .childdbg 1
Processes created by the current process will be debugged
```

Now let the parent process run, and break in after it has created the child process. Use the [**| (Process Status)**](---process-status-.md) command to see the process numbers for the parent and child processes.

```dbgcmd
0:002> |*
.  0    id: 7f8 attach  name: C:\Parent\x64\Debug\Parent.exe
   1    id: 2d4 child   name: notepad.exe
```

In the preceding output, the number of the child process (notepad.exe) is 1. The dot (.) at the beginning of the first line tells us that the parent process is the current process. To make the child process the current process, enter **|1s**.

```dbgcmd
0:002> |1s
...
1:001> |*
#  0    id: 7f8 attach  name: C:\Parent\x64\Debug\Parent.exe
.  1    id: 2d4 child   name: notepad.exe
```

To kill the child process, enter the command **.kill**. The parent process continues to run.

```dbgcmd
1:001> .kill
Terminated.  Exit thread and process events will occur.
1:001> g
```

**Using the -o parameter**

When you start WinDbg or CDB, you can use the **-o** parameter to tell the debugger that it should attach to child processes. For example, the following command starts WinDbg, which starts and attaches to Parent.exe. When Parent.exe creates a child process, WinDbg attaches to the child process.

**windbg -g -G -o Parent.exe**

For more information, see [**WinDbg Command-Line Options**](windbg-command-line-options.md) and [**CDB Command-Line Options**](cdb-command-line-options.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Versions:(Kernel mode) Supported in Windows Server 2003 and later.</p></td>
</tr>
</tbody>
</table>

 

 





