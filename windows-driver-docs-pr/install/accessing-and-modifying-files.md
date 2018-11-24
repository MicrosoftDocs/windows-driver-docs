---
title: Accessing and Modifying Files
description: Accessing and Modifying Files
ms.assetid: DD5A527F-5F8D-4892-A2D5-C0279913B6A3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing and Modifying Files


The following guidelines apply to driver package components when they access or modify files:

-   Files should be modified only by using [INF directives](inf-directives.md) within an INF file. For example, use the INF [**CopyFiles**](inf-copyfiles-directive.md) directive to copy files and the INF [**RenFiles**](inf-renfiles-directive.md) directive to rename files.

-   Files that appear in an INF [**CopyFiles**](inf-copyfiles-directive.md) directive must not also appear in an INF [**RenFiles**](inf-renfiles-directive.md) or [**DelFiles**](inf-delfiles-directive.md) directive in the INF file.

**Important**  The INF [**RenFiles**](inf-renfiles-directive.md) and [**DelFiles**](inf-delfiles-directive.md) directives must be used carefully. You should not use these directives in the INF file for a Plug and Play (PnP) function driver.

 

 

 





