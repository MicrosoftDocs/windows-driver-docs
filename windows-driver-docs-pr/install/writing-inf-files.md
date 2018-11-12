---
title: Writing INF Files
description: Writing INF Files
ms.assetid: 0A31484C-3A61-4a6d-B500-E5C69E2130F9
keywords:
- INF files WDK device installations , writing
- writing INF files WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing INF Files


When you write an [INF file](inf-files.md) for your [driver package](driver-packages.md), you should follow these guidelines:

-   An INF file must use valid structure and syntax to pass driver package validation checks at the beginning of the installation process.

    Use the [INFVerif](../devtest/infverif.md) tool to validate the structure and syntax of INF files.

-   An INF file must contain valid INF [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) and [**SourceDisksNames**](inf-sourcedisksnames-section.md) sections. Starting with Windows Vista, the operating system does not copy the driver package into the [driver store](driver-store.md) unless these sections are present and filled in correctly.

-   It is sometimes necessary to copy INF files during device installation so that Windows can find them without repetitively displaying user prompts. For example, the base INF file for a multifunction device might copy the INF files for the device's individual functions so that Windows can find these INF files without prompting the user every time that it installs one of the device's functions.

    Starting with Windows XP, if you want to stage other INF files during an installation that is driven by an INF file, use the [**INF CopyINF directive**](inf-copyinf-directive.md).

    **Note**  Do not use the [**INF CopyFiles directive**](inf-copyfiles-directive.md) to copy INF files.

     

-   The components of a driver package must never directly copy or delete INF files directly into a system's *%SystemRoot%/Inf* directory. This results in the driver's digital signature to be invalidated, and this causes the driver not to load successfully.

 

 





