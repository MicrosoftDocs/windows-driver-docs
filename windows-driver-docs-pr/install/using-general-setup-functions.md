---
title: Using General Setup Functions
description: Using General Setup Functions
ms.assetid: 08a7b585-7930-47a3-9fa0-a36625242e5d
keywords: ["SetupAPI functions WDK , general Setup functions", "general Setup functions WDK SetupAPI"]
---

# Using General Setup Functions


## <a href="" id="ddk-using-general-setup-functions-dg"></a>


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20General%20Setup%20Functions%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




