---
title: General Guidelines for INF Files
description: General Guidelines for INF Files
ms.assetid: a0394708-46ed-47f8-a629-0c7d3088df3b
keywords:
- INF files WDK device installations , general guidelines
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General Guidelines for INF Files





INF files have many common parts and follow a single set of syntax rules. However, they are also as different as the variety of devices that are supported by Microsoft Windows. When you write an INF file, refer to the following sources of information:

-   This section and the [INF File Sections and Directives](inf-file-sections-and-directives.md) reference material.

-   The documentation for your class of device.

    For example, if your device is a printer, see [Installing and Configuring Printer Drivers](https://msdn.microsoft.com/library/windows/hardware/ff551648).

-   WDK tools for INF files.

    For more information, see [Tools for INF Files](https://msdn.microsoft.com/library/windows/hardware/ff552956). These tools are included in the \\Tools subdirectory of the WDK.

-   Sample INF files and INF files for similar devices.

    The WDK includes INF files for its sample drivers. Look through the sample drivers to see whether there are INF files for devices similar to your device.

You can create or modify an INF file by using any text editor in which you can control the insertion of line breaks. If your INF contains non-ASCII characters, save the file as a Unicode file.

INF files that ship with Windows 7 and earlier operating systems must have a file name of <em>xxxxxxxx</em>**.inf**, where "*xxxxxxxx*" does not exceed eight characters. The name of an INF file that ships separately from the operating system is not limited to eight characters.

Beginning with Windows 8, INF file names are not limited to eight characters, regardless if they ship with the operating system or not.

Do not arbitrarily modify the time stamps of your INF files, as a version control mechanism. Version control of INF files should be based on a date and version number that is specified in an [**INF Version section**](inf-version-section.md).

 

 





