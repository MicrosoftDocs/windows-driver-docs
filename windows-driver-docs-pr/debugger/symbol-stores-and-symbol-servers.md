---
title: Symbol Stores and Symbol Servers
description: Symbol Stores and Symbol Servers
ms.assetid: de35abe7-93ad-4ca0-94d4-bed1230e057b
keywords: ["symbol servers", "symbol servers, overview", "symbol stores", "symbol stores, overview", "SymSrv", "SymSrv, overview", "SymStore", "SymStore, overview"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Symbol%20Stores%20and%20Symbol%20Servers%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




