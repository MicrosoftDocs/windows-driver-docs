---
title: Using General Setup Functions
description: Using General Setup Functions
ms.assetid: 08a7b585-7930-47a3-9fa0-a36625242e5d
keywords:
- SetupAPI functions WDK , general Setup functions
- general Setup functions WDK SetupAPI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using General Setup Functions





This section summarizes the general Setup functions. [*Device installation applications*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) can use these functions to do the following:

-   Read and process INF files.

-   Determine the amount of free space that is required on the installation's target system.

-   Move files from installation source media to media on the installation's target system, while requesting user intervention as needed.

-   Create a log of files moved during an installation.

-   Write log entries to the [SetupAPI text logs](setupapi-text-logs.md).

Installation software typically uses these functions together with [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299) and [PnP configuration manager functions](https://msdn.microsoft.com/library/windows/hardware/ff549713).

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

[SetupAPI Logging Functions](setupapi-logging-functions.md)

 

 





