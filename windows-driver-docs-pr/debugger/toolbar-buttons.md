---
title: Toolbar Buttons - WinDBg (Classic)
description: Toolbar Buttons - WinDBg (Classic)
keywords: ["toolbar (WinDbg), button descriptions", "buttons (WinDbg Toolbar), descriptions"]
ms.date: 05/23/2017
---

# Toolbar Buttons - WinDBg (Classic)


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
<td align="left"><p>Opens a source file as a read-only file. Equivalent to File | Open Source File.</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbcut.png" alt="Screen shot of the Cut button" /></td>
<td align="left"><p>Removes the selected text from the active window and puts it on the clipboard. Equivalent to Edit | Cut.</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbcopy.png" alt="Screen shot of the Copy button" /></td>
<td align="left"><p>Copies the selected text from the active window to the clipboard. Edit | Copy.</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbpaste.png" alt="Screen shot of the Paste button" /></td>
<td align="left"><p>Pastes the text on the clipboard to where the cursor is located. Equivalent to Edit | Paste.</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbgo.png" alt="Screen shot of the Go button" /></td>
<td align="left"><p>Starts or resumes execution. Execution continues until a breakpoint is reached, an exception or event occurs, the process ends, or the debugger breaks into the target. Equivalent to Debug | Go.</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbrestart.png" alt="Screen shot of the Restart button" /></td>
<td align="left"><p>Restarts execution at the beginning of the process. Equivalent to Debug | Restart.</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbstop.png" alt="Screen shot of the Stop Debugging button" /></td>
<td align="left"><p>Stops execution and terminates the target process permanently. Equivalent to Debug | Stop Debugging.</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbbreak.png" alt="Screen shot of the Break button" /></td>
<td align="left"><p>In user mode, this button stops the process and its threads. In kernel mode, this button breaks into the target computer. Control is returned to the debugger. This button is also useful for cutting off long <a href="the-debugger-command-window.md" data-raw-source="[Debugger Command window](the-debugger-command-window.md)">Debugger Command window</a> displays. Equivalent to Debug | Break.</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbinto.png" alt="Screen shot of the Step Into button" /></td>
<td align="left"><p>Executes a single instruction. If the instruction is a function call, the debugger steps into the function. Equivalent to Debug | Step Into.</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbover.png" alt="Screen shot of the Step Over button" /></td>
<td align="left"><p>Executes a single instruction. If the instruction is a function call, the debugger executes the whole function in one step. Equivalent to Debug | Step Over.</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbout.png" alt="Screen shot of the Step Out button" /></td>
<td align="left"><p>Executes the rest of the current function, and breaks when the function return is completed. Equivalent to Debug | Step Out.</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbcursor.png" alt="Screen shot of the Run to Cursor button" /></td>
<td align="left"><p>Executes all instructions from the current instruction up to the instruction marked in the active Disassembly window or Source window. Equivalent to Debug | Run to Cursor.</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbbp.png" alt="Screen shot of the Breakpoints button" /></td>
<td align="left"><p><strong>If the active window is a Source or Disassembly window:</strong> Inserts a breakpoint at the current line. (If there already is a breakpoint set at the current line, this button removes the breakpoint.)</p>
<p><strong>Otherwise:</strong> Opens the <strong>Breakpoints</strong> dialog box like Edit | Breakpoints.</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbcmd.png" alt="Screen shot of the Command button" /></td>
<td align="left"><p>Opens or activates the <a href="the-debugger-command-window.md" data-raw-source="[Debugger Command](the-debugger-command-window.md)">Debugger Command</a> window. Equivalent to View | Command.</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbwatch.png" alt="Screen shot of the Watch button" /></td>
<td align="left"><p>Opens or activates the Watch window. View | Watch.</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tblocal.png" alt="Screen shot of the Locals button" /></td>
<td align="left"><p>Opens or activates the Locals window. Equivalent to View | Locals.</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbreg.png" alt="Screen shot of the Registers button" /></td>
<td align="left"><p>Opens or activates the Registers window. Equivalent to View | Registers.</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbmem.png" alt="Screen shot of the Memory button" /></td>
<td align="left"><p>Opens a new Memory window. Equivalent to View | Memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbcall.png" alt="Screen shot of the Call Stack button" /></td>
<td align="left"><p>Opens or activates the Calls window. Equivalent to View | Call Stack.</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbdisasm2.png" alt="Screen shot of the Disassembly button" /></td>
<td align="left"><p>Opens or activates the Disassembly window. Equivalent to View | Disassembly.</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbspad.png" alt="Screen shot of the Scratch Pad button" /></td>
<td align="left"><p>Opens or activates the Scratch Pad. Equivalent to View | Scratch Pad.</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbsrcasm.png" alt="Screen shot of the Source Mode button" /></td>
<td align="left"><p>Switches between source-mode and assembly-mode debugging. Equivalent to selecting or clearing Debug | Source Mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><img src="images/tbfont.png" alt="Screen shot of the Font button" /></td>
<td align="left"><p>Enables you to change the font that is used in the debugging information windows. Equivalent to View | Font.</p></td>
</tr>
<tr class="even">
<td align="left"><img src="images/tbopt.png" alt="Screen shot of the Options button" /></td>
<td align="left"><p>Displays the <strong>Options</strong> dialog box. Equivalent to View | Options.</p></td>
</tr>
</tbody>
</table>

 

 

 





