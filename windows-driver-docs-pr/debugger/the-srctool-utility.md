---
title: The SrcTool Utility
description: The SrcTool Utility
keywords: ["SrcSrv, SrcTool utility", "SrcTool utility"]
ms.date: 04/16/2026
ms.topic: concept-article
---

# The SrcTool utility

The SrcTool (Srctool.exe) utility lists all files indexed within the .pdb file. For each file, it lists the full path, source control server, and version number of the file. Use this information for reference.

You can also use SrcTool to list the raw source file information from the .pdb file. To do this, use the **-s** switch on the command line.

SrcTool has other options as well. Use the **?** switch to see them. Of most interest is that this utility can be used to extract all of the source files from version control. This action is done by using the **-x** switch.

> [!NOTE]
> Previous versions of this program created a directory named **src** under the current directory when extracting files. This version no longer creates that directory. If you want to use the **src** directory, you must create it yourself and run the command from that directory.
