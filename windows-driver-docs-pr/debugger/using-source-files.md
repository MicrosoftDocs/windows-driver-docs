---
title: Using Source Files
description: Using Source Files
ms.assetid: c6dfcb37-140f-43d8-aa15-14f0317b5e19
keywords: ["Debugger Engine API, source"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Source Files


The [debugger engine](introduction.md#debugger-engine) maintains a *source path*, which is a list of directories and source servers that contain source code files associated with the current targets. The debugger engine can search these directories and source servers for the source files. With the help of symbol files, the debugger engine can match lines in the source files with locations in the target's memory.

For an overview of using source files with debuggers, see [Debugging in Source Mode](debugging-in-source-mode.md). For an overview of source paths, see [Source Path](source-path.md). For an overview of using source servers from the debugger engine, see [Using a Source Server](using-a-source-server.md).

### <span id="source_path"></span><span id="SOURCE_PATH"></span>Source Path

To add a directory or source server to the source path, use the method [**AppendSourcePath**](https://msdn.microsoft.com/library/windows/hardware/ff538102). The whole source path is returned by [**GetSourcePath**](https://msdn.microsoft.com/library/windows/hardware/ff548358) and can be changed using [**SetSourcePath**](https://msdn.microsoft.com/library/windows/hardware/ff556781). A single directory or source server can be retrieved from the source path using [**GetSourcePathElement**](https://msdn.microsoft.com/library/windows/hardware/ff548367).

To find a source file relative to the source path, use [**FindSourceFile**](https://msdn.microsoft.com/library/windows/hardware/ff545423) or, for more advanced options when using source servers, use [**FindSourceFileAndToken**](https://msdn.microsoft.com/library/windows/hardware/ff545430). **FindSourceFileAndToken** can also be used along with [**GetSourceFileInformation**](https://msdn.microsoft.com/library/windows/hardware/ff548321) to retrieve variables related to a file on a source server.

### <span id="matching_source_files_to_code_in_memory"></span><span id="MATCHING_SOURCE_FILES_TO_CODE_IN_MEMORY"></span>Matching Source Files to Code in Memory

The debugger engine provides three methods for locating the memory locations that correspond to lines in a source file. To map a single line of source code to a memory location, use [**GetOffsetByLine**](https://msdn.microsoft.com/library/windows/hardware/ff548022). To search for memory locations for more than one source line or for nearby source lines, use [**GetSourceEntriesByLine**](https://msdn.microsoft.com/library/windows/hardware/ff548305). The [**GetSourceFileLineOffsets**](https://msdn.microsoft.com/library/windows/hardware/ff548339) method will return the memory location of every line in a source file.

To perform the opposite operation and find the line of a source file that matches a location in the target's memory, use [**GetLineByOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546995).

**Note**  The relationship between memory locations and lines in a source file is not necessarily one-to-one. It is possible for a single line of source code to correspond to multiple memory locations and for a single memory location to correspond to multiple lines of source code.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20Source%20Files%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




