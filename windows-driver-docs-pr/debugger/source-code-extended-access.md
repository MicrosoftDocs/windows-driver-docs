---
title: Source Code Extended Access
description: Learn more about Source Code Extended Access
ms.assetid: 7a81a0b2-5472-453c-8aca-bf2cfd7386e1
keywords: ["SourceLink, DebugInfoD, debugging"]
ms.date: 04/27/2021
---

# Source Code Extended Access

Starting WinDbg version 1.2104, the source path command ([.srcpath, .lsrcpath (Set Source Path)](-srcpath---lsrcpath--set-source-path-.md)) supports file retrieval from [DebugInfoD servers](https://sourceware.org/elfutils/Debuginfod.html) through the `DebugInfoD*` tag.

The `DebugInfoD*` tag can point to one or more DebugInfoD servers with each server URL formatted as `https://domain.com` and separated by `*`. The servers will be searched in the same order as listed in the source path and the files will be retrieved from the first matching URL.

The `DebugInfoD*` tag can be combined with `srv*` to prioritize source retrieval from specific locations. 

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

The `srv*` tag supports automatice file retrieval using Source Link 1.0 or Source Link 2.0, it does not support *DebugInfoD* URLs.

## Resources

[.srcpath, .lsrcpath (Set Source Path)](-srcpath---lsrcpath--set-source-path-.md)

[Source Path](source-path.md)

[Using a Source Server](using-a-source-server.md)

[Source Link](/dotnet/standard/library-guidance/sourcelink)

[ELFUTILS DEBUGINFOD](https://sourceware.org/elfutils/Debuginfod.html)
