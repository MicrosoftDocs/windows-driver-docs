---
title: Debugger Data Model - The FileSystem Namespace
description: The FileSystem namespace provides the  properties and methods for manipulating the file system.
ms.date: 12/13/2018
ms.localizationpriority: medium
---
# The FileSystem Namespace

> [!IMPORTANT]
>  This interface is under active development and will change.
>
## Summary
The FileSystem namespace provides the  properties and methods for manipulating the file system. This can be used from JavaScript for reading or writing files that are needed to support your debugger extension.

## Sample
For a simple end-to-end example of how to use this namespace and these objects, check out the sample on GitHub - https://github.com/Microsoft/WinDbg-Samples/tree/master/FileSystem 

## Object Methods
|Name|Return Type|Signature|Description|
|--- |--- |--- |--- |
|CreateFile|[file](dbgmodel-object-file.md)|CreateFile(path, [disposition])|Creates a new file at the specified path and opens it for writing. *Disposition* may be one of "OpenExisting", "CreateNew", or "CreateAlways".|
|CreateTempFile|[file](dbgmodel-object-file.md)|CreateTempFile()|Creates a new temporary file in the %TEMP% folder and opens it for writing.|
|CreateTextReader|[text reader](dbgmodel-object-text-reader.md)|CreateTextReader(file \| path, [encoding])|Creates a text reader from the given [file](dbgmodel-object-file.md) object or path which will read text of the specified encoding. Encoding may be one of "Ascii", "Utf8", or "Utf16". If not specified, "Ascii" is the default.|
|CreateTextWriter|[text writer](dbgmodel-object-text-writer.md)|CreateTextWriter(file \| path, [encoding])|Creates a text writer from the given [file](dbgmodel-object-file.md) object or path which will write text of the specified encoding. Encoding may be one of "Ascii", "Utf8", or "Utf16". If not specified, "Ascii" is the default.|
|DeleteFile||DeleteFile(path)|Deletes the file at the specified path.|
|FileExists|True or False|FileExists(path)|Returns true or false as to whether a file exists at the given path|
|OpenFile|[file](dbgmodel-object-file.md)|OpenFile(path)|Opens a file at the specified path for reading.|

## Object Properties
|Name|Description|
|--- |--- |
|CurrentDirectory|A [directory](dbgmodel-object-directory.md) object representing the current working directory of the debugger process.|
|TempDirectory|A [directory](dbgmodel-object-directory.md) object representing the %TEMP% directory of the debugger process. |