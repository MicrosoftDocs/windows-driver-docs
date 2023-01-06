---
title: Keyboard shortcuts
description: Learn how to use keyboard shortcuts to switch between windows, select menu commands, use KD and CDB control keys, move the caret, select text, and delete text.
keywords: ["control keys, WinDbg shortcut keys", "WinDbg, shortcut keys", "shortcut keys"]
ms.date: 12/19/2022
---

# Keyboard shortcuts

You can use the following keyboard shortcuts to switch between windows. For more information about how to move between the windows, see [Positioning the windows](positioning-the-windows.md).

| Keys | Effect |
|:---- |:------ |
| Ctrl+Tab | Switches between debugging information windows. By using this key repeatedly, you can scan through all of the windows, regardless of whether they're floating, docked by themselves, or part of a tabbed collection of docked windows. |
| Alt+Tab | Switches between the windows that are currently on your desktop. You can also use this keyboard shortcut to switch between the WinDbg frame and any other docks you've created. |

You can use the following keyboard shortcuts instead of the mouse to select menu commands. For more information about each command, see the individual command articles.

| Keys | Menu equivalent |
|:---- |:--------------- |
| F1 | [Help \| Contents](help---contents.md) |
| F3 | [Edit \| Find Next](edit---find-next.md) |
| Shift+F3 | Same as [Edit \| Find Next](edit---find-next.md), except that the search is performed in the reverse direction. |
| Alt+F4 | [File \| Exit](file---exit.md) |
| Ctrl+F4 | [File \| Close Current Window](file---close-current-window.md) |
| F5 | [Debug \| Go](debug---go.md) |
| Shift+F5 | [Debug \| Stop Debugging](debug---stop-debugging.md) |
| Ctrl+Shift+F5 | [Debug \| Restart](debug---restart.md) |
| F6 | [File \| Attach to a Process](file---attach-to-a-process.md) |
| F7 | [Debug \| Run to Cursor](debug---run-to-cursor.md) |
| F8 | [Debug \| Step Into](debug---step-into.md) |
| F9 | If the active window is a **Source** or **Disassembly** window: Inserts a breakpoint at the current line. If there already is a breakpoint set at the current line, this key removes the breakpoint. Otherwise: Opens the **Breakpoints** dialog box like [Edit \| Breakpoints](edit---breakpoints.md). |
| Alt+F9 | [Edit \| Breakpoints](edit---breakpoints.md) |
| F10 | [Debug \| Step Over](debug---step-over.md) |
| Ctrl+F10 | [Debug \| Run to Cursor](debug---run-to-cursor.md) |
| F11 | [Debug \| Step Into](debug---step-into.md) |
| Shift+F11 | [Debug \| Step Out](debug---step-out.md) |
| Alt+1 | [Debugger Command window](debugger-command-window.md), same as [View \| Command](view---command.md). |
| Alt+Shift+1 | Closes the **Command** window. |
| Alt+2 | Opens the **Watch** window, same as [View \| Watch](view---watch.md). |
| Alt+Shift+2 | Closes the **Watch** window |
| Alt+3 | [Locals window](locals-window.md), same as [View \| Locals](view---locals.md). |
| Alt+Shift+3 | Closes the **Locals** window. |
| Alt+4 | Opens the [Registers window](registers-window.md), same as [View \| Registers](view---registers.md). |
| Alt+Shift+4 | Closes the **Registers** window. |
| Alt+5 | [Memory window](memory-window.md), same as [View \| Memory](view---memory.md). |
| Alt+Shift+5 | Closes the **Memory** window. |
| Alt+6 | Opens the [Calls window](calls-window.md), same as [View \| Call Stack](view---call-stack.md). |
| Alt+Shift+6 | Closes the **Calls** window |
| Alt+7 | Opens the [Disassembly window](disassembly-window.md), same as [View \| Disassembly](view---disassembly.md). |
| Alt+Shift+7 | Closes the **Disassembly** window. |
| Alt+8 | Opens the **Scratch Pad**, same as [View \| Scratch Pad](view---scratch-pad.md). |
| Alt+Shift+8 | Closes the **Scratch Pad**. |
| Alt+9 | Opens the [Processes and Threads window](processes-and-threads-window.md), same as [View \| Processes and Threads](view---processes-and-threads.md). |
| Alt+Shift+9 | Closes the **Processes and Threads** window. |
| Ctrl+A | [Edit \| Select All](edit---select-all.md) |
| Ctrl+C | [Edit \| Copy](edit---copy.md) |
| Ctrl+D | [File \| Open Crash Dump](file---open-crash-dump.md) |
| Ctrl+E | [File \| Open Executable](file---open-executable.md) |
| Ctrl+F | [Edit \| Find](edit---find.md) |
| Ctrl+G | [Edit \| Go to Address](edit---go-to-address.md) |
| Ctrl+I | [File \| Image File Path](file---image-file-path.md) |
| Ctrl+Shift+I | [Edit \| Set Current Instruction](edit---set-current-instruction.md) |
| Ctrl+K | [File \| Kernel Debug](file---kernel-debug.md) |
| Ctrl+L | [Edit \| Go to Line](edit---go-to-line.md) |
| Ctrl+O | [File \| Open Source File](file---open-source-file.md) |
| Ctrl+P | [File \| Source File Path](file---source-file-path.md) |
| Ctrl+R | [File \| Connect to Remote Session](file---connect-to-remote-session.md) |
| Ctrl+S | [File \| Symbol File Path](file---symbol-file-path.md) |
| Ctrl+V | [Edit \| Paste](edit---paste.md) |
| Ctrl+Shift+V | [Edit \| Evaluate Selection](edit---evaluate-selection.md) |
| Ctrl+W | [File \| Open Workspace](file---open-workspace.md) |
| Ctrl+X | [Edit \| Cut](edit---cut.md) |
| Ctrl+Shift+Y | [Edit \| Display Selected Type](edit---display-selected-type.md) |
| Alt+* (numeric keypad) | [Edit \| Go to Current Instruction](edit---go-to-current-instruction.md) |
| Shift+Delete | [Edit \| Cut](edit---cut.md) |
| Shift+Insert | [Edit \| Paste](edit---paste.md) |
| Ctrl+Insert | [Edit \| Copy](edit---copy.md) |
| Ctrl+Break | [Debug \| Break](debug---break.md) |
| Alt+Delete | [Debug \| Break](debug---break.md) |

The following shortcut keys are equivalent to KD / CDB control keys.

| Keys | Menu equivalent | KD / CDB control key |
|:---- |:--------------- |:-------------------- |
| Ctrl+Alt+A | [Debug \| Kernel Connection \| Cycle Baud Rate](debug---kernel-connection---cycle-baud-rate.md) | Ctrl+A |
| Ctrl+Alt+D | | [Ctrl+D (Toggle Debug Info)](ctrl-d--toggle-debug-info-.md) |
| Ctrl+Alt+K | [Debug \| Kernel Connection \| Cycle Initial Break](debug---kernel-connection---cycle-initial-break.md) | Ctrl+K |
| Ctrl+Alt+R | [Debug \| Kernel Connection \| Resynchronize](debug---kernel-connection---resynchronize.md) | Ctrl+R |
| Ctrl+Alt+V | [View \| Verbose Output](view---verbose-output.md) | Ctrl+V |
| Ctrl+Alt+W | [View \| Show Version](view---show-version.md) | Ctrl+W |

You can use the following keyboard shortcuts to move the caret (^) in most of the debugging information windows.

| Caret movement | Keys |
|:-------------- |:---- |
| One character left | Left arrow |
| One character right | Right arrow |
| Word left | Ctrl+Left arrow |
| Word right | Ctrl+Right arrow |
| Line up | Up arrow |
| Line down | Down arrow |
| Page up | Page up |
| Page down | Page down |
| Beginning of the current line | Home |
| End of the line | End |
| Beginning of the file | Ctrl+Home |
| End of the file | Ctrl+End |

In the [Debugger Command window](debugger-command-window.md), the Up arrow key and the Down arrow key browse through the command history. You can use the **Insert** key to turn insert mode on and off.

Use the following keyboard shortcuts to select text.

| Select | Keys |
|:------ |:---- |
| Character to the left of current location | Shift+Left arrow |
| Character to the right of current location | Shift+Right arrow |
| Word to the left of current location | Shift+Ctrl+Left arrow |
| Word to the right of current location | Shift+Ctrl+Right arrow |  
| Current line | Shift+Down arrow if the caret is in column 1 |
| Line above the current location | Shift+Up arrow if the caret is in column 1 |
| To the end of the line | Shift+End |
| To the beginning of the line | Shift+Home |
| Screen up | Shift+Page up |
| Screen down | Shift+Page down |
| To beginning of file | Shift+Ctrl+Home |
| To end of file | Shift+Ctrl+End |

Use the following keyboard shortcuts to delete text.

| Delete | Key |
|:------ |:--- |
| Character to the right of caret | Delete |
| Character to the left of caret | Backspace |
| Selected text | Delete |
