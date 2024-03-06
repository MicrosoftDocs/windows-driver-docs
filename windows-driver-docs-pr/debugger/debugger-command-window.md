---
title: Entering Debugger Commands in WinDbg (Classic)
description: Entering Debugger Commands in WinDbg (Classic) using the Debugger Command window 
keywords: debugging information windows, command window, WinDbg
ms.date: 05/23/2017
---

# Entering Debugger Commands in WinDbg (Classic)

The Debugger Command window is the primary debugging information window in WinDbg. You can enter debugger commands and view the command output in this window.

This window displays "Command" in the title bar. However, this documentation always refers to this window as "the Debugger Command window" to avoid confusing it with the Command Prompt windows that are used to issue Microsoft MS-DOS commands.

## Opening the Debugger Command Window

To open the Debugger Command window, choose **Command** from the **View** menu. (You can also press ALT+1 or select the **Command** button on the toolbar. ALT+SHIFT+1 closes the Debugger Command window.)

The following screen shot shows an example of a Debugger Command window.

:::image type="content" source="images/window-command.png" alt-text="Screenshot of an example Debugger Command window.":::

### Using the Debugger Command Window

The Debugger Command window is split into two panes. You type commands in the smaller pane (the command entry pane) at the bottom of the window and view the output in the larger pane at the top of the window.

In the command entry pane, use the UP ARROW and DOWN ARROW keys to scroll through the command history. When a command appears, you can edit it or press ENTER to run the command.

The Debugger Command window contains a shortcut menu with additional commands. To access this menu, select and hold (or right-click) the title bar of the window or select the icon near the upper-right corner of the window. The following list describes some of the menu commands.

- **Add to command output** adds a comment to the command output, similar to the **Edit | Add to Command Output** command.

- **Clear command output** deletes all of the text in the window.

- **Choose text color and recolor selection...** opens a dialog box that enables you to choose the text color in which to display the text that is selected in the Debugger Command window.

- **Word wrap** turns the word wrap status on and off. This command affects the whole window, not only commands that you use after this state is selected. Because many commands and extensions produce formatted displays, it is not recommended that you use word wrap.

- **Mark current location** sets a marker at the current cursor location in the command window. The name of the mark is the contents of the line to the right of the cursor.

- **Go to mark** causes the window to scroll so that the line that contains the chosen mark is positioned at the top of the window.

- **Always floating** causes the window to remain undocked, even if it is dragged to a docking location.

- **Move with frame** causes the window to move when the WinDbg frame is moved, even if the window is undocked. 
