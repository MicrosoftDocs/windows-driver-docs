---
title: Source Code Extended Access
description: Learn more about Source Code Extended Access
ms.assetid: 7a81a0b2-5472-453c-8aca-bf2cfd7386e1
keywords: ["SourceLink, DebugInfoD, debugging"]
ms.date: 04/27/2021
ms.localizationpriority: medium
---

# Source Code Extended Access

The source path command ([.srcpath, .lsrcpath (Set Source Path)](-srcpath---lsrcpath--set-source-path-.md)) has been updated to include a new tag – *DebugInfoD*, starting with version 1.2104.13002.0 of the WinDbg, released in April 2021.

The *DebugInfoD* tag can contain a single or multiple URLs separated with *. The listed URLs will be searched in the specified order for the source file, and if found, that file will be downloaded from that location.

The *DebugInfoD* tag can be combined with srv* to create URL search priority and the source file will be downloaded from the first available location.

Where the url format is: `https://www.somename.com`.

Some symbol files contain checksum information about the source code. In such cases, the local folders in the source path will be searched first for the file with same file name and matching checksum. If no checksum information is available, or no file with matching name and checksum has been found, then the search path will be traversed in the specified order as shown in the following examples.

In this example the source path can use *DebugInfoD* as shown here, where it follows the srv* tag.

`.srcpath srv*;DebugInfoD*url1*url2…*urlN;o:\src\folder`

In this example, the target source code locations will be searched in the following order:

- srv* (source link version 1 or version 2),
- then debuginfoD urls: url1, url2, … urlN
- lastly the local folder o:\src\folder

In this second example the  *DebugInfoD* tag is used twice.

`.srcpath DebugInfoD*url1;srv*;DebugInfoD*url2;o:\src\folder`

For this second example, the search order will be:

- *DebugInfoD* url1,
- then srv* (source link version 1 or version 2),
- then *DebugInfoD* url2
- lastly the local folder o:\src\folder

## Supported source code formats

The srv* allows native source link version 1 or version 2 files to be downloaded. It does not include *DebugInfoD* files.

## Resources

[.srcpath, .lsrcpath (Set Source Path)](-srcpath---lsrcpath--set-source-path-.md)

[Source Path](source-path.md)

[Using a Source Server](using-a-source-server.md)

[Source Link](/dotnet/standard/library-guidance/sourcelink)

[ELFUTILS DEBUGINFOD](https://sourceware.org/elfutils/Debuginfod.html)