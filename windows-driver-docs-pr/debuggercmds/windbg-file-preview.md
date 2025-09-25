---
title: "WinDbg - File Menu"
description: "This article describes how to use the File menu in the WinDbg debugger."
keywords: ["File Menu", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 01/10/2020
ms.topic: how-to
---

# WinDbg: File menu

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This article describes how to use the **File** menu in WinDbg, the debugger for Windows.

### Start debugging

When you first open the **File** menu, you see **Start debugging** and your recent debugger targets. Use **Start debugging** to configure new and open previous debugger sessions.

#### Recent

The recent list contains a list of your recent workspaces and debugger connections. For more information on how to work with settings and workspaces, see [WinDbg setup: Settings and workspaces](windbg-setup-preview.md).

You can use the right-click menu to manage your workspaces, like pinning, renaming, and moving them. You can also edit them in Notepad.

:::image type="content" source="images/windbgx-workspace-right-click.png" alt-text="Right-click the menu for a workspace file with options to open, rename, edit in Notepad, pin, remove from lists, and clear unpinned targets.":::

#### Start a new session

Use the other tabs in the **Start debugging** section to start a new debugger session, like attaching or starting a process. For more information on starting a new session, see [WinDbg: Start a user-mode session](windbg-user-mode-preview.md)
and [WinDbg: Start a kernel mode session](windbg-kernel-mode-preview.md).

### Save workspace

Use **Save workspace** to save the current workspace.

Session connection information is stored in workspace configuration files. Workspace files are stored with a .debugTarget file extension.

The default location for workspace files is:

```console
C:\Users\*UserName*\AppData\Local\DBG\targets
```

### Open source file

Use **Open source file** to open a source file. Do this step when you want to work with other source files that didn't load because of code execution. For more information on working with source files, see [Source code debugging in WinDbg (classic)](../debugger/source-window.md)

### Open script

Use **Open script** to open an existing JavaScript or NatVis script. For more information on working with scripts, see [WinDbg: Scripting menu](windbg-scripting-preview.md).

### Settings

Use the **Settings** menu to set the source and symbol path and choose the light or dark theme for the debugger. For more information on settings, see [WinDbg setup: Settings and workspaces](windbg-setup-preview.md).

### About

Use **About** to display build version information for the debugger. You can also use this screen to view the Microsoft privacy statement.

### Exit

Use **Exit** to exit the debugger.

---

## Related content

- [WinDbg features](../debugger/debugging-using-windbg-preview.md)