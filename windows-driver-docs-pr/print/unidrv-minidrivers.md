---
title: Unidrv Minidrivers
author: windows-driver-content
description: Unidrv Minidrivers
ms.assetid: ebf12f61-6194-4033-92a2-2bbccc40a6fd
keywords:
- Unidrv, minidrivers
- minidrivers WDK Unidrv
- text-based printer descriptions WDK Unidrv
- printer descriptions WDK Unidrv
- GPD files WDK Unidrv , Unidrv capabilities
- Unidrv WDK print
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Unidrv Minidrivers


## <a href="" id="ddk-unidrv-minidrivers-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Unidrv%20Minidrivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


