---
title: Symbol Store Folder Tree
description: The symbol store backing SMB and HTTP requests is a folder tree residing on a local disk.
ms.assetid: AB23A180-71C3-4EBE-A3DE-765D264EF130
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Symbol Store Folder Tree


The symbol store backing SMB and HTTP requests is a folder tree residing on a local disk.

To keep administration simple, the sub-folder name (e.g. Symbols) can also be used as the File Share name and also the Virtual Directory name. If a new symbol store was to be added, a new sub-folder would be made under D:\\SymStore, and a new File Share and Virtual Directory of that name would be made to expose the store to clients.

The folder tree’s location should be chosen carefully as well as the disk’s file system. The symbol store can get extremely big (terabytes) when caching files from (internal) build servers and the Internet. The folder tree should reside on a disk that is capable of a high number of reads and low number of writes. The file system can affect performance - ReFS may perform better than NTFS and should be investigated for large deployments. Equally, the networking to the server should be of sufficient speed to handle the load from the clients and also the load to the upstream symbol stores to retrieve the symbols for cache population.

## <span id="Symbol_Store_Single-Tier_or_Two-Tier_Structure"></span><span id="symbol_store_single-tier_or_two-tier_structure"></span><span id="SYMBOL_STORE_SINGLE-TIER_OR_TWO-TIER_STRUCTURE"></span>Symbol Store Single-Tier or Two-Tier Structure


Normally files are placed in a single tier directory structure in which a single subdirectory exists for each filename cached. Under each filename folder, additional folders are made to store each version of the file. The tree will have this structure:

```console
D:\SymStore\Symbols\ntdll.dll\...\
D:\SymStore\Symbols\ntdll.pdb\...\
D:\SymStore\Symbols\kernel32.dll\...\
D:\SymStore\Symbols\kernel32.pdb\...\
```

If a large number of files are to be stored, a two-tier structure can be used at the root of the symbol store. The first 2 letters of the filename are used as an intermediate folder name.

To use a two-tier structure, place a file called index2.txt in the root of D:\\SymStore\\Symbols. The content of the file is of no importance. When this file exists, symsrv.dll will create and consume files from the two-tier tree using this structure:

```console
D:\SymStore\Symbols\nt\ntdll.dll\...\
D:\SymStore\Symbols\nt\ntdll.pdb\...\
D:\SymStore\Symbols\ke\kernel32.dll\...\
D:\SymStore\Symbols\ke\kernel32.pdb\...\
```

If you want to convert the structure after the symbol store is populated, use the convertstore.exe application in the debugger folder. To allow the tool to work, create a folder called 000Admin in the root folder. This folder is required by convertstore.exe so that it can control the locking of the symbol store.

## <span id="related_topics"></span>Related topics


[HTTP Symbol Stores](http-symbol-stores.md)

[File Share (SMB) Symbol Server](file-share--smb--symbol-server.md)

 

 






