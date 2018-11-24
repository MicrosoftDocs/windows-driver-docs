---
title: Introduction to GPD Files
description: Introduction to GPD Files
ms.assetid: f29415cf-d8ca-42a2-bbae-2be53e3621a6
keywords:
- generic printer description WDK Unidrv
- GPD files WDK Unidrv
- Unidrv, GPD files
- GPD files WDK Unidrv , about GPD files
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to GPD Files





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

 

 




