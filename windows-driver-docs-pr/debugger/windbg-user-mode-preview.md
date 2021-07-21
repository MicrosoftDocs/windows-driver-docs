---
title: WinDbg Preview - Start a user mode session
description: This section describes how to start a user mode session with the WinDbg preview debugger.
ms.date: 01/09/2020
ms.localizationpriority: medium
---

# WinDbg Preview - Start a user mode session

![Small logo on windbg preview.](images/windbgx-preview-logo.png)

This section describes how to start a user mode session with the WinDbg preview debugger.

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

![Screenshot that shows the Launch Executable (advanced) dialog box with advanced options.](images/windbgx-launch-executable-advanced.png)

## Attach to a process

Use this option to attach to an existing process.

Select *Show process from all users* to show additional processes.

Use the search box to filter down the process list, for example by searching for SystemApps.

> [!NOTE]
> Items with a UAC shield will need the debugger to be elevated to attach.

Use the pull down dialog on the *Attach* button to select *non-invasive attach*.

![Launch Executable (advanced) dialog box with advanced options.](images/windbgx-attach-to-a-process.png)

## Launch App Package

Use this option to launch and attach to an app package using either the Applications of Background Task tabs. Use the search box to locate a specific app or background task. Use the Package Details button to display information about the package.

![Launch App Package Applications tab showing cal in the search box with three apps listed.](images/windbgx-launch-app-package.png)

---

## See Also

[Debugging Using WinDbg Preview](debugging-using-windbg-preview.md)
