---
title: ASP Files for Print Web Pages
author: windows-driver-content
description: ASP Files for Print Web Pages
ms.assetid: 01ca39ed-be16-41fb-b432-1cbd0908358d
keywords:
- customized print Web pages WDK , ASP files
- ASP files WDK printer
- print Web pages WDK , ASP files
- Web pages WDK printer , ASP files
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ASP Files for Print Web Pages


## <a href="" id="ddk-asp-files-for-print-web-pages-gg"></a>


Print Web pages are created by using ASP files. Microsoft provides ASP files that create the following print Web pages:

-   A print server page that is referenced by the URL http://*&lt;ServerName&gt;*/printers, where *&lt;ServerName&gt;* represents the DNS or WINS name for a print server. This page contains links to a page for every printer installed on the server.

-   A print queue page for each of the server's print queues. These pages are accessible by links in the print server page, or they can be referenced directly from a browser using the URL http://*&lt;ServerName&gt;*/*&lt;ShareName&gt;*.

-   Additional pages for queued documents, printer properties, and printer-specific details. These pages are displayed within a frame of the print queue page.

The printer-specific details page can be customized by replacing its ASP file. For more information, see [Customizing the Printer Details Web Page](customizing-the-printer-details-web-page.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ASP%20Files%20for%20Print%20Web%20Pages%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


