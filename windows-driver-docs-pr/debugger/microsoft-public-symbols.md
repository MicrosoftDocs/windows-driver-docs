---
title: Microsoft Public Symbol Server
description: Learn about the Microsoft symbol server, which makes Windows debugger symbols publicly available.
keywords: ["SymSrv, public Microsoft symbols", "symbol servers, public Microsoft symbols", "public symbol store", "Microsoft symbol store"]
ms.date: 12/21/2023
---

# Microsoft public symbol server

**Server Status:** No known issues :white_check_mark:  
The Microsoft public symbol server is fully operational.

Report any known issues to [windbgfb@microsoft.com](mailto:windbgfb@microsoft.com).

---

The Microsoft symbol server makes Windows debugger symbols publicly available.

You can refer directly to the public symbol server in your symbol path in a number of different ways, described in [Symbol path for Windows debuggers](symbol-path.md). For example to set the _NT_SYMBOL_PATH environment value, use this command.

```console
set _NT_SYMBOL_PATH=srv*DownstreamStore*https://msdl.microsoft.com/download/symbols
```

*DownstreamStore* must specify a directory on your local computer or network that will be used to cache symbols. This downstream store holds symbols that the debugger has accessed. Most symbols that have never been accessed remain on the symbol store at Microsoft. This storage process keeps your downstream store relatively small and allows the symbol server to work quickly, only downloading each file once.

To avoid typing this long symbol path, use the [.symfix (Set symbol store path)](../debuggercmds/-symfix--set-symbol-store-path-.md) command. The following command appends the public symbol store to your existing symbol path:

```dbgcmd
.symfix+ C:\MySymbols
```

If local symbol cache location is omitted, the sym subdirectory of the debugger installation directory is used.

Use the [.sympath (Set symbol store path)](../debuggercmds/-symfix--set-symbol-store-path-.md) command to display the full symbol path. The following example shows how to use symfix to create a local symbol cache and use the Microsoft http symbol server.

```dbgcmd
0: kd> .symfix c:\MyCache
0: kd> .sympath
Symbol search path is: srv*
Expanded Symbol search path is: cache*c:\MyCache;SRV*https://msdl.microsoft.com/download/symbols
```

For more information about working with symbols, see [Using a Symbol Server](using-a-symbol-server.md) and [Symbol path for Windows debuggers](./symbol-path.md).

## Symbol file compression

The Microsoft symbol server provides compressed versions of the symbol files. The files have an underscore at the end of the filename’s extension to indicate that they're compressed. For example, the PDB for **ntdll.dll** is available as **ntdll.pd_**. When SymProxy downloads a compressed file, it stores the file decompressed in the local file system. The `DontUncompress` registry key can be set to disable this behavior in SymProxy.

## Microsoft license terms - Microsoft symbol server

Microsoft makes certain symbols, binary code, and other executables available via the Microsoft symbol server. These resources are used in debugging and testing of the user’s software with Microsoft software. They aren't intended for unauthorized use. Refer to the [Microsoft license terms - Microsoft symbol server](/legal/windows-sdk/microsoft-symbol-server-license-terms).

See also

[Symbol path for Windows debuggers](symbol-path.md)

[Symbols and Symbol Files](symbols-and-symbol-files.md)

[.symfix (Set symbol store path)](../debuggercmds/-symfix--set-symbol-store-path-.md)
