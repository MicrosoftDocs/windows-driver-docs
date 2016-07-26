---
title: Using a Universal INF File
description: If you are building a universal or mobile driver package, you must use a universal INF file.
ms.assetid: 2CBEB814-974D-4E8B-A44A-2CFAA8D4C94E
---

# Using a Universal INF File


If you are building a universal or mobile driver package, you must use a universal INF file. If you are building a desktop driver package, you don't have to use a universal INF file, but doing so is recommended because of the performance benefits.

A universal INF file uses a subset of the [INF syntax](inf-file-sections-and-directives.md) that is available to a Windows driver. A universal INF file installs a driver and configures device hardware, but does not perform any other action, such as running a co-installer.

## Why is a universal INF file required on OneCoreUAP-based, non-desktop editions of Windows?


Some editions of Windows, such as Windows 10 Mobile, do not support the Plug and Play mechanism for driver installation. Therefore, driver installation takes place on an offline image of the target system. When Microsoft Visual Studio builds your driver for such a target system, it generates an XML-based configuration file that contains all of the registry settings to be applied. As a result, an INF file for such a system must perform only additive operations that do not depend on the runtime behavior of the system. An INF file with such restricted syntax is called a universal INF file.

A universal INF file installs predictably, with the same result each time. The results of the installation do not depend on the runtime behavior of the system. For example, co-installer references are not valid in a universal INF file because code in an additional DLL cannot be executed on an offline system.

As a result, a driver package with a universal INF file can be configured in advance and added to an offline system.

You can use the [InfVerif](https://msdn.microsoft.com/library/windows/hardware/dn929319) tool to test if your driver's INF file is universal.

## Which INF sections are invalid in a universal INF file?


You can use any INF section in a universal INF file except for the following:

-   [**INF ClassInstall32 Section**](inf-classinstall32-section.md)
-   [**INF DDInstall.CoInstallers Section**](inf-ddinstall-coinstallers-section.md)
-   [**INF DDInstall.FactDef Section**](inf-ddinstall-factdef-section.md)
-   [**INF DDInstall.LogConfigOverride Section**](inf-ddinstall-logconfigoverride-section.md)

The [**INF Manufacturer Section**](inf-manufacturer-section.md) is valid as long as the **TargetOSVersion** decoration does not contain a **ProductType** flag or **SuiteMask** flag.

## Which INF directives are invalid in a universal INF file?


You can use any INF directive in a universal INF file except for the following:

-   [**INF BitReg Directive**](inf-bitreg-directive.md)
-   [**INF DelFiles Directive**](inf-delfiles-directive.md)
-   [**INF DelProperty Directive**](inf-delproperty-directive.md)
-   [**INF DelReg Directive**](inf-delreg-directive.md)
-   [**INF DelService Directive**](inf-delservice-directive.md)
-   [**INF Ini2Reg Directive**](inf-ini2reg-directive.md)
-   [**INF LogConfig Directive**](inf-logconfig-directive.md)
-   [**INF ProfileItems Directive**](inf-profileitems-directive.md)
-   [**INF RegisterDlls Directive**](inf-registerdlls-directive.md)
-   [**INF RenFiles Directive**](inf-renfiles-directive.md)
-   [**INF UnregisterDlls Directive**](inf-unregisterdlls-directive.md)
-   [**INF UpdateIniFields Directive**](inf-updateinifields-directive.md)
-   [**INF UpdateInis Directive**](inf-updateinis-directive.md)

The following directives are valid with some caveats:

-   The [**INF AddReg Directive**](inf-addreg-directive.md) is valid only if entries in the specified *add-registry-section* have a *reg-root* value of **HKR**.

-   [**INF CopyFiles Directive**](inf-copyfiles-directive.md) is valid only if the destination directory is one of the following:

    -   11 (corresponds to %WINDIR%\\System32)
    -   12 (corresponds to %WINDIR%\\System32\\Drivers)

## Related topics


[Installing a Universal Windows driver](https://msdn.microsoft.com/windows-drivers/develop/installing_a_universal_driver)

[InfVerif](https://msdn.microsoft.com/library/windows/hardware/dn929319)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20a%20Universal%20INF%20File%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





