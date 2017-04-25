---
title: XML Restrictions on Allowed Characters in Snapshots
author: windows-driver-content
description: XML Restrictions on Allowed Characters in Snapshots
ms.assetid: e90fb0f2-28f7-4264-bd8c-cd5994717bad
keywords:
- snapshots WDK GDL , allowed characters
- GDL WDK , source files
- GDL WDK , strings
- source files WDK GDL
- strings WDK GDL , allowed characters
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# XML Restrictions on Allowed Characters in Snapshots


XML source files can contain only the control characters (that is, those characters with ANSI values less than 0x20 hex): 0x09, 0x0a, and 0x0d. This restriction implies that GDL source files cannot contain any control characters that XML forbids. Also because the contents of a GDL string are directly mapped to an XML string (with any hex string values converted into their ANSI or Unicode equivalents), GDL strings must not contain or represent by using hex-string format or any forbidden control characters. However, command strings, because they are not interpreted, can continue to represent control characters by using hex-string format.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XML%20Restrictions%20on%20Allowed%20Characters%20in%20Snapshots%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


