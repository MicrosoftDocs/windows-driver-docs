---
title: Replacing the Default Printer Details Page
description: Replacing the Default Printer Details Page
ms.assetid: 451f442b-a882-4540-82dd-e96dab5e7619
keywords:
- customized print Web pages WDK , replacing default page
- replacing default printer details page
- default printer details page
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Replacing the Default Printer Details Page





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

 

 

 




