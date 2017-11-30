---
title: Using a Symbol Server
description: Using a Symbol Server
ms.assetid: 6c1687c7-7b9d-45f7-8778-c7284c4a8222
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using a Symbol Server


A symbol server enables the debugger to automatically retrieve the correct symbol files from a symbol store - an indexed collection of symbol files - without the user needing to know product names, releases, or build numbers. The Debugging Tools for Windows package includes the symbol server [SymSrv](symsrv.md) (symsrv.exe).

### <span id="using_symsrv_with_a_debugger"></span><span id="USING_SYMSRV_WITH_A_DEBUGGER"></span>Using SymSrv with a Debugger

SymSrv can be used with WinDbg, KD, NTSD, or CDB.

To use this symbol server with the debugger, simply include the text **srv\*** in the symbol path. For example:

```
set _NT_SYMBOL_PATH = srv*DownstreamStore*SymbolStoreLocation
```

where *DownstreamStore* specifies the local directory or network share that will be used to cache individual symbol files, and *SymbolStoreLocation* is the location of the symbol store either in the form *\\\\server\\share* or as an internet address. For more syntax options, see [Advanced SymSrv Use](advanced-symsrv-use.md).

Microsoft has a Web site that makes Windows symbols publicly available. You can refer directly to this site in your symbol path in the following manner:

```
set _NT_SYMBOL_PATH=srv*DownstreamStore*https://msdl.microsoft.com/download/symbols
```

where, again, *DownstreamStore* specifies the local directory or network share that will be used to cache individual symbol files. For more information, see [Microsoft Public Symbols](microsoft-public-symbols.md).

If you plan to create a symbol store, configure a symbol store for web (HTTP) access, or write your own symbol server or symbol store, see [Symbol Stores and Symbol Servers](symbol-stores-and-symbol-servers.md).

### <span id="using_agestore_to_reduce_the_cache_size"></span><span id="USING_AGESTORE_TO_REDUCE_THE_CACHE_SIZE"></span>Using AgeStore to Reduce the Cache Size

Any symbol files downloaded by SymSrv will remain on your hard drive after the debugging session is over. To control the size of the symbol cache, the AgeStore tool can be used to delete cached files that are older than a specified date, or to reduce the contents of the cache below a specified size. For details, see [AgeStore](agestore.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20a%20Symbol%20Server%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




