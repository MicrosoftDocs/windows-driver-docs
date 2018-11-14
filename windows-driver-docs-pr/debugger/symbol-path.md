---
title: Symbol path for Windows debuggers
description: The symbol path specifies locations where the Windows debuggers (WinDbg, KD, CDB, NTST) look for symbol files. 
ms.assetid: 705df98f-717f-40ad-a424-101826970691
keywords: symbol files and paths, symbols, lazy symbol loading, deferred symbol loading, symbol path
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Symbol path for Windows debuggers


The symbol path specifies locations where the Windows debuggers (WinDbg, KD, CDB, NTST) look for symbol files. For more information about symbols and symbol files, see [Symbols](symbols.md).

Some compilers (such as Microsoft Visual Studio) put symbol files in the same directory as the binary files. The symbol files and the checked binary files contain path and file name information. This information frequently enables the debugger to find the symbol files automatically. If you are debugging a user-mode process on the computer where the executable was built, and if the symbol files are still in their original location, the debugger can locate the symbol files without you setting the symbol path.

In most other situations, you have to set the symbol path to point to your symbol file locations.

## <span id="Symbol_Path_Syntax"></span><span id="symbol_path_syntax"></span><span id="SYMBOL_PATH_SYNTAX"></span>Symbol Path Syntax


The debugger's symbol path is a string that consists of multiple directory paths, separated by semicolons.

Relative paths are supported. However, unless you always start the debugger from the same directory, you should add a drive letter or a network share before each path. Network shares are also supported.

For each directory in the symbol path, the debugger looks in three directories. For example, if the symbol path includes the `c:\MyDir` directory, and the debugger is looking for symbol information for a DLL, the debugger first looks in `c:\MyDir\symbols\dll`, then in `c:\MyDir\dll`, and finally in `c:\MyDir`. The debugger then repeats this process for each directory in the symbol path. Finally, the debugger looks in the current directory and then in the current directory with `..\dll` appended to it. (The debugger appends `..\dll` , `..\exe` , or `..\sys` , depending on which binaries it is debugging.)

Symbol files have date and time stamps. You do not have to worry that the debugger will use the wrong symbols that it may find first in this sequence. It always looks for the symbols that match the time stamp on the binary files that it is debugging. For more information about responses when symbols files are not available, see [Compensating for Symbol-Matching Problems](matching-symbol-names.md).

One way to set the symbol path is by entering the [**.sympath**](-sympath--set-symbol-path-.md) command. For other ways to set the symbol path, see [Controlling the Symbol Path](#controlling-the-symbol-path) later in this topic.

## <span id="Caching_Symbols_Locally"></span><span id="caching_symbols_locally"></span><span id="CACHING_SYMBOLS_LOCALLY"></span>Caching Symbols Locally


We strongly recommend that you always cache your symbols locally. One way to cache symbols locally is to include `cache*;` or `cache*localsymbolcache;*` in your symbol path.

If you include the string `cache*;` in your symbol path, symbols loaded from any element that appears to the right of this string are stored in the default symbol cache directory on the local computer. For example, the following command tells the debugger to get symbols from the network share `\\someshare` and cache the symbols in the default location on the local computer.

```dbgcmd
.sympath cache*;\\someshare
```

If you include the string `cache*localsymbolcache;` in your symbol path, symbols loaded from any element that appears to the right of this string are stored in the *localsymbolcache* directory.

For example, the following command tells the debugger to obtain symbols from the network share `\\someshare` and cache the symbols in the `c:\MySymbols` directory.

```dbgcmd
.sympath cache*c:\MySymbols;\\someshare
```

## <span id="Using_a_Symbol_Server"></span><span id="using_a_symbol_server"></span><span id="USING_A_SYMBOL_SERVER"></span>Using a Symbol Server


If you are connected to the Internet or a corporate network, the most efficient way to access symbols is to use a symbol server. You can use a symbol server by using the `srv*`, `srv*symbolstore`, or `srv*localsymbolcache*symbolstore` string in your symbol path.

If you include the string `srv*` in your symbol path, the debugger uses a symbol server to get symbols from the default symbol store. For example, the following command tells the debugger to use a symbol server to get symbols from the default symbol store. These symbols are not cached on the local computer.

```dbgcmd
.sympath srv*
```

If you include the string `srv*symbolstore` in your symbol path, the debugger uses a symbol server to get symbols from the *symbolstore* store. For example, the following command tells the debugger to use a symbol server to get symbols from the symbol store at https://msdl.microsoft.com/download/symbols. These symbols are not cached on the local computer.

```dbgcmd
.sympath srv*https://msdl.microsoft.com/download/symbols
```

If you include the string `srv*localcache*symbolstore` in your symbol path, the debugger uses a symbol server to get symbols from the *symbolstore* store and caches them in the *localcache* directory. For example, the following command tells the debugger to use a symbol server to get symbols from the symbol store at https://msdl.microsoft.com/download/symbols and cache the symbols in `c:\MyServerSymbols`.

```dbgcmd
.sympath srv*c:\MyServerSymbols*https://msdl.microsoft.com/download/symbols
```

If you have a directory on your computer where you manually place symbols, do not use that directory as the cache for symbols obtained from a symbol server. Instead, use two separate directories. For example, you can manually place symbols in `c:\MyRegularSymbols` and then designate `c:\MyServerSymbols` as a cache for symbols obtained from a server. The following example shows how to specify both directories in your symbol path.

```dbgcmd
.sympath c:\MyRegularSymbols;srv*c:\MyServerSymbols*https://msdl.microsoft.com/download/symbols
```

For more information about symbol servers, see [Symbol Stores and Symbol Servers](symbol-stores-and-symbol-servers.md).

## <span id="Combining_cache__and_srv_"></span><span id="combining_cache__and_srv_"></span><span id="COMBINING_CACHE__AND_SRV_"></span>Combining cache\* and srv\*


If you include the string `cache*;` in your symbol path, symbols loaded from any element that appears to the right of this string are stored in the default symbol cache directory on the local computer. For example, the following command tells the debugger to use a symbol server to get symbols from the store at https://msdl.microsoft.com/download/symbols and cache them in the default symbol cache directory.

```dbgcmd
.sympath cache*;srv*https://msdl.microsoft.com/download/symbols
```

If you include the string `cache*localsymbolcache;` in your symbol path, symbols loaded from any element that appears to the right of this string are stored in the *localsymbolcache* directory.

For example, the following command tells the debugger to use a symbol server to get symbols from the store at https://msdl.microsoft.com/download/symbols and cache the symbols in the `c:\MySymbols` directory.

```dbgcmd
.sympath cache*c:\MySymbols;srv*https://msdl.microsoft.com/download/symbols
```

## <span id="using_agestore_to_reduce_the_cache_size"></span><span id="USING_AGESTORE_TO_REDUCE_THE_CACHE_SIZE"></span>Using AgeStore to Reduce the Cache Size


You can use the AgeStore tool to delete cached files that are older than a specified date, or to delete enough old files that the resulting size of the cache is less than a specified amount. This can be useful if your downstream store is too large. For details, see [AgeStore](agestore.md).

For more information about symbol servers and symbol stores, see [Symbol Stores and Symbol Servers](symbol-stores-and-symbol-servers.md).

## <span id="lazy_symbol_loading"></span><span id="LAZY_SYMBOL_LOADING"></span>Lazy Symbol Loading


The debugger's default behavior is to use *lazy symbol loading* (also known as *deferred symbol loading*). This kind of loading means that symbols are not loaded until they are required.

When the symbol path is changed, for example by using the [`.sympath`](-sympath--set-symbol-path-.md) command, all loaded modules with export symbols are lazily reloaded.

Symbols of modules with full PDB symbols will be lazily reloaded if the new path no longer includes the original path that was used to load the PDB symbols. If the new path still includes the original path to the PDB symbol file, those symbols will not be lazily reloaded.

For more information about lazy symbol loading, see [Deferred Symbol Loading](deferred-symbol-loading.md).

You can turn off lazy symbol loading in CDB and KD by using the `-s` [command-line option](command-line-options.md). You can also force symbol loading by using the `ld` [**(Load Symbols)**](ld--load-symbols-.md) command or by using the `.reload` [**(Reload Module)**](-reload--reload-module-.md) command together with the `/f` option.

## <span id="ddk_symbol_path_dbg"></span><span id="DDK_SYMBOL_PATH_DBG"></span>


### <span id="controlling-the-symbol-path"></span><span id="CONTROLLING-THE-SYMBOL-PATH"></span>Controlling the Symbol Path

To control the symbol path, you can do one of the following:

-   Use the [`.sympath`](-sympath--set-symbol-path-.md) command to display, set, change, or append to the path. The `.symfix` [**(Set Symbol Store Path)**](-symfix--set-symbol-store-path-.md) command is similar to `.sympath` but saves you some typing.

-   Before you start the debugger, use the `_NT_SYMBOL_PATH` and `_NT_ALT_SYMBOL_PATH` [environment variables](environment-variables.md) to set the path. The symbol path is created by appending `_NT_SYMBOL_PATH` after `_NT_ALT_SYMBOL_PATH`. (Typically, the path is set through the `_NT_SYMBOL_PATH`. However, you might want to use `_NT_ALT_SYMBOL_PATH` to override these settings in special cases, such as if you have private versions of shared symbol files.) If you try to add an invalid directory through these environment variables, the debugger ignores this directory.

-   When you start the debugger, use the `-y` [command-line option](command-line-options.md) to set the path.

-   (WinDbg only) Use the [File | Symbol File Path](file---symbol-file-path.md) command or press `CTRL+S` to display, set, change, or append to the path.

If you use the `-sins` [command-line option](command-line-options.md), the debugger ignores the symbol path environment variable.

## <span id="related_topics"></span>Related topics


[Advanced SymSrv Use](advanced-symsrv-use.md)

 

 

