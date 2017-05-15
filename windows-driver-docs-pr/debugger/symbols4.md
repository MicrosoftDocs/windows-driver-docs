---
title: Symbols
description: Symbols
ms.assetid: 7eec815b-f81a-4c0f-b862-6ee31be7ed8f
keywords: ["Debugger Engine, symbols"]
---

# Symbols


A *symbol* is a named unit of data or code from a source file that appears in a module. Information about symbols can include the name, type (if applicable), the address or register where it is stored, and any parent or child symbols. Examples of symbols include variables (local and global), functions, and any entry point into a module.

The symbol information is used by the engine to help interpret data and code in the target. With this information, the engine can search for symbols by name or location in memory and provide a description of a symbol.

The engine gets its information about symbols from symbol files, which are located on the local file system or loaded from a symbol server. When using a symbol server, the engine will automatically use the correct version of the symbol file to match the module in the target. Symbol files can be loaded whenever the corresponding module is loaded, or they can be loaded as needed.

**Note**   Often optimizing compilers do not include accurate information in symbol files. This can cause the engine to misinterpret the value of some variables as the variable's location or lifetime might be incorrectly described, causing the engine to look at the wrong piece of memory or think a variable value is live when it is dead (or vice versa). It is also possible for an optimizing compiler to change the order of execution or to split a function into several pieces. Best results are usually obtained when debugging unoptimized code.

 

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about using symbols, see [Using Symbols](using-symbols.md). For an overview of using symbol files and symbol servers, see [Symbols](symbols.md) in the Debuggers section of this documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Symbols%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




