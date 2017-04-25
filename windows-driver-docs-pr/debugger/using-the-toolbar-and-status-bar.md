---
title: Using the Toolbar and Status Bar
description: Using the Toolbar and Status Bar
ms.assetid: 96427166-b6df-4f6b-b550-69d0eb33042d
keywords: ["toolbar (WinDbg)", "toolbar (WinDbg), overview", "buttons (WinDbg Toolbar)", "buttons (WinDbg Toolbar), overview", "status bar", "status bar, overview", "WinDbg, toolbar", "WinDbg, status bar", "WinDbg, buttons"]
---

# Using the Toolbar and Status Bar


## <span id="ddk_using_the_toolbar_and_status_bar_dbg"></span><span id="DDK_USING_THE_TOOLBAR_AND_STATUS_BAR_DBG"></span>


The *toolbar* appears underneath the menu bar, near the top of the WinDbg window. The *status bar* appears at the bottom of the WinDbg window.

### <span id="using_the_toolbar"></span><span id="USING_THE_TOOLBAR"></span>Using the Toolbar

The following screen shot shows the WinDbg toolbar.

![screen shot of the windbg toolbar](images/toolbar4.png)

The toolbar buttons have various effects. Most of them are equivalent to menu commands. To execute the command that is associated with a toolbar button, click the toolbar button. When you cannot use a button, it appears unavailable.

For more information about each button, see [Toolbar Buttons](https://msdn.microsoft.com/library/windows/hardware/ff558907).

### <span id="using_the_status_bar"></span><span id="USING_THE_STATUS_BAR"></span>Using the Status Bar

The following screen shot shows the WinDbg status bar.

![screen shot of the windbg status bar](images/statusbar3.png)

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
<td align="left"><p>Displays the line number and column number at the cursor in the active [Source window](source-window.md).</p></td>
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

 

### <span id="hiding_the_toolbar_or_status_bar"></span><span id="HIDING_THE_TOOLBAR_OR_STATUS_BAR"></span>Hiding the Toolbar or Status Bar

To display or hide the toolbar, select or clear [Toolbar](https://msdn.microsoft.com/library/windows/hardware/ff560319) on the **View** menu. To display or hide the status bar, select or clear [Status Bar](https://msdn.microsoft.com/library/windows/hardware/ff560318) on the **View** menu.

If you hide the toolbar or the status bar, you have more space for debugging information windows in the WinDbg display area.

### <span id="setting_the_window_title"></span><span id="SETTING_THE_WINDOW_TITLE"></span>Setting the Window Title

You can change the title of the WinDbg window by using the [**.wtitle (Set Window Title)**](https://msdn.microsoft.com/library/windows/hardware/ff566185) command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20the%20Toolbar%20and%20Status%20Bar%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




