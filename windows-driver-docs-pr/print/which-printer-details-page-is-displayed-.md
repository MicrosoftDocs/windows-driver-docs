---
title: Which Printer Details Page is Displayed
description: Which Printer Details Page is Displayed
ms.assetid: f7824350-a6de-45ca-8d72-859edf77e86d
keywords:
- customized print Web pages WDK , viewing specific pages
- viewing printer details page
- displaying printer details page
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Which Printer Details Page is Displayed?





When a user attempts to view a printer's details page, the server uses the following algorithm to determine which ASP file to read.

-   If the standard TCP/IP port monitor is used with the printer:
    1.  The server first checks to see if a set of printer type-specific ASP files has been installed. If so, they are used.
    2.  If printer type-specific ASP files are not available, the server checks to see if a set of manufacturer-specific ASP files have been installed. If so, they are used.
    3.  If manufacturer-specific ASP files are not available, and if the Printer MIB (RFC 1759) for SNMP is supported for the printer, Microsoft's default ASP files are used.
    4.  If SNMP is not supported, a printer details page is not provided.
-   If the standard TCP/IP port monitor is not used with the printer, the server checks to see if a set of monitor-specific ASP files have been installed. If so, they are used. If not, a printer details page is not provided.

For more information, see [Installing Customized Print Web Pages](installing-customized-print-web-pages.md).

 

 




