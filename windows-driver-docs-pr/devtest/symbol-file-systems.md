---
title: Symbol File Systems
description: Symbol File Systems
ms.assetid: 06f536e2-13d8-4727-9d34-a29a63eb01bc
keywords: ["BinPlace WDK , symbol file systems", "symbol files WDK BinPlace", "current symbol file systems WDK BinPlace", "old symbol file systems WDK", ".pdf files", "pdf symbol files WDK BinPlace", "dbg symbol files WDK BinPlace", ".dbg files"]
---

# Symbol File Systems


## <span id="ddk_symbol_file_systems_tools"></span><span id="DDK_SYMBOL_FILE_SYSTEMS_TOOLS"></span>


There are two common symbol file systems. In this document, these will be referred to as the *current system* and the *old system*.

### <span id="current_symbol_file_system"></span><span id="CURRENT_SYMBOL_FILE_SYSTEM"></span>Current Symbol File System

In the current system, there are always two files: the executable file and a .pdb file. The .pdb file contains all the symbols. The executable file contains a pointer to the .pdb file.

If a .pdb symbol file contains private symbols, BinPlace can strip this information out and produce a stripped symbol file. See [Public Symbols and Private Symbols](public-symbols-and-private-symbols.md) for details.

### <span id="old_symbol_file_system"></span><span id="OLD_SYMBOL_FILE_SYSTEM"></span>Old Symbol File System

In the old system, executable files and symbol files can be arranged in two different ways:

-   The executable file and a .pdb file. In this arrangement, most symbol information is in the .pdb file. The remainder of the symbol information is included in the executable file. The executable file also contains a pointer to the .pdb file.

-   The executable file, a .pdb file, and a .dbg file. The .pdb file is the same as in the two-file arrangement: it holds most of the symbols. The remainder of the symbol information is in the .dbg file. No symbol information is in the executable file. The executable file contains a pointer to the .dbg file, and the .dbg file contains a pointer to the .pdb file.

In the old symbol file system, both the two-file arrangement and the three-file arrangement contain the same executable code and the same symbols. The program can run and can be debugged in either arrangement. However, the three-file arrangement speeds up execution, because the executable file is smaller.

If you have binaries that were built with the old symbol file system in the two-file arrangment, BinPlace can convert it to the three-file arrangement. In other words, BinPlace can "split" the executable file into a symbol-free executable file and a new .dbg file containing the symbols that were in the executable file.

BinPlace can also strip private symbol information from files in the old symbol file system, but only if it is also splitting the files (in other words, only if it is changing the files from the two-file arrangement to the three-file arrangement). BinPlace cannot strip private symbols out of files in the old symbol file system and leave them in the two-file arrangement. And if the files are already in the three-file arrangement, BinPlace will not perform any stripping; indeed, it will not even move the symbol files if the executable file is named on the BinPlace command line. See [Public Symbols and Private Symbols](public-symbols-and-private-symbols.md) for details.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Symbol%20File%20Systems%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




