---
title: Microsoft public symbol server
description: The Microsoft symbol server makes Windows debugger symbols publicly available.
ms.assetid: b0d38104-c386-4d20-8d9c-7701347c1643
keywords: ["SymSrv, public Microsoft symbols", "symbol servers, public Microsoft symbols", "public symbol store", "Microsoft symbol store"]
---

# Microsoft public symbol server


The Microsoft symbol server makes Windows debugger symbols publicly available.

You can refer directly to the public symbol server in your symbol path in the following manner:

``` syntax
set _NT_SYMBOL_PATH=srv*DownstreamStore*https://msdl.microsoft.com/download/symbols
```

*DownstreamStore* must specify a directory on your local computer or network that will be used to cache symbols. This downstream store holds symbols that the debugger has accessed; the vast majority of symbols that have never been accessed remain on the symbol store at Microsoft. This keeps your downstream store relatively small and allows the symbol server to work quickly, only downloading each file once.

To avoid typing this long symbol path, use the [**.symfix (Set Symbol Store Path)**](https://msdn.microsoft.com/library/windows/hardware/ff565400) command. The following command appends the public symbol store to your existing symbol path:

``` syntax
.symfix+ DownstreamStore 
```

**Note**   To successfully access Microsoft's public symbol store, you will need a fast internet connection. If your internet connection is only 56 Kbps or slower, you should install Windows symbols directly onto your hard drive. For details, see [Installing Windows Symbol Files](installing-windows-symbol-files.md).

 

For more information about the public symbol store, see the [Windows Symbols](http://go.microsoft.com/fwlink/p/?linkid=17363) Web site.

**Symbol File Compression**

The Microsoft Symbol Server provides compressed versions of the symbol files. The files have an underscore at the end of the filename’s extension to indicate that they are compressed. For example, the PDB for ntdll.dll is available as ntdll.pd\_. When SymProxy downloads a compressed file, it will store the file decompressed in the local file system. The DontUncompress registry key can be set to disable this behavior in SymProxy.

Refer to the Debugger topic [SymStore](symstore.md) for information on using SymStore.exe /compress to store your own symbols compressed on your symbol server.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Microsoft%20public%20symbol%20server%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




