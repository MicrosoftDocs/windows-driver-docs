---
title: Tools included in Debugging Tools for Windows
description: Learn about the tools that are included in Debugging Tools for Windows in addition to the debugging engine and debugging environments.
ms.date: 12/15/2022
---

# Tools included in Debugging Tools for Windows

Debugging Tools for Windows includes several tools in addition to the debugging engine and [debugging environments](debuggers-in-the-debugging-tools-for-windows-package.md). The tools are in the [installation directory](#installation-directories) of Debugging Tools for Windows.

<a name="additional_tools_and_utilities"></a>

## Tools and utilities

| Name | Description |
| --- | --- |
| [DumpChk](dumpchk.md) | Validate a memory dump file. |
| [GFlags](gflags.md) | Control registry keys and other settings. |
| [Kill](kill-tool.md) | Terminate a process. |
| [Logger and LogViewer](logger-and-logviewer.md) | Record and display function calls and other actions of a program. |
| [PLMDebug](plmdebug.md) | Use the Windows debugger to debug Windows app that run under Process Lifecycle Management (PLM). With PLMDebug, you can take manual control of suspending, resuming, and terminating a Windows app. |
| [Remote Tool](remote-tool.md) | Remotely control any console program, including KD, CDB, and NTSD. See [Remote debugging by using Remote.exe](remote-debugging-through-remote-exe.md). |
| [TList](tlist.md) | List all running processes. |
| [UMDH](umdh.md) | Analyze heap allocations. |
| [USBView](usbview.md) | Display USB host controllers and connected devices. |
| DbgRpc (Dbgrpc.exe) | Display Microsoft Remote Procedure Call (RPC) state information. See [RPC debugging](rpc-debugging.md) and [Using the DbgRpc tool](using-the-dbgrpc-tool.md). |
| KDbgCtrl (Kernel Debugging Control, Kdbgctrl.exe) | Control and configure the kernel debugging connection. See [Using KDbgCtrl](using-kdbgctrl.md). |
| [SrcSrv](srcsrv.md) | A source server that can be used to deliver source files while debugging. |
| SymSrv | A symbol server that the debugger can use to connect to a symbol store. For information about working with the symbol server, see [Microsoft public symbols](microsoft-public-symbols.md). |
| [SymProxy](symproxy.md) | Create a single HTTP symbol server on your network that all your debuggers can point to. This approach has the benefit of pointing to multiple symbol servers (both internal and external) with a single symbol path, handling all authentication, and increasing performance via symbol caching. *Symproxy.dll* is in the *SymProxy* folder in the [installation directory](#installation-directories). |
| [SymChk](symchk.md) | Compare executable files to symbol files to verify that the correct symbols are available. |
| [SymStore](symstore.md) | Create a symbol store. See [Using SymStore](symstore.md). |
| [AgeStore](agestore.md) | Remove old entries in the downstream store of a symbol server or a source server. |
| [DBH](dbh.md) | Display information about the contents of a symbol file. |
| [PDBCopy](pdbcopy.md) | Remove private symbol information from a symbol file, and control that public symbols are included in the file. |
| DbgSrv | A process server used for remote debugging. See [Process servers (user mode)](process-servers--user-mode-.md). |
| KdSrv | A KD connection server used for remote debugging. See [KD connection servers (kernel mode)](kd-connection-servers--kernel-mode-.md). |
| DbEngPrx | A repeater (small proxy server) used for remote debugging. See [Repeaters](repeaters.md). |
| Breakin (Breakin.exe) | Causes a user-mode break to occur in a process. For help, open a Command Prompt window, go to the [installation directory](#installation-directories), and enter `breakin /?`. |
| List (File List Utility) (List.exe) | For help, open a Command Prompt window, go to the [installation directory](#installation-directories), and enter `list /?`. |
| RTList (Remote Task List Viewer) (Rtlist.exe) | List running processes via a DbgSrv process server. For help, open a Command Prompt window, go to the [installation directory](#installation-directories), and enter `rtlist /?`. |

<a name="installation-directories"></a>

## Installation directory

The default installation directory for 64-bit OS installations of the debugging tools is C:\\Program Files (x86)\\Windows Kits\\10\\Debuggers\\. If you have a 32-bit OS, you can find the Windows Kits folder under C:\\Program Files. To determine whether you should use the 32-bit or 64-bit tools, see [Choosing the 32-bit or 64-bit debugging tools](choosing-a-32-bit-or-64-bit-debugger-package.md).

## Related topics

[Tools related to Debugging Tools for Windows](tools-related-to-debugging-tools-for-windows.md)
