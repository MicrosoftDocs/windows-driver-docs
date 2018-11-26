---
title: Pscript Minidrivers
description: Pscript Minidrivers
ms.assetid: b1108a6b-e0cc-413c-b3ea-53a1aa3156c0
keywords:
- PostScript Printer Driver WDK print , minidrivers
- Pscript WDK print , minidrivers
- minidrivers WDK Pscript
- minidrivers WDK Pscript , about Pscript minidrivers
- PPD files WDK print
- .ppd files
- NTF files
- .ntf files
- East Asian fonts WDK print
- Asian fonts WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pscript Minidrivers





Pscript minidrivers are created from .ppd files and .ntf files.

### <a href="" id="ddk-ppd-files-gg"></a>PPD Files

Text-based PostScript Printer Description files (.ppd files) describe a PostScript printer's characteristics. The Pscript driver for Microsoft Windows 2000 and later supports .ppd files that are compatible with version 4.3 of the PPD specification from Adobe Systems, Inc. Pscript reads a printer's .ppd file and converts the text into a binary format, stored locally as a .bpd file that is regenerated every time the .ppd file changes.

### <a href="" id="ddk-ntf-files-gg"></a>NTF Files

Windows 2000 and later font files (.ntf files) are binary files used for describing the device fonts of printers supported by Pscript.

Microsoft provides a default .ntf file, named pscript.ntf, that contains descriptions of commonly encountered US device fonts. For East Asian printers, Microsoft also provides a default .ntf file, named pscrptfe.ntf, which contains descriptions of commonly encountered East Asian device fonts.

In addition, hardware vendors can supply device font descriptions for fonts not supported by pscript.ntf. These font descriptions can be created by [converting AFM files to NTF files](converting-afm-files-to-ntf-files.md). Customized, printer model-specific .ntf files can be installed by listing them as dependent files in a [printer INF file](printer-inf-files.md). For more information, see [Installing a Pscript Minidriver](installing-a-pscript-minidriver.md).

Pscript searches for font metrics by first checking printer model-specific .ntf files, then checking pscript.ntf, and using the first font description found.

This section contains the following topics:

[Converting AFM Files to NTF Files](converting-afm-files-to-ntf-files.md)

[Converting East Asian AFM Files to NTF Files](converting-east-asian-afm-files-to-ntf-files.md)

[Installing a Pscript Minidriver](installing-a-pscript-minidriver.md)

[PostScript Printer Standard Features](postscript-printer-driver-standard-features.md)

[Pscript Printer Minidriver Versioning](pscript-printer-minidriver-versioning.md)

[Pscript Support for Stapling](pscript-support-for-stapling.md)

[AddEuro](addeuro.md)

[TrueGray](truegray.md)

 

 




