---
title: Customizing the Printer Details Web Page
description: Customizing the Printer Details Web Page
ms.assetid: 4853d5de-b855-4698-9178-877455e257c5
keywords:
- customized print Web pages WDK , creating pages
- ASP files WDK printer
- port monitors WDK print , customized Web pages
- customized print Web pages WDK , details page
- details page WDK printer
- print Web pages WDK , details page
- Web pages WDK printer , details page
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customizing the Printer Details Web Page

If you want to replace the printer details page provided by Microsoft, you can provide one or more customized ASP files. If you replace the default page, you can also provide links to additional customized pages installed on the server, plus links to any other pages on the Web.

If Microsoft's standard TCP/IP [port monitor](https://docs.microsoft.com/windows-hardware/drivers/print/port-monitors) (Tcpmon.dll) is used with your printer, customized ASP files can be used to replace the default printer details pages on a per-printer type or per-manufacturer basis. If customized ASP files have not been installed, the default printer details page is used.

Customized ASP files can also be used to replace the default printer details pages for printers using other port monitors, but per-printer type and per-manufacturer replacements are not allowed.

The method used for installing customized ASP files determines whether the customized files replace the default files for a printer type, a manufacturer, or a port monitor. For more information, see [Installing Customized Print Web Pages](installing-customized-print-web-pages.md).

The following topics provide more information about creating print Web pages:

[Replacing the Default Printer Details Page](replacing-the-default-printer-details-page.md)

[Which Printer Details Page is Displayed?](which-printer-details-page-is-displayed-.md)

[ASP Variables for Print Web Pages](asp-variables-for-print-web-pages.md)

[ActiveX Objects for Print Web Pages](activex-objects-for-print-web-pages.md)

[Updating Web Page Information](updating-web-page-information.md)
