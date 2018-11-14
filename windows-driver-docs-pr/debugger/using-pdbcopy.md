---
title: Using PDBCopy
description: Using PDBCopy
ms.assetid: f8207b09-5a1b-4ff3-b99d-20daa88cfe10
keywords: ["PDBCopy, using"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using PDBCopy


PDBCopy is a command-line tool that creates a stripped symbol file from a full symbol file. In other words, it takes a symbol file that contains both private symbol data and a public symbol table, and creates a copy of that file that contains only the public symbol table. Depending on which PDBCopy options are used, the stripped symbol file contains either the entire public symbol table or a specified subset of the public symbol table.

PDBCopy works with any PDB-format symbol file (with file name extension .pdb), but not with the older format (.dbg) symbol files.

For a description of public symbol tables and private symbol data, see [Public and Private Symbols](public-and-private-symbols.md).

### <span id="removing_private_symbols"></span><span id="REMOVING_PRIVATE_SYMBOLS"></span>Removing Private Symbols

If you wish to create a stripped symbol file that contains all the public symbols and none of the private symbols, use PDBCopy with three parameters: the path and name of the original symbol file, the path and name of the new symbol file, and the -p option.

For example, the following command creates a new file, named publicsymbols.pdb, which contains the same public symbol table as mysymbols.pdb but contains none of the private symbol data:

**pdbcopy mysymbols.pdb publicsymbols.pdb -p**

If mysymbols.pdb happens to already be a stripped symbol file, the symbolic content of the new file and the old file will be identical.

After issuing this command, you should move the new file to a new location and rename it to the original name of the symbol file (in this example, mysymbols.pdb), because most debugging programs and symbol extraction programs look for symbols based on a specific file name. Alternatively, you could use the same file name for the input file and the output file on the PDBCopy command line, as long as different directories are specified:

**pdbcopy c:\\dir1\\mysymbols.pdb c:\\dir2\\mysymbols.pdb -p**

**Note**  The destination file should not exist before PDBCopy is run. If a file with this name exists, various errors may occur.

 

### <span id="removing_private_symbols_and_selected_public_symbols"></span><span id="REMOVING_PRIVATE_SYMBOLS_AND_SELECTED_PUBLIC_SYMBOLS"></span>Removing Private Symbols and Selected Public Symbols

If you wish to not only remove the private symbol data, but also reduce the amount of information in the public symbol table, you can use the -f option to specify a list of public symbols that are to be removed.

The following example illustrates this procedure:

1.  Determine the full names, including decorations, of the symbols you wish to remove. If you are not sure of the decorated symbol names, you can use the [DBH](dbh.md) tool to determine them. See Determining the Decorations of a Specific Symbol for details. In this example, let us suppose that the decorated names of the symbols you wish to remove are **\_myGlobal1** and **\_myGlobal2**.

2.  Create a text file containing a list of the symbols to be removed. Each line in this file should include the name of one symbol, including decorations, but not including module names. In this example, the file would contain the following two lines:

    ```text
    _myGlobal1
    _myGlobal2 
    ```

    The file can be given any name you choose. Let us suppose that you name this file listfile.txt and place it in the directory C:\\Temp.

3.  Use the following PDBCopy command line:

    ```console
    pdbcopy OldPDB NewPDB-p -f:@TextFile 
    ```

    where *OldPDB* and *NewPDB* are the original symbol file and the new symbol file, and *TextFile* is the file created in step two. The -f option indicates that certain public symbols are to be removed, and the ampersand ( @ ) indicates that these symbols are listed in the specified text file.

    In the current example, the command would look like this:

    ```console
    pdbcopy c:\dir1\mysymbols.pdb c:\dir3\mysymbols.pdb -p -f:@c:\temp\listfile.txt 
    ```

    This creates a new symbol file, C:\\dir2\\mysymbols.pdb, which does not contain any private symbols and does not contain the two global variables you listed in listfile.txt.

As shown in this example, PDBCopy's -f option removes a specific list of public symbols. The ampersand ( @ ) indicates that these symbols are listed in a text file. An alternate method is to list all the symbols on the command line, using the -f option without an ampersand. Thus the following command line is equivalent to the example in the procedure above:

**pdbcopy c:\\dir1\\mysymbols.pdb c:\\dir3\\mysymbols.pdb -p -f:\_myGlobal1 -f:\_myGlobal2**

Unless you wish to remove only one or two symbols, it is simpler to use a text file than to list them on the command line.

If you wish to remove the majority of public symbols from your .pdb file, the -F option is the easiest method. While the -f option requires you to list those public symbols you wish to remove, the -F option requires you to list those public symbols you do not wish to remove. All other public symbols (as well as all private symbols) will be removed. The -F option supports the same two syntax options as the -f option: either -F: followed by the name of a symbol to be retained, or -F:@ followed by the name of a text file that contains a list of the symbols to be retained. In either case, decorated symbol names must be used.

For example, the following command removes all private symbols and almost all public symbols, leaving only the symbols **\_myFunction5** and **\_myGlobal7**:

**pdbcopy c:\\dir1\\mysymbols.pdb c:\\dir3\\mysymbols.pdb -p -F:\_myFunction5 -F:\_myGlobal7**

If you combine multiple instances of the -f option on one line, all the specified symbols are removed. If you combine multiple instances of the -F option on one line, all the specified symbols are retained, and all other symbols are removed. You cannot combine -f with -F.

The -f and -F options cannot be used without the -p option, which removes all private symbol data. Even if your original file contains no private symbols, you must still include the -p option (although it has no effect in this case).

The -F option cannot be used to prevent the private symbol data from being removed. If you use this option with a symbol that is not included in the public symbol table, PDBCopy ignores it.

### <span id="the_mspdb__dll_file"></span><span id="THE_MSPDB__DLL_FILE"></span>The mspdb\*.dll File

PDBCopy must access either the Mspdb80.dll file or the Mspdb60.dll file in order to run. By default, PDBCopy uses Mspdb80.dll, which is the version used by Visual Studio .NET 2002 and later versions of Visual Studio. If your symbols were built using Visual Studio 6.0 or an earlier version, you can specify the -vc6 command-line option so that PDBCopy uses Mspdb60.dll instead, although this is not required. PDBCopy looks for the appropriate file even if the -vc6 option is not used. You can find these files within your installation of Visual Studio, the Platform SDK, or the Windows Driver Kit (WDK).

Before running PDBCopy, make sure that the correct version of mspdb\*.dll file is accessible to your computer, and make sure that its location is part of the command path. If it is not, you should use the **path** command to add this location to the command path.

### <span id="the_file_signature_and_the_symsrv_index"></span><span id="THE_FILE_SIGNATURE_AND_THE_SYMSRV_INDEX"></span>The File Signature and the SymSrv Index

Each symbol file has a fixed signature that uniquely identifies it. SymSrv uses the signature to generate a unique "index value" for the file. If two files have different contents or different creation times, they will also have distinct signatures and distinct SymSrv index values.

Files created with PDBCopy are an exception to the rule of unique index values. When PDBCopy creates a new symbol file, it has the same signature and SymSrv index value as the old file. This feature allows one file to be replaced with the other without altering the behavior of symbol-related tools.

If you wish the new file to have a distinct signature and SymSrv index, use the -s option. In most cases you will not wish to use this option, since the most common use of PDBCopy is to create an altered symbol file that can replace the old file without causing a mismatch. A new signature may cause SymSrv to assign a different index value to the new file than to the old file, preventing new file from properly replacing the old one.

For the complete command line syntax, see [**PDBCopy Command-Line Options**](pdbcopy-command-line-options.md).

 

 





