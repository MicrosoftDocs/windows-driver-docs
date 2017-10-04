---
title: Keyboard Shortcuts
description: Keyboard Shortcuts
ms.assetid: 57c16d54-5b7a-4de8-9798-790aac7ec30d
keywords: ["control keys, WinDbg shortcut keys", "WinDbg, shortcut keys", "shortcut keys"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Keyboard Shortcuts


## <span id="ddk_shortcut_keys_dbg"></span><span id="DDK_SHORTCUT_KEYS_DBG"></span>


You can use the following keyboard shortcuts to switch between windows. For more information about how to move between the windows, see [Positioning the Windows](positioning-the-windows.md).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Keys</th>
<th align="left">Effect</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>CTRL+TAB</p></td>
<td align="left"><p>Switches between debugging information windows. By using this key repeatedly, you can scan through all of the windows, regardless of whether they are floating, docked by themselves, or part of a tabbed collection of docked windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ALT+TAB</p></td>
<td align="left"><p>Switches between the windows that are currently on your desktop. You can also use this keyboard shortcut to switch between the WinDbg frame and any additional docks you have created.</p></td>
</tr>
</tbody>
</table>

 

You can use the following keyboard shortcuts instead of the mouse to select menu commands. For more information about each command, see the individual command topics.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Keys</th>
<th align="left">Menu equivalent</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>F1</p></td>
<td align="left"><p>[Help | Contents](help---contents.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>F3</p></td>
<td align="left"><p>[Edit | Find Next](edit---find-next.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SHIFT+F3</p></td>
<td align="left"><p>Same as [Edit | Find Next](edit---find-next.md), except the search is performed in the reverse direction.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ALT+F4</p></td>
<td align="left"><p>[File | Exit](file---exit.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+F4</p></td>
<td align="left"><p>[File | Close Current Window](file---close-current-window.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>F5</p></td>
<td align="left"><p>[Debug | Go](debug---go.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SHIFT+F5</p></td>
<td align="left"><p>[Debug | Stop Debugging](debug---stop-debugging.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+SHIFT+F5</p></td>
<td align="left"><p>[Debug | Restart](debug---restart.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>F6</p></td>
<td align="left"><p>[File | Attach to a Process](file---attach-to-a-process.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>F7</p></td>
<td align="left"><p>[Debug | Run to Cursor](debug---run-to-cursor.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>F8</p></td>
<td align="left"><p>[Debug | Step Into](debug---step-into.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>F9</p></td>
<td align="left"><p>If the active window is a Source or Disassembly window: Inserts a breakpoint at the current line. (If there already is a breakpoint set at the current line, this button removes the breakpoint.)</p>
<p>Otherwise: Opens the <strong>Breakpoints</strong> dialog box like [Edit | Breakpoints](edit---breakpoints.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ALT+F9</p></td>
<td align="left"><p>[Edit | Breakpoints](edit---breakpoints.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>F10</p></td>
<td align="left"><p>[Debug | Step Over](debug---step-over.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+F10</p></td>
<td align="left"><p>[Debug | Run to Cursor](debug---run-to-cursor.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>F11</p></td>
<td align="left"><p>[Debug | Step Into](debug---step-into.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SHIFT+F11</p></td>
<td align="left"><p>[Debug | Step Out](debug---step-out.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>ALT+1</p></td>
<td align="left"><p>Opens the [Debugger Command window](debugger-command-window.md) (same as [View | Command](view---command.md)).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ALT+SHIFT+1</p></td>
<td align="left"><p>Closes the Command window.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ALT+2</p></td>
<td align="left"><p>Opens the Watch window (same as [View | Watch](view---watch.md)).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ALT+SHIFT+2</p></td>
<td align="left"><p>Closes the Watch window</p></td>
</tr>
<tr class="even">
<td align="left"><p>ALT+3</p></td>
<td align="left"><p>Opens the [Locals window](locals-window.md) (same as [View | Locals](view---locals.md))</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ALT+SHIFT+3</p></td>
<td align="left"><p>Closes the Locals window.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ALT+4</p></td>
<td align="left"><p>Opens the [Registers window](registers-window.md) (same as [View | Registers](view---registers.md)).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ALT+SHIFT+4</p></td>
<td align="left"><p>Closes the Registers window.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ALT+5</p></td>
<td align="left"><p>Opens a new [Memory window](memory-window.md) (same as [View | Memory](view---memory.md)).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ALT+SHIFT+5</p></td>
<td align="left"><p>Closes the Memory window.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ALT+6</p></td>
<td align="left"><p>Opens the [Calls window](calls-window.md) (same as [View | Call Stack](view---call-stack.md)).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ALT+SHIFT+6</p></td>
<td align="left"><p>Closes the Calls window</p></td>
</tr>
<tr class="even">
<td align="left"><p>ALT+7</p></td>
<td align="left"><p>Opens the [Disassembly window](disassembly-window.md) (same as [View | Disassembly](view---disassembly.md)).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ALT+SHIFT+7</p></td>
<td align="left"><p>Closes the Disassembly window.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ALT+8</p></td>
<td align="left"><p>Opens the Scratch Pad (same as [View | Scratch Pad](view---scratch-pad.md)).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ALT+SHIFT+8</p></td>
<td align="left"><p>Closes the Scratch Pad.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ALT+9</p></td>
<td align="left"><p>Opens the [Processes and Threads window](processes-and-threads-window.md) (same as [View | Processes and Threads](view---processes-and-threads.md)).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ALT+SHIFT+9</p></td>
<td align="left"><p>Closes the Processes and Threads window.</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+A</p></td>
<td align="left"><p>[Edit | Select All](edit---select-all.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+C</p></td>
<td align="left"><p>[Edit | Copy](edit---copy.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+D</p></td>
<td align="left"><p>[File | Open Crash Dump](file---open-crash-dump.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+E</p></td>
<td align="left"><p>[File | Open Executable](file---open-executable.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+F</p></td>
<td align="left"><p>[Edit | Find](edit---find.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+G</p></td>
<td align="left"><p>[Edit | Go to Address](edit---go-to-address.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+I</p></td>
<td align="left"><p>[File | Image File Path](file---image-file-path.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+SHIFT+I</p></td>
<td align="left"><p>[Edit | Set Current Instruction](edit---set-current-instruction.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+K</p></td>
<td align="left"><p>[File | Kernel Debug](file---kernel-debug.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+L</p></td>
<td align="left"><p>[Edit | Go to Line](edit---go-to-line.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+O</p></td>
<td align="left"><p>[File | Open Source File](file---open-source-file.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+P</p></td>
<td align="left"><p>[File | Source File Path](file---source-file-path.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+R</p></td>
<td align="left"><p>[File | Connect to Remote Session](file---connect-to-remote-session.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+S</p></td>
<td align="left"><p>[File | Symbol File Path](file---symbol-file-path.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+V</p></td>
<td align="left"><p>[Edit | Paste](edit---paste.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+SHIFT+V</p></td>
<td align="left"><p>[Edit | Evaluate Selection](edit---evaluate-selection.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+W</p></td>
<td align="left"><p>[File | Open Workspace](file---open-workspace.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+X</p></td>
<td align="left"><p>[Edit | Cut](edit---cut.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+SHIFT+Y</p></td>
<td align="left"><p>[Edit | Display Selected Type](edit---display-selected-type.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
ALT+<strong>*</strong>
(number keypad)</td>
<td align="left"><p>[Edit | Go to Current Instruction](edit---go-to-current-instruction.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>SHIFT+DELETE</p></td>
<td align="left"><p>[Edit | Cut](edit---cut.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SHIFT+INSERT</p></td>
<td align="left"><p>[Edit | Paste](edit---paste.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+INSERT</p></td>
<td align="left"><p>[Edit | Copy](edit---copy.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+BREAK</p></td>
<td align="left"><p>[Debug | Break](debug---break.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>ALT+DEL</p></td>
<td align="left"><p>[Debug | Break](debug---break.md)</p></td>
</tr>
</tbody>
</table>

 

The following shortcut keys are equivalent to KD / CDB control keys.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Keys</th>
<th align="left">Menu equivalent</th>
<th align="left">KD / CDB control key</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>CTRL+ALT+A</p></td>
<td align="left"><p>[Debug | Kernel Connection | Cycle Baud Rate](debug---kernel-connection---cycle-baud-rate.md)</p></td>
<td align="left"><p>CTRL+A</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+ALT+D</p></td>
<td align="left"></td>
<td align="left"><p><strong>[CTRL+D (Toggle Debug Info)](ctrl-d--toggle-debug-info-.md)</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+ALT+K</p></td>
<td align="left"><p>[Debug | Kernel Connection | Cycle Initial Break](debug---kernel-connection---cycle-initial-break.md)</p></td>
<td align="left"><p>CTRL+K</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+ALT+R</p></td>
<td align="left"><p>[Debug | Kernel Connection | Resynchronize](debug---kernel-connection---resynchronize.md)</p></td>
<td align="left"><p>CTRL+R</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CTRL+ALT+V</p></td>
<td align="left"><p>[View | Verbose Output](view---verbose-output.md)</p></td>
<td align="left"><p>CTRL+V</p></td>
</tr>
<tr class="even">
<td align="left"><p>CTRL+ALT+W</p></td>
<td align="left"><p>[View | Show Version](view---show-version.md)</p></td>
<td align="left"><p>CTRL+W</p></td>
</tr>
</tbody>
</table>

 

You can use the following keyboard shortcuts to move the caret (^) in most of the debugging information windows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Caret movement</th>
<th align="left">Key</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>One character left</p></td>
<td align="left"><p>LEFT</p></td>
</tr>
<tr class="even">
<td align="left"><p>One character right</p></td>
<td align="left"><p>RIGHT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Word left</p></td>
<td align="left"><p>CTRL+LEFT</p></td>
</tr>
<tr class="even">
<td align="left"><p>Word right</p></td>
<td align="left"><p>CTRL+RIGHT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Line up</p></td>
<td align="left"><p>UP</p></td>
</tr>
<tr class="even">
<td align="left"><p>Line down</p></td>
<td align="left"><p>DOWN</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Page up</p></td>
<td align="left"><p>PAGE UP</p></td>
</tr>
<tr class="even">
<td align="left"><p>Page down</p></td>
<td align="left"><p>PAGE DOWN</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Beginning of the current line</p></td>
<td align="left"><p>HOME</p></td>
</tr>
<tr class="even">
<td align="left"><p>End of the line</p></td>
<td align="left"><p>END</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Beginning of the file</p></td>
<td align="left"><p>CTRL+HOME</p></td>
</tr>
<tr class="even">
<td align="left"><p>End of the file</p></td>
<td align="left"><p>CTRL+END</p></td>
</tr>
</tbody>
</table>

 

**Note**   In the [Debugger Command window](debugger-command-window.md), the UP and DOWN keys browse through the command history. You can use the INSERT key to turn insert mode on and off.

 

Use the following keyboard shortcuts to select text.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Select</th>
<th align="left">Keys</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Character to the left</p></td>
<td align="left"><p>SHIFT+LEFT</p></td>
</tr>
<tr class="even">
<td align="left"><p>Character to the right</p></td>
<td align="left"><p>SHIFT+RIGHT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Word to the left</p></td>
<td align="left"><p>SHIFT+CTRL+LEFT</p></td>
</tr>
<tr class="even">
<td align="left"><p>Word to the right</p></td>
<td align="left"><p>SHIFT+CTRL+RIGHT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Current line</p></td>
<td align="left"><p>SHIFT+DOWN if the caret is in column 1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Line above</p></td>
<td align="left"><p>SHIFT+UP if the caret is in column 1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>To the end of the line</p></td>
<td align="left"><p>SHIFT+END</p></td>
</tr>
<tr class="even">
<td align="left"><p>To the beginning of the line</p></td>
<td align="left"><p>SHIFT+HOME</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Screen up</p></td>
<td align="left"><p>SHIFT+PAGE UP</p></td>
</tr>
<tr class="even">
<td align="left"><p>Screen down</p></td>
<td align="left"><p>SHIFT+PAGE DOWN</p></td>
</tr>
<tr class="odd">
<td align="left"><p>To beginning of file</p></td>
<td align="left"><p>SHIFT+CTRL+HOME</p></td>
</tr>
<tr class="even">
<td align="left"><p>To end of file</p></td>
<td align="left"><p>SHIFT+CTRL+END</p></td>
</tr>
</tbody>
</table>

 

Use the following keyboard shortcuts to delete text.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Delete</th>
<th align="left">Key</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Character to the right of caret</p></td>
<td align="left"><p>DELETE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Character to the left of caret</p></td>
<td align="left"><p>BACKSPACE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Selected text</p></td>
<td align="left"><p>DELETE</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Keyboard%20Shortcuts%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




