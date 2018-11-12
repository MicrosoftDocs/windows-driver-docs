---
title: BinPlace Capabilities
description: BinPlace Capabilities
ms.assetid: 2fd49ce3-8617-4c3e-bb86-8642343ca756
keywords:
- BinPlace WDK , capabilities
- stripping files
- splitting files
- moving files WDK BinPlace
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# BinPlace Capabilities


## <span id="ddk_binplace_capabilities_tools"></span><span id="DDK_BINPLACE_CAPABILITIES_TOOLS"></span>


BinPlace primarily performs three actions: stripping files, splitting files, and moving files.

### <span id="stripping_files"></span><span id="STRIPPING_FILES"></span>Stripping Files

The symbols that compilers and linkers create can be divided into two categories: public symbols and private symbols. Stripping a symbol file removes private symbol information and leaves just the public symbol information.

For more information, see [Public Symbols and Private Symbols](public-symbols-and-private-symbols.md).

### <span id="splitting_files"></span><span id="SPLITTING_FILES"></span>Splitting Files

Some executable files contain symbols. BinPlace can split a file of this sort into two files:

-   a symbol file without executable code

-   an executable file without symbol information

For more information, see [Symbol File Systems](symbol-file-systems.md).

### <span id="moving_files"></span><span id="MOVING_FILES"></span>Moving Files

BinPlace can move files. When BinPlace is used on any file other than an executable file, it will move it to its destination directory tree without altering its contents.

When BinPlace is used on an executable file, and there is an associated symbol file in the same directory, the executable file and the symbol file will both be moved. Stripping or splitting will also occur if the appropriate BinPlace options have been selected.

For a large project, BinPlace can be used to organize a great number of files into the proper project directories. If you are building a large set of binary files and you are going to collect various subsets of the files into different packages, BinPlace can manage this process.

For more information, see [BinPlace Destination Directories](binplace-destination-directories.md).

 

 





