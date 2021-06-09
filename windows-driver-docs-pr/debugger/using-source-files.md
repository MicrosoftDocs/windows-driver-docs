---
title: Using Source Files
description: Using Source Files
keywords: ["Debugger Engine API, source"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Source Files


The [debugger engine](introduction.md#debugger-engine) maintains a *source path*, which is a list of directories and source servers that contain source code files associated with the current targets. The debugger engine can search these directories and source servers for the source files. With the help of symbol files, the debugger engine can match lines in the source files with locations in the target's memory.

For an overview of using source files with debuggers, see [Debugging in Source Mode](debugging-in-source-mode.md). For an overview of source paths, see [Source Path](source-path.md). For an overview of using source servers from the debugger engine, see [Using a Source Server](using-a-source-server.md).

### <span id="source_path"></span><span id="SOURCE_PATH"></span>Source Path

To add a directory or source server to the source path, use the method [**AppendSourcePath**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-appendsourcepath). The whole source path is returned by [**GetSourcePath**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getsourcepath) and can be changed using [**SetSourcePath**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-setsourcepath). A single directory or source server can be retrieved from the source path using [**GetSourcePathElement**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getsourcepathelement).

To find a source file relative to the source path, use [**FindSourceFile**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-findsourcefile) or, for more advanced options when using source servers, use [**FindSourceFileAndToken**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-findsourcefileandtoken). **FindSourceFileAndToken** can also be used along with [**GetSourceFileInformation**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-getsourcefileinformation) to retrieve variables related to a file on a source server.

### <span id="matching_source_files_to_code_in_memory"></span><span id="MATCHING_SOURCE_FILES_TO_CODE_IN_MEMORY"></span>Matching Source Files to Code in Memory

The debugger engine provides three methods for locating the memory locations that correspond to lines in a source file. To map a single line of source code to a memory location, use [**GetOffsetByLine**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getoffsetbyline). To search for memory locations for more than one source line or for nearby source lines, use [**GetSourceEntriesByLine**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getsourceentriesbyline). The [**GetSourceFileLineOffsets**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getsourcefilelineoffsets) method will return the memory location of every line in a source file.

To perform the opposite operation and find the line of a source file that matches a location in the target's memory, use [**GetLineByOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getlinebyoffset).

**Note**  The relationship between memory locations and lines in a source file is not necessarily one-to-one. It is possible for a single line of source code to correspond to multiple memory locations and for a single memory location to correspond to multiple lines of source code.

 

 

