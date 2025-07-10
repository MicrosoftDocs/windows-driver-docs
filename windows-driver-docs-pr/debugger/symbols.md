---
title: Symbols for Windows Debugging
description: Explore symbols for the Windows debuggers (WinDbg, KD, CDB, and NTSD) that are available from a public symbol server.
keywords: ["symbols", "setup, symbols", "symbols, setup"]
ms.date: 07/11/2025
---

# Symbols for Windows debugging

Symbol files hold various data that while not essential for running the binaries, can be useful for debugging. Symbols can include the name, type (if applicable), store address (or register), and any parent or child symbols. Examples of symbols include variable names (local and global), functions, and any entry point into a module.

The debugger gets its information about symbols from symbol files located on the local file system or loaded from a remote symbol server. When you use a symbol server, the debugger automatically uses the correct version of the symbol file to match the module in the target. 

## Locate symbols for Windows debuggers

Symbols for the Windows debuggers are available from a public symbol server over the internet. Windows debuggers include WinDbg (a kernel-mode and user-mode debugger), the kernel debugger (KD), Microsoft Console Debugger (CDB), and Microsoft NT Symbolic Debugger (NTSD).

- For user-mode debugging, you need symbols for your target application.

- For kernel-mode debugging, you need symbols for the driver you're debugging and also the Windows public symbols. 

You can load symbols automatically with the `.symfix` command, which [sets the symbol store path)](../debuggercmds/-symfix--set-symbol-store-path-.md). To run the command, you need access to the internet while your debugger is running. Next, use the `.reload` command to [reload the module and symbols](../debuggercmds/-reload--reload-module-.md).

To learn more about symbols, including WinDbg support for Portable PDB symbols, see the following articles:

- [Symbols and symbol files](symbols-and-symbol-files.md)
- [Public and private symbols](public-and-private-symbols.md)
- [Portable Program Database (PDB) symbols](symbols-portable-pdb.md)

## Access symbols while debugging

The following articles describe how to access symbols during a debugging session. They also explain how to control the debugger's symbol options and symbol matching.

- [Microsoft public symbol server](microsoft-public-symbols.md)
- [Windows symbol packages for debugging](debugger-download-symbols.md)
- [Symbol path for Windows debuggers](symbol-path.md)

> [!TIP]
> To configure your debugger to access symbols for your own programs and for Windows, get started quickly by reading [Symbol path](symbol-path.md) and [Microsoft public symbol server](microsoft-public-symbols.md). Use the `!sym noisy` command to display more detail as symbols are loaded to troubleshoot issues with symbols. For more information, see the [!sym command reference](../debuggercmds/-sym.md).

## Related articles

- [Use a symbol server (SymSrv)](using-a-symbol-server.md)
- [Advanced use cases for SymSrv](advanced-symsrv-use.md)
- [Firewalls and proxy servers](firewalls-and-proxy-servers.md)
- [Symbol syntax and symbol matching](symbol-syntax-and-symbol-matching.md)
- [Custom symbol stores and symbol servers](symbol-stores-and-symbol-servers.md)
- [Symbol problems while debugging](symbol-problems-while-debugging.md)