---
title: Debugger Data Model - File Objects
description: File objects are used to open, edit, and otherwise manipulate files on the file system.
ms.date: 12/13/2018
---
# File Objects 
## Summary
File objects are used to open, edit, and otherwise manipulate files on the file system.

## Object Methods
|Name|Return Type|Signature|Description|
|--- |--- |--- |--- |
|Close||Close()|Closes the file. |
|Delete||Delete()|Deletes the file|
|Open||Open(disposition)|Opens the file with the given *disposition*. The *disposition* may be one of "OpenExisting", "CreateNew", or "CreateAlways".|
|ReadBytes|Array of bytes|ReadBytes(byteCount)|Reads the specified number of bytes from the file and returns an indexable and iterable array of those bytes.|
|WriteBytes||WriteBytes(bytes, [byteCount])|Writes the specified bytes to the file. If *byteCount* is not supplied, every byte which can be iterated out of *bytes* is written to the file; otherwise, the first *byteCount* bytes within *bytes* is written.|

## Object Properties
|Name|Description|
|--- |--- |
|Extension|A string containing the file extension.|
|Name|A string containing the name of the file.|
|Path|A string containing the fully qualified path to the file.|
|Position|The position of the current read/write cursor within the file.|
|Size|The size of the file in bytes.|

## Remarks
If the files are being used from a garbage collected environment such as a JavaScript script, they should be closed when no longer in use rather than waiting for a garbage collection to cause the file to close.
