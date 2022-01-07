---
title: Using a Universal INF File
description: If you are building a universal or mobile driver package, you must use a universal INF file.
ms.date: 04/28/2020
---

# Using a Universal INF File

Some editions of Windows use only a subset of the driver installation methods that are available on Windows 10 Desktop. An INF file for non-Desktop versions of Windows must perform only additive operations that do not depend on the runtime behavior of the system. An INF file with such restricted syntax is called a *universal INF file*.

A universal INF file installs predictably, with the same result each time. The results of the installation do not depend on the runtime behavior of the system. For example, co-installer references are not valid in a universal INF file because code in an additional DLL cannot be executed on an offline system.

A driver package with a universal INF file can be configured in advance and added to an offline system.

To test if your INF is universal, use `infverif /u`.
 
A [Windows Driver](../develop/getting-started-with-windows-drivers.md) must pass `infverif /w`, which tests `/u` as well as [Driver Package Isolation](../develop/driver-isolation.md).

For a list of InfVerif options, see [Running InfVerif from the command line](../devtest/running-infverif-from-the-command-line.md).

If you are building a Windows Desktop Driver package, you don't have to use a universal INF file, but doing so is recommended because of the performance benefits.

## Which INF sections are invalid in a universal INF file?

You can use any INF section in a universal INF file except for the following:

-   [**INF ClassInstall32 Section**](inf-classinstall32-section.md)
-   [**INF DDInstall.CoInstallers Section**](inf-ddinstall-coinstallers-section.md)
-   [**INF DDInstall.FactDef Section**](inf-ddinstall-factdef-section.md)
-   [**INF DDInstall.LogConfigOverride Section**](inf-ddinstall-logconfigoverride-section.md)

The [**INF Manufacturer Section**](inf-manufacturer-section.md) is valid as long as the **TargetOSVersion** decoration does not contain a **ProductType** flag or **SuiteMask** flag.

The [**INF DefaultInstall Section**](inf-defaultinstall-section.md) is valid only if it has an architecture decoration, for example `[DefaultInstall.NTAMD64]`.

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

-   The [**INF AddReg Directive**](inf-addreg-directive.md) is valid if entries in the specified *add-registry-section* have a *reg-root* value of **HKR**, or in the following cases:
	-	For registration of [Component Object Model](/windows/desktop/com) (COM) objects, a key may be written under:
		-	HKCR
		-	HKLM\SOFTWARE\Classes
	-	For creation of [Hardware Media Foundation Transforms](/windows/desktop/medfound/media-foundation-transforms) (MFTs), a key may be written under:
		-	HKLM\SOFTWARE\Microsoft\Windows Media Foundation
		-	HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows Media Foundation
		-	HKLM\SOFTWARE\WOW3232Node\Microsoft\Windows Media Foundation

-   [**INF CopyFiles Directive**](inf-copyfiles-directive.md) is valid only if the [destination directory](inf-destinationdirs-section.md) is one of the following:

    -   11 (corresponds to %WINDIR%\\System32)
    -   12 (corresponds to %WINDIR%\\System32\\Drivers)
    -   13 (corresponds to the directory under %WINDIR%\\System32\\DriverStore\\FileRepository where the driver is stored)  
        	**Note:**  CopyFiles may not be used to rename a file for which **DestinationDirs** includes *dirid* 13. Also, *dirid* 13 is only valid on Windows 10 products for a limited subset of device installation scenarios.  Please consult guidance and samples for your specific device class for more details.
    -   10,SysWOW64 (corresponds to %WINDIR%\\SysWOW64)
	-   10,*vendor-specific subdirectory name*  
			**Note:** In Windows 10, version 1709, using *dirid* 10 with a vendor-specific subdirectory name is valid in a universal INF as measured using the [InfVerif](../devtest/infverif.md) tool.  In later releases, this value may not be supported.  We recommend moving to *dirid* 13.

## See Also

* [Getting Started with Windows Drivers](../develop/getting-started-with-windows-drivers.md)
* [InfVerif](../devtest/infverif.md)
