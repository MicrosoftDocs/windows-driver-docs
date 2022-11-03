---
title: Microsoft public symbol server
description: The Microsoft symbol server makes Windows debugger symbols publicly available.
keywords: ["SymSrv, public Microsoft symbols", "symbol servers, public Microsoft symbols", "public symbol store", "Microsoft symbol store"]
ms.date: 11/02/2022
---

# Microsoft public symbol server


**Server Status:** No known issues :white_check_mark: <br> 
The Microsoft public symbol server is fully operational. <br>
Please report any known issues to [windbgfb@microsoft.com](mailto:windbgfb@microsoft.com). 

---

The Microsoft symbol server makes Windows debugger symbols publicly available.

You can refer directly to the public symbol server in your symbol path in the following manner:

```console
set _NT_SYMBOL_PATH=srv*DownstreamStore*https://msdl.microsoft.com/download/symbols
```

*DownstreamStore* must specify a directory on your local computer or network that will be used to cache symbols. This downstream store holds symbols that the debugger has accessed; the vast majority of symbols that have never been accessed remain on the symbol store at Microsoft. This keeps your downstream store relatively small and allows the symbol server to work quickly, only downloading each file once.

To avoid typing this long symbol path, use the [**.symfix (Set Symbol Store Path)**](-symfix--set-symbol-store-path-.md) command. The following command appends the public symbol store to your existing symbol path:

```dbgcmd
.symfix+ C:\MySymbols
```

If local symbol cache location is omitted, the sym subdirectory of the debugger installation directory will be used.

Use the [**.sympath (Set Symbol Store Path)**](-symfix--set-symbol-store-path-.md) command to display the full symbol path. This example shows how to use symfix to create a local symbol cache and use the Microsoft http symbol server.

```dbgcmd
0: kd> .symfix c:\MyCache
0: kd> .sympath
Symbol search path is: srv*
Expanded Symbol search path is: cache*c:\MyCache;SRV*https://msdl.microsoft.com/download/symbols
```

For more information about working with symbols, see the [Symbol path for Windows debuggers](./symbol-path.md).

**Symbol File Compression**

The Microsoft Symbol Server provides compressed versions of the symbol files. The files have an underscore at the end of the filename’s extension to indicate that they are compressed. For example, the PDB for ntdll.dll is available as ntdll.pd\_. When SymProxy downloads a compressed file, it will store the file decompressed in the local file system. The DontUncompress registry key can be set to disable this behavior in SymProxy.


**Microsoft License Terms - Microsoft Symbol Server**

Microsoft makes certain symbols, binary code and other executables available via the Microsoft Symbol Server for use in debugging and testing of the user’s software in connection with Microsoft software, and not for any unauthorized use.  Please refer to the [Microsoft License Terms - Microsoft Symbol Server](/legal/windows-sdk/microsoft-symbol-server-license-terms).
