---
title: Symbols for Windows debugging (WinDbg, KD, CDB, NTSD)
description: Symbols for the Windows debuggers (WinDbg, KD, CDB, and NTSD) are available from a public symbol server. 
keywords: ["symbols", "setup, symbols", "symbols, setup"]
ms.date: 10/28/2021
ms.localizationpriority: High
---

# Symbols for Windows debugging (WinDbg, KD, CDB, NTSD)

Symbol files hold a variety of data which are not actually needed when running the binaries, but which could be very useful in the debugging process.

Symbols can include the name, type (if applicable), the address or register where it is stored, and any parent or child symbols. Examples of symbols include variable names (local and global), functions, and any entry point into a module.

The debugger gets its information about symbols from symbol files, which are located on the local file system or loaded from a remote symbol server. When using a symbol server, the debugger will automatically use the correct version of the symbol file to match the module in the target. 

Symbols for the Windows debuggers (WinDbg, KD, CDB, and NTSD) are available from a public symbol server via the internet. 

>[!TIP] 
> Symbols can be loaded automatically using the [**.symfix (Set Symbol Store Path)**](-symfix--set-symbol-store-path-.md) command, as long as you have access to the internet while your debugger is running. Then use the [**.reload (Reload Module)**](-reload--reload-module-.md) command to load the symbols.

If you are performing user-mode debugging, you will need symbols for your target application. If you are performing kernel-mode debugging, you will need symbols for the driver you are debugging, as well as the Windows public symbols. 

These topics explain how to access symbols during a debugging session, how to control the debugger's symbol options and symbol matching.

[Microsoft public symbol server](microsoft-public-symbols.md)

[Symbol path for Windows debuggers](symbol-path.md)

These topics explain what symbols are, as well as describe WinDbg support for Portable PDB symbols.

[Symbols and Symbol Files](symbols-and-symbol-files.md)

[Public and Private Symbols](public-and-private-symbols.md)

[Portable PDB Symbols](symbols-portable-pdb.md)

For additional detail on working with symbols refer to these pages.

[Using a Symbol Server](using-a-symbol-server.md)

[Advanced SymSrv Use](advanced-symsrv-use.md)

[Firewalls and Proxy Servers](firewalls-and-proxy-servers.md)

[Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md)

[Custom Symbol Stores and Symbol Servers](symbol-stores-and-symbol-servers.md)

[Symbol Problems While Debugging](symbol-problems-while-debugging.md)

If you simply want to configure your debugger to access symbols for your own programs and for Windows, you may find it quicker to read the less-detailed introductory topics [Symbol Path](symbol-path.md) and [Microsoft public symbol server](microsoft-public-symbols.md). Use the Use [**!sym noisy**](-sym.md) command to display additional detail as symbols are loaded to troubleshoot issues with symbols.





 

 





