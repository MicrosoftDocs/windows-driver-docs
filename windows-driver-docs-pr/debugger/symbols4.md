---
title: Symbols
description: Symbols
ms.assetid: 7eec815b-f81a-4c0f-b862-6ee31be7ed8f
keywords: ["Debugger Engine, symbols"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Symbols


A *symbol* is a named unit of data or code from a source file that appears in a module. Information about symbols can include the name, type (if applicable), the address or register where it is stored, and any parent or child symbols. Examples of symbols include variables (local and global), functions, and any entry point into a module.

The symbol information is used by the engine to help interpret data and code in the target. With this information, the engine can search for symbols by name or location in memory and provide a description of a symbol.

The engine gets its information about symbols from symbol files, which are located on the local file system or loaded from a symbol server. When using a symbol server, the engine will automatically use the correct version of the symbol file to match the module in the target. Symbol files can be loaded whenever the corresponding module is loaded, or they can be loaded as needed.

**Note**   Often optimizing compilers do not include accurate information in symbol files. This can cause the engine to misinterpret the value of some variables as the variable's location or lifetime might be incorrectly described, causing the engine to look at the wrong piece of memory or think a variable value is live when it is dead (or vice versa). It is also possible for an optimizing compiler to change the order of execution or to split a function into several pieces. Best results are usually obtained when debugging unoptimized code.

 

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about using symbols, see [Using Symbols](using-symbols.md). For an overview of using symbol files and symbol servers, see [Symbols](symbols.md) in the Debuggers section of this documentation.

 

 





