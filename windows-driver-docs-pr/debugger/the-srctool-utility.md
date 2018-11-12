---
title: The SrcTool Utility
description: The SrcTool Utility
ms.assetid: d8669a91-4361-41d6-a7ba-a6d1a706ff66
keywords: ["SrcSrv, SrcTool utility", "SrcTool utility"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# The SrcTool Utility


The SrcTool (Srctool.exe) utility lists all files indexed within the .pdb file. For each file, it lists the full path, source control server, and version number of the file. You can use this information for reference.

You can also use SrcTool to list the raw source file information from the .pdb file. To do this, use the **-s** switch on the command line.

SrcTool has other options as well. Use the **?** switch to see them. Of most interest is that this utility can be used to extract all of the source files from version control. This is done with the **-x** switch.

**Note**   Previous versions of this program created a directory called src below the current directory when extracting files. This is no longer the case. If you want the src directory used, you must create it yourself and run the command from that directory.

 

 

 





