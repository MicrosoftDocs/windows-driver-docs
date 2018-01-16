---
title: Source Indexing
description: Source Indexing
ms.assetid: 381020c6-26b1-48ab-bc7d-9ab718ecb89f
keywords: ["source indexing"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Source Indexing


Generally, binaries are source-indexed during the build process after the application has been built. The information needed by SrcSrv is stored in the .pdb files. SrcSrv currently supports the following source control systems:

-   Perforce

-   Microsoft Visual SourceSafe

-   Microsoft Team Foundation Server

You can also create a custom script to index your code for a different source control system. One such module for Subversion is included in this package.

SrcSrv includes five tools that are used in the source indexing process:

[The Srcsrv.ini File](the-srcsrv-ini-file.md)

[The Ssindex.cmd Script](the-ssindex-cmd-script.md)

[The SrcTool Utility](the-srctool-utility.md)

[The PDBStr Tool](the-pdbstr-tool.md)

[The VSSDump Tool](the-vssdump-tool.md)

These tools are installed with Debugging Tools for Windows in the subdirectory srcsrv, and should remain installed in the same path as SrcSrv. The PERL scripts in these tools require PERL 5.6 or later.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Source%20Indexing%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




