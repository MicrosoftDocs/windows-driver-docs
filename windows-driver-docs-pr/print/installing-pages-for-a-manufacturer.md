---
title: Installing Pages for a Manufacturer
author: windows-driver-content
description: Installing Pages for a Manufacturer
ms.assetid: 637b265f-9138-4696-b52a-ce63cd1f2c01
keywords:
- installing customized print Web pages WDK
- customized print Web pages WDK , installing
- manufacturer-specific printer installations WDK
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing Pages for a Manufacturer


## <a href="" id="ddk-installing-pages-for-a-manufacturer-gg"></a>


You can install a printer details page that is manufacturer-specific, for all the manufacturer's printer types that use the standard TCP/IP port monitor. To do so, place the page's ASP file, along with all subordinate files (such as .gif files or ASP files for linked pages), in the manufacturer's subdirectory (\\%windir%\\web\\printers\\&lt;Manufacturer&gt;). A customized setup program must be provided to accomplish this.

The page's initial ASP file must be named Page1.asp. All ASP file names with a format of Page*N*.asp, where *N* is 1, 2, 3, and so on, are reserved by Microsoft.

The manufacturer-specific page will be used for all of the manufacturer's printer types that use the standard TCP/IP port monitor and do not have printer type-specific pages.

The system determines a printer's manufacturer by reading the printer's INF file at installation time. When a user attempts to view a printer details page, the system first checks to see if a file named Page1.asp exists in &lt;Root&gt;\\&lt;Manufacturer&gt;\\&lt;Printer Type&gt;. If a file is not found, the system checks &lt;Root&gt;\\&lt;Manufacturer&gt;.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20Pages%20for%20a%20Manufacturer%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


