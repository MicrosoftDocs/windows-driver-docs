---
title: Using the Command Browser Window in WinDbg (Classic) Classic
description: Using the Command Browser Window in WinDbg (Classic) Classic
keywords: ["debugging information windows, command browser window", "command browser window", "Debugger Command window, command browser window"]
ms.date: 05/23/2017
---

# Using the Command Browser Window in WinDbg (Classic) Classic

A Command Browser window displays and stores the text results of a debugger command. This window creates a command reference that enables you to view the results of a specific command without re-entering the command. A Command Browser window also provides navigation through the stored commands, so you can more quickly access commands than with the [Debugger Command window](debugger-command-window.md).

## Opening the Command Browser Window

You can open multiple Command Browser windows at one time. To open a Command Browser window, choose **Command Browser** from the **View** menu. (You can also press CTRL+N or click the **Command Browser** button on the toolbar. ALT+SHIFT+N closes the Command Browser window.)

You can also open a Command Browser window by entering [**.browse (Display Command in Browser)**](../debuggercmds/-browse--display-command-in-browser-.md) in the regular Debugger Command window.

The following screen shot shows an example of a Command Browser window.

:::image type="content" source="images/window-commandbrowser.png" alt-text="Screenshot of an example Command Browser window.":::

## Using the Command Browser Window

In the Command Browser window, you can do the following:

- To enter a command, type it in the **Command** box.

- To view the results of a previously entered command, use the **Start**, **Prev**, and **Next** buttons to scroll through the command list, or select one of the preceding 20 commands from the **Command** menu. To find a command that is not one of the preceding 20 commands, use the **Next** button.

The Command Browser window has a shortcut menu with additional commands. To access the menu, right-click the title bar or click the icon near the upper-right corner of the window. The following list describes some of the menu commands.

- **Start**, **Prev**, and **Next** move the cursor to the start of the command history or to the previous or next command, respectively.

- **Add to Recent Commands** puts the current command into the **Recent Commands** menu of the **View** menu in the WinDbg window. Recent commands are saved in the workspace.

- **Toolbar** turns the toolbar on and off.

- **Move to new dock** closes the Command Browser window and opens it in a new dock.

- **Always floating** causes the window to remain undocked even if it is dragged to a docking location.

- **Move with frame** causes the window to move when the WinDbg frame is moved, even if the window is undocked. 

Commands that you enter in a Command Browser window are executed by the debugger engine, not by the WinDbg user interface. This means that you cannot enter user interface commands like [**.cls**](../debuggercmds/-cls--clear-screen-.md) in a Command Browser window. If the user interface is a remote client, the server (not the client) executes the command.

A command that you enter in a Command Browser window executes synchronously, so it does not display output until it has completed.

Command Browser windows are saved in the WinDbg workspace, but the command histories are not saved. Only the current command for each Command Browser window is saved in the workspace.
