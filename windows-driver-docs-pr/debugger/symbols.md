---
title: Symbols for Windows debugging (WinDbg, KD, CDB, NTSD)
description: Symbols for the Windows debuggers (WinDbg, KD, CDB, and NTSD) are available from a public symbol server. 
keywords: ["symbols", "setup, symbols", "symbols, setup"]
ms.date: 09/30/2021
ms.localizationpriority: High
---

# Symbols for Windows debugging (WinDbg, KD, CDB, NTSD)

Symbols for the Windows debuggers (WinDbg, KD, CDB, and NTSD) are available from a public symbol server. Symbol files hold a variety of data which are not actually needed when running the binaries, but which could be very useful in the debugging process.

These topics explain how to access symbols during a debugging session, how to control the debugger's symbol options and symbol matching.

[Symbol path for Windows debuggers](symbol-path.md)

[Microsoft public symbol server](microsoft-public-symbols.md)

[Using a Symbol Server](using-a-symbol-server.md)

[Advanced SymSrv Use](advanced-symsrv-use.md)

[Firewalls and Proxy Servers](firewalls-and-proxy-servers.md)

These topics explain what symbols are, as well as describe WinDbg support for Portable PDB symbols.

[Symbols and Symbol Files](symbols-and-symbol-files.md)

[Public and Private Symbols](public-and-private-symbols.md)

[Portable PDB Symbols](symbols-portable-pdb.md)

If you simply want to configure your debugger to access symbols for your own programs and for Windows, you may find it quicker to read the less-detailed introductory topics [Symbol Path](symbol-path.md) and [Microsoft public symbol server](microsoft-public-symbols.md).

For additional detail on working with symbols refer to these pages.

[Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md)

[Symbol Stores and Symbol Servers](symbol-stores-and-symbol-servers.md)

[Symbol Problems While Debugging](symbol-problems-while-debugging.md)

## Symbol Utilities

The following utilities allow for the distribution and control of symbols in larger software development projects.

| Utility  | Description                                                                                                          |
|----------|----------------------------------------------------------------------------------------------------------------------|
| [SymProxy](symproxy.md) | Use to configure your HTTP-based symbol store to act as a proxy between client computers and other symbol stores.    |
| [SymStore](symstore.md) | SymStore (symstore.exe) is a tool for creating symbol stores.                                                        |
| [AgeStore](agestore.md) | The AgeStore tool (agestore.exe) deletes files in a directory or directory tree, based on their last access dates.   |
| [DBH](dbh.md)      | The DBH tool (dbh.exe) is a command-line tool that displays information about the contents of a symbol file.         |
| [PDBCopy](pdbcopy.md)  | The PDBCopy tool (pdbcopy.exe) is a command-line tool that removes private symbol information from a symbol file.    |
| [SymChk](symchk.md)   | SymChk (the Microsoft Symbol Checker tool), Symchk.exe, is a program that compares executable files to symbol files. |



 

 





