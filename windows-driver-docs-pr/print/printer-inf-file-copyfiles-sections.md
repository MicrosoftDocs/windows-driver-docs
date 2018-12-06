---
title: Printer INF File CopyFiles Sections
description: Printer INF File CopyFiles Sections
ms.assetid: 92c96019-d2dd-4b2c-818a-80ae091ec662
keywords:
- INF files WDK print , CopyFiles sections
- sections WDK printer
- CopyFiles directive
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer INF File CopyFiles Sections





When a printer INF file contains a file list section that is referenced by an [**INF CopyFiles directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346), each file in the file list must be specified using the following format:

**\[**<em>file-list-section</em>**\]**
*destination-file-name\[,,flag\]*
*destination-file-name\[,,flag\]*
*destination-file-name\[,,flag\]*
...
The *destination-file-name* field is required, and the *flag* field is optional. File specifications must not include the optional *source-file-name* or *temporary-file-name* fields that are defined for file list sections used with the INF CopyFiles directive. This restriction is required for installing print drivers from a Web page.

 

 




