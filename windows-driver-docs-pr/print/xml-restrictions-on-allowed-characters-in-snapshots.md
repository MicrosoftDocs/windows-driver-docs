---
title: XML Restrictions on Allowed Characters in Snapshots
description: XML Restrictions on Allowed Characters in Snapshots
ms.assetid: e90fb0f2-28f7-4264-bd8c-cd5994717bad
keywords:
- snapshots WDK GDL , allowed characters
- GDL WDK , source files
- GDL WDK , strings
- source files WDK GDL
- strings WDK GDL , allowed characters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# XML Restrictions on Allowed Characters in Snapshots


XML source files can contain only the control characters (that is, those characters with ANSI values less than 0x20 hex): 0x09, 0x0a, and 0x0d. This restriction implies that GDL source files cannot contain any control characters that XML forbids. Also because the contents of a GDL string are directly mapped to an XML string (with any hex string values converted into their ANSI or Unicode equivalents), GDL strings must not contain or represent by using hex-string format or any forbidden control characters. However, command strings, because they are not interpreted, can continue to represent control characters by using hex-string format.

 

 




