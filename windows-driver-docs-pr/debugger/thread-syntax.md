---
title: Thread Syntax
description: Thread Syntax
ms.assetid: f3eaa0ee-7c4f-47a4-aba9-c1d21c1529d1
keywords: ["thread, command syntax", "~ (thread identifier)", "thread, thread identifier ( ~ )", "thread, thread ID", "~ (thread identifier)", "syntax rules for commands, ~ (thread identifier)", "syntax rules for commands, ~ (thread identifier)", "syntax rules for commands, threads"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Thread%20Syntax%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




