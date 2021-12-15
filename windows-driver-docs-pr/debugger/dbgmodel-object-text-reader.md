---
title: Debugger Data Model - Text Reader Objects
description: Reads text out of files.
ms.date: 12/13/2018
---
# Text Reader Objects 
## Summary
Text reader objects read text from a file.

## Object Methods
|Name|Signature|Description|
|--- |--- |--- |
|ReadLine|ReadLine()|Reads from the file until the next end-of-line (or the end-of-file marker) and returns the read as a string.|
|ReadLineContents|ReadLineContents()|Returns an iterable collection of strings. Each string in the collection represents one line in the file.|
