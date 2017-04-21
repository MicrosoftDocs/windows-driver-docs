---
title: Installing Pages for a Port Monitor
author: windows-driver-content
description: Installing Pages for a Port Monitor
ms.assetid: acb1a6f9-65d1-4097-b702-28dc4da8e4cf
keywords:
- installing customized print Web pages WDK
- customized print Web pages WDK , installing
- port monitors WDK print , customized Web pages
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing Pages for a Port Monitor


## <a href="" id="ddk-installing-pages-for-a-port-monitor-gg"></a>


You can provide a customized printer details page for use with printers that do not use the standard TCP/IP port monitor. Place the page's ASP file, along with all subordinate files (such as .gif files or ASP files for linked pages), in the monitor's subdirectory (&lt;Root&gt;\\&lt;Monitor&gt;, where &lt;Monitor&gt; matches the monitor name returned in a PORT\_INFO\_2 structure; for more information, see the Microsoft Windows SDK documentation). Your monitor's installer program must perform this task.

The page's initial ASP file must be named Page1.asp. All ASP file names with a format of Page*N*.asp, where *N* is 1, 2, 3, and so on, are reserved by Microsoft.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20Pages%20for%20a%20Port%20Monitor%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


