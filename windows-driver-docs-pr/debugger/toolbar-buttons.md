---
title: Toolbar Buttons
description: Toolbar Buttons
ms.assetid: a32702fe-28c5-4b41-b4da-9a750946e5dd
keywords: ["toolbar (WinDbg), button descriptions", "buttons (WinDbg Toolbar), descriptions"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Toolbar Buttons


## <span id="ddk_toolbar_buttons_dbg"></span><span id="DDK_TOOLBAR_BUTTONS_DBG"></span>


Except for the breakpoint button, each button on the toolbar is equivalent to a menu command. For a full description of each button's effects, see the page for the corresponding menu command.

The buttons on the toolbar have the following effects.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Button</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><img src="images/tbopen.png" alt="Screen shot of the Open Source File button" /></td>
<td align="left"><p>Opens a source file as a read-only file. Equivalent to [File | Open Source File](file---open-source-file.md).</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbcut.png" alt="Screen shot of the Cut button" /></td>
<td align="left"><p>Removes the selected text from the active window and puts it on the clipboard. Equivalent to [Edit | Cut](edit---cut.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbcopy.png" alt="Screen shot of the Copy button" /></td>
<td align="left"><p>Copies the selected text from the active window to the clipboard. Equivalent to [Edit | Copy](edit---copy.md).</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbpaste.png" alt="Screen shot of the Paste button" /></td>
<td align="left"><p>Pastes the text on the clipboard to where the cursor is located. Equivalent to [Edit | Paste](edit---paste.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbgo.png" alt="Screen shot of the Go button" /></td>
<td align="left"><p>Starts or resumes execution. Execution continues until a breakpoint is reached, an exception or event occurs, the process ends, or the debugger breaks into the target. Equivalent to [Debug | Go](debug---go.md).</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbrestart.png" alt="Screen shot of the Restart button" /></td>
<td align="left"><p>Restarts execution at the beginning of the process. Equivalent to [Debug | Restart](debug---restart.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbstop.png" alt="Screen shot of the Stop Debugging button" /></td>
<td align="left"><p>Stops execution and terminates the target process permanently. Equivalent to [Debug | Stop Debugging](debug---stop-debugging.md).</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbbreak.png" alt="Screen shot of the Break button" /></td>
<td align="left"><p>In user mode, this button stops the process and its threads. In kernel mode, this button breaks into the target computer. Control is returned to the debugger. This button is also useful for cutting off long [Debugger Command window](the-debugger-command-window.md) displays. Equivalent to [Debug | Break](debug---break.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbinto.png" alt="Screen shot of the Step Into button" /></td>
<td align="left"><p>Executes a single instruction. If the instruction is a function call, the debugger steps into the function. Equivalent to [Debug | Step Into](debug---step-into.md).</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbover.png" alt="Screen shot of the Step Over button" /></td>
<td align="left"><p>Executes a single instruction. If the instruction is a function call, the debugger executes the whole function in one step. Equivalent to [Debug | Step Over](debug---step-over.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbout.png" alt="Screen shot of the Step Out button" /></td>
<td align="left"><p>Executes the rest of the current function, and breaks when the function return is completed. Equivalent to [Debug | Step Out](debug---step-out.md).</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbcursor.png" alt="Screen shot of the Run to Cursor button" /></td>
<td align="left"><p>Executes all instructions from the current instruction up to the instruction marked in the active Disassembly window or Source window. Equivalent to [Debug | Run to Cursor](debug---run-to-cursor.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbbp.png" alt="Screen shot of the Breakpoints button" /></td>
<td align="left"><p><strong>If the active window is a Source or Disassembly window:</strong> Inserts a breakpoint at the current line. (If there already is a breakpoint set at the current line, this button removes the breakpoint.)</p>
<p><strong>Otherwise:</strong> Opens the <strong>Breakpoints</strong> dialog box like [Edit | Breakpoints](edit---breakpoints.md).</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbcmd.png" alt="Screen shot of the Command button" /></td>
<td align="left"><p>Opens or activates the [Debugger Command](the-debugger-command-window.md) window. Equivalent to [View | Command](view---command.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbwatch.png" alt="Screen shot of the Watch button" /></td>
<td align="left"><p>Opens or activates the Watch window. Equivalent to [View | Watch](view---watch.md).</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tblocal.png" alt="Screen shot of the Locals button" /></td>
<td align="left"><p>Opens or activates the Locals window. Equivalent to [View | Locals](view---locals.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbreg.png" alt="Screen shot of the Registers button" /></td>
<td align="left"><p>Opens or activates the Registers window. Equivalent to [View | Registers](view---registers.md).</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbmem.png" alt="Screen shot of the Memory button" /></td>
<td align="left"><p>Opens a new Memory window. Equivalent to [View | Memory](view---memory.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbcall.png" alt="Screen shot of the Call Stack button" /></td>
<td align="left"><p>Opens or activates the Calls window. Equivalent to [View | Call Stack](view---call-stack.md).</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbdisasm2.png" alt="Screen shot of the Disassembly button" /></td>
<td align="left"><p>Opens or activates the Disassembly window. Equivalent to [View | Disassembly](view---disassembly.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbspad.png" alt="Screen shot of the Scratch Pad button" /></td>
<td align="left"><p>Opens or activates the Scratch Pad. Equivalent to [View | Scratch Pad](view---scratch-pad.md).</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbsrcasm.png" alt="Screen shot of the Source Mode button" /></td>
<td align="left"><p>Switches between source-mode and assembly-mode debugging. Equivalent to selecting or clearing [Debug | Source Mode](debug---source-mode.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbfont.png" alt="Screen shot of the Font button" /></td>
<td align="left"><p>Enables you to change the font that is used in the debugging information windows. Equivalent to [View | Font](view---font.md).</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbopt.png" alt="Screen shot of the Options button" /></td>
<td align="left"><p>Displays the <strong>Options</strong> dialog box. Equivalent to [View | Options](view---options.md).</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Toolbar%20Buttons%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




