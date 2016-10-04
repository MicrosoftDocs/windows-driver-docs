---
title: Pscript Capabilities
author: windows-driver-content
description: Pscript Capabilities
MS-HAID:
- 'pscript\_78c8dda7-391d-425e-81ab-f58b90b7fcbb.xml'
- 'print.pscript\_capabilities'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1530cb64-a1b1-4ff5-a6bf-b3634e83a225
keywords: ["PostScript Printer Driver WDK print , capabilities", "Pscript WDK print , capabilities"]
---

# Pscript Capabilities


## <a href="" id="ddk-pscript-capabilities-gg"></a>


The PostScript Printer Driver (Pscript) provides the following capabilities:

-   Support for all PostScript printers, using printer-specific [*PPD*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-postscript-printer-description--ppd-)-based [Pscript minidrivers](pscript-minidrivers.md) that describe each printer's characteristics.

-   A [Pscript user interface](pscript-user-interface.md), based on the TreeView control and property sheets, that is consistent for all printers, but is also modifiable for each printer's unique options.

-   A single [Pscript renderer](pscript-renderer.md) that, along with the GDI graphics engine, converts Microsoft Win32 GDI calls from applications into printer commands that can be sent to the print spooler.

-   Support for version 3.1 of the Document Structuring Convention, described in the PostScript Language Reference Manual published by Adobe Systems, Inc.

-   Support for printers that provide PostScript Level 1, Level 2, or Level 3 features.

-   The following types of support for fonts:
    -   Incremental downloading of OpenType fonts as PostScript Type 1 or Type 2 fonts.
    -   Incremental downloading of TrueType fonts as PostScript Type 1, Type 3, Type 32, Type 42, or CID-based Type 42 fonts.
    -   Incremental downloading of host-resident raster fonts as PostScript Type 3 or Type 32 fonts.
    -   Full downloading of host-resident PostScript Type 1 fonts.
    -   Printer-resident PostScript Type 1, Type 2, and CID fonts.
    -   Font substitution per glyph, for glyphs that exist in the printer's character set.
-   Support for ICM 2.0, and allowing image color management to be performed on the host system or by printer hardware.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Pscript%20Capabilities%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


