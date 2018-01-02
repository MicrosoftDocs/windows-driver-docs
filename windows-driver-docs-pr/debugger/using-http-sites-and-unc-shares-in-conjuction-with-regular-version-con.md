---
title: Using HTTP Sites and UNC Shares in Conjuction with Regular Version Control
description: Using HTTP Sites and UNC Shares in Conjuction with Regular Version Control
ms.assetid: 1b045a00-45e7-47e8-9447-7d94f70253fe
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using HTTP Sites and UNC Shares in Conjuction with Regular Version Control


You may find that you must support your developers using the standard SrcSrv functionality that extracts files from version control but must also make source files available through a Web site or UNC share. This could happen if you have set up a test lab that does not have access to version control. It is possible to support both users using the same set of .pdb files.

First, extract the source files using SrcTool; see [Extracting Source Files](extracting-source-files.md) for details. Make the share available as either a Web site or UNC share. For the current purpose, you should not convert the .pdb files using the Cv2http.cmd script.

Now on the computers that will use the HTTP/UNC shares, edit the [Srcsrv.ini](the-srcsrv-ini-file.md) file that is in the debugger directory. In the variables section of the file, add the following three statements:

```
MY_SOURCE_ROOT=\\server\share
 SRCSRVCMD=
 SRCSRVTRG=%MY_SOURCE_ROOT%\%var2%\%var3%\%var4%\%fnfile%(%var1%)
```

You should replace \\\\server\\share with the root of the UNC share that you are providing or the URL of the Web site that contains the source files. You can also change MY\_SOURCE\_ROOT to be any alias you want to describe this location. With these exceptions, everything else should be entered exactly as described.

All debuggers set up in this fashion ignore the standard version control extraction instructions and instead access the source files from the location specified. Meanwhile, all debuggers without these items included in Srcsrv.ini use the normal version control mechanism to extract source files.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20HTTP%20Sites%20and%20UNC%20Shares%20in%20Conjuction%20with%20Regular%20Version%20Control%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




