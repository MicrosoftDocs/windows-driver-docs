---
title: Process Syntax
description: Process Syntax
ms.assetid: fe08b5fe-ec27-4264-baee-de4c11bcb2bf
keywords: ["process, command syntax", "(process identifier)", "process, process identifier ( )", "process, process ID (PID)", "PID (process ID)", "(process identifier)", "syntax rules for commands, (process identifier)", "syntax rules for commands, (process identifier)", "process identifier ( )"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Process%20Syntax%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




