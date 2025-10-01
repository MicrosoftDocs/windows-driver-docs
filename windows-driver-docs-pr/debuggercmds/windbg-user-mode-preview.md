---
title: 'WinDbg: Start a user mode session'
description: "This article describes how to start a user mode session with the WinDbg debugger."
keywords: ["Start a user mode session", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 11/23/2022
ms.topic: how-to
---

# WinDbg: Start a user mode session

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This article describes how to start a user mode session with WinDbg, the debugger for Windows.

Select **File** > **Start debugging**, and select either of these four options:

- **Launch executable**: Starts an executable and attaches to it by browsing for the target.
- **Launch executable (advanced)**: Starts an executable and attaches to it by using a set of dialogs with advanced options.
- **Attach to process**: Attaches to an existing process.
- **Launch app package**: Starts and attaches to an app package.

## Launch executable

Use this option to start an executable and attach to it.

Browse to the executable that you want in the file dialog and open it.

## Launch executable (advanced)

Use this option to start an executable and attach to it by using a set of text boxes with advanced options.

Specify the following options:

- **Executable**: Path to the executable, such as C:\Windows\notepad.exe.
- **Arguments**: Optional arguments to provide to the executable when launched.
- **Start directory**: Optional start directory location.
- **Target bitness**: Options are **Autodetect**, **32 bit**, or **64 bit**.
- **Debug child processes**: Option to enable the debug child process.
- **Record with Time Travel Debugging**: Option to enable Time Travel Debugging.

:::image type="content" source="images/windbgx-launch-executable-advanced.png" alt-text="Screenshot of the Launch executable (advanced) dialog displaying options.":::

## Attach to process

Use this option to attach to an existing process.

Select **Show process from all users** to show more processes.

Use the search box to filter down the process list, for example, by searching for `SystemApps`.

> [!NOTE]
> Items with a User Account Control shield need the debugger to be elevated to attach.

Use **Attach** to select **Non-invasive attach**.

:::image type="content" source="images/windbgx-attach-to-a-process.png" alt-text="Screenshot of the Attach to process dialog with process list and options.":::

## Launch app package

Use this option to launch and attach to an app package by using either the **Applications** or **Background Task** tabs. Use the search box to locate a specific app or background task. Select **Package Details** to display information about the package.

:::image type="content" source="images/windbgx-launch-app-package.png" alt-text="Screenshot of the Launch app package Applications tab with search results for cal and three apps displayed.":::

---

## Related content

- [WinDbg features](../debugger/debugging-using-windbg-preview.md)