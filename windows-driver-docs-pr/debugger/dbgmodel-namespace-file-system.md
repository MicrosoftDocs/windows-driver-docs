---
title: Debugger Data Model - The FileSystem Namespace
description: The FileSystem namespace provides the  properties and methods for manipulating the file system.
ms.date: 12/13/2018
---
> [!IMPORTANT]
>  This interface is under active development and will change.
>
# The FileSystem Namespace
## Summary
The FileSystem namespace provides the  properties and methods for manipulating the file system.

## Object Methods
|Name|Return Type|Signature|Description|
|--- |--- |--- |--- |
|CreateFile|`File`|CreateFile(path, [disposition])|Creates a new file at the specified path and opens it for writing. *Disposition* may be one of "OpenExisting", "CreateNew", or "CreateAlways".|
|CreateTempFile|`File`|CreateTempFile()|Creates a new temporary file in the %TEMP% folder and opens it for writing.|
|CreateTextReader|`Text Reader`|CreateTextReader(file \| path, [encoding])|Creates a text reader from the given  `file object ` or path which will read text of the specified encoding. Encoding may be one of "Ascii", "Utf8", or "Utf16". If not specified, "Ascii" is the default.|
|CreateTextWriter|`Text Writer`|CreateTextWriter(file \| path, [encoding])|Creates a text writer from the given  `file object ` or path which will write text of the specified encoding. Encoding may be one of "Ascii", "Utf8", or "Utf16". If not specified, "Ascii" is the default.|
|DeleteFile||DeleteFile(path)|Deletes the file at the specified path.|
|FileExists|True or False|FileExists(path)|Returns true or false as to whether a file exists at the given path|
|OpenFile|`File`|OpenFile(path)|Opens a file at the specified path for reading.|

## Object Properties
|Name|Description|
|--- |--- |
|CurrentDirectory|A `directory` object representing the current working directory of the debugger process.|
|TempDirectory|A `directory` object representing the %TEMP% directory of the debugger process. |