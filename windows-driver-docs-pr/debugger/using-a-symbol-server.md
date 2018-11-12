---
title: Using a Symbol Server
description: Using a Symbol Server
ms.assetid: 6c1687c7-7b9d-45f7-8778-c7284c4a8222
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Using a Symbol Server


A symbol server enables the debugger to automatically retrieve the correct symbol files from a symbol store - an indexed collection of symbol files - without the user needing to know product names, releases, or build numbers. The Debugging Tools for Windows package includes the symbol server [SymSrv](symsrv.md) (symsrv.exe).

### <span id="using_symsrv_with_a_debugger"></span><span id="USING_SYMSRV_WITH_A_DEBUGGER"></span>Using SymSrv with a Debugger

SymSrv can be used with WinDbg, KD, NTSD, or CDB.

To use this symbol server with the debugger, simply include the text **srv\\*** in the symbol path. For example:

```console
set _NT_SYMBOL_PATH = srv*DownstreamStore*SymbolStoreLocation
```

where *DownstreamStore* specifies the local directory or network share that will be used to cache individual symbol files, and *SymbolStoreLocation* is the location of the symbol store either in the form *\\\\server\\share* or as an internet address. For more syntax options, see [Advanced SymSrv Use](advanced-symsrv-use.md).

Microsoft has a Web site that makes Windows symbols publicly available. You can refer directly to this site in your symbol path in the following manner:

```console
set _NT_SYMBOL_PATH=srv*DownstreamStore*https://msdl.microsoft.com/download/symbols
```

where, again, *DownstreamStore* specifies the local directory or network share that will be used to cache individual symbol files. For more information, see [Microsoft Public Symbols](microsoft-public-symbols.md).

If you plan to create a symbol store, configure a symbol store for web (HTTP) access, or write your own symbol server or symbol store, see [Symbol Stores and Symbol Servers](symbol-stores-and-symbol-servers.md).

### <span id="using_agestore_to_reduce_the_cache_size"></span><span id="USING_AGESTORE_TO_REDUCE_THE_CACHE_SIZE"></span>Using AgeStore to Reduce the Cache Size

Any symbol files downloaded by SymSrv will remain on your hard drive after the debugging session is over. To control the size of the symbol cache, the AgeStore tool can be used to delete cached files that are older than a specified date, or to reduce the contents of the cache below a specified size. For details, see [AgeStore](agestore.md).

 

 





