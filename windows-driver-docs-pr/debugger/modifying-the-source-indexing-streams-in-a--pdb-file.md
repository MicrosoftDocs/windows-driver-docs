---
title: Modifying the Source Indexing Streams in a .pdb File
description: Modifying the Source Indexing Streams in a .pdb File
ms.assetid: 9c319667-fc71-4baf-ad12-a20e18b67d40
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Modifying the Source Indexing Streams in a .pdb File


For the debugger clients to use the SrcSrv Web site, the .pdb files must be modified to point to it. To do this manually, you make a copy of all the .pdb files, change them, and make them available from a separate location--usually the Web site itself.

Debugging Tools for Windows provides three files to assist in reconfiguring the .pdb files. The Cv2http.cmd and Cv2http.pl files extract the SrcSrv stream, modify it using a Perl script, and put the altered stream back in the .pdb file. The syntax is as follows:

```console
cv2http.cmd PDB Alias URL
```

where *PDB* specifies the name of the .pdbfile to modify, *Alias* specifies the logical name to apply to your Web site, and *URL* specifies the full URL of the site. Note that the *Alias* parameter is stored in the PDB as a variable name that can be overridden on the debugger client in Scrsrv.ini, should you ever move the location of the Web site.

This script requires that all the standard SrcSrv tools be available in the path because it calls both SrcTool and PDBStr. Remember that Cv2http.pl is a Perl script and can be modified to meet your needs.

The third file, the Walk (walk.cmd) script, modifies an entire set of .pdb files. For example:

```console
walk.cmd *.pdb cv2http.cmd HttpAlias https:///source
```

The preceding command calls Cv2http.cmd on every .pdb file in a tree, using HttpAlias for the alias and https://server/source for the URL. For more details on Walk, see [Extracting Source Files](extracting-source-files.md).

After this command is executed on a tree of .pdb files, they are ready for installation into the Web site or whatever location in which you want to put them. Remember that you can use SrcTool and PDBStr to examine the changes to the .pdb files.

 

 





