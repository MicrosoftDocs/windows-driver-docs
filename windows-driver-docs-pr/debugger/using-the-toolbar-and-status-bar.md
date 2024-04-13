---
title: Using the Toolbar and Status Bar - WinDbg (Classic)
description: Using the Toolbar and Status Bar - WinDbg (Classic)
keywords: ["toolbar (WinDbg)", "toolbar (WinDbg), overview", "buttons (WinDbg Toolbar)", "buttons (WinDbg Toolbar), overview", "status bar", "status bar, overview", "WinDbg, toolbar", "WinDbg, status bar", "WinDbg, buttons"]
ms.date: 05/23/2017
---

# Using the Toolbar and Status Bar - WinDbg (Classic)

The *toolbar* appears underneath the menu bar, near the top of the WinDbg window. The *status bar* appears at the bottom of the WinDbg window.

## Using the Toolbar

The following screen shot shows the WinDbg toolbar.

:::image type="content" source="images/toolbar4.png" alt-text="Screenshot of the WinDbg toolbar with various buttons.":::

The toolbar buttons have various effects. Most of them are equivalent to menu commands. To execute the command that is associated with a toolbar button, click the toolbar button. When you cannot use a button, it appears unavailable.

For more information about each button, see [Toolbar Buttons - WinDBg (Classic)](toolbar-buttons.md).

## Using the Status Bar

The following screen shot shows the WinDbg status bar.

:::image type="content" source="images/statusbar3.png" alt-text="Screenshot of the WinDbg status bar displaying different sections.":::

The following table describes the sections of the WinDbg status bar.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Section</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Message</p></td>
<td align="left"><p>Displays messages from the debugger.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Ln, Col</p></td>
<td align="left"><p>Displays the line number and column number at the cursor in the active <a href="source-window.md" data-raw-source="[Source window](source-window.md)">Source window</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Sys</p></td>
<td align="left"><p>Shows the internal decimal number of the system that you are debugging, followed by its computer name (or <strong>&lt;Local&gt;</strong> if it is the same as the computer as the debugger is running on).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Proc</p></td>
<td align="left"><p>Shows the internal decimal number of the process that you are debugging, followed by its hexadecimal process ID.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Thrd</p></td>
<td align="left"><p>Shows the internal decimal number of the thread that you are debugging, followed by its hexadecimal thread ID.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ASM</p></td>
<td align="left"><p>Indicates that WinDbg is in assembly mode. If ASM is unavailable, WinDbg is in source mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>OVR</p></td>
<td align="left"><p>Indicates that overtype mode is active. If OVR is unavailable, insert mode is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p>CAPS</p></td>
<td align="left"><p>Indicates that CAPS LOCK is on.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>NUM</p></td>
<td align="left"><p>Indicates that NUM LOCK is on.</p></td>
</tr>
</tbody>
</table>

## Hiding the Toolbar or Status Bar

To display or hide the toolbar, select or clear **Toolbar** on the **View** menu. To display or hide the status bar, select or clear **Status Bar** on the **View** menu.

If you hide the toolbar or the status bar, you have more space for debugging information windows in the WinDbg display area.

## Setting the Window Title

You can change the title of the WinDbg window by using the [**.wtitle (Set Window Title)**](../debuggercmds/-wtitle--set-window-title-.md) command.
