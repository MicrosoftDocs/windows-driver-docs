---
title: Deferred Symbol Loading
description: Deferred Symbol Loading
ms.assetid: 58771089-dd0c-4ea9-8a9a-41553f290e88
keywords: ["deferred symbol loading", "symbols, deferred symbol loading", "lazy symbol loading", "symbols, lazy symbol loading"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Deferred Symbol Loading


## <span id="ddk_deferred_symbol_loading_dbg"></span><span id="DDK_DEFERRED_SYMBOL_LOADING_DBG"></span>


By default, symbol information is not actually loaded when the target modules are loaded. Instead, symbols are loaded by the debugger as they are needed. This is called *deferred symbol loading* or *lazy symbol loading*. When this option is enabled, the debugger loads symbols whenever it encounters an unrecognized symbol.

When the symbol path is changed, for example by using the [**.sympath (Set Symbol Path)**](-sympath--set-symbol-path-.md) command, all loaded modules with export symbols are lazily reloaded. Symbols of modules with full PDB symbols will be lazily reloaded if the new path no longer includes the original path that was used to load the PDB symbols. If the new path still includes the original path to the PDB symbol file, those symbols will not be lazily reloaded.

When deferred symbol loading is disabled, process startup can be much slower, because all symbols are read whenever a module is loaded.

In WinDbg, the deferred symbol loading behavior can be modified for symbols that have no module prefix by using the [Resolve Unqualified Symbols](debug---resolve-unqualified-symbols.md) option on the **Debug** menu.

You can override deferred symbol loading by using the [**ld (Load Symbols)**](ld--load-symbols-.md) command or the [**.reload (Reload Module)**](-reload--reload-module-.md) command with the **/f** option. These force the specified symbols to be loaded immediately, although the loading of other symbols is deferred.

By default, deferred symbol loading is enabled. In CDB and KD, the **-s** [command-line option](command-line-options.md) will turn this option off. It can also be turned off in CDB by using the *LazyLoad* variable in the [tools.ini](configuring-tools-ini.md) file. Once the debugger is running, this option can be turned on or off by using [**.symopt+0x4**](-symopt--set-symbol-options-.md) or **.symopt-0x4**, respectively.

 

 





