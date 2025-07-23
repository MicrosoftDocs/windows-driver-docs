---
title: Tools Included in Debugging Tools for Windows
description: Learn about the other tools included in Debugging Tools for Windows that are in addition to the debugging engine and debugging environments.
ms.date: 07/11/2025
ms.topic: overview
---

# Tools included in Debugging Tools for Windows

Debugging Tools for Windows includes several other tools in addition to the debugging engine and [debugging environments](debuggers-in-the-debugging-tools-for-windows-package.md). The extra tools are available in the [installation directory](#installation-directory) of Debugging Tools for Windows, as described in this article.

The following tables use acronyms to refer to several Windows debuggers, including the kernel debugger (KD), Microsoft Console Debugger (CDB), and Microsoft NT Symbolic Debugger (NTSD).

## Tools and utilities

The following table lists the available tools and utilities:

| Name | Description |
| ---- | ----------- |
| Breakin | Cause a user-mode break to occur in a process. To view the help for the command, open a Command Prompt window, go to the [installation directory](#installation-directory), and enter `breakin /?`. |
| [DumpChk](dumpchk.md) | Validate a memory dump file. |
| [GFlags](gflags.md) | Control registry keys and other settings. |
| [Kill](kill-tool.md) | Terminate a process. |
| List (File List Utility) | To view the help for the command, open a Command Prompt window, go to the [installation directory](#installation-directory), and enter `list /?`. |
| [Logger and LogViewer](logger-and-logviewer.md) | Record and display function calls and other actions of a program. |
| [PLMDebug](plmdebug.md) | Use the Windows debugger to debug Windows apps that run under Process Lifecycle Management (PLM). With PLMDebug, you can take manual control of suspending, resuming, and terminating a Windows app. |
| [TList](tlist.md) | List all running processes. |
| [UMDH](umdh.md) | Analyze heap allocations with the User-Mode Dump Heap (UMDH) tool. |
| [USBView](usbview.md) | Display Universal Serial Bus (USB) host controllers and connected devices. |
| USBView2 | Display USB host controllers and connected devices. To view the help for the command, open a Command Prompt window, go to the [installation directory](#installation-directory), and enter `USBView2 /?`. |

### Symbol and source tools

The following table describes the extra tools that support debugging a source or symbol server:

| Name | Description |
| --- | --- |
| [AgeStore](agestore.md) | Remove old entries in the downstream store of a symbol server or a source server. |
| [DBH](dbh.md) | Display debug help (DBH) information about the contents of a symbol file. |
| [PDBCopy](pdbcopy.md) | Remove private symbol information from a Python debug (PDB) symbol file, and control whether public symbols are included in the file. |
| [SrcSrv](srcsrv.md) | Use this source server to deliver source files while debugging. |
| [SymChk](symchk.md) | Compare executable files to symbol files to verify the correct symbols are available. |
| [SymProxy](symproxy.md) | Create a single HTTP symbol server on your network that all your debuggers can point to. This approach has the benefit of pointing to multiple symbol servers (both internal and external) with a single symbol path, handling all authentication, and increasing performance via symbol caching. The *symproxy.dll* file is in the *SymProxy* folder in the [installation directory](#installation-directory). |
| SymSrv | Use this symbols server in the debugger and connect to a symbol store. For information about working with the symbol server, see [Microsoft public symbols](microsoft-public-symbols.md). |
| [SymStore](symstore.md) | Create a symbol store. For more information, see [Using SymStore](symstore.md). |

### Remote and proxy debugger tools

The following table describes the extra tools that support debugging the remote or proxy server, and includes links to resources for more information:

| Name | Description |
| --- | --- |
| DbgRpc | Display Microsoft Remote Procedure Call (RPC) state information. For more information, see [RPC debugging](rpc-debugging.md) and [Using the DbgRpc tool](using-the-dbgrpc-tool.md). |
| DbgSrv | Use this process server for remote debugging. For more information, see [Process servers (user mode)](process-servers--user-mode-.md). |
| DbEngPrx | Use this repeater (a small proxy server) for remote debugging. For more information, see [Repeaters](repeaters.md). |
| KDbgCtrl (Kernel Debugging Control) | Control and configure the kernel debugging connection. For more information, see [Using KDbgCtrl](using-kdbgctrl.md). |
| KdSrv | Use this KD connection server for remote debugging. For more information, see [KD connection servers (kernel mode)](kd-connection-servers--kernel-mode-.md). |
| RTList (Remote Task List Viewer) | List running processes via a DbgSrv process server. To view the help for the command, open a Command Prompt window, go to the [installation directory](#installation-directory), and enter `rtlist /?`. |
| [Remote](remote-tool.md) | Remotely control any console program, including KD, CDB, and NTSD. For more information, see [Remote debugging by using remote.exe](remote-debugging-through-remote-exe.md). |

## Installation directory

The default install location for the Debugging Tools for Windows is different based on the operating system. To determine whether you should use the 32-bit or 64-bit tools, see [Choosing the 32-bit or 64-bit debugging tools](choosing-a-32-bit-or-64-bit-debugger-package.md).

- For 64-bit tools: The default folder location is _C:\Program Files (x86)\Windows Kits\10\Debuggers_.

- For 32-bit tools: Locate the _Windows Kits_ folder under the _C:\Program Files_ folder. 

## Related articles

- [Tools related to Debugging Tools for Windows](tools-related-to-debugging-tools-for-windows.md)