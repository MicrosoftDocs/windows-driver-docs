---
title: Installing Pages for a Manufacturer
description: Installing Pages for a Manufacturer
ms.assetid: 637b265f-9138-4696-b52a-ce63cd1f2c01
keywords:
- installing customized print Web pages WDK
- customized print Web pages WDK , installing
- manufacturer-specific printer installations WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Pages for a Manufacturer





You can install a printer details page that is manufacturer-specific, for all the manufacturer's printer types that use the standard TCP/IP port monitor. To do so, place the page's ASP file, along with all subordinate files (such as .gif files or ASP files for linked pages), in the manufacturer's subdirectory (\\%windir%\\web\\printers\\&lt;Manufacturer&gt;). A customized setup program must be provided to accomplish this.

The page's initial ASP file must be named Page1.asp. All ASP file names with a format of Page*N*.asp, where *N* is 1, 2, 3, and so on, are reserved by Microsoft.

The manufacturer-specific page will be used for all of the manufacturer's printer types that use the standard TCP/IP port monitor and do not have printer type-specific pages.

The system determines a printer's manufacturer by reading the printer's INF file at installation time. When a user attempts to view a printer details page, the system first checks to see if a file named Page1.asp exists in &lt;Root&gt;\\&lt;Manufacturer&gt;\\&lt;Printer Type&gt;. If a file is not found, the system checks &lt;Root&gt;\\&lt;Manufacturer&gt;.

 

 




