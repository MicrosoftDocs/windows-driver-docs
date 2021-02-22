---
title: Installing a File System Driver
description: Installing a File System Driver
keywords:
- drivers WDK file system , installing
- file system drivers WDK , installing
- creating an INF file , file system
- INF files WDK file system
- INF files WDK file system , about file system driver installation
- SetupAPI WDK file system
- Strings section WDK file system
- DefaultUninstall section WDK file system
- ServiceInstall section WDK file system
- DefaultInstall section WDK file system
- SourceDisksNames section WDK file system
- DestinationDirs section WDK file system
- Version section WDK file system
- creating INF files WDK file system
ms.date: 10/16/2019
ms.localizationpriority: medium
---

# Installing a File System Driver

## About Driver Installation

The Setup application programming interface ([SetupAPI](../install/setupapi.md)) provides the functions that control Windows setup and driver installation, including the installation of file system and file system filter drivers.

The installation process is controlled by INF files. For more information about INF files:

- For file system driver-specific INF file information, see [below](#creating-an-inf-file-for-a-file-system-driver)

- For more information about general driver installation (including information about driver packages, INF files, and driver signing), see [Device and Driver Installation](../install/index.md).

After creating an INF file, you will typically write the source code for your setup application. The setup application calls user-mode setup functions to access the information in the INF file and perform installation operations.

The following information regarding installing and uninstalling file system filter drivers also applies to file system drivers:

- [Using an INF File to Install a File System Filter Driver](using-an-inf-file-to-install-a-file-system-filter-driver.md)

- [Using an INF File to Uninstall a File System Filter Driver](using-an-inf-file-to-uninstall-a-file-system-filter-driver.md)

## Creating an INF File for a File System Driver

A file system driver's INF file provides instructions that SetupAPI uses to install the driver. The INF file is a text file that specifies the files that must be present for your driver to run and the source and destination directories for the driver files. An INF file also contains driver configuration information that SetupAPI stores in the registry, such as the driver's start type and load order group.

You can create a single INF file to install your driver on multiple versions of the Windows operating system. For more information about creating such an INF file, see [Creating INF Files for Multiple Platforms and Operating Systems](../install/creating-inf-files-for-multiple-platforms-and-operating-systems.md) and [Creating International INF Files](../install/creating-international-inf-files.md).

Starting with 64-bit versions of Windows Vista, all kernel-mode components, including non-PnP (Plug and Play) drivers such as file system drivers (file system, legacy filter, and minifilter drivers), must be signed in order to load and execute. For these versions of the Windows operating system, the following list contains information that is relevant to file system drivers.

- INF files for non-PnP drivers, including file system drivers, are not required to contain \[Manufacturer\] or \[Models\] sections.

- The [**SignTool**](../devtest/signtool.md) command-line tool, located in the \bin\SelfSign directory of the WDK installation directory, can be used to directly "embed sign" a driver SYS executable file. For performance reasons, boot-start drivers must contain an embedded signature.

- Given an INF file, the [**Inf2Cat**](../devtest/inf2cat.md) command-line tool can be used to create a catalog (.cat) file for a driver package.

- With Administrator privileges, an unsigned driver can still be installed on x64-based systems starting with Windows Vista. However, the driver will fail to load (and thus execute) because it is unsigned.

- For detailed information about the driving signing process, including the driving signing process for 64-bit versions of Windows Vista, see [Kernel-Mode Code Signing Walkthrough](https://go.microsoft.com/fwlink/p/?linkid=79445).

- All kernel-mode components, including custom kernel-mode development tools, must be signed. For more information, see [Signing Drivers during Development and Test (Windows Vista and Later)](../install/introduction-to-test-signing.md).

INF files cannot be used to read information from the registry or to launch a user-mode application.

## Sections in a File System Driver INF File

To construct your own file system driver INF file, use the following information as a guide. You can use the [InfVerif](../devtest/infverif.md) tool to check the syntax of your INF file.

An INF file for a file system driver generally contains the following sections.

- [Version (required)](#version-section-required)

- [DestinationDirs (optional but recommended)](#destinationdirs-section-optional-but-recommended)

- [SourceDisksNames (required)](#sourcedisksnames-section-required)

- [SourceDisksFiles (required)](#sourcedisksfiles-section-required)

- [DefaultInstall (required)](#defaultinstall-section-required)

- [DefaultInstall.Services (required)](#defaultinstallservices-section-required)

- [ServiceInstall (required)](#serviceinstall-section-required)

- [DefaultUninstall (optional)](#defaultuninstall-section-optional)

- [DefaultUninstall.Services (optional)](#defaultuninstallservices-section-optional)

- [Strings (required)](#strings-section-required)

### Version Section (required)

The [**Version**](../install/inf-version-section.md) section specifies the driver version information, as shown in the following code example.

```cpp
[Version]
Signature   = "$WINDOWS NT$"
Provider    = %Msft%
DriverVer   = 08/28/2000,1.0.0.1
CatalogFile =
```

The following table shows the values that file system filter drivers should specify in the [**Version**](../install/inf-version-section.md) section.

| Entry | Value |
| ----- | ----- |
| **Signature** | "$WINDOWS NT$" |
| **Provider** | In your own INF file, you should specify a provider other than Microsoft. |
| **DriverVer** | See [**INF DriverVer directive**](../install/inf-driverver-directive.md) |
| **CatalogFile** | Leave this entry blank. In the future, it will contain the name of a WHQL-supplied catalog file for signed drivers. |

### DestinationDirs Section (optional but recommended)

The [**DestinationDirs**](../install/inf-destinationdirs-section.md) section specifies the directories where the file system driver files will be copied.

In this section and in the **ServiceInstall** section, you can specify well-known system directories by using system-defined numeric values. For a list of these values, see [**INF DestinationDirs Section**](../install/inf-destinationdirs-section.md). In the following code example, the value "12" refers to the Drivers directory (%windir%\system32\drivers).

```cpp
[DestinationDirs]
DefaultDestDir = 12
ExampleFileSystem.DriverFiles = 12
```

### SourceDisksNames Section (required)

The [**SourceDisksNames**](../install/inf-sourcedisksnames-section.md) section specifies the distribution media to be used.

In the following code example, the [**SourceDisksNames**](../install/inf-sourcedisksnames-section.md) section lists a single distribution media for the file system driver. The unique identifier for the media is 1. The name of the media is specified by the %Disk1% token, which is defined in the **Strings** section of the INF file.

```cpp
[SourceDisksNames]
1 = %Disk1%
```

### SourceDisksFiles Section (required)

The [**SourceDisksFiles**](../install/inf-sourcedisksfiles-section.md) section specifies the location and names of the files to be copied.

In the following code example, the [**SourceDisksFiles**](../install/inf-sourcedisksfiles-section.md) section lists the file to be copied for the file system driver and specifies that the files can be found on the media whose unique identifier is 1 (This identifier is defined in the [**SourceDisksNames**](../install/inf-sourcedisksnames-section.md) section of the INF file.)

```cpp
[SourceDisksFiles]
examplefilesystem.sys = 1
```

### DefaultInstall Section (required)

In the [**DefaultInstall**](../install/inf-defaultinstall-section.md) section, a [**CopyFiles**](../install/inf-copyfiles-directive.md) directive copies the file system driver's driver files to the destination that is specified in the [**DestinationDirs**](../install/inf-destinationdirs-section.md) section.

> [!NOTE]
> The [**CopyFiles**](../install/inf-copyfiles-directive.md) directive should not refer to the catalog file or the INF file itself; SetupAPI copies these files automatically.

You can create a single INF file to install your driver on multiple versions of the Windows operating system. This type of INF file is created by creating additional [**DefaultInstall**](../install/inf-defaultinstall-section.md), [**DefaultInstall.Services**](../install/inf-defaultinstall-services-section.md), **DefaultUninstall**, and **DefaultUninstall.Services** sections for each operating system version. Each section is labeled with a *decoration* (for example, .ntx86, .ntia64, or .nt) that specifies the operating system version to which it applies. For more information about creating this type of INF file, see [Creating INF Files for Multiple Platforms and Operating Systems](../install/creating-inf-files-for-multiple-platforms-and-operating-systems.md).

In the following code example, the [**CopyFiles**](../install/inf-copyfiles-directive.md) directive copies the files that are listed in the ExampleFileSystem.DriverFiles section of the INF file.

```cpp
[DefaultInstall]
OptionDesc = %ServiceDesc%
CopyFiles = ExampleFileSystem.DriverFiles

[ExampleFileSystem.DriverFiles]
examplefilesystem.sys
```

### DefaultInstall.Services Section (required)

The [**DefaultInstall.Services**](../install/inf-defaultinstall-services-section.md) section contains an [**AddService**](../install/inf-addservice-directive.md) directive that controls how and when the services of a particular driver are loaded.

In the following code example, the [**AddService**](../install/inf-addservice-directive.md) directive adds the file system service to the operating system. The %ServiceName% token contains the service name string, which is defined in the **Strings** section of the INF file. ExampleFileSystem.Service is the name of the file system driver's **ServiceInstall** section.

```cpp
[DefaultInstall.Services]
AddService = %ServiceName%,,ExampleFileSystem.Service
```

### ServiceInstall Section (required)

The **ServiceInstall** section adds subkeys or value names to the registry and sets values. The name of the **ServiceInstall** section must appear in an [**AddService directive**](../install/inf-addservice-directive.md) in the [**DefaultInstall.Services section**](../install/inf-defaultinstall-services-section.md).

The following code example shows the **ServiceInstall** section for the file system driver.

```cpp
[ExampleFileSystem.Service]
DisplayName    = %ServiceName%
Description    = %ServiceDesc%
ServiceBinary  = %12%\examplefilesystem.sys
ServiceType    = 2 ;    SERVICE_FILE_SYSTEM_DRIVER
StartType      = 1 ;    SERVICE_SYSTEM_START
ErrorControl   = 1 ;    SERVICE_ERROR_NORMAL
LoadOrderGroup = "File System"
AddReg         = ExampleFileSystem.AddRegistry
```

The **DisplayName** entry specifies the name for the service. In the preceding example, the service name string is specified by the %ServiceName% token, which is defined in the **Strings** section of the INF file.

The **Description** entry specifies a string that describes the service. In the preceding example, this string is specified by the %ServiceDesc% token, which is defined in the **Strings** section of the INF file.

The **ServiceBinary** entry specifies the path to the executable file for the service. In the preceding example, the value 12 refers to the Drivers directory (%windir%\system32\drivers).

The **ServiceType** entry specifies the type of service. The following table lists the possible values for **ServiceType** and their corresponding service types.

| Value | Description |
| ----- | ----------- |
| 0x00000001 | SERVICE_KERNEL_DRIVER (Device driver service) |
| 0x00000002 | SERVICE_FILE_SYSTEM_DRIVER (File system or file system filter driver service) |
| 0x00000010 | SERVICE_WIN32_OWN_PROCESS (Microsoft Win32 service that runs in its own process) |
| 0x00000020 | SERVICE_WIN32_SHARE_PROCESS (Win32 service that shares a process) |

The **ServiceType** entry should always be set to SERVICE_FILE_SYSTEM_DRIVER for a file system driver.

The **StartType** entry specifies when to start the service. The following table lists the possible values for **StartType** and their corresponding start types.

| Value | Description |
| ----- | ----------- |
| 0x00000000 | SERVICE_BOOT_START |
| 0x00000001 | SERVICE_SYSTEM_START |
| 0x00000002 | SERVICE_AUTO_START |
| 0x00000003 | SERVICE_DEMAND_START |
| 0x00000004 | SERVICE_DISABLED |

For detailed descriptions of these start types to determine which one is appropriate for your file system driver, see [What Determines When a Driver Is Loaded](what-determines-when-a-driver-is-loaded.md).

Starting with x64-based Windows Vista systems, the binary image file of a boot-start driver (a driver that has a start type of SERVICE_BOOT_START) must contain an embedded signature. This requirement ensures optimal system boot performance. For more information, see [Kernel-Mode Code Signing Walkthrough](https://go.microsoft.com/fwlink/p/?linkid=79445).

For information about how the **StartType** and **LoadOrderGroup** entries determine when the driver is loaded, see [What Determines When a Driver Is Loaded](what-determines-when-a-driver-is-loaded.md).

The **ErrorControl** entry specifies the action to be taken if the service fails to start during system startup. The following table lists the possible values for **ErrorControl** and their corresponding error control values.

| Value | Description |
| ----- | ----------- |
| 0x00000000 | SERVICE_ERROR_IGNORE (Log the error and continue system startup.) |
| 0x00000001 | SERVICE_ERROR_NORMAL (Log the error, display a message to the user, and continue system startup.) |
| 0x00000002 | SERVICE_ERROR_SEVERE (Switch to the registry's LastKnownGood control set and continue system startup. |
| 0x00000003 | SERVICE_ERROR_CRITICAL (If system startup is not using the registry's LastKnownGood control set, switch to LastKnownGood and try again. If startup still fails, run a bug-check routine. Only the drivers that are needed for the system to startup should specify this value in their INF files.) |

The **LoadOrderGroup** entry must always be set to "File System" for a file system driver. This is different from what is specified for a file system filter driver or file system minifilter driver where the **LoadOrderGroup** entry is set to one of the file system filter load order groups. For more information about the load order groups that are used for file system filter drivers and file system minifilter drivers, see [Load Order Groups for File System Filter Drivers](load-order-groups-for-file-system-filter-drivers.md) and [Load Order Groups and Altitudes for Minifilter Drivers](load-order-groups-and-altitudes-for-minifilter-drivers.md).

The [**AddReg directive**](../install/inf-addreg-directive.md) refers to one or more INF writer-defined **AddRegistry** sections that contain any information to be stored in the registry for the newly installed service.

>[!NOTE]
> If the INF file will also be used for upgrading the driver after the initial install, the entries that are contained in the **AddRegistry** section should specify the 0x00000002 (FLG_ADDREG_NOCLOBBER) flag. Specifying this flag preserves the registry entries in HKLM\CurrentControlSet\Services when subsequent files are installed. For example:

```cpp
[ExampleFileSystem.AddRegistry]
HKR,Parameters,ExampleParameter,0x00010003,1
```

### DefaultUninstall Section (optional)

The **DefaultUninstall** section is optional but recommended if your driver can be uninstalled. It contains [**DelFiles**](../install/inf-delfiles-directive.md) and [**DelReg**](../install/inf-delreg-directive.md) directives to remove files and registry entries.

In the following code example, the [**DelFiles**](../install/inf-delfiles-directive.md) directive removes the files that are listed in the ExampleFileSystem.DriverFiles section of the INF file.

```cpp
[DefaultUninstall]
DelFiles   = ExampleFileSystem.DriverFiles
DelReg     = ExampleFileSystem.DelRegistry
```

The [**DelReg**](../install/inf-delreg-directive.md) directive refers to one or more INF writer-defined **DelRegistry** sections that contain any information to be removed from the registry for the service that is being uninstalled.

### DefaultUninstall.Services Section (optional)

The **DefaultUninstall.Services** section is optional but recommended if your driver can be uninstalled. It contains [**DelService**](../install/inf-delservice-directive.md) directives to remove the file system driver's services.

In the following code example, the [**DelService**](../install/inf-delservice-directive.md) directive removes the file system driver's service from the operating system.

```cpp
[DefaultUninstall.Services]
DelService = %ServiceName%,0x200
```

> [!NOTE]
> The [**DelService**](../install/inf-delservice-directive.md) directive should always specify the 0x200 (SPSVCINST_STOPSERVICE) flag to stop the service before it is deleted.

> [!NOTE]
> There are certain classes of file system products that cannot be completely uninstalled. In this situation, it is acceptable to just uninstall the components of the product that can be uninstalled and leave installed the components of the product that cannot be uninstalled. An example of such a product is the Microsoft Single Instance Store (SIS) feature.

### Strings Section (required)

The [**Strings**](../install/inf-strings-section.md) section defines each %strkey% token that is used in the INF file.

For example, the file system driver defines the following strings in its INF file.

```cpp
[Strings]
Msft        = "Microsoft Corporation"
ServiceDesc = "Example File System Driver"
ServiceName = "ExampleFileSystem"
ParameterPath = "SYSTEM\CurrentControlSet\Services\ExampleFileSystem\Parameters"
Disk1       = "Example File System Driver CD"
```

You can create a single international INF file by creating additional locale-specific **Strings**.*LanguageID* sections in the INF file. For more information about international INF files, see [Creating International INF Files](../install/creating-international-inf-files.md).
