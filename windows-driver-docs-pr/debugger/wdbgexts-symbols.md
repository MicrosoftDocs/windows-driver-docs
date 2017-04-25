---
title: WdbgExts Symbols
description: WdbgExts Symbols
ms.assetid: 7e1a1799-b87c-42cb-94ce-fbdc9a5ec973
keywords: ["WdbgExts extensions, symbols"]
---

# WdbgExts Symbols


This topic provides a brief overview of how symbols can be manipulated using the WdbgExts API. For an overview of using symbols in the [debugger engine](introduction.md#debugger-engine), see [Symbols](symbols.md) in the [Debugger Engine Overview](debugger-engine-overview.md) section of this documentation.

To evaluate a MASM or C++ expression, use the functions [**GetExpression**](https://msdn.microsoft.com/library/windows/hardware/ff546683) or [**GetExpressionEx**](https://msdn.microsoft.com/library/windows/hardware/ff546691).

To read the value of a member in a structure, use the [**GetFieldData**](https://msdn.microsoft.com/library/windows/hardware/ff546743) function or, if, the member contains a primitive value, [**GetFieldValue**](https://msdn.microsoft.com/library/windows/hardware/ff546781) can be used. To determine the size of an instance of a symbol in the target's memory, use the [**GetTypeSize**](https://msdn.microsoft.com/library/windows/hardware/ff549446) function.

To locate the offset of a member in a structure, use the [**GetFieldOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546758) function.

To read multiple members in a structure, first use the [**InitTypeRead**](https://msdn.microsoft.com/library/windows/hardware/ff550953) function to initialize the structure. Then, you can use the [**ReadField**](https://msdn.microsoft.com/library/windows/hardware/ff553539) function to read the members with size less than or equal to 8 bytes one at a time. For structure addresses in physical memory, use the [**InitTypeReadPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff550957) function instead of **InitTypeRead**.

There are two functions that you can use for iterating over linked lists. For doubly-linked lists that use the LIST\_ENTRY32 or LIST\_ENTRY64 structures, the function [**ReadListEntry**](https://msdn.microsoft.com/library/windows/hardware/ff553585) can be used to find the next and previous entries. The function [**ListType**](https://msdn.microsoft.com/library/windows/hardware/ff551988) will iterate over all the entries in a linked list and call a callback function for each entry.

To locate a symbol near a specified address in the target's memory, use the [**GetSymbol**](https://msdn.microsoft.com/library/windows/hardware/ff548447) function.

To delete all the symbol information from the debugger engine's cache, use the [**ReloadSymbols**](https://msdn.microsoft.com/library/windows/hardware/ff554381) function. To read or change the symbol path, which is used to search for symbol files, use the [**GetSetSympath**](https://msdn.microsoft.com/library/windows/hardware/ff548291) function.

Almost all symbol operations provided by the debugger engine can be executed using the [**Ioctl**](https://msdn.microsoft.com/library/windows/hardware/ff551084) operation [**IG\_DUMP\_SYMBOL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff550906). However, while being a very flexible function, it is advanced and we recommend that you use the above simpler functions where applicable.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a more powerful symbols API, see [Using Symbols](using-symbols.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20WdbgExts%20Symbols%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




