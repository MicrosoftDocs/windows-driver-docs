---
title: ASP Files for Print Web Pages
description: ASP Files for Print Web Pages
ms.assetid: 01ca39ed-be16-41fb-b432-1cbd0908358d
keywords:
- customized print Web pages WDK , ASP files
- ASP files WDK printer
- print Web pages WDK , ASP files
- Web pages WDK printer , ASP files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ASP Files for Print Web Pages





Print Web pages are created by using ASP files. Microsoft provides ASP files that create the following print Web pages:

- A print server page that is referenced by the URL http://<em>&lt;ServerName&gt;</em>/printers, where *&lt;ServerName&gt;* represents the DNS or WINS name for a print server. This page contains links to a page for every printer installed on the server.

- A print queue page for each of the server's print queues. These pages are accessible by links in the print server page, or they can be referenced directly from a browser using the URL http://<em>&lt;ServerName&gt;</em>/*&lt;ShareName&gt;*.

- Additional pages for queued documents, printer properties, and printer-specific details. These pages are displayed within a frame of the print queue page.

The printer-specific details page can be customized by replacing its ASP file. For more information, see [Customizing the Printer Details Web Page](customizing-the-printer-details-web-page.md).

 

 




