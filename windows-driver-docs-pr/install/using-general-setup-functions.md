---
title: Using General Setup Functions
description: Using General Setup Functions
keywords:
- SetupAPI functions WDK , general Setup functions
- general Setup functions WDK SetupAPI
ms.date: 03/11/2022
---

# Using General Setup Functions

This section summarizes the general Setup functions. Applications can use these functions to do the following:

-   Read and process INF files.

-   Determine the amount of free space that is required on the installation's target system.

-   Move files from installation source media to media on the installation's target system, while requesting user intervention as needed.

-   Create a log of files moved during an installation.

> [!NOTE]
> The general setup functions are intended to be used with INF files that are not [driver package](driver-packages.md) INF files if an application is using processing of an INF file to install various of its own components.  For driver packages, the standard driver package and device installation APIs should be used.

The general Setup functions listed in this section are described in detail in the Microsoft Windows SDK documentation.

This section includes the following topics:

[INF File Processing Functions](inf-file-processing-functions.md)

[Disk Prompting and Error Handling Functions](disk-prompting-and-error-handling-functions.md)

[File Queuing Functions](file-queuing-functions.md)

[Default Queue Callback Routine Functions](default-queue-callback-routine-functions.md)

[Cabinet File Function](cabinet-file-function.md)

[Disk-Space List Functions](disk-space-list-functions.md)

[MRU Source List Functions](mru-source-list-functions.md)

[File Log Functions](file-log-functions.md)

[User Interface Functions](user-interface-functions.md)
