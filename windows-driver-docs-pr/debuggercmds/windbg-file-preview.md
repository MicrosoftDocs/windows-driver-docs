---
title: 'WinDbg: File Menu'
description: "This article describes how to use the File menu in the WinDbg debugger."
keywords: ["File Menu", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 02/28/2026
ai-usage: ai-assisted
ms.topic: how-to
---

# WinDbg: File menu

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This article describes how to use the **File** menu in WinDbg.

### Start debugging

When you first open the **File** menu, you see **Start debugging** and your recent debugger targets. Use **Start debugging** to configure new and open previous debugger sessions.

#### Recent

The recent list contains a list of your recent debug sessions and debugger connections. For more information on how to work with settings, workspaces, and debug sessions, see [WinDbg setup: Settings, workspaces, and saved debug sessions](windbg-setup-preview.md).

You can use the right-click menu to manage your recent debug sessions, like pinning, renaming, and moving them. You can also edit them in Notepad.

:::image type="content" source="images/windbgx-workspace-right-click.png" alt-text="Right-click the menu for a workspace file with options to open, rename, edit in Notepad, pin, remove from lists, and clear unpinned targets.":::

#### Start a new session

Use the other tabs in the **Start debugging** section to start a new debugger session, like attaching or starting a process. For more information on starting a new session, see [WinDbg: Start a user-mode session](windbg-user-mode-preview.md)
and [WinDbg: Start a kernel mode session](windbg-kernel-mode-preview.md).

### Save debug session

Use **Save debug session** to save the current target connection information to a file. Debug session files use the `.debugtarget` extension. This option is only available when a debug target is active.

The default location for debug session files is:

```console
C:\Users\*UserName*\AppData\Local\DBG\Targets
```

### Open workspace

Use **Open workspace** to load settings from a previously saved workspace file. Workspace files use the `.xml` extension and are stored by default in:

```console
C:\Users\*UserName*\AppData\Local\DBG\Workspaces
```

### Save workspace

Use **Save workspace** to save the current settings to the active workspace file.

### Save workspace as

Use **Save workspace as** to save the current settings to a new workspace file.

### Open source file

Use **Open source file** to open a source file. Do this step when you want to work with other source files that didn't load because of code execution. For more information on working with source files, see [Source code debugging in WinDbg (Classic)](../debugger/source-window.md).

### Open script

Use **Open script** to open an existing JavaScript or NatVis script. For more information on working with scripts, see [WinDbg: Scripting menu](windbg-scripting-preview.md).

### Settings

Use **Settings** to set the source and symbol path and choose the theme for the debugger. The available themes are System (follows OS setting), Light, and Dark. For more information on settings, see [WinDbg setup: Settings, workspaces, and saved debug sessions](windbg-setup-preview.md).

### About

Use **About** to display build version information for the debugger. You can also use this screen to view the Microsoft privacy statement.

### Exit

Use **Exit** to exit the debugger.

---

## Related content

- [WinDbg features](../debugger/debugging-using-windbg-preview.md)
