---
title: Printer INF File CopyFiles Sections
description: Printer INF File CopyFiles Sections
keywords:
- INF files WDK print , CopyFiles sections
- sections WDK printer
- CopyFiles directive
ms.date: 04/20/2017
---

# Printer INF File CopyFiles Sections





When a printer INF file contains a file list section that is referenced by an [**INF CopyFiles directive**](../install/inf-copyfiles-directive.md), each file in the file list must be specified using the following format:

**\[**<em>file-list-section</em>**\]**
*destination-file-name\[,,flag\]*
*destination-file-name\[,,flag\]*
*destination-file-name\[,,flag\]*
...
The *destination-file-name* field is required, and the *flag* field is optional. File specifications must not include the optional *source-file-name* or *temporary-file-name* fields that are defined for file list sections used with the INF CopyFiles directive. This restriction is required for installing print drivers from a Web page.

 

