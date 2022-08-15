---
title: ew Keyword for PPD Schema
description: ew Keyword for PPD Schema
keywords:
- root-level keywords WDK printer autoconfiguration
- PPD files WDK autoconfiguration , keywords
- keywords WDK printer autoconfiguration
- in-box autoconfiguration support WDK printer , keywords
ms.date: 04/20/2017
---

# ew Keyword for PPD Schema


For Windows Vista and later versions of Windows, a new root-level keyword should be added to the PPD file which points to the GDL file in the PPD, \***MSBidiQueryFile**, which would identify a GDL file that contains the bidi mapping information required for AutoConfig. If the keyword is missing, AutoConfig does not need to invoke the GDL parser or hit the file system again to search for a GDL file.

Developers writing PScript-based drivers must use a separate GDL file that the driver's main PPD file references directly using the \***MSBidiQueryFile** Keyword.

 

 




