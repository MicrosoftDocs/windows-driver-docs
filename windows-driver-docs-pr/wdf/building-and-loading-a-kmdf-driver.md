---
title: Building and Loading a WDF Driver
description: This topic describes how to select a target operating system and framework version for a driver project in Visual Studio. It also describes the co-installer and how to determine if you should include this component in your driver package.
ms.assetid: 82c77b1f-4bf0-46d9-bae3-822e9be5a7fb
keywords: ["kernel-mode drivers WDK KMDF , building drivers", "KMDF WDK , building drivers", "Kernel-Mode Driver Framework WDK , building drivers", "kernel-mode drivers WDK KMDF , loading drivers", "KMDF WDK , loading drivers", "Kernel-Mode Driver Framework WDK , loading drivers", "building drivers WDK , KMDF", "loading drivers WDK KMDF", "Build utility WDK , KMDF", "KMDF drivers WDK KMDF , building", "KMDF drivers WDK KMDF , loading"]
---

# Building and Loading a WDF Driver


This topic describes how to select a target operating system and framework version for a driver project in Visual Studio. It also describes the co-installer and how to determine if you should include this component in your driver package.

## Which framework version should I use?


If your driver needs to run only on Windows 8.1, use Kernel-Mode Driver Framework (KMDF) version 1.13 or User-Mode Driver Framework (UMDF) version 2.0.

If your driver must work on operating systems earlier than Windows 8.1, we recommend that you use KMDF or UMDF version 1.11.

You can use the Windows Driver Kit (WDK) that ships with Windows 8.1 to build KMDF 1.9, 1.11, and 1.13 drivers, as well as UMDF 1.9, 1.11, and 2.0 drivers.

## How do I set the versions in Visual Studio?


If you're building your driver project for the latest version of Windows and the most recent KMDF or UMDF version, you can keep the defaults and skip this step.

Otherwise, follow these steps:

-   Change the **Project Configuration** setting in the **Configuration Manager** to an appropriate value (such as **Win7 Debug**).
-   Change the KMDF\_VERSION\_MINOR or UMDF\_VERSION\_MINOR value in the [Driver Model Settings](https://msdn.microsoft.com/windows-drivers/develop/driver_model_settings_properties_for_driver_projects) to an appropriate value (such as 11).

For detailed information about KMDF and UMDF versions, see [KMDF Version History](kmdf-version-history.md) and [UMDF Version History](umdf-version-history.md).

## When do I need to include a co-installer or .msu in my driver package?


If you build a driver for Windows 8.1 using KMDF 1.13 or UMDF 2.0, you do not need to include a co-installer, custom installer, or reference in the INF file.

If your driver must work on operating systems earlier than Windows 8.1, we recommend that you use KMDF or UMDF version 1.11, and that you include Microsoft-supplied framework updates in your driver package.

The framework updates make it possible to run a driver built with a later framework version than the one included in an operating system. For example, KMDF 1.11 is included in Windows 8. But you can run a KMDF 1.11 driver on Windows Vista or Windows 7. Before you can do so, however, you must ensure that the KMDF 1.11 framework library replaces the framework library included in the earlier operating system (in this case, KMDF 1.7 and KMDF 1.9 respectively). You do this by redistributing a Microsoft-supplied co-installer or .msu file with your driver package.

## Linking and loading


When you build a Windows Driver Frameworks (WDF) project in Microsoft Visual Studio, MSBuild links your driver to the appropriate framework library, the library's loader, and a stub file, all of which are included in the WDK. (The library and loader are also included in the framework's [co-installer](installing-the-framework-s-co-installer.md) so that if necessary, you can distribute them with your driver package.)

The stub file contains a special entry point routine: **FxDriverEntry**. MSBuild sets the stub's **FxDriverEntry** routine as the initial entry point for framework-based drivers.

When the operating system loads a framework-based driver, it also loads the stub file and the library's loader. Next, the system calls the stub file's **FxDriverEntry** routine. This routine then calls the loader. The loader determines the version of the framework library that the driver requires and then loads the correct [version of the library](framework-library-versioning.md) as a kernel-mode service (if it is not already loaded). Finally, the library calls the driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) routine.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Building%20and%20Loading%20a%20WDF%20Driver%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




