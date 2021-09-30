---
title: Symbol Stores and Symbol Servers
description: Symbol Stores and Symbol Servers
keywords: ["symbol servers", "symbol servers, overview", "symbol stores", "symbol stores, overview", "SymSrv", "SymSrv, overview", "SymStore", "SymStore, overview"]
ms.date: 09/29/2021
ms.localizationpriority: medium
---

# Symbol Stores and Symbol Servers


## <span id="ddk_using_symbol_servers_and_symbol_stores_dbg"></span><span id="DDK_USING_SYMBOL_SERVERS_AND_SYMBOL_STORES_DBG"></span>


A *symbol store* is a collection of symbol files, an index, and a tool for adding and deleting files. A symbol store may also contain executable image files. The debugger accesses the files in a symbol store by using a *symbol server*. Debugging Tools for Windows includes both a symbol store creation tool, [SymStore](symstore.md), and a symbol server, *SymSrv*. It also includes a tool, [SymProxy](symproxy.md), for setting up an HTTP symbol store on a network to serve as a proxy for all symbol stores that the debugger may need to access.

This section includes:

[Accessing Symbols for Debugging](accessing-symbols-for-debugging.md)

[HTTP Symbol Stores](http-symbol-stores.md)

[File Share (SMB) Symbol Server](file-share--smb--symbol-server.md)

[Symbol Store Folder Tree](symbol-store-folder-tree.md)

[Other Symbol Stores](other-symbol-stores.md)

[Installing Windows Symbol Files](installing-windows-symbol-files.md)

[Offline Symbols for Windows Update](symbols-windows-update.md)

If you are not setting up your own symbol store, but just intend to use the public Microsoft symbol store, see [Microsoft Public Symbols](microsoft-public-symbols.md).


