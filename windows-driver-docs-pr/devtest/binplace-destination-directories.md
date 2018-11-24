---
title: BinPlace Destination Directories
description: BinPlace Destination Directories
ms.assetid: 7a5a2324-b2a1-488b-b8de-cb5a6319d3ec
keywords:
- BinPlace WDK , destination directories
- destination directories WDK BinPlace
- symbol root directories WDK BinPlace
- class subdirectories WDK BinPlace
- file-type subdirectories WDK BinPlace
- place files WDK BinPlace
- directories WDK BinPlace
- symbol files WDK BinPlace
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# BinPlace Destination Directories


## <span id="ddk_binplace_destination_directories_tools"></span><span id="DDK_BINPLACE_DESTINATION_DIRECTORIES_TOOLS"></span>


BinPlace creates a directory tree to hold the files it is placing. The structure of that tree is determined by the parameters that are passed to BinPlace's command line, the values of certain environment variables, and the contents of a text file known as a *place file*.

BinPlace will place files if one of two conditions is met:

1.  The file is specified on the BinPlace command line.

2.  The file is a symbol file residing in the same directory as its associated executable file, and the executable file is specified on the command line. In this case, the symbol file and the executable file will be placed in different directories. BinPlace may also perform splitting or stripping (see [Public Symbols and Private Symbols](public-symbols-and-private-symbols.md)) or stripping (see [Symbol File Systems](symbol-file-systems.md)) in this scenario.

When BinPlace places files, it will automatically overwrite an older file with the same name. However, BinPlace will not, by default, overwrite a newer file. In particular, if a newer (or identical) version of an executable file is present, neither the executable file nor any associated symbol files will be written to the disk. If you wish BinPlace to overwrite files regardless of their timestamp, use the **-f** command-line option.

### <span id="file_destinations"></span><span id="FILE_DESTINATIONS"></span>File Destinations

The name of the directory into which BinPlace places any file specified on its command line is created by concatenating two directories: the *root destination directory* and the *class subdirectory*. (The directories can have any names you choose, but typically the root destination directory is the root of the directory tree where you are placing your files, and the class subdirectory is a subdirectory where it seems logical to place a specific file or group of files.)

-   The root destination directory can be specified by using the -r RootDestinationPath command-line parameter. If this is omitted, the default is determined by the \_NT386TREE, \_NTIA64TREE, or \_NTAMD64TREE environment variable on an x86-based, Itanium-based, or x64-based computer, respectively. The root destination directory must be defined in one of these ways; if it is not defined at all, BinPlace will not run.

-   The class subdirectory is usually specified in the place file. It is possible to specify multiple class subdirectories for one file; this causes BinPlace to make copies of the file and place them in each of the specified locations. See [**Place File Syntax**](place-file-syntax.md) for full details. The class subdirectory can also be specified by using the -:DEST ClassPath command-line parameter.

### <span id="symbol_file_destinations"></span><span id="SYMBOL_FILE_DESTINATIONS"></span>Symbol File Destinations

When an executable file is listed on BinPlace's command line and there is an associated symbol file in the same directory, BinPlace will copy (or alter) the symbol file as well. The directory in which this symbol file is placed is created by concatenating three directories: the *symbol root directory*, the *class subdirectory*, and the *file-type subdirectory*.

-   The symbol root directory can be specified by using the -s SymbolRoot command-line parameter. If you are using the **-a** and **-x** switches, stripped symbol files will be placed under the *SymbolRoot* directory -- in this case, you can use -n FullSymbolRoot to specify the location of full symbol files.

-   The class subdirectory is usually specified in the place file. It is possible to specify multiple class subdirectories for one file; this causes BinPlace to make copies of the file and place them in each of the specified locations. See [**Place File Syntax**](place-file-syntax.md) for full details. The class subdirectory can also be specified by using the -:DEST ClassPath command-line parameter. And if the **-y** command-line switch is used, no class subdirectory will be used for symbol files -- the destination directory will simply consist of the symbol root directory plus the file-type subdirectory.

-   The file-type subdirectory is only used for symbol files. It is determined by the file name extension of the original executable file. Thus, symbol files associated with .exe files will be placed in an exe subdirectory, symbol files associated with DLLs will be placed in a dll subdirectory, and symbol files associated with drivers will be placed in a sys subdirectory. This convention helps to avoid file name conflicts -- for example, myprogram.exe and myprogram.dll might both have symbol files named myprogram.pdb, but these symbol files will be placed in different subdirectories.

There is one exception to this algorithm. If neither **-s** nor **-n** is supplied, the full symbol files will be placed in the same location as the binaries.

**Note**   If you list the symbol file name in BinPlace's command line, BinPlace will move it like any other file and will not examine its contents. To use BinPlace's symbol file manipulation techniques, you must list the executable file name, not the symbol file name.

 

 

 





