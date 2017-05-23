---
title: The Ssindex.cmd Script
description: The Ssindex.cmd Script
ms.assetid: 38bff31a-af4e-4fd4-bdf6-da901067bdd0
keywords: ["SrcSrv, Ssindex.cmd script", "Ssindex.cmd script"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# The Ssindex.cmd Script


The Ssindex.cmd script builds the list of files checked into source control along with the version information of each file. It stores a subset of this information in the .pdb files generated when you built the application. SSIndex uses one of the following Perl modules to interface with source control:

-   p4.pm (Perforce)

-   vss.pm (Visual SourceSafe)

-   tfs.pm (Team Foundation Servers)

-   svn.pm (Subversion)

For more information, run Ssindex.cmd with the **-?** or **-??** (verbose help) option or examine the script.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20The%20Ssindex.cmd%20Script%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




