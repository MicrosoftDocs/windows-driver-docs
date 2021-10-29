---
title: Custom Symbol Stores and Symbol Servers
description: Custom Symbol Stores and Symbol Servers
keywords: ["symbol servers", "symbol servers, overview", "symbol stores", "symbol stores, overview", "SymSrv", "SymSrv, overview", "SymStore", "SymStore, overview"]
ms.date: 10/28/2021
ms.localizationpriority: medium
---

# Custom Symbol Stores and Symbol Servers

## <span id="ddk_using_symbol_servers_and_symbol_stores_dbg"></span><span id="DDK_USING_SYMBOL_SERVERS_AND_SYMBOL_STORES_DBG"></span>

Setting up symbols correctly for debugging can be a challenging task, particularly for kernel debugging. It often requires that you know the names and releases of all products on your computer. The debugger must be able to locate each of the symbol files corresponding to the product releases and service packs.

This can result in an extremely long symbol path consisting of a long list of directories. To simplify these difficulties in coordinating symbol files, the symbol files can be gathered into a *symbol store*, which is then accessed by a *symbol server*.

A *symbol store* is a collection of symbol files, an index, and a tool that can be used by an administrator for adding and deleting files. A symbol store may also contain executable image files. 

The files are indexed according to unique parameters such as the time stamp and image size. A symbol store can also hold executable image files which can be extracted using a symbol server. Debugging Tools for Windows contains a symbol store creation tool called [SymStore](symstore.md).

The debugger accesses the files in a symbol store by using a *symbol server*. Debugging Tools for Windows includes both a symbol store creation tool, [SymStore](symstore.md), and a symbol server, *SymSrv*. It also includes a tool, [SymProxy](symproxy.md), for setting up an HTTP symbol store on a network to serve as a proxy for all symbol stores that the debugger may need to access.

A symbol server enables the debuggers to automatically retrieve the correct symbol files from a symbol store without the user needing to know product names, releases, or build numbers. Debugging Tools for Windows contains a symbol server called *SymSrv*. The symbol server is activated by including a certain text string in the symbol path. Each time the debugger needs to load symbols for a newly loaded module, it calls the symbol server to locate the appropriate symbol files. For information about working with the symbol server, see see [Microsoft Public Symbols](microsoft-public-symbols.md).

If you wish to use a different method for your symbol search than that provided by SymSrv, it is possible to develop your own symbol server DLL. For details on implementing such a symbol server, see [Other Symbol Servers](other-symbol-servers.md).

This section includes:

[HTTP Symbol Stores](http-symbol-stores.md)

[File Share (SMB) Symbol Server](file-share--smb--symbol-server.md)

[Symbol Store Folder Tree](symbol-store-folder-tree.md)

[Other Symbol Stores](other-symbol-stores.md)

[Installing Windows Symbol Files](installing-windows-symbol-files.md)

[Offline Symbols for Windows Update](symbols-windows-update.md)

If you are not setting up your own symbol store, but just intend to use the public Microsoft symbol store, see [Microsoft Public Symbols](microsoft-public-symbols.md).

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
