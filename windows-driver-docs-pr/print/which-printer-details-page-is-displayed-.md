---
title: Which Printer Details Page is Displayed
author: windows-driver-content
description: Which Printer Details Page is Displayed
MS-HAID:
- 'inetpri\_0c79fea0-cd1d-41af-90ae-e5da4f820bfe.xml'
- 'print.which\_printer\_details\_page\_is\_displayed\_'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f7824350-a6de-45ca-8d72-859edf77e86d
keywords: ["customized print Web pages WDK , viewing specific pages", "viewing printer details page", "displaying printer details page"]
---

# Which Printer Details Page is Displayed?


## <a href="" id="ddk-which-printer-details-page-is-displayed-gg"></a>


When a user attempts to view a printer's details page, the server uses the following algorithm to determine which ASP file to read.

-   If the standard TCP/IP port monitor is used with the printer:
    1.  The server first checks to see if a set of printer type-specific ASP files has been installed. If so, they are used.
    2.  If printer type-specific ASP files are not available, the server checks to see if a set of manufacturer-specific ASP files have been installed. If so, they are used.
    3.  If manufacturer-specific ASP files are not available, and if the Printer MIB (RFC 1759) for SNMP is supported for the printer, Microsoft's default ASP files are used.
    4.  If SNMP is not supported, a printer details page is not provided.
-   If the standard TCP/IP port monitor is not used with the printer, the server checks to see if a set of monitor-specific ASP files have been installed. If so, they are used. If not, a printer details page is not provided.

For more information, see [Installing Customized Print Web Pages](installing-customized-print-web-pages.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Which%20Printer%20Details%20Page%20is%20Displayed?%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


