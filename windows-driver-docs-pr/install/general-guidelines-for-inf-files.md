---
title: General guidelines for INF files
description: Provides general guidelines for INF files.
keywords:
- INF files WDK device installations, general guidelines
ms.date: 03/23/2023
---

# General guidelines for INF files

INF files have many common parts and follow a single set of syntax rules. However, they are also as different as the variety of devices that are supported by Microsoft Windows. When you write an INF file, refer to the following sources of information:

- This section and the summary of [INF sections](summary-of-inf-sections.md) and [INF directives](summary-of-inf-directives.md) reference material

- An INF file must use valid structure and syntax to pass driver package validation checks at the beginning of the installation process.

    Use the [INFVerif](../devtest/infverif.md) tool to validate the structure and syntax of INF files.

- An INF file must contain valid INF [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) and [**SourceDisksNames**](inf-sourcedisksnames-section.md) sections. Starting with Windows Vista, the operating system does not copy the driver package into the [driver store](driver-store.md) unless these sections are present and filled in correctly.

- The documentation for your class of device

    For example, if your device is a printer, see [Installing and configuring printer drivers](../print/installing-and-configuring-printer-drivers.md).

- WDK tools for INF files

    For more information, see [Tools for INF files](../devtest/tools-for-inf-files.md). These tools are included in the \\Tools subdirectory of the WDK.

- Sample INF files and INF files for similar devices

    Look through the [sample drivers](https://github.com/Microsoft/Windows-driver-samples) to see whether there are INF files for devices similar to your device.

- The components of a driver package must never directly copy or delete INF files directly in a system's *%SystemRoot%/Inf* directory.

## Editing INF files and file encodings

You can create or modify an INF file by using any text editor in which you can control the insertion of line breaks. The file must be saved with an ANSI or Unicode (UTF-16 LE) file encoding. Unicode (UTF-16 LE) is preferred since it allows the INF to support localizing the [INF Strings section](./inf-strings-section.md) in a wide variety of languages. If your INF contains non-ASCII characters, you must save the file as a Unicode (UTF-16 LE) file.

## Best practices for naming and versioning your INF file

- INF names should be named in a way that reduces the chance of conflicts with INFs from other vendors.  For example, the INF name could include in it, either as a prefix or a suffix, an abbreviation of your company name.

- If you have two different variants of the same driver package differing in aspects such as branding strings, settings, and so on, those two driver packages should have unique names.

- Do not arbitrarily modify the time stamps of your INF files as a version control mechanism. Version control of INF files should be based on a date and version number that is specified via the [**INF DriverVer directive**](inf-driverver-directive.md) directive in an [**INF Version section**](inf-version-section.md).

- Each time you update an INF or any file the INF references, you should update the date and version in the [**INF DriverVer directive**](inf-driverver-directive.md) directive in the INF.
