---
title: Introduction to GPD Files
description: Introduction to GPD Files
ms.assetid: f29415cf-d8ca-42a2-bbae-2be53e3621a6
keywords: ["generic printer description WDK Unidrv", "GPD files WDK Unidrv", "Unidrv, GPD files", "GPD files WDK Unidrv , about GPD files", "Unidrv WDK print"]
---

# Introduction to GPD Files


## <a href="" id="ddk-introduction-to-gpd-files-gg"></a>


GPD files are used for creating [Unidrv minidrivers](unidrv-minidrivers.md). A Unidrv minidriver consists of a text-based generic printer description (GPD), which can be contained in one or more GPD files.

GPD files use the GPD language to describe a printer. The files contain [GPD file entries](gpd-file-entries.md) that use the GPD language to provide the following types of information:

-   [Printer attributes](printer-attributes.md) that describe printer characteristics.

-   [Printer commands](printer-commands.md) that control printer operations.

-   [Printer features](printer-features.md) describing the printer capabilities that can be controlled by Unidrv.

-   [Printer options](printer-options.md) representing the states that can be assigned to printer features.

-   [Printer font descriptions](printer-font-descriptions.md) that specify the characteristics associated with hardware-resident and cartridge fonts.

-   [Conditional statements](conditional-statements.md) that describe dependencies between printer attributes and a printer's configuration.

The GPD language also defines GPD file entries that control the following operations:

[Compressing raster data](compressing-raster-data.md)

[Handling color formats](handling-color-formats.md)

[Halftoning with Unidrv](halftoning-with-unidrv.md)

[Handling installable features and options](handling-installable-features-and-options.md)

[Describing printer memory configurations](describing-printer-memory-configurations.md)

This introductory section also includes discussions of [master units](master-units.md), [using multiple GPD files in a minidriver](using-multiple-gpd-files-in-a-minidriver.md), and [using resource DLLs in a minidriver](using-resource-dlls-in-a-minidriver.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Introduction%20to%20GPD%20Files%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




