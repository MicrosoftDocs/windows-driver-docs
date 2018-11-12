---
title: Process Syntax
description: Process Syntax
ms.assetid: fe08b5fe-ec27-4264-baee-de4c11bcb2bf
keywords: ["process, command syntax", "(process identifier)", "process, process identifier ( )", "process, process ID (PID)", "PID (process ID)", "(process identifier)", "syntax rules for commands, (process identifier)", "syntax rules for commands, (process identifier)", "process identifier ( )"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Process Syntax


## <span id="ddk_process_syntax_dbg"></span><span id="DDK_PROCESS_SYNTAX_DBG"></span>


Many debugger commands have process identifiers as their parameters. A vertical bar ( | ) appears before the process identifier.

The process identifier can be one of the following values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Process identifier</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>|.</strong></p></td>
<td align="left"><p>The current process.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>|#</strong></p></td>
<td align="left"><p>The process that caused the current exception or debug event.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>|*</strong></p></td>
<td align="left"><p>All processes.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>|</strong><em>Number</em></p></td>
<td align="left"><p>The process whose ordinal is <em>Number</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>|~[</strong><em>PID</em><strong>]</strong></p></td>
<td align="left"><p>The process whose process ID is <em>PID</em>. (The brackets are required and you cannot add a space between the tilde (~) and the opening bracket.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>|[</strong><em>Expression</em><strong>]</strong></p></td>
<td align="left"><p>The process whose process ID is the integer to which the numerical <em>Expression</em> resolves.</p></td>
</tr>
</tbody>
</table>

 

Processes are assigned ordinals as they are created. Note that this number differs from the process ID (PID) that the Microsoft Windows operating system uses.

The current process defines the memory space and the set of threads that are used. When debugging begins, the current process is the one that caused the present exception or debug event (or the process that the debugger attached to). That process remains the current process until you specify a new one by using a [**|s (Set Current Process)**](-s--set-current-process-.md) command or by using the [Processes and Threads window](processes-and-threads-window.md) in WinDbg.

Process identifiers are used as parameters in several commands, frequently as the command prefix. Note that WinDbg and CDB can debug child processes that the original process created. WinDbg and CDB can also attach to multiple unrelated processes.

An example of the |\[*Expression*\] syntax would be \[|@$t0\]. In this example, the process changes depending on the value of a user-defined pseudo-register. This syntax allows debugger scripts to programmatically select a process.

### <span id="controlling_processes_in_kernel_mode"></span><span id="CONTROLLING_PROCESSES_IN_KERNEL_MODE"></span>Controlling Processes in Kernel Mode

In kernel mode, you cannot control processes by using process identifiers. For more information about how to access process-specific information in kernel mode, see [Changing Contexts](changing-contexts.md).

 

 





