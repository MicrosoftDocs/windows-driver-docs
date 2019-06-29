---
title: WdbgExts Symbols
description: WdbgExts Symbols
ms.assetid: 7e1a1799-b87c-42cb-94ce-fbdc9a5ec973
keywords: ["WdbgExts extensions, symbols"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# WdbgExts Symbols


This topic provides a brief overview of how symbols can be manipulated using the WdbgExts API. For an overview of using symbols in the [debugger engine](introduction.md#debugger-engine), see [Symbols](symbols.md) in the [Debugger Engine Overview](debugger-engine-overview.md) section of this documentation.

To evaluate a MASM or C++ expression, use the functions [**GetExpression**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/nc-wdbgexts-pwindbg_get_expression) or [**GetExpressionEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/nf-wdbgexts-getexpressionex).

To read the value of a member in a structure, use the [**GetFieldData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/nf-wdbgexts-getfielddata) function or, if, the member contains a primitive value, [**GetFieldValue**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/nf-wdbgexts-getfieldvalue) can be used. To determine the size of an instance of a symbol in the target's memory, use the [**GetTypeSize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/nf-wdbgexts-gettypesize) function.

To locate the offset of a member in a structure, use the [**GetFieldOffset**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugsymbols-getfieldoffset) function.

To read multiple members in a structure, first use the [**InitTypeRead**](https://docs.microsoft.com/previous-versions/ff550953(v=vs.85)) function to initialize the structure. Then, you can use the [**ReadField**](https://docs.microsoft.com/previous-versions/ff553539(v=vs.85)) function to read the members with size less than or equal to 8 bytes one at a time. For structure addresses in physical memory, use the [**InitTypeReadPhysical**](https://docs.microsoft.com/previous-versions/ff550957(v=vs.85)) function instead of **InitTypeRead**.

There are two functions that you can use for iterating over linked lists. For doubly-linked lists that use the LIST\_ENTRY32 or LIST\_ENTRY64 structures, the function [**ReadListEntry**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/nf-wdbgexts-readlistentry) can be used to find the next and previous entries. The function [**ListType**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/nf-wdbgexts-listtype) will iterate over all the entries in a linked list and call a callback function for each entry.

To locate a symbol near a specified address in the target's memory, use the [**GetSymbol**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/nc-wdbgexts-pwindbg_get_symbol) function.

To delete all the symbol information from the debugger engine's cache, use the [**ReloadSymbols**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/nf-wdbgexts-reloadsymbols) function. To read or change the symbol path, which is used to search for symbol files, use the [**GetSetSympath**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/nf-wdbgexts-getsetsympath) function.

Almost all symbol operations provided by the debugger engine can be executed using the [**Ioctl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/nc-wdbgexts-pwindbg_ioctl_routine) operation [**IG\_DUMP\_SYMBOL\_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/ns-wdbgexts-_sym_dump_param). However, while being a very flexible function, it is advanced and we recommend that you use the above simpler functions where applicable.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a more powerful symbols API, see [Using Symbols](using-symbols.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation.

 

 





