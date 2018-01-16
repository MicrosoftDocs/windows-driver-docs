---
title: Controlling the Target
description: Controlling the Target
ms.assetid: bc08b925-2a55-4af6-a5e2-949637a4c7ee
keywords: ["controlling the target", "controlling the target, overview", "starting and stopping the target", "execution of the target"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Controlling the Target


## <span id="ddk_controlling_the_target_dbg"></span><span id="DDK_CONTROLLING_THE_TARGET_DBG"></span>


While you are debugging a target application in user mode or a target computer in kernel mode, the target can be *running* or *stopped*.

When the debugger connects to a kernel-mode target, the debugger leaves the target running, unless you use the **-b** [command-line option](command-line-options.md), the target system has stopped responding (that is, *crashed*), or the target system is still stopped because of an earlier kernel debugging action.

When the debugger starts or connects to a user-mode target, the debugger immediately stops the target, unless you use the **-g** command-line option. For more information, see [Initial Breakpoint](initial-breakpoint.md).

### <span id="when_the_target_is_running"></span><span id="WHEN_THE_TARGET_IS_RUNNING"></span>When the Target is Running

When the target is running, most debugger actions are unavailable.

If you want to stop a running target, you can issue a **Break** command. This command causes the debugger to *break into the target*. That is, the debugger stops the target and all control is given to the debugger. The application might not break immediately. For example, if all threads are currently executing system code, or are in a wait operation, the application breaks only after control has returned to the application's code.

If a running target encounters an exception, if certain [events](controlling-exceptions-and-events.md) occur, if a [breakpoint](using-breakpoints.md) is hit, or if the application closes normally, the target *breaks into the debugger*. This action stops the target and gives all control to the debugger. A message appears in the [Debugger Command window](debugger-command-window.md) and describes the error, event, or breakpoint.

### <span id="when_the_target_is_stopped"></span><span id="WHEN_THE_TARGET_IS_STOPPED"></span>When the Target is Stopped

To start or control the target's execution, you can do the following:

-   To cause the application to begin running, issue the **Go** command.

-   To step through the application one instruction at a time, use the **Step Into** or **Step Over** commands. If a function call occurs, **Step Into** enters the function and continues stepping through each instruction. **Step Over** treats the function call as a single step. When the debugger is in [Assembly Mode](debugging-in-assembly-mode.md), stepping occurs one machine instruction at a time. When the debugger is in [Source Mode](debugging-in-source-mode.md), stepping occurs one source line at a time.

-   To finish the current function and stop when the return occurs, use the **Step Out** or **Trace and Watch** commands. The **Step Out** command continues until the current function ends. **Trace and Watch** continues until the current function ends and also displays a summary of the function's calls. However, you must issue the **Trace and Watch** command on the first instruction of the function in question.

-   If an exception occurs, you can use the **Go with Exception Handled** and **Go with Exception Not Handled** commands to resume execution and control the status of the exception. (For more information about exceptions, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).)

-   (WinDbg only) If you select a line in the [Disassembly window](disassembly-window.md) or a [Source window](source-window.md) and then use the **Run to Cursor** command, the program runs until it encounters the selected line.

-   (User Mode only) To close the target application and restart it from the beginning, use the **Restart** command. You can use this command only with a process that the debugger created. After the process is restarted, it immediately breaks into the debugger.

-   (WinDbg only) To close the target application and clear the debugger, use the **Stop Debugging** command. This command enables you to start debugging a different target.

### <span id="command_forms"></span><span id="COMMAND_FORMS"></span>Command Forms

Most commands for starting or controlling the target's execution exist as text commands, menu commands, toolbar buttons, and shortcut keys. As basic text commands, you can use these commands in CDB, KD, or WinDbg. (The text form of the commands frequently supports additional options, such as changing the location of the program counter or executing a fixed number of instructions.) You can use the menu commands, toolbar buttons, and shortcut keys in WinDbg.

You can use the commands in the following forms.

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
<th align="left">Command</th>
<th align="left">WinDbg button</th>
<th align="left">WinDbg command</th>
<th align="left">WinDbg shortcut keys</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"></td>
<td align="left"><img src="images/tbcursor.png" alt="Screen shot of the Run to Cursor button" /></td>
<td align="left"><p>[Debug | Run to Cursor](debug---run-to-cursor.md)</p></td>
<td align="left"><p>F7</p>
<p>CTRL + F10</p></td>
<td align="left"><p>(WinDbg only) Executes until it reaches the line that the cursor marks.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><img src="images/tbstop.png" alt="Screen shot of the Stop Debugging button" /></td>
<td align="left"><p>[Debug | Stop Debugging](debug---stop-debugging.md)</p></td>
<td align="left"><p>SHIFT + F5</p></td>
<td align="left"><p>Stops all debugging and closes the target.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>(CDB/KD only) <strong>[CTRL+C](ctrl-c--break-.md)</strong></p></td>
<td align="left"><img src="images/tbbreak.png" alt="Screen shot of the Break button" /></td>
<td align="left"><p>[Debug | Break](debug---break.md)</p></td>
<td align="left"><p>CTRL + BREAK</p></td>
<td align="left"><p>Execution stops, and the debugger breaks into the target.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[.restart (Restart Target Application)](-restart--restart-target-application-.md)</strong></p></td>
<td align="left"><img src="images/tbrestart.png" alt="Screen shot of the Restart button" /></td>
<td align="left"><p>[Debug | Restart](debug---restart.md)</p></td>
<td align="left"><p>CTRL + SHIFT + F5</p></td>
<td align="left"><p>(User mode only) Restarts the target application.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[g (Go)](g--go-.md)</strong></p></td>
<td align="left"><img src="images/tbgo.png" alt="Screen shot of the Go button" /></td>
<td align="left"><p>[Debug | Go](debug---go.md)</p></td>
<td align="left"><p>F5</p></td>
<td align="left"><p>Target executes freely.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[gc (Go from Conditional Breakpoint)](gc--go-from-conditional-breakpoint-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Resumes execution after a [conditional breakpoint](setting-a-conditional-breakpoint.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[gh (Go with Exception Handled)](gh--go-with-exception-handled-.md)</strong></p></td>
<td align="left"></td>
<td align="left"><p>[Debug | Go Handled Exception](debug---go-handled-exception.md)</p></td>
<td align="left"></td>
<td align="left"><p>Same as <strong>g (Go)</strong>, except that the current exception is treated as handled.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[gn (Go with Exception Not Handled)](gn--gn--go-with-exception-not-handled-.md)</strong></p></td>
<td align="left"></td>
<td align="left"><p>[Debug | Go Unhandled Exception](debug---go-unhandled-exception.md)</p></td>
<td align="left"></td>
<td align="left"><p>Same as <strong>g (Go)</strong>, except that the current exception is treated as unhandled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[gu (Go Up)](gu--go-up-.md)</strong></p></td>
<td align="left"><img src="images/tbout.png" alt="Screen shot of the Step Out button" /></td>
<td align="left"><p>[Debug | Step Out](debug---step-out.md)</p></td>
<td align="left"><p>SHIFT + F11</p></td>
<td align="left"><p>Target executes until the current function is complete.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[p (Step)](p--step-.md)</strong></p></td>
<td align="left"><img src="images/tbover.png" alt="Screen shot of the Step Over button" /></td>
<td align="left"><p>[Debug | Step Over](debug---step-over.md)</p></td>
<td align="left"><p>F10</p></td>
<td align="left"><p>Target executes one instruction. If this instruction is a function call, that function is executed as a single step.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[pa (Step to Address)](pa--step-to-address-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Target executes until it reaches the specified address. All steps in this function are displayed (but steps in called functions are not).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[pc (Step to Next Call)](pc--step-to-next-call-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Target executes until the next <strong>call</strong> instruction. If the current instruction is a <strong>call</strong> instruction, this call is executed completely and execution continues until the next <strong>call</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[pct (Step to Next Call or Return)](pct--step-to-next-call-or-return-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Target executes until it reaches a <strong>call</strong> instruction or a <strong>return</strong> instruction.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[ph (Step to Next Branching Instruction)](ph--step-to-next-branching-instruction-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Target executes until it reaches any kind of branching instruction, including conditional or unconditional branches, calls, returns, and system calls.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[pt (Step to Next Return)](pt--step-to-next-return-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Target executes until it reaches a <strong>return</strong> instruction.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[t (Trace)](t--trace-.md)</strong></p></td>
<td align="left"><img src="images/tbinto.png" alt="Screen shot of the Step Into button" /></td>
<td align="left"><p>[Debug | Step Into](debug---step-into.md)</p></td>
<td align="left"><p>F11</p>
<p>F8</p></td>
<td align="left"><p>Target executes one instruction. If this instruction is a function call, debugger traces into that call.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[ta (Trace to Address)](ta--trace-to-address-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Target executes until it reaches the specified address. All steps in this function and called functions are displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[tb (Trace to Next Branch)](tb--trace-to-next-branch-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>(All modes, except kernel mode, only on x86-based systems) Target executes until it reaches the next branch instruction.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[tc (Trace to Next Call)](tc--trace-to-next-call-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Target executes until the next <strong>call</strong> instruction. If the current instruction is a <strong>call</strong> instruction, the instruction is traced into until a new <strong>call</strong> is reached.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[tct (Trace to Next Call or Return)](tct--trace-to-next-call-or-return-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Target executes until it reaches a <strong>call</strong> instruction or <strong>return</strong> instruction. If the current instruction is a <strong>call</strong> instruction or <strong>return</strong> instruction, the instruction is traced into until a new <strong>call</strong> or <strong>return</strong> is reached.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[th (Trace to Next Branching Instruction)](th--trace-to-next-branching-instruction-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Target executes until it reaches any kind of branching instruction, including conditional or unconditional branches, calls, returns, and system calls. If the current instruction is a branching instruction, the instruction is traced into until a new branching instruction is reached.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>[tt (Trace to Next Return)](tt--trace-to-next-return-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Target executes until it reaches a <strong>return</strong> instruction. If the current instruction is a <strong>return</strong> instruction, the instruction is traced into until a new <strong>return</strong> is reached.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>[wt (Trace and Watch Data)](wt--trace-and-watch-data-.md)</strong></p></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>Target executes until the completion of the whole specified function. Statistics are then displayed.</p></td>
</tr>
</tbody>
</table>

 

For more information about how to restart the target computer, see [Crashing and Rebooting the Target Computer](crashing-and-rebooting-the-target-computer.md).

### <span id="command_line_options"></span><span id="COMMAND_LINE_OPTIONS"></span>Command-Line Options

If you do not want the application to stop immediately when it starts or loads, use CDB or WinDbg together with the **-g** command-line option. For more information about this situation, see [Initial Breakpoint](initial-breakpoint.md).

CDB and WinDbg also support the **-G** [command-line option](command-line-options.md). This option causes the debugging session to end if the application completes properly.

The following command tries to run the application from start to finish, and the debugger prompt appears only if an error occurs.

```
cdb -g -G ApplicationName 
```

You can use the **-pt** [command-line option](command-line-options.md) to set the break time-out. There are certain problems that can make the target unable to communicate with the debugger. If a break command is issued and the debugger cannot break into the target after this time, the debugger displays a "Break-in timed out" message.

At this point, the debugger stops trying to break into the target. Instead, the debugger pauses the target and enables you to examine (but not control) the target application.

The default time-out is 30 seconds.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Controlling%20the%20Target%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




