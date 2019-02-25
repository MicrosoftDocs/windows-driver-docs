---
title: New Keyword for GPD Schema
description: New Keyword for GPD Schema
ms.assetid: 4814d019-0556-4e5a-8c55-c05454bafbd3
keywords:
- root-level keywords WDK printer autoconfiguration
- GPD files WDK GDL extensions , keywords
- keywords WDK printer autoconfiguration
- in-box autoconfiguration support WDK printer , keywords
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# New Keyword for GPD Schema


Starting with Windows Vista, you should add a new root-level keyword to the GPD file that points to the GDL file in the GPD, \***BidiQueryFile**, which would identify a GDL file that contains the bidi mapping information that is required for autoconfiguration. If the keyword is missing, autoconfiguration does not need to call the GDL parser or hit the file system again to search for a GDL file.

If you are writing Unidrv-based drivers, you must use a separate GDL file that the driver's main GPD file references directly by using the \***BidiQueryFile** keyword.

 

 




