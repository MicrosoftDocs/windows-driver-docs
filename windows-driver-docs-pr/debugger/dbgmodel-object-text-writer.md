---
title: Debugger Data Model - Text Wrtier Objects
description: Writes text to files.
ms.date: 12/13/2018
---
# Text Writer Objects 
## Summary
Text writer objects write text of the given encoding to a file.

## Object Methods
|Name|Signature|Description|
|--- |--- |--- |
|Write|Write(object)|Writes the string conversion of the given object to the file without a newline.|
|WriteLine|WriteLine(object)|Writes the string conversion of the given object to the file followed by a newline.|
|WriteContents|WriteContents(object)|Iterates *object* and writes the string conversion of each iterated element to the file without a newline between each.|
|WriteLineContents|WriteLineContents(object)|Iterates *object* and writes the string conversion of each iterated element to the file with a newline between each.|
