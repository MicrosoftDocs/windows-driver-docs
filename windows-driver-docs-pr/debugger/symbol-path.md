---
title: Symbol path for Windows debuggers
description: Learn how the symbol path specifies locations where Windows debuggers, such as WinDbg, KD, CDB, and NTST, look for symbol files. 
keywords: symbol files and paths, symbols, lazy symbol loading, deferred symbol loading, symbol path
ms.date: 12/29/2022
---

# Symbol path for Windows debuggers

The symbol path specifies locations where Windows debuggers, such as WinDbg, KD, CDB, and NTST, look for symbol files. For more information about symbols and symbol files, see [Symbols](symbols.md).

Some compilers, including Microsoft Visual Studio, put symbol files in the same directory as the binary files. The symbol files and the checked binary files contain path and file name information, which lets the debugger find the symbol files automatically. If you debug a user-mode process on the computer where the executable was built, and if the symbol files are in their original location, the debugger can locate the symbol files without you setting the symbol path.

In most other situations, you need to set the symbol path to point to your symbol file locations.

 >[!TIP]
 > Use [.symfix](-symfix--set-symbol-store-path-.md) to set a default path to the public Microsoft public symbol server that works well in many situations.


## Symbol path syntax

The debugger's symbol path is a string that consists of multiple directory paths separated by semicolons. For example, `C:\Dir1;C:\Dir2\DirA;C:\Dir2\DirB`.

Relative paths are supported. However, you should add a drive letter or a network share before each path, unless you always start the debugger from the same directory. Network shares are also supported.

For each directory in the symbol path, the debugger looks in three directories. For example, if the symbol path includes `C:\Dir1` and the debugger is looking for symbol information for a DLL, the debugger looks for symbol information in the following directories, listed in order:

- `C:\Dir1\symbols\dll`
- `C:\Dir1\dll`
- `C:\Dir1`

The debugger then repeats this process for each directory in the symbol path. Finally, the debugger looks in the current directory and then in the current directory with `..\dll` appended to it. The debugger appends `..\dll`, `..\exe`, or `..\sys`, depending on which binaries it's debugging.

Symbol files have date and time stamps. The debugger always looks for the symbols that match the time stamp on the binary files that it's debugging. You don't have to worry about the debugger using the wrong symbols that it finds first in this sequence. For more information about responses when symbols files aren't available, see [Matching symbol names](matching-symbol-names.md).

One way to set the symbol path is by entering the [.sympath command](-sympath--set-symbol-path-.md). For other ways to set the symbol path, see [Control the symbol path](#control-the-symbol-path) later in this topic.

## Cache symbols locally

You should cache your symbols locally. One way to cache symbols locally is to include `cache*;` or `cache*localsymbolcache;*` in your symbol path.

If you include the string `cache*;` in your symbol path, symbols loaded from any element that appears to the right of this string are stored in the default symbol cache directory on the local computer. For example, the following command tells the debugger to get symbols from the network share named `\\someshare` and cache the symbols in the default location on the local computer.

```dbgcmd
.sympath cache*;\\someshare
```

If you include the string `cache*localsymbolcache;` in your symbol path, symbols loaded from any element that appears to the right of this string are stored in the *localsymbolcache* directory.

For example, the following command tells the debugger to obtain symbols from the network share `\\someshare` and cache the symbols in the `c:\MySymbols` directory.

```dbgcmd
.sympath cache*C:\MySymbols;\\someshare
```

## Using a symbol server: srv*

If you're connected to the Internet or a corporate network, the most efficient way to access symbols is to use a symbol server such as the public [Microsoft public symbol server](https://msdl.microsoft.com/download/symbols). You can use a symbol server by using one of the following strings in your symbol path.

* The `srv*` string

  If you include the string `srv*` in your symbol path, the debugger uses a symbol server to get symbols from the default symbol store. For example, the following command tells the debugger to get symbols from the default symbol store. These symbols aren't cached on the local computer.

  ```dbgcmd
  .sympath srv*
  ```

* The `srv*symbolstore` string

  If you include the string `srv*symbolstore` in your symbol path, the debugger uses a symbol server to get symbols from the *symbolstore*. For example, the following command tells the debugger to get symbols from the [Microsoft symbol server](https://msdl.microsoft.com/download/symbols) store. These symbols aren't cached on the local computer.

  ```dbgcmd
  .sympath srv*https://msdl.microsoft.com/download/symbols
  ```

* The `srv*localsymbolcache*symbolstore` string

  If you include the string `srv*localcache*symbolstore` in your symbol path, the debugger uses a symbol server to get symbols from the *symbolstore* and caches them in the *localcache* directory. For example, the following command tells the debugger to get symbols from the [Microsoft symbol server](https://msdl.microsoft.com/download/symbols) store and cache the symbols in `c:\MyServerSymbols`.

  ```dbgcmd
  .sympath srv*C:\MyServerSymbols*https://msdl.microsoft.com/download/symbols
  ```

If you have a directory on your computer where you manually place symbols, don't use that directory as the cache for symbols obtained from a symbol server. Instead, use two separate directories. For example, you can manually place symbols in `c:\MyRegularSymbols` and then designate `c:\MyServerSymbols` as a cache for symbols obtained from a server. The following example shows how to specify both directories in your symbol path.

```dbgcmd
.sympath C:\MyRegularSymbols;srv*C:\MyServerSymbols*https://msdl.microsoft.com/download/symbols
```

For more information about symbol servers and symbol stores, see [Custom symbol stores and symbol servers](symbol-stores-and-symbol-servers.md).

## Combine cache\* and srv\*

If you include the string `cache*;` in your symbol path, symbols loaded from any element that appears to the right of this string are stored in the default symbol cache directory on the local computer. For example, the following command tells the debugger to get symbols from the [Microsoft symbol server](https://msdl.microsoft.com/download/symbols) store and cache them in the default symbol cache directory.

```dbgcmd
.sympath cache*;srv*https://msdl.microsoft.com/download/symbols
```

If you include the string `cache*localsymbolcache;` in your symbol path, symbols loaded from any element that appears to the right of this string are stored in the *localsymbolcache* directory.

For example, the following command tells the debugger to get symbols from the [Microsoft symbol server](https://msdl.microsoft.com/download/symbols) store and cache the symbols in the `c:\MySymbols` directory.


```dbgcmd
.sympath cache*C:\MySymbols;srv*https://msdl.microsoft.com/download/symbols
```

## Use AgeStore to reduce the cache size

You can use the [AgeStore](agestore.md) tool to delete cached files that are older than a specified date, or to delete enough old files so that the resulting cache size is less than a specified amount. This cleanup of cache files is useful if your downstream store gets too large.

## Lazy symbol loading

The debugger's default behavior is to use *lazy symbol loading*, also known as [*deferred symbol loading*](deferred-symbol-loading.md). This kind of loading means that symbols aren't loaded until they're required.

When the symbol path is changed, for example by using the [.sympath command](-sympath--set-symbol-path-.md), all loaded modules with export symbols are lazily reloaded.

Symbols of modules with full [PDB symbols](symbols-portable-pdb.md) are lazily reloaded if the new path no longer includes the original path that was used to load the PDB symbols. If the new path still includes the original path to the PDB symbol file, those symbols aren't lazily reloaded.

You can turn off lazy symbol loading in CDB and KD by using the [-s command-line option](command-line-options.md). You can also force symbol loading by using the [ld load symbols](ld--load-symbols-.md) command or by using the [.reload module command](-reload--reload-module-.md) together with the `/f` option.

## Azure DevOps Services Artifacts

A symbol server is available with [Azure Artifacts in Azure DevOps Services](/azure/devops/artifacts). To learn about working with Azure Artifacts in WinDbg, see [Debug with symbols in WinDbg](/azure/devops/artifacts/symbols/debug-with-symbols-visual-studio). For general information about Azure-generated symbols, see [Symbols overview](/azure/devops/artifacts/concepts/symbols).

## Control the symbol path

To control the symbol path, you can select one of the following methods:

* Use the [.symfix set symbol store path command](-symfix--set-symbol-store-path-.md) to set a default path to the public Microsoft symbol server that works well in many situations. To set a local cache, just type `.symfix C:\MyCache`.

* Use the [.sympath command](-sympath--set-symbol-path-.md) to display, set, change, or append to the path. 

* Before you start the debugger, use the `_NT_SYMBOL_PATH` and `_NT_ALT_SYMBOL_PATH` [environment variables](environment-variables.md) to set the path. The symbol path is created by appending `_NT_SYMBOL_PATH` after `_NT_ALT_SYMBOL_PATH`. Typically, the path is set through the `_NT_SYMBOL_PATH`. However, you might want to use `_NT_ALT_SYMBOL_PATH` to override these settings in special cases, such as if you have private versions of shared symbol files. If you try to add an invalid directory through these environment variables, the debugger ignores this directory.

* When you start the debugger, use the [-y command-line option](command-line-options.md) to set the path.

* In WinDbg only, you can use the [File | Symbol File Path command](file---symbol-file-path.md) or press `CTRL+S` to display, set, change, or append to the path.

If you use the [-sins command-line option](command-line-options.md), the debugger ignores the symbol path environment variable.

## Troubleshooting

Use [**!sym noisy**](-sym.md) or the *-n* [**WinDbg Command-Line Option**](windbg-command-line-options.md) to display additional detail as symbols are loaded. For additional troubleshooting strategies, see [Verifying Symbols](verifying-symbols.md).

## See also

[Advanced SymSrv use](advanced-symsrv-use.md)
