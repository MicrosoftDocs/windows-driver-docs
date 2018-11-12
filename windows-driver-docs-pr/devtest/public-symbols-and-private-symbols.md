---
title: Public Symbols and Private Symbols
description: Public Symbols and Private Symbols
ms.assetid: 83979008-f9ea-4976-8acd-d7efb82947cd
keywords:
- BinPlace WDK , public symbols
- BinPlace WDK , private symbols
- symbol files WDK BinPlace
- private symbols WDK BinPlace
- public symbols WDK BinPlace
- reducing symbols in symbol files
- full symbol files WDK BinPlace
- stripped symbol files WDK BinPlace
- SymChk tool WDK BinPlace
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Public Symbols and Private Symbols


## <span id="ddk_public_symbols_and_private_symbols_tools"></span><span id="DDK_PUBLIC_SYMBOLS_AND_PRIVATE_SYMBOLS_TOOLS"></span>


When you build a driver or other program, the program's symbols are usually stored in *symbol files*, although some older compilers store certain symbols in the executable file. When a debugger is analyzing a program, it needs to access the program's symbols.

Typically, symbol files can include any or all of the following symbols:

-   The names and addresses of all functions

-   All data type, structure, and class definitions

-   The names, data types, and addresses of global variables

-   The names, data types, addresses, and scopes of local variables

-   The line numbers in the source code that correspond to each binary instruction

Some program developers might feel uncomfortable sharing all this information with their customers. BinPlace can be used to reduce the amount of symbols in a symbol file.

Some basic symbols, such as function names and global variables, are needed for even the most rudimentary debugging. These are called *public symbols*. Symbols such as data structure names, global variables visible in only one object file, local variables, and line number information are not always required for debugging, although they are useful for a more in-depth debugging session. These are called *private symbols*.

A symbol file that contains both private and public symbols is called a *full symbol file*. A symbol file that contains public symbols alone is called a *stripped symbol file*.

BinPlace can create a stripped symbol file. It does this by creating a new symbol file that contains only public symbols; the private symbols are removed ("stripped" out). When the most common BinPlace options are used (-a -x -s -n), the stripped symbol files are placed in the directory that is listed after the **-s** switch, and the full symbol files are placed in the directory that is listed after the **-n** switch.

When BinPlace strips a symbol file, the stripped and full versions of the file are given identical signatures and other identifying information. This allows you to use either version for debugging.

**Note**   BinPlace will strip private symbols out of a symbol file when the symbol file is in the same directory as the executable file, and you specify the name of the *executable* file (along with the appropriate options) on the BinPlace command line. You should not specify the name of the symbol file itself -- doing so will result in BinPlace moving the file without altering it.

 

If you need to determine whether a symbol file contains private symbols, you can use the [SymChk](https://msdn.microsoft.com/library/windows/hardware/ff558844) tool. SymChk is part of the Debugging Tools for Windows package. See SymChk and [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063) for details.

If you are submitting your driver to the [Windows Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016), you can submit stripped symbol files if you prefer not to share your private symbols with Microsoft. Symbol files that have been stripped by BinPlace do not expose any parts of your driver's architecture that normally would be considered confidential. For more information, see the [Windows Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016).

 

 





