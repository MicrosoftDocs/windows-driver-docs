---
title: New Keyword for GPD Schema
author: windows-driver-content
description: New Keyword for GPD Schema
ms.assetid: 4814d019-0556-4e5a-8c55-c05454bafbd3
keywords:
- root-level keywords WDK printer autoconfiguration
- GPD files WDK GDL extensions , keywords
- keywords WDK printer autoconfiguration
- in-box autoconfiguration support WDK printer , keywords
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# New Keyword for GPD Schema


Starting with Windows Vista, you should add a new root-level keyword to the GPD file that points to the GDL file in the GPD, \***BidiQueryFile**, which would identify a GDL file that contains the bidi mapping information that is required for autoconfiguration. If the keyword is missing, autoconfiguration does not need to call the GDL parser or hit the file system again to search for a GDL file.

If you are writing Unidrv-based drivers, you must use a separate GDL file that the driver's main GPD file references directly by using the \***BidiQueryFile** keyword.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20New%20Keyword%20for%20GPD%20Schema%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


