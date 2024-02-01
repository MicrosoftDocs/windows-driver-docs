---
title: Creating an INF File for a Minifilter Driver
description: Describes how to create an INF file for a filter driver
keywords:
- INF files WDK file system , minifilter drivers
- INF files WDK file system , filter drivers
- DestinationDirs section WDK file system
- Version section WDK file system
- Strings section WDK file system
- ServiceInstall section WDK file system
- DefaultInstall section WDK file system
- AddRegistry section WDK file system
ms.date: 05/05/2023
---

# Creating an INF file for a minifilter driver

## Introduction

> [!NOTE]
>
> Starting in Windows 10 version 1903, INF requirements for primitive drivers (such as file system minifilter drivers) changed. See [Creating a new primitive driver](../develop/creating-a-primitive-driver.md) for details.

Filter drivers need an INF file to be installed on the Windows operating system. You'll find sample INF files in the [minifilter samples](https://github.com/Microsoft/Windows-driver-samples/tree/main/filesys/miniFilter).

An INF file for a file system filter driver generally contains the following sections:

| Section                       | Notes |
| -------                       | ----- |
| **Version**                   | Required |
| **DestinationDirs**           | Optional but recommended |
| **DefaultInstall**            | Required |
| **DefaultInstall.Services**   | Required |
| **ServiceInstall**            | Required |
| **AddRegistry**               | Required |
| **Strings**                   | Required |

> [!NOTE]
>
> Starting with Windows 10 version 1903, the **DefaultUninstall** and **DefaultUninstall.Services** sections are prohibited, [(with exception)](../develop/creating-a-primitive-driver.md#legacy-compatibility). These sections were optional in prior OS versions.
>
> All drivers running on 64-bit versions of Windows systems must be signed before Windows will load them. See [Signing a driver](../develop/signing-a-driver.md) for more information.

## Version Section (required)

The [**Version**](../install/inf-version-section.md) section specifies a class and GUID that are determined by the type of minifilter driver, as shown in the following code example.

```inf
[Version]
Signature   = "$WINDOWS NT$"
Class       = "ActivityMonitor"
ClassGuid   = {b86dff51-a31e-4bac-b3cf-e8cfe75c9fc2}
Provider    = %Msft%
DriverVer   = 10/09/2001,1.0.0.0
CatalogFile =
PnpLockdown = 1
```

The following table shows the values that file system minifilter drivers should specify in the [**Version**](../install/inf-version-section.md) section.

| Entry | Value |
| ----- | ----- |
| **Signature** | "$WINDOWS NT$" |
| **Class** | See [File System Filter Driver Classes and Class GUIDs](file-system-filter-driver-classes-and-class-guids.md). |
| **ClassGuid** | See [File System Filter Driver Classes and Class GUIDs](file-system-filter-driver-classes-and-class-guids.md). |
| **Provider** | In your own INF file, you should specify a provider other than Microsoft. |
| **DriverVer** | See [INF DriverVer directive](../install/inf-driverver-directive.md). |
| **CatalogFile** | For antivirus minifilter drivers that are signed, this entry contains the name of a [WHQL-supplied catalog file](../install/catalog-files.md). All other minifilter drivers should leave this entry blank. For more information, see the description of the **CatalogFile** entry in [INF Version Section](../install/inf-version-section.md) |

## DestinationDirs Section (optional but recommended)

The [**DestinationDirs**](../install/inf-destinationdirs-section.md) section specifies the directories where minifilter driver and application files will be copied.

In this section and in the **ServiceInstall** section, you can specify well-known system directories by system-defined numeric values. For a list of these values, see [INF DestinationDirs Section](../install/inf-destinationdirs-section.md). In the following code example, the value 12 refers to the Drivers directory (%windir%\\system32\\drivers), and the value 10 refers to the Windows directory (%windir%).

```inf
[DestinationDirs]
DefaultDestDir = 12
Minispy.DriverFiles = 12
Minispy.UserFiles   = 10,FltMgr
```

## DefaultInstall Section (required)

In the [**DefaultInstall**](../install/inf-defaultinstall-section.md) section, a [**CopyFiles**](../install/inf-copyfiles-directive.md) directive copies the minifilter driver's driver files and user-application files to the destinations that are specified in the [**DestinationDirs**](../install/inf-destinationdirs-section.md) section.

> [!NOTE]
>
> The [**CopyFiles**](../install/inf-copyfiles-directive.md) directive should not refer to the catalog file or the INF file itself. SetupAPI copies these files automatically.

You can create a single INF file to install your driver on multiple versions of the Windows operating systems. You can create this type of INF file by creating additional [**DefaultInstall**](../install/inf-defaultinstall-section.md) and [**DefaultInstall.Services**](../install/inf-defaultinstall-services-section.md) sections for each operating system version. Each section is labeled with a *decoration* (for example, .ntx86, .ntia64, or .nt) that specifies the operating system version to which it applies. For more information about creating this type of INF file, see [Creating INF Files for Multiple Platforms and Operating Systems](../install/creating-inf-files-for-multiple-platforms-and-operating-systems.md).

The following code example shows a typical [**DefaultInstall**](../install/inf-defaultinstall-section.md) section.

```inf
[DefaultInstall.NTamd64]
OptionDesc = %MinispyServiceDesc%
CopyFiles = Minispy.DriverFiles, Minispy.UserFiles
```

## DefaultInstall.Services Section (required)

The [**DefaultInstall.Services**](../install/inf-defaultinstall-services-section.md) section contains an [**AddService**](../install/inf-addservice-directive.md) directive that controls how and when the services of a particular driver are loaded, as shown in the following code example.

```inf
[DefaultInstall.NTamd64.Services]
AddService = %MinispyServiceName%,,Minispy.Service
```

## ServiceInstall Section (required)

The **ServiceInstall** section contains information used for loading the driver service. In the [MiniSpy sample driver](/samples/microsoft/windows-driver-samples/minispy-file-system-minifilter-driver/), this section is named "Minispy.Service", as shown in the following code example. The name of the **ServiceInstall** section must appear in an [**AddService**](../install/inf-addservice-directive.md) directive in the [**DefaultInstall.Services**](../install/inf-defaultinstall-services-section.md) section.

```inf
[Minispy.Service]
DisplayName    = %MinispyServiceName%
Description    = %MinispyServiceDesc%
ServiceBinary  = %12%\minispy.sys
ServiceType    = 2 ;    SERVICE_FILE_SYSTEM_DRIVER
StartType      = 3 ;    SERVICE_DEMAND_START
ErrorControl   = 1 ;    SERVICE_ERROR_NORMAL%
LoadOrderGroup = "FSFilter Activity Monitor"
AddReg         = Minispy.AddRegistry
Dependencies   = FltMgr
```

The **ServiceType** entry specifies the type of service. Minifilter drivers should specify a value of 2 (SERVICE_FILE_SYSTEM_DRIVER). For more information about the **ServiceType** entry, see [INF AddService Directive](../install/inf-addservice-directive.md).

The **StartType** entry specifies when to start the service. The following table lists the possible values for **StartType** and their corresponding start types.

| Value      | Description |
| -----      | ----------- |
| 0x00000000 | SERVICE_BOOT_START |
| 0x00000001 | SERVICE_SYSTEM_START |
| 0x00000002 | SERVICE_AUTO_START |
| 0x00000003 | SERVICE_DEMAND_START |
| 0x00000004 | SERVICE_DISABLED |

For more information about these start types, see "Driver Start Types" in [What Determines When a Driver Is Loaded](what-determines-when-a-driver-is-loaded.md).

The **LoadOrderGroup** entry provides the filter manager with information that it needs to ensure interoperability between minifilter drivers and legacy file system filter drivers. You should specify a **LoadOrderGroup** value that is appropriate for the type of minifilter driver that you are developing. To choose a load order group, see [Load Order Groups and Altitudes for Minifilter Drivers](load-order-groups-and-altitudes-for-minifilter-drivers.md).

Note that you must specify a **LoadOrderGroup** value, even if your minifilter driver's start type is not SERVICE_BOOT_START. In this way, minifilter drivers are different from legacy file system filter drivers.

> [!NOTE]
>
> The filter manager's **StartType** value is SERVICE_BOOT_START, and its **LoadOrderGroup** value is FSFilter Infrastructure. These values ensure that the filter manager is always loaded before any minifilter drivers are loaded.

For more information about how the **StartType** and **LoadOrderGroup** entries determine when the driver is loaded, see [What Determines When a Driver Is Loaded](what-determines-when-a-driver-is-loaded.md).

For minifilter drivers, unlike legacy file system filter drivers, the **StartType** and **LoadOrderGroup** values do not determine where the minifilter driver attaches in the minifilter instance stack. This location is determined by the altitude that is specified for the minifilter instance.

The **ErrorControl** entry specifies the action to be taken if the service fails to start during system startup. Minifilter drivers should specify a value of 1 (SERVICE_ERROR_NORMAL). For more information about the **ErrorControl** entry, see [INF AddService Directive](../install/inf-addservice-directive.md).

The [**AddReg**](../install/inf-addreg-directive.md) directive refers to one or more INF writer-defined **AddRegistry** sections that contain information to be stored in the registry for the newly installed service. Minifilter drivers use **AddRegistry** sections to define minifilter driver instances and to specify a default instance.

The **Dependencies** entry specifies the names of any services or load order groups on which the driver depends. All minifilter drivers must specify FltMgr, which is the service name of the filter manager.

## AddRegistry Section (required)

The **AddRegistry** section adds keys and values to the registry. Minifilter drivers use an **AddRegistry** section to define minifilter instances and to specify a default instance. This information is used whenever the filter manager creates a new instance for the minifilter driver.

In the [MiniSpy sample driver](/samples/microsoft/windows-driver-samples/minispy-file-system-minifilter-driver/), the following **AddRegistry** section, together with the %strkey% token definitions in the [**Strings**](../install/inf-strings-section.md) section, defines three instances, one of which is named as the MiniSpy sample driver's default instance.

```inf
[Minispy.AddRegistry]
HKR,%RegInstancesSubkeyName%,%RegDefaultInstanceValueName%,0x00000000,%DefaultInstance%
HKR,%RegInstancesSubkeyName%"\"%Instance1.Name%,%RegAltitudeValueName%,0x00000000,%Instance1.Altitude%
HKR,%RegInstancesSubkeyName%"\"%Instance1.Name%,%RegFlagsValueName%,0x00010001,%Instance1.Flags%
HKR,%RegInstancesSubkeyName%"\"%Instance2.Name%,%RegAltitudeValueName%,0x00000000,%Instance2.Altitude%
HKR,%RegInstancesSubkeyName%"\"%Instance2.Name%,%RegFlagsValueName%,0x00010001,%Instance2.Flags%
HKR,%RegInstancesSubkeyName%"\"%Instance3.Name%,%RegAltitudeValueName%,0x00000000,%Instance3.Altitude%
HKR,%RegInstancesSubkeyName%"\"%Instance3.Name%,%RegFlagsValueName%,0x00010001,%Instance3.Flags%
```

## Strings Section (required)

The [**Strings**](../install/inf-strings-section.md) section defines each %strkey% token that is used in the INF file.

You can create a single international INF file by creating additional locale-specific **Strings**.*LanguageID* sections in the INF file. For more information about international INF files, see [Creating International INF Files](../install/creating-international-inf-files.md).

The following code example shows a typical [**Strings**](../install/inf-strings-section.md) section.

```inf
[Strings]
Msft               = "Microsoft Corporation"
MinispyServiceDesc = "Minispy mini-filter driver"
MinispyServiceName = "Minispy"
RegInstancesSubkeyName = "Instances"
RegDefaultInstanceValueName  = "DefaultInstance"
RegAltitudeValueName    = "Altitude"
RegFlagsValueName  = "Flags"

DefaultInstance    = "Minispy - Top Instance"
Instance1.Name     = "Minispy - Middle Instance"
Instance1.Altitude = "370000"
Instance1.Flags    = 0x1 ; Suppress automatic attachments
Instance2.Name     = "Minispy - Bottom Instance"
Instance2.Altitude = "365000"
Instance2.Flags    = 0x1 ; Suppress automatic attachments
Instance3.Name     = "Minispy - Top Instance"
Instance3.Altitude = "385000"
Instance3.Flags    = 0x1 ; Suppress automatic attachments
```

## DefaultUninstall and DefaultUninstall.Services sections

> [!NOTE]
>
> The **DefaultUninstall** and **DefaultUninstall.Services** sections are prohibited [(with exception)](../develop/creating-a-primitive-driver.md#legacy-compatibility) starting with Windows 10 version 1903.

In Windows 10 prior to version 1903, the **DefaultUninstall** and **DefaultUninstall.Services** sections were optional but recommended if the driver could be uninstalled:

* **DefaultUninstall** contained [**DelFiles**](../install/inf-delfiles-directive.md) and [**DelReg**](../install/inf-delreg-directive.md) directives to remove files and registry entries.
* **DefaultUninstall.Services** contained [**DelService**](../install/inf-delservice-directive.md) directives to remove the minifilter driver's services. The [**DelService**](../install/inf-delservice-directive.md) directive always specified the SPSVCINST_STOPSERVICE flag (0x00000200) to stop the service before it was deleted.

The following example shows typical **DefaultUninstall** and **DefaultUninstall.Services** sections prior to Windows 10, version 1903.

```inf
[DefaultUninstall.NTamd64]
DelFiles   = Minispy.DriverFiles, Minispy.UserFiles
DelReg     = Minispy.DelRegistry

[DefaultUninstall.NTamd64.Services]
DelService = Minispy,0x200
```
