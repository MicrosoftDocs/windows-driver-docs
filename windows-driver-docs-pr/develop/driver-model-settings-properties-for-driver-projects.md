---
ms.assetid: 3D0CB4E7-D1BC-44AA-93D9-5CCDE98C9691
title: Driver Model Settings Properties for Driver Projects
description: Sets the basic properties for a kernel-mode or user-mode driver, including the WDF library version and preprocessor definitions.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Model Settings Properties for Driver Projects

Sets the basic properties for a kernel-mode or user-mode driver, including the WDF library version and preprocessor definitions.

## Setting driver model properties for driver projects


1.  Open the property pages for your driver project. Right-click the driver project in **Solution Explorer** and select **Properties**.
2.  In the property pages for the driver project, click **Configuration Properties** and then click **Driver Model Settings**.
3.  Set the properties for the project.

**Type of driver**  
The type of driver when the driver **Configuration type** is **Driver**. Note that this option is available only when projects use the **WindowsKernelModeDriver8.0** toolset.

Possible values are:

* **WDM** (including all miniport/port drivers such as NDIS or StorPort).
* **KMDF** A KMDF driver.
* **Export driver (WDM)** A WDM driver that exports functions which other drivers can call. For more information, see [Creating Export Drivers](https://msdn.microsoft.com/Library/Windows/Hardware/Ff542891).

**KMDF Version Major**  
When the type of driver is KMDF, this option specifies the major version of KMDF that will be used when compiling your driver.

The KMDF\_VERSION\_MAJOR entry informs the MSBuild utility that it must link the driver to the KMDF library.

For more information, see [Framework Library Versioning](https://msdn.microsoft.com/Library/Windows/Hardware/Ff542842).

**KMDF Version Minor (Target Version)** (was **KMDF Version Minor** prior to Windows 10, version 1803)
When the type of driver is KMDF, this option specifies the minor version of KMDF that will be used when compiling your driver.

For more information, see [Framework Library Versioning](https://msdn.microsoft.com/Library/Windows/Hardware/Ff542842). If you do not specify **KMDF Version Minor (Target Version)**, Visual Studio uses the following defaults:
* Windows 10: 1.15
* Windows 8 / Windows 8.1: 1.11
* Windows 7: 1.9

**KMDF Version Minor (Minimum Required)** (optional, available starting in Windows 10, version 1803)
Starting in KMDF version 1.25 and UMDF version 2.25 on Windows 10 version 1803 (Redstone 4), you can build a KMDF driver that targets a span of framework versions. Use this optional setting to specify the minimum KMDF version of this range.

For details, see [Building a WDF driver for multiple versions of Windows](../wdf/building-a-wdf-driver-for-multiple-versions-of-windows.md).

**UMDF Version Major**  
When you have a UMDF driver, this option specifies the major version of UMDF that will be used when compiling your driver. See [UMDF Version History](https://msdn.microsoft.com/Library/Windows/Hardware/Ff561356). When you have a UMDF driver, the **Configuration type** is **Dynamic Library (.dll)**.

**UMDF Version Minor (Target Version)** (was **UMDF Version Minor** prior to Windows 10, version 1803)
When you have a UMDF driver, this option specifies the minor version of UMDF that will be used when compiling your driver. If you do not specify **UMDF Version Minor (Target Version)**, Visual Studio uses the following defaults:

For major version = 2:
* Windows 10: 2.15
* Others: 2.0

For major version = 1:
* Windows 8 and above: 1.11
* Windows 7: 1.9

**UMDF Version Minor (Minimum Required)** (optional, available starting in Windows 10, version 1803)

Starting in KMDF version 1.25 and UMDF version 2.25 on Windows 10 version 1803 (Redstone 4), you can build a UMDF driver that targets a span of framework versions. Use this optional setting to specify the minimum UMDF version of this range.

For details, see [Building a WDF driver for multiple versions of Windows](../wdf/building-a-wdf-driver-for-multiple-versions-of-windows.md).

**Allow Date, Time, and Timestamp**  
Defines the standard C/CPP macros for \_\_DATE\_\_, \_\_TIME\_\_, \_\_TIMESTAMP\_\_.

**Override Target Configuration Preprocessor Definitions**  
Overrides the default values for preprocessing symbols: \_WIN32\_WINNT, WINVER, WINNT, and NTDDI\_VERSION for your source file. Note that the default values are controlled by the current target configuration.

## Related topics


* [Framework Library Versioning](https://msdn.microsoft.com/Library/Windows/Hardware/Ff542842)
* [Building and Loading a Framework-based Driver](https://msdn.microsoft.com/Library/Windows/Hardware/Ff540730)
* [UMDF Version History](https://msdn.microsoft.com/Library/Windows/Hardware/Ff561356)
* [Building UMDF Drivers](https://msdn.microsoft.com/Library/Windows/Hardware/Ff540730)
* [Creating Export Drivers](https://msdn.microsoft.com/Library/Windows/Hardware/Ff542891)
 

 






