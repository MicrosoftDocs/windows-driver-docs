---
title: Installing Pages for a Printer Type
description: Installing Pages for a Printer Type
ms.assetid: 6c878612-d490-4791-a284-c48f1db0cde8
keywords:
- installing customized print Web pages WDK
- customized print Web pages WDK , installing
- printer-specific installations WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Pages for a Printer Type





If the standard TCP/IP port monitor is used with your printer, you can install a printer details page that is specific to the printer type. To do so, include the page's ASP file, along with all subordinate files (such as .gif files or ASP files for linked pages), in the [printer INF file](printer-inf-files.md) for the printer type. Following is a sample section of a printer INF file:

```cpp
[Manufacturer]
"ACME"
 
[ACME]
"ACME Mega Laser" = ACML01.PPD
 
[ACML01.PPD]
CopyFiles=@ACML01.PPD,PSCRIPT,ACML1WEB
DataSection=PSCRIPT_DATA
 
[ACML1WEB]
PAGE1.ASP, ACML1.ASP ;ACML1.ASP renamed to PAGE1.ASP during installation
ACML2.ASP
ACGF001.GIF
 
[DestinationDirs]
DefaultDestiDir=66000
ACML1WEB=66004
```

When the printer class installer encounters this INF file section, it will perform the following operations:

-   Create a directory formatted as &lt;Root&gt;\\&lt;Manufacturer&gt;\\&lt;Printer Type&gt;. For the example, the following subdirectory would be created:

    ..\\ACME\\ACME Mega Laser

-   Copy Acml1.asp, Asml2.asp, and Acgf001.gif into the subdirectory.

-   Rename Acml1.asp to Page1.asp (caused by the first statement in the ACML1WEB section).

Note that you must identify the first ASP file to be viewed by preceding it by the Page1.asp file name, as shown in the example. The installer renames this file to Page1.asp in the target directory.

All ASP file names with a format of Page*N*.asp, where *N* is 1, 2, 3, and so on, are reserved by Microsoft.

A sample INF file is provided with the [sample ASP files](sample-asp-files.md) in the Windows Driver Kit.

 

 




