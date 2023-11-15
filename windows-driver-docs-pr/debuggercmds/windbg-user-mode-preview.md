---
title: WinDbg - Start a user mode session
description: This section describes how to start a user mode session with the WinDbg debugger.
ms.date: 11/23/2022
---

# WinDbg - Start a user mode session

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This section describes how to start a user mode session with the WinDbg debugger.

Select *File*, *Start debugging*, and select either of these four options:

- *Launch Executable* - Starts an executable and attaches to it by browsing for the target.
- *Launch Executable (advanced)* - Starts an executable and attaches to it using a set of dialog boxes with advanced options.
- *Attach to a process* - Attaches to an existing process.
- *Launch App Package* - Launches and attaches to an app package.

All four options are described here.

## Launch Executable

Use this option to starts an executable and attach to it.

Browse to the desired executable in the provided file dialog and open it. 

## Launch Executable (advanced)

Use this option to start an executable and attach to it using a set of text boxes with advanced options. 

Specify the following options:
- Path to the executable, such as *C:\Windows\notepad.exe*
- Optional arguments to provide to the executable when launched
- Optional start directory location
- Target bitness, auto 32 or 64.
- Enable Debug child process
- Record with Time Travel Debugging

:::image type="content" source="images/windbgx-launch-executable-advanced.png" alt-text="Screenshot of Launch Executable (advanced) dialog box displaying various options.":::

## Attach to a process

Use this option to attach to an existing process.

Select *Show process from all users* to show additional processes.

Use the search box to filter down the process list, for example by searching for SystemApps.

> [!NOTE]
> Items with a UAC shield will need the debugger to be elevated to attach.

Use the pull down dialog on the *Attach* button to select *non-invasive attach*.

:::image type="content" source="images/windbgx-attach-to-a-process.png" alt-text="Screenshot of Attach to a Process dialog box with process list and options.":::

## Launch App Package

Use this option to launch and attach to an app package using either the Applications of Background Task tabs. Use the search box to locate a specific app or background task. Use the Package Details button to display information about the package.

:::image type="content" source="images/windbgx-launch-app-package.png" alt-text="Screenshot of Launch App Package Applications tab with search results for 'cal' and three apps displayed.":::

---

## See Also

[WinDbg Features](../debugger/debugging-using-windbg-preview.md)
