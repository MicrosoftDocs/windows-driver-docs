---
title: Symbol path for Windows debuggers
description: The symbol path specifies locations where the Windows debuggers (WinDbg, KD, CDB, NTST) look for symbol files. 
keywords: symbol files and paths, symbols, lazy symbol loading, deferred symbol loading, symbol path
ms.date: 12/15/2022
---

# Symbol path for Windows debuggers

The symbol path specifies the directories in which Windows debuggers (WinDbg, KD, CDB, NTST) look for [symbol files](symbols.md).

Some compilers (such as Microsoft Visual Studio) put symbol files in the same directory as the binary files. The symbol files and the checked binary files contain path and file name information. This information frequently enables the debugger to find the symbol files automatically.

The debugger can locate the symbol files without you setting the symbol path when you're debugging a user-mode process on the computer where the executable was built and the symbol files are still in their original location. In most other situations, you have to set the symbol path to point to your symbol file locations.

## Symbol path syntax

The debugger's symbol path is a string that consists of multiple directory paths separated by semicolons; for example, ```C:\Dir1;C:\Dir2\DirA;C:\Dir2\DirB```.

Relative paths are supported. However, unless you always start the debugger from the same directory, you should add a drive letter or a network share before each path.

For each directory in the symbol path, the debugger looks in three directories. For example, if the symbol path includes *c:\Dir1* and the debugger is looking for symbol information for a DLL, the debugger will look for symbol information in the following directories, listed in order:

1. *c:\Dir1\symbols\dll*
2. *c:\Dir1\dll*
3. *c:\Dir1*

The debugger then repeats this process for each directory in the symbol path. Finally, the debugger looks in the current directory and then in the current directory with *..\dll* appended to it. (The debugger appends *..\dll*, *..\exe*, or *..\sys*, depending on which binaries it's debugging.)

You don't need to worry that the debugger will use the wrong symbols that it might first find in this sequence. Symbol files have date and time stamps, and the debugger always looks for the symbols that match the time stamp on the binary files that it's debugging. For more information about responses when symbols files aren't available, see [Matching Symbol Names](matching-symbol-names.md).

One way to set the symbol path is by entering the [**.sympath**](-sympath--set-symbol-path-.md) command. For other ways to set the symbol path, see [Controlling the Symbol Path](#controlling-the-symbol-path).

## Caching symbols locally: cache\*

We strongly recommend that you always cache your symbols locally. One way to cache symbols locally is to include `cache*;` or `cache*localsymbolcache;*` in your symbol path.

If you include the string `cache*;` in your symbol path, symbols loaded from any element that appears to the right of this string are stored in the default symbol cache directory on the local computer. For example, the following command tells the debugger to get symbols from the network share named *\\someshare* and cache the symbols in the default location on the local computer.

```dbgcmd
.sympath cache*;\\someshare
```

If you include the string `cache*localsymbolcache;` in your symbol path, symbols loaded from any element that appears to the right of this string are stored in the *localsymbolcache* directory.

For example, the following command tells the debugger to obtain symbols from the network share *\\\someshare* and cache the symbols in the *c:\MySymbols* directory.

```dbgcmd
.sympath cache*c:\MySymbols;\\someshare
```

## Using a symbol server: srv*

If you're connected to the Internet or a corporate network, the most efficient way to access symbols is to use a symbol server such as the public [Microsoft Internet Symbol Server](https://msdl.microsoft.com/download/symbols). You can use a symbol server by using one of the following strings in your symbol path.

* The `srv*` string

  If you include the string `srv*` in your symbol path, the debugger uses a symbol server to get symbols from the default symbol store. For example, the following command tells the debugger to use a symbol server to get symbols from the default symbol store. These symbols aren't cached on the local computer.

  ```dbgcmd
  .sympath srv*
  ```

* The `srv*symbolstore` string

  If you include the string `srv*symbolstore` in your symbol path, the debugger uses a symbol server to get symbols from the *symbolstore* store. For example, the following command tells the debugger to use a symbol server to get symbols from the [Microsoft Internet Symbol Server](https://msdl.microsoft.com/download/symbols) store. These symbols aren't cached on the local computer.

  ```dbgcmd
  .sympath srv*https://msdl.microsoft.com/download/symbols
  ```

* The `srv*localsymbolcache*symbolstore` string

  If you include the string `srv*localcache*symbolstore` in your symbol path, the debugger uses a symbol server to get symbols from the *symbolstore* store and caches them in the *localcache* directory. For example, the following command tells the debugger to use a symbol server to get symbols from the [Microsoft Internet Symbol Server](https://msdl.microsoft.com/download/symbols) store and cache the symbols in *c:\MyServerSymbols*.

  ```dbgcmd
  .sympath srv*c:\MyServerSymbols*https://msdl.microsoft.com/download/symbols
  ```

If you have a directory on your computer where you manually place symbols, don't use that directory as the cache for symbols obtained from a symbol server. Instead, use two separate directories. For example, you can manually place symbols in *c:\MyRegularSymbols* and then designate *c:\MyServerSymbols* as a cache for symbols obtained from a server. The following example shows how to specify both directories in your symbol path.

```dbgcmd
.sympath c:\MyRegularSymbols;srv*c:\MyServerSymbols*https://msdl.microsoft.com/download/symbols
```

## Combining cache\* and srv\*

If you include the string `cache*;` in your symbol path, symbols loaded from any element that appears to the right of this string are stored in the default symbol cache directory on the local computer. For example, the following command tells the debugger to use a symbol server to get symbols from the [Microsoft Internet Symbol Server](https://msdl.microsoft.com/download/symbols) store and cache them in the default symbol cache directory.

```dbgcmd
.sympath cache*;srv*https://msdl.microsoft.com/download/symbols
```

If you include the string `cache*localsymbolcache;` in your symbol path, symbols loaded from any element that appears to the right of this string are stored in the *localsymbolcache* directory.

For example, the following command tells the debugger to use a symbol server to get symbols from the [Microsoft Internet Symbol Server](https://msdl.microsoft.com/download/symbols) store and cache the symbols in the *c:\MySymbols* directory.

```dbgcmd
.sympath cache*c:\MySymbols;srv*https://msdl.microsoft.com/download/symbols
```

## Using AgeStore to reduce the cache size

You can use the [AgeStore](agestore.md) tool to delete cached files that are older than a specified date or to delete enough old files such that the resulting cache size is less than a specified amount. This cleanup of cache files is useful if your downstream store gets too large.

For more information about symbol servers and symbol stores, see [Custom Symbol Stores and Symbol Servers](symbol-stores-and-symbol-servers.md).

## Lazy symbol loading

The debugger's default behavior is to use *lazy symbol loading*, also known as [*deferred symbol loading*](deferred-symbol-loading.md). This kind of loading means that symbols aren't loaded until they're required.

When the symbol path is changed, for example by using the [`.sympath`](-sympath--set-symbol-path-.md) command, all loaded modules with export symbols are lazily reloaded.

Symbols of modules with full [PDB symbols](symbols-portable-pdb.md) will be lazily reloaded if the new path no longer includes the original path that was used to load the PDB symbols. If the new path still includes the original path to the PDB symbol file, those symbols won't be lazily reloaded.

You can turn off lazy symbol loading in CDB and KD by using the `-s` [command-line option](command-line-options.md). You can also force symbol loading by using the `ld` [**(Load Symbols)**](ld--load-symbols-.md) command or by using the `.reload` [**(Reload Module)**](-reload--reload-module-.md) command together with the `/f` option.

## Azure DevOps Services Artifacts

A symbol server is available with [Azure Artifacts in Azure DevOps Services](/azure/devops/artifacts). For information on working with Azure Artifacts in WinDbg, see [Debug with WinDbg](/azure/devops/artifacts/symbols/debug-with-symbols-windbg). For general information about Azure generated symbols, see [Symbol files (PDBs)](/azure/devops/artifacts/concepts/symbols).

### Controlling the symbol path

To control the symbol path, you can use one of the following methods:

* Use the [`.sympath`](-sympath--set-symbol-path-.md) command to display, set, change, or append to the path. The `.symfix` [**(Set Symbol Store Path)**](-symfix--set-symbol-store-path-.md) command is similar to `.sympath` but saves you some typing.

* Before you start the debugger, use the `_NT_SYMBOL_PATH` and `_NT_ALT_SYMBOL_PATH` [environment variables](environment-variables.md) to set the path. The symbol path is created by appending `_NT_SYMBOL_PATH` after `_NT_ALT_SYMBOL_PATH`. (Typically, the path is set through the `_NT_SYMBOL_PATH`. However, you might want to use `_NT_ALT_SYMBOL_PATH` to override these settings in special cases, such as if you have private versions of shared symbol files.) If you try to add an invalid directory through these environment variables, the debugger ignores this directory.

* When you start the debugger, use the `-y` [command-line option](command-line-options.md) to set the path.

* (WinDbg only) Use the [File | Symbol File Path](file---symbol-file-path.md) command or press `CTRL+S` to display, set, change, or append to the path.

If you use the `-sins` [command-line option](command-line-options.md), the debugger ignores the symbol path environment variable.

## Related articles

[Advanced SymSrv Use](advanced-symsrv-use.md)
