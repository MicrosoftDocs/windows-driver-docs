---
title: XPSDrv Driver Options
author: windows-driver-content
description: XPSDrv Driver Options
ms.assetid: 51db3cce-a95a-4084-9927-542c2d06312a
keywords: ["Version 3 XPS drivers WDK XPSDrv , options"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20XPSDrv%20Driver%20Options%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


