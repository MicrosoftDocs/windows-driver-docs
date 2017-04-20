---
title: SetupAPI
description: SetupAPI
ms.assetid: aa12ec50-2842-4ddd-9fc5-84436d69ea7a
keywords:
- SetupAPI WDK device installations , functions
- SetupAPI functions WDK , about SetupAPI functions
- SetupAPI functions WDK
- Device setup WDK device installations , SetupAPI
- device installations WDK , SetupAPI
- installing devices WDK , SetupAPI
- functions WDK SetupAPI
- device installations WDK , SetupAPI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SetupAPI


## <a href="" id="ddk-using-setupapi-functions-dg"></a>


The Setup application programming interface (SetupAPI) is a system component that provides two sets of functions:

-   [General setup functions](https://msdn.microsoft.com/library/windows/hardware/ff544985)

-   [Device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299)

Device installation software can use these functions to perform custom operations in [*class installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-installer), [*co-installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer), and [*device installation applications*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application).

For device installation applications, Driver Install Frameworks (DIFx) provides high-level tools that abstract the low-level SetupAPI operations that install Plug and Play (PnP) function drivers and manage the association between application software and the drivers. If the DIFx tools provide the functionality that an installation application requires to install PnP drivers and application software for devices, the installation application should use the DIFx tools instead of directly calling SetupAPI functions. However, co-installers and class installers are Microsoft Win32 DLLs that assist the default installation operation by performing custom operations for a device or all devices in a [device setup class](device-setup-classes.md). These operations typically require direct calls to Win32 functions and SetupAPI functions.

This section contains the following topics, which provide general information about how to use the [general Setup functions](https://msdn.microsoft.com/library/windows/hardware/ff544985) and [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299) that are provided by SetupAPI:

[Using General Setup Functions](using-general-setup-functions.md)

[Using Device Installation Functions](using-device-installation-functions.md)

[Typical SetupAPI Usage](typical-setupapi-usage.md)

[Guidelines for Using SetupAPI](guidelines-for-using-setupapi.md)

**Note**  This section describes only a subset of the Setup functions in SetupAPI. For more information about this API, see [Setup API](http://go.microsoft.com/fwlink/p/?linkid=192108) .

 

 

 





