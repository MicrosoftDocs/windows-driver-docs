---
title: Thread Syntax
description: Thread Syntax
ms.assetid: f3eaa0ee-7c4f-47a4-aba9-c1d21c1529d1
keywords: ["thread, command syntax", "~ (thread identifier)", "thread, thread identifier ( ~ )", "thread, thread ID", "~ (thread identifier)", "syntax rules for commands, ~ (thread identifier)", "syntax rules for commands, ~ (thread identifier)", "syntax rules for commands, threads"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Thread Syntax


## <span id="ddk_thread_syntax_dbg"></span><span id="DDK_THREAD_SYNTAX_DBG"></span>


Many debugger commands have thread identifiers as their parameters. A tilde ( ~ ) appears before the thread identifier.

The thread identifier can be one of the following values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Thread identifier</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>~.</strong></p></td>
<td align="left"><p>The current thread.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>~#</strong></p></td>
<td align="left"><p>The thread that caused the current exception or debug event.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>~*</strong></p></td>
<td align="left"><p>All threads in the process.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>~</strong><em>Number</em></p></td>
<td align="left"><p>The thread whose index is <em>Number</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>~~</strong>[<em>TID</em>]</p></td>
<td align="left"><p>The thread whose thread ID is <em>TID</em>. (The brackets are required And you cannot add a space between the second tilde and the opening bracket.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>~</strong>[<em>Expression</em>]</p></td>
<td align="left"><p>The thread whose thread ID is the integer to which the numerical <em>Expression</em> resolves.</p></td>
</tr>
</tbody>
</table>

 

Threads are assigned indexes as they are created. Note that this number differs from the thread ID that the Microsoft Windows operating system uses.

When debugging begins, the current thread is the one that caused the present exception or debug event (or the active thread when the debugger attached to the process). That thread remains the current thread until you specify a new one by using a [**~s (Set Current Thread)**](-s--set-current-thread-.md) command or by using the [Processes and Threads window](processes-and-threads-window.md) in WinDbg.

Thread identifiers typically appear as command prefixes. Note that not all wildcard characters are available in all commands that use thread identifiers.

An example of the ~\[*Expression*\] syntax would be `~[@$t0]`. In this example, the thread changes depending on the value of a user-defined pseudo-register. This syntax allows debugger scripts to programmatically select a thread.

### <span id="controlling_threads_in_kernel_mode"></span><span id="CONTROLLING_THREADS_IN_KERNEL_MODE"></span>Controlling Threads in Kernel Mode

In kernel mode, you cannot control threads by using thread identifiers. For more information about how to access thread-specific information in kernel mode, see [Changing Contexts](changing-contexts.md).

**Note**  You can use the tilde character ( ~ ) to specify threads during user-mode debugging. In kernel-mode debugging, you can use the tilde to specify processors. For more information about how to specify processors, see [Multiprocessor Syntax](multiprocessor-syntax.md).

 

 

 





