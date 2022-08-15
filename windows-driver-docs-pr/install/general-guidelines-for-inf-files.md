---
title: General Guidelines for INF Files
description: General Guidelines for INF Files
keywords:
- INF files WDK device installations , general guidelines
ms.date: 01/14/2022
---

# General Guidelines for INF Files

INF files have many common parts and follow a single set of syntax rules. However, they are also as different as the variety of devices that are supported by Microsoft Windows. When you write an INF file, refer to the following sources of information:

-   This section and the summary of [INF sections](summary-of-inf-sections.md) and [INF directives](summary-of-inf-directives.md) reference material.

-   The documentation for your class of device.

    For example, if your device is a printer, see [Installing and Configuring Printer Drivers](../print/installing-and-configuring-printer-drivers.md).

-   WDK tools for INF files.

    For more information, see [Tools for INF Files](../devtest/tools-for-inf-files.md). These tools are included in the \\Tools subdirectory of the WDK.

-   Sample INF files and INF files for similar devices.

    Look through the [sample drivers](https://github.com/Microsoft/Windows-driver-samples) to see whether there are INF files for devices similar to your device.

You can create or modify an INF file by using any text editor in which you can control the insertion of line breaks. If your INF contains non-ASCII characters, save the file as a Unicode (UTF-16) file.

Do not arbitrarily modify the time stamps of your INF files, as a version control mechanism. Version control of INF files should be based on a date and version number that is specified via the *DriverVer* directive in an [**INF Version section**](inf-version-section.md).

## Best Practices for Naming and Versioning Your INF File

- INF names should be named in a way that reduces the chance of conflicts with INFs from other vendors.  For example, the INF name could include in it, either as a prefix or a suffix, an abbreviation of your company name.
- If you have two different variants of the same driver package differing in aspects such as branding strings, settings, etc., those two driver packages should have unique names.
- Each time you update an INF or any file the INF references, you should update the date and version in the INF.
