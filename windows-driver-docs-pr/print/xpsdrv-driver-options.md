---
title: XPSDrv Driver Options
description: XPSDrv Driver Options
ms.assetid: 51db3cce-a95a-4084-9927-542c2d06312a
keywords:
- Version 3 XPS drivers WDK XPSDrv , options
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# XPSDrv Driver Options


You can implement the configuration module of an XPSDrv print driver by using one of the following methods:

<a href="" id="text-file-only-------"></a>**Text file only**   
The configuration module is defined by a GPD or PPD file and uses the Undriv or PScript5 configuration module to implement all of the configuration functions. The text file only method offers the fastest development time and the lowest development cost, but it has limited support for customization. This method is best suited for XPSDrv passthrough or basic XPSDrv print drivers.

<a href="" id="plug-in-------"></a>**Plug-in**   
The configuration module is defined by a GPD or PPD file and one or more Unidrv or PScript5 print driver configuration plug-ins. The plug-in method gives you the flexibility to customize certain aspects of the configuration behavior and user experience while relying on the Unidrv or PScript5 configuration module for all other aspects. The required development time for this method depends on the degree of customization that you want for your print driver. This method is suitable for all types of print drivers.

One such plug-in, Mxdwdui.dll, is provided by Microsoft to enable configuration of the Microsoft XPS Document Converter (MXDC) via the [IPrintOemUIMXDC COM Interface](iprintoemuimxdc-com-interface.md). The MXDC converts output from a GDI-based application to produce an XPS package. This utilization of a plug-in to quickly add features to an XPS driver is an example of what you can do with your own plug-ins.

<a href="" id="monolithic"></a>**Monolithic**  
You completely define and implement the configuration module. The monolithic method is generally the most costly method because you must perform all print driver development and testing, but this method also offers the most opportunity for customization.

 

 




