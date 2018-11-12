---
title: Public and Private Symbols
description: Public and Private Symbols
ms.assetid: 61ed583d-8b97-4929-8d86-1a6353c13304
keywords: ["symbols, public", "symbols, private", "public symbols", "private symbols", "retail symbols", "export symbols", "symbol file, full symbol file", "symbol file, stripped symbol file", "full symbol file"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Public and Private Symbols


When a full-sized .pdb or .dbg symbol file is built by a linker, it contains two distinct collections of information: the *private symbol data* and a *public symbol table*. These collections differ in the list of items they contain and the information they store about each item.

The private symbol data includes the following items:

-   Functions

-   Global variables

-   Local variables

-   Information about user-defined structures, classes, and data types

-   The name of the source file and the line number in that file corresponding to each binary instruction

The public symbol table contains fewer items:

-   Functions (except for functions declared **static**)

-   Global variables specified as **extern** (and any other global variables visible across multiple object files)

As a general rule, the public symbol table contains exactly those items that are accessible from one source file to another. Items visible in only one object file--such as **static** functions, variables that are global only within a single source file, and local variables--are not included in the public symbol table.

These two collections of data also differ in what information they include for each item. The following information is typically included for each item contained in the private symbol data:

-   Name of the item

-   Address of the item in virtual memory

-   Frame pointer omission (FPO) records for each function

-   Data type of each variable, structure, and function

-   Types and names of the parameters for each function

-   Scope of each local variable

-   Symbols associated with each line in each source file

On the other hand, the public symbol table stores only the following information about each item included in it:

-   The name of the item.

-   The address of the item in the virtual memory space of its module. For a function, this is the address of its entry point.

-   Frame pointer omission (FPO) records for each function.

In other words, the public symbol data can be thought of as a subset of the private symbol data in two ways: it contains a shorter list of items, and it also contains less information about each item. For example, the public symbol data does not include local variables at all. Each local variable is included only in the private symbol data, with its address, data type, and scope. Functions, on the other hand, are included both in the private symbol data and public symbol table, but while the private symbol data includes the function name, address, FPO records, input parameter names and types, and output type, the public symbol table includes just the function name, address, and FPO record.

There is one other difference between the private symbol data and the public symbol table. Many of the items in the public symbol table have names that are *decorated* with a prefix, a suffix, or both. These decorations are added by the C compiler, the C++ compiler, and the MASM assembler. Typical prefixes include a series of underscores or the string **\_\_imp\_** (designating an imported function). Typical suffixes include one or more at signs ( **@** ) followed by addresses or other identifying strings. These decorations are used by the linker to disambiguate the symbol, since it is possible that function names or global variable names could be repeated across different modules. These decorations are an exception to the general rule that the public symbol table is a subset of the private symbol data.

### <span id="full_symbol_files_and_stripped_symbol_files"></span><span id="FULL_SYMBOL_FILES_AND_STRIPPED_SYMBOL_FILES"></span>Full Symbol Files and Stripped Symbol Files

A *full symbol file* contains both the private symbol data and the public symbol table. This kind of file is sometimes referred to as a *private symbol file*, but this name is misleading, for such a file contains both private and public symbols.

A *stripped symbol file* is a smaller file that contains only the public symbol table - or, in some cases, only a subset of the public symbol table. This file is sometimes referred to as a *public symbol file*.

### <span id="creating_full_and_stripped_symbol_files"></span><span id="CREATING_FULL_AND_STRIPPED_SYMBOL_FILES"></span>Creating Full and Stripped Symbol Files

If you build your binaries with Visual Studio, you can create either full or stripped symbol files. When building a "debug build" of a binary, Visual Studio typically will create full symbol files. When building a "retail build", Visual Studio typically creates no symbol files, but a full or stripped symbol file will be created if the proper options are set.

If you build your binaries with the Build utility, the utility will create full symbol files.

Using the BinPlace tool, you can create a stripped symbol file from a full symbol file. When the most common BinPlace options are used (**-a -x -s -n**), the stripped symbol files are placed in the directory that is listed after the **-s** switch, and the full symbol files are placed in the directory that is listed after the **-n** switch. When BinPlace strips a symbol file, the stripped and full versions of the file are given identical signatures and other identifying information. This allows you to use either version for debugging.

Using the PDBCopy tool, you can create a stripped symbol file from a full symbol file by removing the private symbol data. PDBCopy can also remove a specified subset of the public symbol table. For details, see [PDBCopy](pdbcopy.md).

Using the SymChk tool, you can determine whether a symbol file contains private symbols. For details, see [SymChk](symchk.md).

### <span id="viewing_public_and_private_symbols_in_the_debugger"></span><span id="VIEWING_PUBLIC_AND_PRIVATE_SYMBOLS_IN_THE_DEBUGGER"></span>Viewing Public and Private Symbols in the Debugger

You can use WinDbg, KD, or CDB to view symbols. When one of these debuggers has access to a full symbol file, it has both the information listed in the private symbol data and the information listed in the public symbol table. The private symbol data is more detailed, while the public symbol data contains symbol decorations.

When accessing private symbols, private symbol data is always used because these symbols are not included in the public symbol table. These symbols are never decorated.

When accessing public symbols, the debugger's behavior depends on certain [symbol options](symbol-options.md):

-   When the [SYMOPT\_UNDNAME](symbol-options.md#symopt-undname) option is on, decorations are not included when the name of a public symbol is displayed. Moreover, when searching for symbols, decorations are ignored. When this option is off, decorations are displayed when displaying public symbols, and decorations are used in searches. Private symbols are never decorated in any circumstances. This option is on by default in all debuggers.

-   When the [SYMOPT\_PUBLICS\_ONLY](symbol-options.md#symopt-publics-only) option is on, private symbol data is ignored, and only the public symbol table is used. This option is off by default in all debuggers.

-   When the [SYMOPT\_NO\_PUBLICS](symbol-options.md#symopt-no-publics) option is on, the public symbol table is ignored, and searches and symbol information use the private symbol data alone. This option is off by default in all debuggers.

-   When the [SYMOPT\_AUTO\_PUBLICS](symbol-options.md#symopt-auto-publics) option is on (and both SYMOPT\_PUBLICS\_ONLY and SYMOPT\_NO\_PUBLICS are off), the first symbol search is performed in the private symbol data. If the desired symbol is found there, the search terminates. If not, the public symbol table is searched. Since the public symbol table contains a subset of the symbols in the private data, normally this results in the public symbol table being ignored.

-   When the SYMOPT\_PUBLICS\_ONLY, SYMOPT\_NO\_PUBLICS, and SYMOPT\_AUTO\_PUBLICS options are all off, both private symbol data and the public symbol table are searched each time a symbol is needed. However, when matches are found in both places, the match in the private symbol data is used. Therefore, the behavior in this instance is the same as when SYMOPT\_AUTO\_PUBLICS is on, except that using SYMOPT\_AUTO\_PUBLICS may cause symbol searches to happen slightly faster.

Here is an example in which the command [**x (Examine Symbols)**](x--examine-symbols-.md) is used three times. The first time, the default symbol options are used, and so the information is taken from the private symbol data. Note that this includes information about the address, size, and data type of the array **typingString**. Next, the command .symopt+ 4000 is used, causing the debugger to ignore the private symbol data. When the **x** command is then run again, the public symbol table is used; this time there is no size and data type information for **typingString**. Finally, the command .symopt- 2 is used, which causes the debugger to include decorations. When the **x** command is run this final time, the decorated version of the function name, **\_typingString**, is shown.

```dbgcmd
0:000> x /t /d *!*typingstring* 
00434420 char [128] TimeTest!typingString = char [128] ""

0:000> .symopt+ 4000

0:000> x /t /d *!*typingstring* 
00434420 <NoType> TimeTest!typingString = <no type information>

0:000> .symopt- 2

0:000> x /t /d *!*typingstring* 
00434420 <NoType> TimeTest!_typingString = <no type information> 
```

### <span id="viewing_public_and_private_symbols_with_the_dbh_tool"></span><span id="VIEWING_PUBLIC_AND_PRIVATE_SYMBOLS_WITH_THE_DBH_TOOL"></span>Viewing Public and Private Symbols with the DBH Tool

Another way to view symbols is by using the [the DBH tool](dbh.md). DBH uses the same symbol options as the debugger. Like the debugger, DBH leaves [SYMOPT\_PUBLICS\_ONLY](symbol-options.md#symopt-publics-only) and [SYMOPT\_NO\_PUBLICS](symbol-options.md#symopt-no-publics) off by default, and turns [SYMOPT\_UNDNAME](symbol-options.md#symopt-undname) and [SYMOPT\_AUTO\_PUBLICS](symbol-options.md#symopt-auto-publics) on by default. These defaults can be overridden by a command-line option or by a DBH command.

Here is an example in which the DBH command **addr 414fe0** is used three times. The first time, the default symbol options are used, and so the information is taken from the private symbol data. Note that this includes information about the address, size, and data type of the function **fgets**. Next, the command symopt +4000 is used, which causes DBH to ignore the private symbol data. When the **addr 414fe0** is then run again, the public symbol table is used; this time there is no size and data type information for the function **fgets**. Finally, the command symopt -2 is used, which causes DBH to include decorations. When the **addr 414fe0** is run this final time, the decorated version of the function name, **\_fgets**, is shown.

```dbgcmd
pid:4308 mod:TimeTest[400000]: addr 414fe0

fgets
   name : fgets
   addr :   414fe0
   size : 113
  flags : 0
   type : 7e
modbase :   400000
  value :        0
    reg : 0
  scope : SymTagNull (0)
    tag : SymTagFunction (5)
  index : 7d

pid:4308 mod:TimeTest[400000]: symopt +4000

Symbol Options: 0x10c13
Symbol Options: 0x14c13

pid:4308 mod:TimeTest[400000]: addr 414fe0

fgets
   name : fgets
   addr :   414fe0
   size : 0
  flags : 0
   type : 0
modbase :   400000
  value :        0
    reg : 0
  scope : SymTagNull (0)
    tag : SymTagPublicSymbol (a)
  index : 7f

pid:4308 mod:TimeTest[400000]: symopt -2

Symbol Options: 0x14c13
Symbol Options: 0x14c11

pid:4308 mod:TimeTest[400000]: addr 414fe0

_fgets
   name : _fgets
   addr :   414fe0
   size : 0
  flags : 0
   type : 0
modbase :   400000
  value :        0
    reg : 0
  scope : SymTagNull (0)
    tag : SymTagPublicSymbol (a)
  index : 7f 
```

 

 





