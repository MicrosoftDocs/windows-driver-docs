---
title: Installing Pages for a Printer Type
description: Installing Pages for a Printer Type
ms.assetid: 6c878612-d490-4791-a284-c48f1db0cde8
keywords: ["installing customized print Web pages WDK", "customized print Web pages WDK , installing", "printer-specific installations WDK"]
---

# Installing Pages for a Printer Type


## <a href="" id="ddk-installing-pages-for-a-printer-type-gg"></a>


If the standard TCP/IP port monitor is used with your printer, you can install a printer details page that is specific to the printer type. To do so, include the page's ASP file, along with all subordinate files (such as .gif files or ASP files for linked pages), in the [printer INF file](printer-inf-files.md) for the printer type. Following is a sample section of a printer INF file:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20Pages%20for%20a%20Printer%20Type%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




