---
title: Symbol Store Folder Tree
description: The symbol store backing SMB and HTTP requests is a folder tree residing on a local disk.
ms.assetid: AB23A180-71C3-4EBE-A3DE-765D264EF130
---

# Symbol Store Folder Tree


The symbol store backing SMB and HTTP requests is a folder tree residing on a local disk.

To keep administration simple, the sub-folder name (e.g. Symbols) can also be used as the File Share name and also the Virtual Directory name. If a new symbol store was to be added, a new sub-folder would be made under D:\\SymStore, and a new File Share and Virtual Directory of that name would be made to expose the store to clients.

The folder tree’s location should be chosen carefully as well as the disk’s file system. The symbol store can get extremely big (terabytes) when caching files from (internal) build servers and the Internet. The folder tree should reside on a disk that is capable of a high number of reads and low number of writes. The file system can affect performance - ReFS may perform better than NTFS and should be investigated for large deployments. Equally, the networking to the server should be of sufficient speed to handle the load from the clients and also the load to the upstream symbol stores to retrieve the symbols for cache population.

## <span id="Symbol_Store_Single-Tier_or_Two-Tier_Structure"></span><span id="symbol_store_single-tier_or_two-tier_structure"></span><span id="SYMBOL_STORE_SINGLE-TIER_OR_TWO-TIER_STRUCTURE"></span>Symbol Store Single-Tier or Two-Tier Structure


Normally files are placed in a single tier directory structure in which a single subdirectory exists for each filename cached. Under each filename folder, additional folders are made to store each version of the file. The tree will have this structure:

```
D:\SymStore\Symbols\ntdll.dll\...\
D:\SymStore\Symbols\ntdll.pdb\...\
D:\SymStore\Symbols\kernel32.dll\...\
D:\SymStore\Symbols\kernel32.pdb\...\
```

If a large number of files are to be stored, a two-tier structure can be used at the root of the symbol store. The first 2 letters of the filename are used as an intermediate folder name.

To use a two-tier structure, place a file called index2.txt in the root of D:\\SymStore\\Symbols. The content of the file is of no importance. When this file exists, symsrv.dll will create and consume files from the two-tier tree using this structure:

```
D:\SymStore\Symbols\nt\ntdll.dll\...\
D:\SymStore\Symbols\nt\ntdll.pdb\...\
D:\SymStore\Symbols\ke\kernel32.dll\...\
D:\SymStore\Symbols\ke\kernel32.pdb\...\
```

If you want to convert the structure after the symbol store is populated, use the convertstore.exe application in the debugger folder. To allow the tool to work, create a folder called 000Admin in the root folder. This folder is required by convertstore.exe so that it can control the locking of the symbol store.

## <span id="related_topics"></span>Related topics


[HTTP Symbol Stores](http-symbol-stores.md)

[File Share (SMB) Symbol Server](file-share--smb--symbol-server.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Symbol%20Store%20Folder%20Tree%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





