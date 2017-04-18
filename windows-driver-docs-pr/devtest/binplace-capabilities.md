---
title: BinPlace Capabilities
description: BinPlace Capabilities
ms.assetid: 2fd49ce3-8617-4c3e-bb86-8642343ca756
keywords: ["BinPlace WDK , capabilities", "stripping files", "splitting files", "moving files WDK BinPlace"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20BinPlace%20Capabilities%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




