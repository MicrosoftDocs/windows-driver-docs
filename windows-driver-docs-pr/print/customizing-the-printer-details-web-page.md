---
title: Customizing the Printer Details Web Page
author: windows-driver-content
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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Customizing the Printer Details Web Page


## <a href="" id="ddk-customizing-the-printer-details-web-page-gg"></a>


If you want to replace the printer details page provided by Microsoft, you can provide one or more customized ASP files. If you replace the default page, you can also provide links to additional customized pages installed on the server, plus links to any other pages on the Web.

If Microsoft's standard TCP/IP [*port monitor*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-port-monitor) (Tcpmon.dll) is used with your printer, customized ASP files can be used to replace the default printer details pages on a per-printer type or per-manufacturer basis. If customized ASP files have not been installed, the default printer details page is used.

Customized ASP files can also be used to replace the default printer details pages for printers using other port monitors, but per-printer type and per-manufacturer replacements are not allowed.

The method used for installing customized ASP files determines whether the customized files replace the default files for a printer type, a manufacturer, or a port monitor. For more information, see [Installing Customized Print Web Pages](installing-customized-print-web-pages.md).

The following topics provide more information about creating print Web pages:

[Replacing the Default Printer Details Page](replacing-the-default-printer-details-page.md)

[Which Printer Details Page is Displayed?](which-printer-details-page-is-displayed-.md)

[ASP Variables for Print Web Pages](asp-variables-for-print-web-pages.md)

[ActiveX Objects for Print Web Pages](activex-objects-for-print-web-pages.md)

[Updating Web Page Information](updating-web-page-information.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Customizing%20the%20Printer%20Details%20Web%20Page%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


