---
title: WinDbg - Remote, Process Server and Dump file Sessions
description: This section describes how to start a remote, process server and dump file session with the WinDbg debugger.
keywords: ["Remote, Process Server and Dump file Sessions", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 01/10/2020
---

# WinDbg - Start a remote, process server and dump file session

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This section describes how to start a  remote, process server and dump file session with the WinDbg debugger.

## Remote Debug Server

Use this option to connect to a remote debugging server.

:::image type="content" source="images/windbgx-remote-session.png" alt-text="Screenshot of the Start Debugging Remote Debug Server dialog with blank connection fields.":::

Remote debugging involves two debuggers running at two different locations. The debugger that performs the debugging is called the debugging server. The second debugger, called the debugging client, controls the debugging session from a remote location. To establish a remote session, you must set up the debugging server first and then connect to it with the debugging client.

For more information about remote sessions, see [Remote WinDbg Features](../debugger/remote-debugging-using-windbg.md).

## Process Debug Server

Remote debugging through a process server involves running a small application called a process server on the server computer. Then a user-mode debugger is started on the client computer. Since this debugger will be doing all of the actual processing, it is called the smart client.

For more information about process server sessions, see [Process Servers (User Mode)](../debugger/process-servers--user-mode-.md).

## Open a dump file

To open a dump file, browse to the desired file in the provided file dialog and open it.

For more information about the different types of dump files, see [Analyze crash dump files by using WinDbg](../debugger/crash-dump-files.md).

---

## See Also

[WinDbg Features](../debugger/debugging-using-windbg-preview.md)
