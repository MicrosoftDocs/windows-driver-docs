---
title: Source Indexing
description: Source Indexing
ms.assetid: 381020c6-26b1-48ab-bc7d-9ab718ecb89f
keywords: ["source indexing"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
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

 

 





