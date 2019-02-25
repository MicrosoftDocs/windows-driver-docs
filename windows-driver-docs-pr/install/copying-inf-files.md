---
title: Copying INF Files
description: Copying INF Files
ms.assetid: 3ef92943-6462-4fe7-bd9b-8235083e8e16
keywords:
- INF files WDK device installations , copying
- copying INF files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Copying INF Files





It is sometimes necessary to copy INF files during device installation so that Windows can find them without repetitively displaying user prompts. For example, the base INF file for a multifunction device might copy the INF files for the device's individual functions so that Windows can find these INF files without prompting the user each time it installs one of the device's functions.

To copy INF files, an INF file can use the [**INF CopyINF directive**](inf-copyinf-directive.md).

Doing so will:

-   Install the appropriate catalog file, if it exists, along with the INF file.

-   Give the INF file a unique name so that it does not overwrite any other INF files, and will not be overwritten by other INF files.

-   Retain the path of the source medium from which device files are to be copied.

-   Ensure compatibility with future versions of Windows.

Installation software must never copy INF files directly into a system's *%SystemRoot%/inf* directory. Copying INF files by using techniques not described in this section will invalidate a driver's digital signature.

 

 





