---
title: Additional DBH Examples
description: Additional DBH Examples
ms.assetid: 6db23b6b-e5da-4ea3-9f0a-ab42c0e712d7
keywords: ["DBH, displaying symbols", "DBH, symbol decorations", "DBH, data types", "DBH, imaginary symbols"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Additional DBH Examples


Here are additional examples of commands that can be issued at the DBH prompt.

### <span id="displaying_private_symbols_and_public_symbols"></span><span id="DISPLAYING_PRIVATE_SYMBOLS_AND_PUBLIC_SYMBOLS"></span>Displaying Private Symbols and Public Symbols

If the target is a full symbol file, then each public symbol appears twice in the file: in the public symbol table, and in the private symbol data. The copy in the public symbol table often contains various decorations (prefixes and suffixes). For details, see [Public and Private Symbols](public-and-private-symbols.md).

DBH can display information about this symbol from the private symbol data, from the public symbol table without decorations, and from the public symbol table with decorations. Here is an example in which all three of these are displayed, using the command **addr 414fe0** each time.

The first time this command appears in this example, DBH uses the default symbol options, so the resulting information comes from the private symbol data. Note that this information includes the address, size, and data type of the function **fgets**. Then, the command symopt +4000 is used, which turns on the SYMOPT\_PUBLICS\_ONLY option. This causes DBH to ignore the private symbol data, and therefore when the **addr 414fe0** command is run the second time, DBH uses the public symbol table, and no size or data type information is shown for the function **fgets**. Finally, the command symopt -2 is used, turning off the SYMOPT\_UNDNAME option and causing DBH to include decorations. When the **addr 414fe0** runs this final time, it shows the decorated version of the function name, **\_fgets**.

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

If the -d command-line option had been used, the results would have shown the decorated public name from the beginning.

### <span id="determining_the_decorations_of_a_specific_symbol"></span><span id="DETERMINING_THE_DECORATIONS_OF_A_SPECIFIC_SYMBOL"></span>Determining the Decorations of a Specific Symbol

DBH can determine the decorations on a specific symbol. This can be useful when used in conjunction with a program that requires symbols to be specified with their decorations, such as [PDBCopy](pdbcopy.md).

For example, suppose you know that the symbol file mysymbols.pdb contains a symbol whose undecorated name is **MyFunction1**. To find the decorated name, use the following procedure.

First, start DBH without the -d command-line option, and then use the symopt +4000 command so that all information comes from the public symbol table:

```console
C:\> dbh c:\mydir\mysymbols.pdb

mysymbols [1000000]: symopt +4000

Symbol Options: 0x10c13
Symbol Options: 0x14c13 
```

Next, use the **name** command or the **enum** command to display the address of the desired symbol:

```dbgcmd
mysymbols [1000000]: enum myfunction1 

 index            address     name
   2ab            102cb4e :   MyFunction1
```

Now use symopt -2 to make symbol decorations visible, and then use the **addr** command with the address of this symbol:

```dbgcmd
mysymbols [1000000]: symopt -2

Symbol Options: 0x14c13
Symbol Options: 0x14c11

mysymbols [1000000]: addr 102cb4e

_MyFunction1@4
   name : _InterlockedIncrement@4
   addr :  102cb4e
   size : 0
  flags : 0
   type : 0
modbase :  1000000
  value :        0
    reg : 0
  scope : SymTagNull (0)
    tag : SymTagPublicSymbol (a)
  index : 2ab  
```

This reveals that the decorated name of the symbol is **\_MyFunction1@4**.

### <span id="decoding_symbol_decorations"></span><span id="DECODING_SYMBOL_DECORATIONS"></span>Decoding Symbol Decorations

The **undec** command can be used to reveal the meaning of C++ symbol decorations. In the following example, the decorations attached to ??\_C@\_03GGCAPAJC@Sep?$AA@ are decoded to indicate that it is a string:

```dbgcmd
dbh: undec ??_C@_03GGCAPAJC@Sep?$AA@

??_C@_03GGCAPAJC@Sep?$AA@ =
`string' 
```

The following examples decode the decorations attached to three function names, revealing their prototypes:

```dbgcmd
dbh: undec ?gcontext@@3_KA

?gcontext@@3_KA =
unsigned __int64 gcontext


dbh: undec ?pathcpy@@YGXPAGPBG1K@Z

?pathcpy@@YGXPAGPBG1K@Z =
void __stdcall pathcpy(unsigned short *,unsigned short const *,unsigned short const *,unsigned long)


dbh: undec ?_set_new_handler@@YAP6AHI@ZP6AHI@Z@Z

?_set_new_handler@@YAP6AHI@ZP6AHI@Z@Z =
int (__cdecl*__cdecl _set_new_handler(int (__cdecl*)(unsigned int)))(unsigned int) 
```

The **undec** command does not display information about initial underscores, the prefix **\_\_imp\_**, or trailing "**@**<em>address</em>" decorations, which are commonly found attached to function names.

You can use the **undec** command with any string, not just the name of a symbol in the currently loaded module.

### <span id="sorting_a_list_of_symbols_by_address"></span><span id="SORTING_A_LIST_OF_SYMBOLS_BY_ADDRESS"></span>Sorting a List of Symbols by Address

If you simply want a list of symbols, sorted in address order, you can run DBH in batch mode and pipe the results to a **sort** command. The address values typically begin in the 18th column of each line, so the following command sorts the results by address:

```dbgcmd
dbh -p:4672 enum mymodule!* | sort /+18
```

### <span id="displaying_source_line_information"></span><span id="DISPLAYING_SOURCE_LINE_INFORMATION"></span>Displaying Source Line Information

When you use a full symbol file, DBH can display source line information. This does not require access to any source files, since this information is stored in the symbol files themselves.

Here, the **line** command displays the hexadecimal address of the binary instructions corresponding to the specified source line, and it displays the symbols associated with that line. (In this example, there are no symbols associated with the line.)

```dbgcmd
dbh [1000000]: line myprogram.cpp#767

   file : e:\mydirectory\src\myprogram.cpp
   line : 767
   addr :  1006191
    key : 0000000000000000
disp : 0
```

Here, the **srclines** command displays the object files associated with the specified source line:

```dbgcmd
dbh [1000000]: srclines myprogram.cpp 767

0x1006191: e:\mydirectory\objchk\amd64\myprogram.obj
line 767 e:\mydirectory\src\myprogram.cpp
```

Note that the output of **srclines** is similar to that of the [**ln (List Nearest Symbols)**](ln--list-nearest-symbols-.md) debugger command.

### <span id="displaying_a_data_type"></span><span id="DISPLAYING_A_DATA_TYPE"></span>Displaying a Data Type

The **type** command can be used to display information about a data type. Here it displays data about the CMDPROC type:

```dbgcmd
dbh [1000000]: type CMDPROC

   name : CMDPROC
   addr :        0
   size : 8
  flags : 0
   type : c
modbase :  1000000
  value :        0
    reg : 0
  scope : SymTagNull (0)
    tag : SymTagTypedef (11)
  index : c
```

The value listed after "tag" specifies the nature of this data type. In this case, **SymTagTypedef** indicates that this type was defined using a **typedef** statement.

### <span id="using_imaginary_symbols"></span><span id="USING_IMAGINARY_SYMBOLS"></span>Using Imaginary Symbols

The **add** command can add an imaginary symbol to the loaded module. The actual symbol file is not altered; only the image of that file in DBH's memory is changed.

The **add** command can be useful if you wish to temporarily override which symbols are associated with a given address range. In the following example, a portion of the address range associated with **MyModule!main** is overridden by the imaginary symbol **MyModule!magic**.

Here is how the module appears before the imaginary symbol is added. Note that the **main** function begins at 0x0042CC56, and has size 0x42B. So when the **addr** command is used with the address 0x0042CD10, it recognizes this address as lying within the boundaries of the **main** function:

```dbgcmd
pid:6040 mod:MyModule[400000]: enum timetest!ma*

 index            address     name
     1             42cc56 :   main
     3             415810 :   malloc
     5             415450 :   mainCRTStartup

pid:6040 mod:MyModule[400000]: addr 42cc56

main
   name : main
   addr :   42cc56
   size : 42b
  flags : 0
   type : 2
modbase :   400000
  value :        0
    reg : 0
  scope : SymTagNull (0)
    tag : SymTagFunction (5)
  index : 1

pid:6040 mod:MyModule[400000]: addr 42cd10

main+ba
   name : main
   addr :   42cc56
   size : 42b
  flags : 0
   type : 2
modbase :   400000
  value :        0
    reg : 0
  scope : SymTagNull (0)
    tag : SymTagFunction (5)
  index : 1 
```

Now the symbol **magic** is added at the address 0x0042CD00, with size 0x10 bytes. When the **enum** command is used, the high bit in the index is set, showing that this is an imaginary symbol:

```dbgcmd
pid:6040 mod:MyModule[400000]: add magic 42cd00 10


pid:6040 mod:MyModule[400000]: enum timetest!ma*

 index            address     name
     1             42cc56 :   main
     3             415810 :   malloc
     5             415450 :   mainCRTStartup
  80000001             42cd00 :   magic 
```

When the **addr** command is used, it looks for any symbols whose ranges include the specified address. Since this search begins with the specified address and runs backward, the address 0x004CD10 is now associated with **magic**. On the other hand, the address 0x004CD40 is still associated with **main**, because it lies outside the range of the **magic** symbol. Note also that the tag **SymTagCustom** indicates an imaginary symbol:

```dbgcmd
pid:6040 mod:MyModule[400000]: addr 42cd10

magic+10
   name : magic
   addr :   42cd00
   size : 10
  flags : 1000
   type : 0
modbase :   400000
  value :        0
    reg : 0
  scope : SymTagNull (0)
    tag : SymTagCustom (1a)
  index : 80000001

pid:6040 mod:MyModule[400000]: addr 42cd40

main+ea
   name : main
   addr :   42cc56
   size : 42b
  flags : 0
   type : 2
modbase :   400000
  value :        0
    reg : 0
  scope : SymTagNull (0)
    tag : SymTagFunction (5)
  index : 1 
```

Finally, the **del** command can delete the symbol **magic**, returning all the symbols to their original ranges:

```dbgcmd
pid:6040 mod:MyModule[400000]: del magic


pid:6040 mod:MyModule[400000]: enum timetest!ma*

 index            address     name
     1             42cc56 :   main
     3             415810 :   malloc
     5             415450 :   mainCRTStartup 
```









