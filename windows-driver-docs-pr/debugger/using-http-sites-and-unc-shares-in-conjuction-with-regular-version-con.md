---
title: Using HTTP Sites and UNC Shares in Conjuction with Regular Version Control
description: Using HTTP Sites and UNC Shares in Conjuction with Regular Version Control
ms.assetid: 1b045a00-45e7-47e8-9447-7d94f70253fe
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Using HTTP Sites and UNC Shares in Conjuction with Regular Version Control


You may find that you must support your developers using the standard SrcSrv functionality that extracts files from version control but must also make source files available through a Web site or UNC share. This could happen if you have set up a test lab that does not have access to version control. It is possible to support both users using the same set of .pdb files.

First, extract the source files using SrcTool; see [Extracting Source Files](extracting-source-files.md) for details. Make the share available as either a Web site or UNC share. For the current purpose, you should not convert the .pdb files using the Cv2http.cmd script.

Now on the computers that will use the HTTP/UNC shares, edit the [Srcsrv.ini](the-srcsrv-ini-file.md) file that is in the debugger directory. In the variables section of the file, add the following three statements:

```ini
MY_SOURCE_ROOT=\\server\share
 SRCSRVCMD=
 SRCSRVTRG=%MY_SOURCE_ROOT%\%var2%\%var3%\%var4%\%fnfile%(%var1%)
```

You should replace \\\\server\\share with the root of the UNC share that you are providing or the URL of the Web site that contains the source files. You can also change MY\_SOURCE\_ROOT to be any alias you want to describe this location. With these exceptions, everything else should be entered exactly as described.

All debuggers set up in this fashion ignore the standard version control extraction instructions and instead access the source files from the location specified. Meanwhile, all debuggers without these items included in Srcsrv.ini use the normal version control mechanism to extract source files.

 

 





