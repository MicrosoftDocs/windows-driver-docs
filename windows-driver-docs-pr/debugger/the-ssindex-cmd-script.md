---
title: The Ssindex.cmd Script
description: The Ssindex.cmd Script
keywords: ["SrcSrv, Ssindex.cmd script", "Ssindex.cmd script"]
ms.date: 03/07/2022
---

# The Ssindex.cmd Script


The Ssindex.cmd script builds the list of files checked into source control along with the version information of each file. It stores a subset of this information in the .pdb files generated when you built the application. SSIndex uses one of the following Perl modules to interface with source control:

-   p4.pm (Perforce)

-   tfs.pm (Team Foundation Servers)

-   svn.pm (Subversion)

For more information, run Ssindex.cmd with the **-?** or **-??** (verbose help) option or examine the script.

 

 