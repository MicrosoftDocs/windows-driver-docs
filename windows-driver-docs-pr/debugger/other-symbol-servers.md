---
title: Other Symbol Servers
description: Other Symbol Servers
keywords: ["symbol servers, writing your own symbol server"]
ms.date: 12/27/2022
---

# Other Symbol Server DLLs

If you wish to use a different method for your symbol search, you can provide your own symbol server DLL rather than using SymSrv.

### Setting the Symbol Path

When implementing a symbol server other than SymSrv, the debugger's symbol path is set in the same way as with SymSrv. See [Microsoft Public Symbols](microsoft-public-symbols.md) and [Advanced SymSrv Use](advanced-symsrv-use.md) for an explanation of the symbol path syntax. The only change you need to make is to replace the string **symsrv.dll** with the name of your own symbol server DLL.

If you wish, you are free to use a different syntax within the parameters to indicate the use of different technologies such as UNC paths, SQL database identifiers, or Internet specifications.

### Implementing Your Own Symbol Server

One approach is to use code that communicates with DbgHelp to find the symbols. Every time DbgHelp requires symbols for a newly loaded module, it calls the symbol server to locate the appropriate symbol files. The symbol server locates each file according to unique parameters such as the time stamp or image size. The server returns a validated path to the requested file. 

You must not change the actual symbol file name returned by your symbol server. DbgHelp stores the name of a symbol file in multiple locations. Therefore, the server must return a file of the same name as that specified when the symbol was requested. This restriction is needed to assure that the symbol names displayed during symbol loading are the ones that the programmer will recognize.

### Restrictions on Multiple Symbol Servers

DbgHelp supports the use of only one symbol server at a time. Your symbol path can contain multiple instances of the same symbol server DLL, but not two different symbol server DLLs. This is not much of a restriction, since you are still free to include multiple instances of a symbol server in your symbol path, each pointing to a different symbol store. But if you want to switch between two different symbol server DLLs, you will have to change the symbol path each time.

### Installing Your Custom Symbol Server DLL

The details of your symbol server installation will depend on your situation. You might wish to set up an installation process that copies your symbol server DLL and sets the \_NT\_SYMBOL\_PATH environment variable automatically.

Depending on the technology used in your server, you may also need to install or access the symbol data itself.

### The Portable PDB (Program Database) 

The Portable PDB (Program Database) format describes an encoding of debugging information produced by compilers of Common Language Infrastructure (CLI) languages and consumed by debuggers and other tools. The format is based on the ECMA-335 Partition II metadata standard. It supports operation on different operating systems and platforms. For more information, see [Portable PDB Symbols](symbols-portable-pdb.md).

### Custom Symbol Stores and Symbol Servers

For information about creating custom symbol servers, see [Custom Symbol Stores and Symbol Servers](symbol-stores-and-symbol-servers.md).
 
 





