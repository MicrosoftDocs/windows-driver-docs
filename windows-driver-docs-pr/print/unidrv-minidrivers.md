---
title: Unidrv Minidrivers
description: Unidrv Minidrivers
ms.assetid: ebf12f61-6194-4033-92a2-2bbccc40a6fd
keywords:
- Unidrv, minidrivers
- minidrivers WDK Unidrv
- text-based printer descriptions WDK Unidrv
- printer descriptions WDK Unidrv
- GPD files WDK Unidrv , Unidrv capabilities
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unidrv Minidrivers





Unidrv minidrivers are text files that contain descriptions of printers. Each minidriver describes one printer type from one manufacturer. This text-based description is called a generic printer description (GPD), and each file is called a GPD file. Each minidriver consists of one or more GPD files.

Using GPD files to describe a printer, Unidrv supports the following capabilities:

-   Generic, standard [printer features](printer-features.md) that are found on most printers.

-   Unique, customized printer features that only your printer provides.

-   Installable [printer options](printer-options.md), which can only be selected if the options are installed.

-   [Option constraints](option-constraints.md), which allow you to specify incompatible options.

-   [Conditional statements](conditional-statements.md), which allow you to specify that some printer characteristics are dependent on others.

-   Specification of [printer commands](printer-commands.md) that can include current values from a large selection of [standard variables](standard-variables.md). You can also perform arithmetic operations on these variables.

-   A customized help file, in addition to the standard help file provided with Unidrv, for describing customized features.

For information about creating GPD files, see [Introduction to GPD Files](introduction-to-gpd-files.md).

A Unidrv minidriver can consist of more than one GPD file. For more information, see [Using Multiple GPD Files in a Minidriver](using-multiple-gpd-files-in-a-minidriver.md).

When a printer is installed, Unidrv's GPD parser reads all the printer's GPD files. The information in the GPD files is used to create a temporary binary file for the printer. Both the [Unidrv user interface](unidrv-user-interface.md) and the [Unidrv renderer](unidrv-renderer.md) reference this binary file.

Typically, a minidriver must provide resources, such as fonts, bitmaps, and localizable text strings. These resources are placed in a resource DLL. For more information, see [Using Resource DLLs in a Minidriver](using-resource-dlls-in-a-minidriver.md).

 

 




