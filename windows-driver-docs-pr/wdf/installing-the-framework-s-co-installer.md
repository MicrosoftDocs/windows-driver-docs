---
title: Specifying the KMDF Co-installer in an INF File
description: If you include a co-installer in your driver package, read this topic for information about sections you must provide in your driver's INF file.
keywords:
- Kernel-Mode Driver Framework WDK , installing drivers
- framework-based drivers WDK KMDF , installing
- INF files WDK KMDF , coinstallers
- coinstallers WDK KMDF
- CoInstallers section WDK KMDF
- DDInstall section WDK KMDF
- Wdf INF file section WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying the KMDF Co-installer in an INF File

> [!NOTE]
> If your driver only targets Windows 10, you do not need to redistribute WDF or provide a Coinstaller in your driver package. To target Windows 10:
>1. In Visual Studio, in the **Project Settings** property page, under **Driver Settings** -> **Target OS Version**, select **Windows 10 or higher**.  This is equivalent to adding the following to the .vcxproj file: 
>```xml
><PropertyGroup Label="Configuration">
><TargetVersion>Windows10</TargetVersion>
>```
>2. In the [INF Manufacturer Section](../install/inf-manufacturer-section.md), specify 10.0 as target OS version, as follows:
>```inf
>[Manufacturer]
>%MyMfg% = MyMfg, NTamd64.10.0
>```

If you include a co-installer in your [driver package](../install/components-of-a-driver-package.md), read this topic for information about sections you must provide in your driver's INF file. This information does not apply if you provide your own setup application that calls Microsoft-supplied .msu redistributables.

##  INF File Sections for the Co-installer


Your driver's INF file must contain an INF <em>DDInstall</em>**.CoInstallers** section that installs the co-installer. For example this section might be named **MyDevice.ntx86.CoInstallers**. For more information about specifying a co-installer in an INF file, see [**INF DDInstall.CoInstallers Section**](../install/inf-ddinstall-coinstallers-section.md).

In addition, your driver's INF file must contain an INF <em>DDInstall</em>**.Wdf** section that the co-installer reads after it has been installed. For example, this section might be named **MyDevice.ntx86.Wdf**. After the framework's co-installer has been installed, it reads this section while it is installing your driver.

The INF <em>DDInstall</em>**.Wdf** section contains the following directive:

- **KmdfService =** <em>DriverService</em>**,**<em>Wdf-install-section</em>

*DriverService* represents the name that the operating system will assign to your driver's kernel-mode service, and *Wdf-install-section* represents the name of an INF section that the co-installer reads to obtain information about your driver.

The INF section that *Wdf-install-section* identifies must contain the following directive:

-   **KmdfLibraryVersion =** *WdfLibraryVersion*

*WdfLibraryVersion* represents a library version number, such as "1.0" or "1.11".

For example, the following INF <em>DDInstall</em>**.Wdf** section specifies **Echo\_wdfsect** as the *Wdf-install-section* name.

```cpp
[ECHO_Device.NT.Wdf]
KmdfService = Echo, Echo_wdfsect
[Echo_wdfsect]
KmdfLibraryVersion = 1.0
```

You can avoid creating multiple INF files for multiple versions of the framework by using INX files and the [Stampinf](../devtest/stampinf.md) tool. For more information about INX files, see [Using INX Files to Create INF Files](using-inx-files-to-create-inf-files.md).

### <a href="" id="sample-inf-ddinstall-coinstallers-and-ddinstall-wdf-sections"></a>**Sample INF** ***DDInstall*.CoInstallers and** ***DDInstall*.Wdf Sections**

The following code example shows how to create the INF <em>DDInstall</em>**.CoInstallers** section and INF <em>DDInstall</em>**.Wdf** section of an INF file for a PnP driver. The example shows how to create an INF file that is called *MyDevice.inf* and is based on the [ECHO](/samples/browse/) sample driver's *Echo.inf* file. The Echo sample driver is located in the samples directory of the WDK.

To create *MyDevice.inf*, you must change all **ECHO\_Device** substrings in *Echo.inf* to a name that is appropriate for your product. The following code example uses **MyDevice**.

You should attempt to match the section layout that the *Echo.inf* sample uses. In other words, if possible, keep the co-installer-related sections together to more easily spot cut-and-paste errors.

Before you have modified *echo.inf*, the sections that install the co-installer are as follows:

```cpp
=============== Top of Echo.inf ====================
....
....
[DestinationDirs]
DefaultDestDir = 12
ECHO_Device_CoInstaller_CopyFiles = 11
....
....
;
;--- ECHO_Device Co-installer installation ------
;
[ECHO_Device.NT.CoInstallers]
AddReg=ECHO_Device_CoInstaller_AddReg
CopyFiles=ECHO_Device_CoInstaller_CopyFiles

[ECHO_Device_CoInstaller_AddReg]
HKR,,CoInstallers32,0x00010000, "WdfCoInstaller01000.dll,WdfCoInstaller"

[ECHO_Device_CoInstaller_CopyFiles]
WdfCoInstaller01000.dll

[ECHO_Device.NT.Wdf]
KmdfService = Echo, Echo_wdfsect
[Echo_wdfsect]
KmdfLibraryVersion = 1.0

===============  End of Echo.inf ===============
```

After you have changed all **ECHO\_Device** substrings, your *MyDevice.inf* file should appear as follows:

```cpp
=============== Top of MyDevice.inf ===============
....
....
[DestinationDirs]
DefaultDestDir = 12
MyDevice_CoInstaller_CopyFiles = 11
....
....
;
;--- MyDevice Co-installer installation ------
;
[MyDevice.NT.CoInstallers]
AddReg=MyDevice_CoInstaller_AddReg
CopyFiles=MyDevice_CoInstaller_CopyFiles

[MyDevice_CoInstaller_AddReg]
HKR,,CoInstallers32,0x00010000, "WdfCoInstaller01000.dll,WdfCoInstaller"

[MyDevice_CoInstaller_CopyFiles]
WdfCoInstaller01000.dll

[MyDevice.NT.Wdf]
KmdfService = MyDevice, MyDevice_wdfsect
[MyDevice_wdfsect]
KmdfLibraryVersion = 1.0
....
....
=============== End of MyDevice.inf ===============
```