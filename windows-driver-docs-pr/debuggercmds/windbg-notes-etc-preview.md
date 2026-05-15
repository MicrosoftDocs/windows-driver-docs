---
title: 'WinDbg: Notes, Command, Memory, and Source Menus'
description: "This article describes how to work with the Notes, Command, Memory, and Source ribbon tab menus."
keywords: ["Notes, Command, Memory and Source Menus", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 02/28/2026
ms.topic: how-to
ai-usage: ai-assisted
---

# WinDbg: Notes, Command, Memory, and Source menus

This article describes how to work with the **Notes**, **Command**, **Memory**, and **Source** ribbon tab menus in WinDbg. These ribbon tabs appear when the corresponding tool window is active.

## Notes

Use the **Notes** ribbon tab to:

- Open a notes file.
- Save a notes file.

## Command

The **Command** ribbon tab appears when the Command window is active. It contains the following groups:

### Preferences

- **Prefer DML** - Toggle whether commands in the engine provide plain text or Debugger Markup Language (DML) output, if available.
- **Auto Scroll** - Toggle whether the command window scroll position automatically synchronizes with the latest output.

### Selection

- **Highlight Selection** - Highlight or un-highlight the current text selection (Ctrl+Alt+H).
- **Erase Selection** - Erase the currently selected text from the command history.
- **Go to Previous** - Go to and select the previous command and its output (Ctrl+[).
- **Go to Next** - Go to and select the next command and its output (Ctrl+]).

### Actions

- **Clear History** - Erase all command window text.
- **Export History** - Write the command window text to a file.

### Command window context menu

You can also right-click in the Command window to access these options from a context menu:

- **Prefer DML** - Toggle DML output preference.
- **Automatically scroll** - Toggle automatic scrolling.
- **Highlight selection** (Ctrl+Alt+H) - Highlight or un-highlight the current text selection.
- **Erase selected text** - Erase the selected text from the command history.
- **Select previous command** (Ctrl+[) - Navigate to and select the previous command section.
- **Select next command** (Ctrl+]) - Navigate to and select the next command section.
- **Clear command history** - Erase all command window text.
- **Export command history** - Write the command window text to a file.

### Command window settings

Additional command window settings are available in the **Settings** page (accessible from the **File** menu) under **Command window**:

- **Command output settings**:
  - Copy text with formatting (font and colors).
  - Display tabular links (dx -g) in the UI instead of the console.
  - Disable keyboard shortcut to jump by section in command window output.
  - Maximum command output size (in lines).
- **Command prompt settings**:
  - Show command completion suggestions automatically.

## Memory

Use the **Memory** ribbon tab to:

- Set a data model memory query.
- Set the memory size, for example, to byte or long.
- Set the display format, for example, to hex or signed.
- Set the text display format, for example, to ASCII.

## Source

Use the **Source** ribbon tab to:

- Open a source file.
- Set an instruction pointer.
- Run to cursor.
- Close all source windows.

## Related content

- [WinDbg features](../debugger/debugging-using-windbg-preview.md)