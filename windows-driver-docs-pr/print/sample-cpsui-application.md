---
title: Sample CPSUI Application
description: Sample CPSUI Application
ms.assetid: 895afbfe-c18a-4bcc-b815-8cb323bbac80
keywords:
- Common Property Sheet User Interface WDK print , samples
- CPSUI WDK print , samples
- property sheet pages WDK print , samples
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample CPSUI Application





Source code for CPSUISAM, a sample CPSUI application, is included in the \\src\\print directory of the WDK. The application causes CPSUI to call into the print spooler to create property sheet pages for the system's default printer. The application then creates an additional property sheet page, in order to illustrate some of the techniques that can be employed when using CPSUI to create a new page.

**Note**  Printer interface DLLs should not call into the print spooler. CPSUISAM illustrates some of the capabilities of CPSUI but does not represent techniques that should be used by printer interface DLLs. Instead, these DLLs should follow the steps described in [Using CPSUI with Printer Drivers](using-cpsui-with-printer-drivers.md).

 

 

 




