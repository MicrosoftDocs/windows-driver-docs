---
title: Installing Pages for a Port Monitor
description: Installing Pages for a Port Monitor
ms.assetid: acb1a6f9-65d1-4097-b702-28dc4da8e4cf
keywords:
- installing customized print Web pages WDK
- customized print Web pages WDK , installing
- port monitors WDK print , customized Web pages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Pages for a Port Monitor





You can provide a customized printer details page for use with printers that do not use the standard TCP/IP port monitor. Place the page's ASP file, along with all subordinate files (such as .gif files or ASP files for linked pages), in the monitor's subdirectory (&lt;Root&gt;\\&lt;Monitor&gt;, where &lt;Monitor&gt; matches the monitor name returned in a PORT\_INFO\_2 structure; for more information, see the Microsoft Windows SDK documentation). Your monitor's installer program must perform this task.

The page's initial ASP file must be named Page1.asp. All ASP file names with a format of Page*N*.asp, where *N* is 1, 2, 3, and so on, are reserved by Microsoft.

 

 




