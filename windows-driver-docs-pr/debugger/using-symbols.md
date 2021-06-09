---
title: Using Symbols
description: Using Symbols
keywords: ["Debugger Engine, symbols", "symbols"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Symbols


## <span id="ddk_symbols_dbx"></span><span id="DDK_SYMBOLS_DBX"></span>


For an overview of symbols, including using symbol files and symbol servers, see [Symbols](symbols.md).

### <span id="symbol_names_and_locations"></span><span id="SYMBOL_NAMES_AND_LOCATIONS"></span>Symbol Names and Locations

To find the location of a symbol given its name, use [**GetOffsetByName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getoffsetbyname). For details on the syntax used to specify symbol names, see [Symbol Syntax and Symbol Matching](symbol-syntax-and-symbol-matching.md).

If the exact name of a symbol is not known, or multiple symbols have the same name, [**StartSymbolMatch**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-startsymbolmatch) will begin a search for symbols whose names match a given pattern. For details on the syntax, see [String Wildcard Syntax](string-wildcard-syntax.md).

To find the name of a symbol given its location, use [**GetNameByOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getnamebyoffset). To find the names of symbols in a module near a given location, use [**GetNearNamebyOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getnearnamebyoffset).

**Note**   Whenever possible, qualify the symbol with the module name -- for example **mymodule!main**. Otherwise, if the symbol does not exist (for example, because of a typographical error) the engine will have to load and search the symbols for every module; this can be a slow process, especially for kernel-mode debugging. If the symbol name was qualified with a module name, the engine will only need to search the symbols for that module.

 

A symbol is uniquely identified using the structure [**DEBUG\_MODULE\_AND\_ID**](/windows-hardware/drivers/ddi/dbgeng/ns-dbgeng-_debug_module_and_id). This structure is returned by the methods [**GetSymbolEntriesByName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getsymbolentriesbyname) and [**GetSymbolEntriesByOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getsymbolentriesbyoffset), which search for symbols based on their name and location, respectively.

The method [**GetSymbolEntryInformation**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getsymbolentryinformation) returns a description of a symbol using the [**DEBUG\_SYMBOL\_ENTRY**](/windows-hardware/drivers/ddi/dbgeng/ns-dbgeng-_debug_symbol_entry) structure.

To find the offset of a field within a structure, use [**GetFieldOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols-getfieldoffset). To find the name of a field given its index within a structure, use [**GetFieldName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getfieldname). To find the name of an enumeration constant given its value, use [**GetConstantName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getconstantname).

The method [**GetSymbolInformation**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-getsymbolinformation) can perform several requests for information about symbols.

### <span id="symbol_options"></span><span id="SYMBOL_OPTIONS"></span>Symbol Options

A number of options control how the symbols are loaded and unloaded. For a description of these options, see [Setting Symbol Options](symbol-options.md).

Symbol options may be turned on by using [**AddSymbolOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-addsymboloptions), and turned off by using [**RemoveSymbolOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-removesymboloptions).

[**GetSymbolOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getsymboloptions) returns the current symbol options. To set all the symbol options at once, use [**SetSymbolOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-setsymboloptions).

### <span id="reloading_symbols"></span><span id="RELOADING_SYMBOLS"></span>Reloading Symbols

After loading symbol files, the engine stores the symbol information in an internal cache. To flush this cache, use [**Reload**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-reload). These symbols will have to be loaded again now or at a later time.

### <span id="synthetic_symbols"></span><span id="SYNTHETIC_SYMBOLS"></span> Synthetic Symbols

*Synthetic symbols* are a way to label an arbitrary address for easy reference. Synthetic symbols can be created in any existing module. The method [**AddSyntheticSymbol**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-addsyntheticsymbol) creates a new synthetic symbol. Synthetic symbols can be removed using [**RemoveSyntheticSymbol**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-removesyntheticsymbol). Reloading the symbols for the module deletes all synthetic symbols associated with that module.

### <span id="symbol_path"></span><span id="SYMBOL_PATH"></span>Symbol Path

To add a directory or symbol server to the symbol path, use the method [**AppendSymbolPath**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-appendsymbolpath). The whole symbol path is returned by [**GetSymbolPath**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getsymbolpath) and can be changed using [**SetSymbolPath**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-setsymbolpath).

 

