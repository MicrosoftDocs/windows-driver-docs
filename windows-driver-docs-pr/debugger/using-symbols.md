---
title: Using Symbols
description: Using Symbols
ms.assetid: 1de1441f-b4d7-49e9-87ad-392a75b3d4be
keywords: ["Debugger Engine, symbols", "symbols"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Symbols


## <span id="ddk_symbols_dbx"></span><span id="DDK_SYMBOLS_DBX"></span>


For an overview of symbols, including using symbol files and symbol servers, see [Symbols](symbols.md).

### <span id="symbol_names_and_locations"></span><span id="SYMBOL_NAMES_AND_LOCATIONS"></span>Symbol Names and Locations

To find the location of a symbol given its name, use [**GetOffsetByName**](https://msdn.microsoft.com/library/windows/hardware/ff548035). For details on the syntax used to specify symbol names, see [Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md).

If the exact name of a symbol is not known, or multiple symbols have the same name, [**StartSymbolMatch**](https://msdn.microsoft.com/library/windows/hardware/ff558815) will begin a search for symbols whose names match a given pattern. For details on the syntax, see [String Wildcard Syntax](string-wildcard-syntax.md).

To find the name of a symbol given its location, use [**GetNameByOffset**](https://msdn.microsoft.com/library/windows/hardware/ff547183). To find the names of symbols in a module near a given location, use [**GetNearNamebyOffset**](https://msdn.microsoft.com/library/windows/hardware/ff547204).

**Note**   Whenever possible, qualify the symbol with the module name -- for example **mymodule!main**. Otherwise, if the symbol does not exist (for example, because of a typographical error) the engine will have to load and search the symbols for every module; this can be a slow process, especially for kernel-mode debugging. If the symbol name was qualified with a module name, the engine will only need to search the symbols for that module.

 

A symbol is uniquely identified using the structure [**DEBUG\_MODULE\_AND\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff541511). This structure is returned by the methods [**GetSymbolEntriesByName**](https://msdn.microsoft.com/library/windows/hardware/ff548458) and [**GetSymbolEntriesByOffset**](https://msdn.microsoft.com/library/windows/hardware/ff548476), which search for symbols based on their name and location, respectively.

The method [**GetSymbolEntryInformation**](https://msdn.microsoft.com/library/windows/hardware/ff548484) returns a description of a symbol using the [**DEBUG\_SYMBOL\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff541662) structure.

To find the offset of a field within a structure, use [**GetFieldOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546758). To find the name of a field given its index within a structure, use [**GetFieldName**](https://msdn.microsoft.com/library/windows/hardware/ff546747). To find the name of an enumeration constant given its value, use [**GetConstantName**](https://msdn.microsoft.com/library/windows/hardware/ff545702).

The method [**GetSymbolInformation**](https://msdn.microsoft.com/library/windows/hardware/ff548505) can perform several requests for information about symbols.

### <span id="symbol_options"></span><span id="SYMBOL_OPTIONS"></span>Symbol Options

A number of options control how the symbols are loaded and unloaded. For a description of these options, see [Setting Symbol Options](symbol-options.md).

Symbol options may be turned on by using [**AddSymbolOptions**](https://msdn.microsoft.com/library/windows/hardware/ff537930), and turned off by using [**RemoveSymbolOptions**](https://msdn.microsoft.com/library/windows/hardware/ff554535).

[**GetSymbolOptions**](https://msdn.microsoft.com/library/windows/hardware/ff549139) returns the current symbol options. To set all the symbol options at once, use [**SetSymbolOptions**](https://msdn.microsoft.com/library/windows/hardware/ff556798).

### <span id="reloading_symbols"></span><span id="RELOADING_SYMBOLS"></span>Reloading Symbols

After loading symbol files, the engine stores the symbol information in an internal cache. To flush this cache, use [**Reload**](https://msdn.microsoft.com/library/windows/hardware/ff554379). These symbols will have to be loaded again now or at a later time.

### <span id="synthetic_symbols"></span><span id="SYNTHETIC_SYMBOLS"></span> Synthetic Symbols

*Synthetic symbols* are a way to label an arbitrary address for easy reference. Synthetic symbols can be created in any existing module. The method [**AddSyntheticSymbol**](https://msdn.microsoft.com/library/windows/hardware/ff537943) creates a new synthetic symbol. Synthetic symbols can be removed using [**RemoveSyntheticSymbol**](https://msdn.microsoft.com/library/windows/hardware/ff554542). Reloading the symbols for the module deletes all synthetic symbols associated with that module.

### <span id="symbol_path"></span><span id="SYMBOL_PATH"></span>Symbol Path

To add a directory or symbol server to the symbol path, use the method [**AppendSymbolPath**](https://msdn.microsoft.com/library/windows/hardware/ff538110). The whole symbol path is returned by [**GetSymbolPath**](https://msdn.microsoft.com/library/windows/hardware/ff549155) and can be changed using [**SetSymbolPath**](https://msdn.microsoft.com/library/windows/hardware/ff556802).

 

 





