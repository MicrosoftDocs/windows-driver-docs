---
title: The SrcTool Utility
description: The SrcTool Utility
ms.assetid: d8669a91-4361-41d6-a7ba-a6d1a706ff66
keywords: ["SrcSrv, SrcTool utility", "SrcTool utility"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# The SrcTool Utility


The SrcTool (Srctool.exe) utility lists all files indexed within the .pdb file. For each file, it lists the full path, source control server, and version number of the file. You can use this information for reference.

You can also use SrcTool to list the raw source file information from the .pdb file. To do this, use the **-s** switch on the command line.

SrcTool has other options as well. Use the **?** switch to see them. Of most interest is that this utility can be used to extract all of the source files from version control. This is done with the **-x** switch.

**Note**   Previous versions of this program created a directory called src below the current directory when extracting files. This is no longer the case. If you want the src directory used, you must create it yourself and run the command from that directory.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20The%20SrcTool%20Utility%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




