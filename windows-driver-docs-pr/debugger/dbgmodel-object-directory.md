---
title: Debugger Data Model - Directory Objects
description: Directory objects represent and manipulate directories on the file system.
ms.date: 12/13/2018
---
# Directory Objects 
## Summary
Directory objects represent and manipulate directories on the file system.

## Object Methods
|Name|Return Type|Signature|Description|
|--- |-- |--- |--- |
|CreateFile|[file](dbgmodel-object-file.md)|CreateFile(relativePath, [disposition])|Creates a file within the directory with the given disposition. Disposition may be one of "OpenExisting", "CreateNew", or "CreateAlways".|
|CreateSubDirectory|[directory](dbgmodel-object-directory.md)|CreateSubDirectory(name)|Creates a new subdirectory within the directory.|
|Delete||Delete()|Deletes the subdirectory if it is empty.|
|OpenFile|[file](dbgmodel-object-file.md)|OpenFile(relativePath)|Opens an existing file for reading from the directory.|


## Object Properties
|Name|Description|
|--- |--- |
|Files|A [collection](dbgmodel-namespace-collections.md) of [file](dbgmodel-object-file.md) within the directory.|
|SubDirectories|A [collection](dbgmodel-namespace-collections.md) of [directory](dbgmodel-object-directory.md) within the directory.|
