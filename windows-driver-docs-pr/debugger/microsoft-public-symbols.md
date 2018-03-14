---
title: Microsoft public symbol server
description: The Microsoft symbol server makes Windows debugger symbols publicly available.
ms.assetid: b0d38104-c386-4d20-8d9c-7701347c1643
keywords: ["SymSrv, public Microsoft symbols", "symbol servers, public Microsoft symbols", "public symbol store", "Microsoft symbol store"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Microsoft public symbol server


The Microsoft symbol server makes Windows debugger symbols publicly available.

You can refer directly to the public symbol server in your symbol path in the following manner:

```
set _NT_SYMBOL_PATH=srv*DownstreamStore*https://msdl.microsoft.com/download/symbols
```

*DownstreamStore* must specify a directory on your local computer or network that will be used to cache symbols. This downstream store holds symbols that the debugger has accessed; the vast majority of symbols that have never been accessed remain on the symbol store at Microsoft. This keeps your downstream store relatively small and allows the symbol server to work quickly, only downloading each file once.

To avoid typing this long symbol path, use the [**.symfix (Set Symbol Store Path)**](-symfix--set-symbol-store-path-.md) command. The following command appends the public symbol store to your existing symbol path:

```
.symfix+ DownstreamStore 
```

**Note**   To successfully access Microsoft's public symbol store, you will need a fast internet connection. If your internet connection is only 56 Kbps or slower, you should install Windows symbols directly onto your hard drive. For details, see [Installing Windows Symbol Files](installing-windows-symbol-files.md).

 

For more information about the public symbol store, see the [Windows Symbols](http://go.microsoft.com/fwlink/p/?linkid=17363) Web site.

**Symbol File Compression**

The Microsoft Symbol Server provides compressed versions of the symbol files. The files have an underscore at the end of the filename’s extension to indicate that they are compressed. For example, the PDB for ntdll.dll is available as ntdll.pd\_. When SymProxy downloads a compressed file, it will store the file decompressed in the local file system. The DontUncompress registry key can be set to disable this behavior in SymProxy.

Refer to the Debugger topic [SymStore](symstore.md) for information on using SymStore.exe /compress to store your own symbols compressed on your symbol server.

 

 





