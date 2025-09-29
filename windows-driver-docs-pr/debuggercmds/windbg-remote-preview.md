---
title: 'WinDbg: Remote, Process Server, and Dump File Sessions'
description: "This article describes how to start a remote, process server, or dump file session with the WinDbg debugger."
keywords: ["Remote, Process Server and Dump file Sessions", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 01/10/2020
ms.topic: how-to
ms.custom: sfi-image-nochange
---

# WinDbg: Start a remote, process server, and dump file session

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This article describes how to start a remote, process server, or dump file session with WinDbg, the debugger for Windows.

## Remote debug server

Use this option to connect to a remote debugging server.

:::image type="content" source="images/windbgx-remote-session.png" alt-text="Screenshot of the Start debugging pane and the Connect to remote debugger dialog with a blank connection field.":::

Remote debugging involves two debuggers running at two different locations. The debugger that performs the debugging is called the debugging server. The second debugger, called the debugging client, controls the debugging session from a remote location. To establish a remote session, you must set up the debugging server first and then connect to it with the debugging client.

For more information about remote sessions, see [Remote WinDbg features](../debugger/remote-debugging-using-windbg.md).

## Process debug server

Remote debugging through a process server involves running a small application called a process server on the server computer. Then a user-mode debugger is started on the client computer. This debugger is called the smart client because it does all the actual processing.

For more information about process server sessions, see [Process servers (user mode)](../debugger/process-servers--user-mode-.md).

## Open a dump file

To open a dump file, browse to the file that you want in the provided file dialog and open it.

For more information about the different types of dump files, see [Analyze crash dump files by using WinDbg](../debugger/crash-dump-files.md).

---

## Related content

-[WinDbg features](../debugger/debugging-using-windbg-preview.md)