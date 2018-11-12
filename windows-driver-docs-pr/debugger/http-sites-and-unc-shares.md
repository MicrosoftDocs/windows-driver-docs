---
title: HTTP Sites and UNC Shares
description: HTTP Sites and UNC Shares
ms.assetid: a1b79242-41ba-4c95-89fd-dbb7f70b24eb
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# HTTP Sites and UNC Shares


It is possible to set up a Web site that provides version-specific source to WinDbg using SrcSrv. Such a mechanism does not provide dynamic extraction of the source files from version control, but it is a valuable feature because it allows you to set the source path of WinDbg to a single unified path that provides source from many versions of many modules, instead of having to set separate paths for each debugging scenario. This is not of interest to debugging clients that have direct access to the actual version control systems but can be of assistance to those wanting to provide secure HTTP-based access to source from remote locations. The Web sites in question can be secured through HTTPS and smart cards, if desired. This same technique can be used to provide source files through a simple UNC share.

This section includes:

[Setting Up the Web Site](setting-up-the-web-site.md)

[Extracting Source Files](extracting-source-files.md)

[Modifying the Source Indexing Streams in a .pdb File](modifying-the-source-indexing-streams-in-a--pdb-file.md)

[Using UNC Shares](using-unc-shares.md)

[Using HTTP Sites and UNC Shares in Conjuction with Regular Version Control](using-http-sites-and-unc-shares-in-conjuction-with-regular-version-con.md)

 

 





