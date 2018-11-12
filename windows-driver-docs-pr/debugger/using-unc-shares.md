---
title: Using UNC Shares
description: Using UNC Shares
ms.assetid: 7baf157d-e8c3-4ad5-a56e-58f8983da4d9
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Using UNC Shares


The Cv2http.cmd, Cv2http.pl, and Walk (Walk.cmd) scripts are used to provide source files from a simple UNC share. The files Cv2http.cmd and Cv2http.pl extract the SrcSrv stream, modify it using a Perl script, and put the altered stream back in the .pdb file. The syntax is as follows:

`cv2http.cmd PDB Alias SourceRoot`

where *PDB* specifies the name of the .pdbfile to modify, *Alias* specifies the logical name to apply to your Web site, and *SourceRoot* specifies the root of the UNC share to which you extracted the source files. Note that the *Alias* parameter is stored in the PDB as a varaible name that can be overridden on the debugger client in Scrsrv.ini, should you ever move the location of the Web site.

This script requires that all the standard SrcSrv tools be available in the path because it calls both SrcTool and PDBStr. Remember that Cv2http.pl is a Perl script and can be modified to meet your needs.

The third file, the Walk (walk.cmd) script, modifies an entire set of .pdb files. For example:

```console
walk.cmd *.pdb cv2http.cmd SourceRoot \\server\share
```

The preceding command calls Cv2http.cmd on every .pdb file in a tree, using SourceRoot for the alias and \\\\server\\share for the UNC share. For more details on Walk, see [Extracting Source Files](extracting-source-files.md).

After this command is executed on a tree of .pdb files, they are ready for installation into the Web site or whatever location in which you want to put them. Remember that you can use SrcTool and PDBStr to examine the changes to the .pdb files.

 

 





