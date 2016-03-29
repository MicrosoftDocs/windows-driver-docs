---
title: Replacing the Default Printer Details Page
description: Replacing the Default Printer Details Page
ms.assetid: 451f442b-a882-4540-82dd-e96dab5e7619
keywords: ["customized print Web pages WDK , replacing default page", "replacing default printer details page", "default printer details page"]
---

# Replacing the Default Printer Details Page


## <a href="" id="ddk-replacing-the-default-printer-details-page-gg"></a>


You can replace the default printer details page with a customized page by using the following steps:

1.  Provide a customized ASP file for the page.

2.  Follow the installation procedures described in [Installing Customized Print Web Pages](installing-customized-print-web-pages.md).

A customized printer detail page can provide links to additional customized pages, or any other URLs. ASP files for additional customized pages must be installed as indicated in [Installing Customized Print Web Pages](installing-customized-print-web-pages.md). For information about specifying links, refer to ASP documentation in the Microsoft Windows SDK documentation.

Customized print Web pages can use the following technologies:

[ASP Variables for Print Web Pages](asp-variables-for-print-web-pages.md)

[ActiveX Objects for Print Web Pages](activex-objects-for-print-web-pages.md)

Customized COM objects

For information about creating and using COM objects, see the Windows SDK documentation.

**Note**   All print Web pages created using ASP files are generated from a single ASP application.
You must not modify the file named Globals.asp, which is contained in the Printers subdirectory of the system disk.

Microsoft reserves the right to modify its print Web pages without notice. Therefore, customized ASP files must not depend on the content of Microsoft-supplied ASP files.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Replacing%20the%20Default%20Printer%20Details%20Page%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




