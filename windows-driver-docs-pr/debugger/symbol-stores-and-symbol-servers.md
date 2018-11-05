---
title: Symbol Stores and Symbol Servers
description: Symbol Stores and Symbol Servers
ms.assetid: de35abe7-93ad-4ca0-94d4-bed1230e057b
keywords: ["symbol servers", "symbol servers, overview", "symbol stores", "symbol stores, overview", "SymSrv", "SymSrv, overview", "SymStore", "SymStore, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Symbol Stores and Symbol Servers


## <span id="ddk_using_symbol_servers_and_symbol_stores_dbg"></span><span id="DDK_USING_SYMBOL_SERVERS_AND_SYMBOL_STORES_DBG"></span>


A *symbol store* is a collection of symbol files, an index, and a tool for adding and deleting files. A symbol store may also contain executable image files. The debugger accesses the files in a symbol store by using a *symbol server*. Debugging Tools for Windows includes both a symbol store creation tool, [SymStore](symstore.md), and a symbol server, [SymSrv](symsrv.md). It also includes a tool, [SymProxy](symproxy.md), for setting up an HTTP symbol store on a network to serve as a proxy for all symbol stores that the debugger may need to access.

This section includes:

[SymSrv](symsrv.md)

[Using a Symbol Server](using-a-symbol-server.md)

[HTTP Symbol Stores](http-symbol-stores.md)

[File Share (SMB) Symbol Server](file-share--smb--symbol-server.md)

[SymStore](symstore.md)

[SymProxy](symproxy.md)

[SymStore](symstore.md)

If you are not setting up your own symbol store, but just intend to use the public Microsoft symbol store, see [Microsoft Public Symbols](microsoft-public-symbols.md).

 

 





