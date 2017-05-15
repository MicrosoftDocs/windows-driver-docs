---
title: Opening a Window
description: Opening a Window
ms.assetid: e056a556-8201-47e5-9a21-dbd5277c15c2
keywords: ["debugging information windows, opening"]
---

# Opening a Window


## <span id="ddk_opening_a_window_dbg"></span><span id="DDK_OPENING_A_WINDOW_DBG"></span>


When WinDbg begins a debugging session, the [Debugger Command window](debugger-command-window.md) automatically opens. The [Disassembly window](disassembly-window.md) also automatically opens, unless you deselect [Automatically Open Disassembly](window---automatically-open-disassembly.md) on the **Window** menu.

Whenever WinDbg discovers a source file that corresponds to the current program counter, WinDbg opens a [Source window](source-window.md) for that file. For other ways to open Source windows, see [Source Path](source-path.md).

You can use the following menu commands, toolbar buttons, and shortcut keys to switch to these windows. That is, if a window is not open, it opens. If a window is open but inactive, it becomes active. If a window is docked and there is a floating window in front of it, the docked window becomes active but the floating window stays in front of the docked window.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Window</th>
<th align="left">Menu command</th>
<th align="left">Button</th>
<th align="left">Shortcut keys</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[Debugger Command window](debugger-command-window.md)</p></td>
<td align="left"><p><strong>View | Command</strong></p></td>
<td align="left"><img src="images/tbcmd.png" alt="Screen shot of the Debugger Command window button" /></td>
<td align="left"><p>ALT+1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Watch window</p></td>
<td align="left"><p><strong>View | Watch</strong></p></td>
<td align="left"><img src="images/tbwatch.png" alt="Screen shot of the Watch button" /></td>
<td align="left"><p>ALT+2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Locals window](locals-window.md)</p></td>
<td align="left"><p><strong>View | Locals</strong></p></td>
<td align="left"><img src="images/tblocal.png" alt="Screen shot of the Locals button" /></td>
<td align="left"><p>ALT+3</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Registers window](registers-window.md)</p></td>
<td align="left"><p><strong>View | Registers</strong></p></td>
<td align="left"><img src="images/tbreg.png" alt="Screen shot of the Registers button" /></td>
<td align="left"><p>ALT+4</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Memory window](memory-window.md)</p></td>
<td align="left"><p><strong>View | Memory</strong></p></td>
<td align="left"><img src="images/tbmem.png" alt="Screen shot of the Memory button" /></td>
<td align="left"><p>ALT+5</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Calls window](calls-window.md)</p></td>
<td align="left"><p><strong>View | Call Stack</strong></p></td>
<td align="left"><img src="images/tbcall.png" alt="Screen shot of the Call Stack button" /></td>
<td align="left"><p>ALT+6</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Disassembly window](disassembly-window.md)</p></td>
<td align="left"><p><strong>View | Disassembly</strong></p></td>
<td align="left"><img src="images/tbdisasm2.png" alt="Screen shot of the Disassembly button" /></td>
<td align="left"><p>ALT+7</p></td>
</tr>
<tr class="even">
<td align="left"><p>Scratch Pad window</p></td>
<td align="left"><p><strong>View | Scratch Pad</strong></p></td>
<td align="left"><img src="images/tbspad.png" alt="Screen shot of the Scratch Pad button" /></td>
<td align="left"><p>ALT+8</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Processes and Threads window](processes-and-threads-window.md)</p></td>
<td align="left"><p><strong>View | Processes and Threads</strong></p></td>
<td align="left"><img src="images/window-processes-threads.png" alt="Screen shot of the Processes and Threads button" /></td>
<td align="left"><p>ALT+9</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Source window](source-window.md)</p></td>
<td align="left"><p>Click [File | Open Source File](file---open-source-file.md) and then select a source file.</p></td>
<td align="left"><img src="images/tbopen.png" alt="Screen shot of the Open Source File button" /></td>
<td align="left"><p>CTRL+O</p></td>
</tr>
</tbody>
</table>

 

You can also activate a window by selecting it from the [list of open windows](list-of-open-windows.md) at the bottom of the **Window** menu.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Opening%20a%20Window%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




