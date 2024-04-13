---
title: Creating an INF File for a Legacy File System Driver
description: How to create an INF File for a legacy file system driver
keywords:
- INF files WDK file system , creating
ms.date: 05/05/2023
---

# Creating an INF file for a legacy file system filter driver

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers.

The Windows Setup and Device Installer Services, known collectively as [SetupAPI](../install/setupapi.md), provide the functions that control Windows setup and driver installation. The installation process is controlled by INF files.

A file system filter driver's INF file provides instructions that SetupAPI uses to install the driver. The INF file is a text file that specifies the files that must be present for your driver to run and the source and destination directories for the driver files. An INF file also contains driver configuration information that SetupAPI stores in the registry, such as the driver's start type and load order group.

For more information about INF files and how they are created, see [Creating an INF File](../install/overview-of-inf-files.md) and [INF File Sections and Directives](../install/index.md). For general information about signing drivers, see [Driver Signing](../install/driver-signing.md).

You can create a single INF file to install your driver on multiple versions of the Windows operating system. For more information about creating such an INF file, see [Creating INF Files for Multiple Platforms and Operating Systems](../install/creating-inf-files-for-multiple-platforms-and-operating-systems.md) and [Creating International INF Files](../install/creating-international-inf-files.md).

Starting with 64-bit versions of Windows Vista, all kernel-mode components, including non-PnP (Plug and Play) drivers such as file system drivers (file system, legacy filter, and minifilter drivers), must be signed in order to load and execute. For these versions of the Windows operating system, the following list contains information that is relevant to file system filter drivers.

-   INF files for non-PnP drivers, including file system drivers, are not required to contain \[Manufacturer\] or \[Models\] sections.

-   The [**SignTool**](../devtest/signtool.md) command-line tool, located in the \\bin\\SelfSign directory of the WDK installation directory, can be used to directly "embed sign" a driver SYS executable file. For performance reasons, boot-start drivers must contain an embedded signature.

-   Given an INF file, the [**Inf2Cat**](../devtest/inf2cat.md) command-line tool can be used to create a catalog (.cat) file for a driver package. Only catalog files can receive [WHQL](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) logo signatures.

-   With Administrator privileges, an unsigned driver can still be installed on x64-based systems starting with Windows Vista. However, the driver will fail to load (and thus execute) because it is unsigned.

-   For detailed information about the driving signing process, including the driving signing process for 64-bit versions of Windows Vista, see [Kernel-Mode Code Signing Walkthrough](https://go.microsoft.com/fwlink/p/?linkid=79445).

-   All kernel-mode components, including custom kernel-mode development tools, must be signed. For more information, see [Signing Drivers during Development and Test (Windows Vista and Later)](../install/introduction-to-test-signing.md).

INF files cannot be used to read information from the registry or to launch a user-mode application.

After creating an INF file, you will typically write the source code for your setup application. The setup application calls user-mode setup functions to access the information in the INF file and perform installation operations.

To construct your own filter driver INF file, use the INF files for the sample file system filter drivers as a template. You can use the [InfVerif](../devtest/infverif.md) tool to check the syntax of your INF file.

An INF file for a file system filter driver generally contains the following sections.

-   Version (required)

-   DestinationDirs (optional but recommended)

-   SourceDisksNames (required)

-   SourceDisksFiles (required)

-   DefaultInstall (required)

-   DefaultInstall.Services (required)

-   ServiceInstall (required)

-   DefaultUninstall (optional)

-   DefaultUninstall.Services (optional)

-   Strings (required)

### <span id="Version_Section__required_"></span><span id="version_section__required_"></span><span id="VERSION_SECTION__REQUIRED_"></span>Version Section (required)

The [**Version**](../install/inf-version-section.md) section specifies a class and GUID that are determined by the type of filter, as shown in the following code example.

```inf
[Version]
Signature   = "$WINDOWS NT$"
Class       = "ActivityMonitor"
ClassGuid   = {b86dff51-a31e-4bac-b3cf-e8cfe75c9fc2}
Provider    = %Msft%
DriverVer   = 08/28/2000,1.0.0.1
CatalogFile =
PnpLockdown = 1
```

The following table shows the values that file system filter drivers should specify in the [**Version**](../install/inf-version-section.md) section.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Entry</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Signature</strong></p></td>
<td align="left"><p>"$WINDOWS NT$"</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Class</strong></p></td>
<td align="left"><p>See <a href="file-system-filter-driver-classes-and-class-guids.md" data-raw-source="[File System Filter Driver Classes and Class GUIDs](file-system-filter-driver-classes-and-class-guids.md)">File System Filter Driver Classes and Class GUIDs</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>ClassGuid</strong></p></td>
<td align="left"><p>See <a href="file-system-filter-driver-classes-and-class-guids.md" data-raw-source="[File System Filter Driver Classes and Class GUIDs](file-system-filter-driver-classes-and-class-guids.md)">File System Filter Driver Classes and Class GUIDs</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Provider</strong></p></td>
<td align="left"><p>In your own INF file, you should specify a provider other than Microsoft.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>DriverVer</strong></p></td>
<td align="left"><p>See <a href="/windows-hardware/drivers/install/inf-driverver-directive" data-raw-source="[&lt;strong&gt;INF DriverVer directive&lt;/strong&gt;](../install/inf-driverver-directive.md)"><strong>INF DriverVer directive</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CatalogFile</strong></p></td>
<td align="left"><p>Leave this entry blank. In the future, it will contain the name of a WHQL-supplied catalog file for signed drivers.</p></td>
</tr>
</tbody>
</table>

 

### <span id="DestinationDirs_Section__optional_but_recommended_"></span><span id="destinationdirs_section__optional_but_recommended_"></span><span id="DESTINATIONDIRS_SECTION__OPTIONAL_BUT_RECOMMENDED_"></span>DestinationDirs Section (optional but recommended)

The [**DestinationDirs**](../install/inf-destinationdirs-section.md) section specifies the directories where filter driver and application files will be copied.

In this section and in the **ServiceInstall** section, you can specify well-known system directories by using system-defined numeric values. For a list of these values, see [**INF DestinationDirs Section**](../install/inf-destinationdirs-section.md). In the following code example, the value "12" refers to the Drivers directory (%windir%\\system32\\drivers), and the value "10" refers to the Windows directory (%windir%).

```inf
[DestinationDirs]
DefaultDestDir             = 12
MyLegacyFilter.DriverFiles = 12
MyLegacyFilter.UserFiles   = 10,MyLegacyFilter
```

### <span id="SourceDisksNames_Section__required_"></span><span id="sourcedisksnames_section__required_"></span><span id="SOURCEDISKSNAMES_SECTION__REQUIRED_"></span>SourceDisksNames Section (required)

The [**SourceDisksNames**](../install/inf-sourcedisksnames-section.md) section specifies the distribution media to be used.

In the following code example, the [**SourceDisksNames**](../install/inf-sourcedisksnames-section.md) section lists a single distribution media. The unique identifier for the media is 1. The name of the media is specified by the %Disk1% token, which is defined in the [**Strings**](../install/inf-strings-section.md) section of the INF file.

```inf
[SourceDisksNames]
1 = %Disk1%
```

### <span id="SourceDisksFiles_Section__required_"></span><span id="sourcedisksfiles_section__required_"></span><span id="SOURCEDISKSFILES_SECTION__REQUIRED_"></span>SourceDisksFiles Section (required)

The [**SourceDisksFiles**](../install/inf-sourcedisksfiles-section.md) section specifies the location and names of the files to be copied.

In the following code example, the [**SourceDisksFiles**](../install/inf-sourcedisksfiles-section.md) section lists the files to be copied for the driver and specifies that the files can be found on the media whose unique identifier is 1 (This identifier is defined in the [**SourceDisksNames**](../install/inf-sourcedisksnames-section.md) section of the INF file.)

```inf
[SourceDisksFiles]
myLegacyFilter.exe = 1
myLegacyFilter.sys = 1
```

### <span id="DefaultInstall_Section__required_"></span><span id="defaultinstall_section__required_"></span><span id="DEFAULTINSTALL_SECTION__REQUIRED_"></span>DefaultInstall Section (required)

In the [**DefaultInstall**](../install/inf-defaultinstall-section.md) section, a [**CopyFiles**](../install/inf-copyfiles-directive.md) directive copies the file system filter driver's driver files and user-application files to the destinations that are specified in the [**DestinationDirs**](../install/inf-destinationdirs-section.md) section.

**Note**  The [**CopyFiles**](../install/inf-copyfiles-directive.md) directive should not refer to the catalog file or the INF file itself; SetupAPI copies these files automatically.

 

You can create a single INF file to install your driver on multiple versions of the Windows operating system. This type of INF file is created by creating additional [**DefaultInstall**](../install/inf-defaultinstall-section.md), [**DefaultInstall.Services**](../install/inf-defaultinstall-services-section.md), **DefaultUninstall**, and **DefaultUninstall.Services** sections for each operating system version. Each section is labeled with a *decoration* (for example, .ntx86, .ntia64, or .nt) that specifies the operating system version to which it applies. For more information about creating this type of INF file, see [Creating INF Files for Multiple Platforms and Operating Systems](../install/creating-inf-files-for-multiple-platforms-and-operating-systems.md).

In the following code example, the [**CopyFiles**](../install/inf-copyfiles-directive.md) directive copies the files that are listed in the MyLegacyFilter.DriverFiles and MyLegacyFilter.UserFiles sections of the INF file.

```inf
[DefaultInstall]
OptionDesc = %MyLegacyFilterServiceDesc%
CopyFiles = MyLegacyFilter.DriverFiles, MyLegacyFilter.UserFiles
```

### <span id="DefaultInstall.Services_Section__required_"></span><span id="defaultinstall.services_section__required_"></span><span id="DEFAULTINSTALL.SERVICES_SECTION__REQUIRED_"></span>DefaultInstall.Services Section (required)

The [**DefaultInstall.Services**](../install/inf-defaultinstall-services-section.md) section contains an [**AddService**](../install/inf-addservice-directive.md) directive that controls how and when the services of a particular driver are loaded.

In the following code example, the [**AddService**](../install/inf-addservice-directive.md) directive adds the MyLegacyFilter service to the operating system. The %MyLegacyFilterServiceName% token contains the service name string, which is defined in the [**Strings**](../install/inf-strings-section.md) section of the INF file. MyLegacyFilter.Service is the name of the example driver's **ServiceInstall** section.

```inf
[DefaultInstall.Services]
AddService = %MyLegacyFilterServiceName%,,MyLegacyFilter.Service
```

### <span id="ddk_serviceinstall_section_if"></span><span id="DDK_SERVICEINSTALL_SECTION_IF"></span>ServiceInstall Section (required)

The **ServiceInstall** section adds subkeys or value names to the registry and sets values. The name of the **ServiceInstall** section must appear in an [**AddService**](../install/inf-addservice-directive.md) directive in the [**DefaultInstall.Services**](../install/inf-defaultinstall-services-section.md) section.

The following code example shows the **ServiceInstall** section for the MyLegacyFilter example driver.

```inf
[MyLegacyFilter.Service]
DisplayName    = %MyLegacyFilterServiceName%
Description    = %MyLegacyFilterServiceDesc%
ServiceBinary  = %12%\myLegacyFilter.sys
ServiceType    = 2 ;    SERVICE_FILE_SYSTEM_DRIVER
StartType      = 3 ;    SERVICE_DEMAND_START
ErrorControl   = 1 ;    SERVICE_ERROR_NORMAL
LoadOrderGroup = "FSFilter Activity Monitor"
AddReg         = MyLegacyFilter.AddRegistry
```

The **DisplayName** entry specifies the name for the service. In the preceding example, the service name string is specified by the %MyLegacyFilterServiceName% token, which is defined in the [**Strings**](../install/inf-strings-section.md) section of the INF file.

The **Description** entry specifies a string that describes the service. In the preceding example, this string is specified by the %MyLegacyFilterServiceDesc% token, which is defined in the [**Strings**](../install/inf-strings-section.md) section of the INF file.

The **ServiceBinary** entry specifies the path to the executable file for the service. In the preceding example, the value 12 refers to the Drivers directory (%windir%\\system32\\drivers).

The **ServiceType** entry specifies the type of service. The following table lists the possible values for **ServiceType** and their corresponding service types.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x00000001</p></td>
<td align="left"><p>SERVICE_KERNEL_DRIVER (Device driver service)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000002</p></td>
<td align="left"><p>SERVICE_FILE_SYSTEM_DRIVER (File system or file system filter driver service)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000010</p></td>
<td align="left"><p>SERVICE_WIN32_OWN_PROCESS (Microsoft Win32 service that runs in its own process)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000020</p></td>
<td align="left"><p>SERVICE_WIN32_SHARE_PROCESS (Win32 service that shares a process)</p></td>
</tr>
</tbody>
</table>

 

The **ServiceType** entry should always be set to SERVICE\_FILE\_SYSTEM\_DRIVER for a file system filter driver.

The **StartType** entry specifies when to start the service. The following table lists the possible values for **StartType** and their corresponding start types.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x00000000</p></td>
<td align="left"><p>SERVICE_BOOT_START</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000001</p></td>
<td align="left"><p>SERVICE_SYSTEM_START</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000002</p></td>
<td align="left"><p>SERVICE_AUTO_START</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000003</p></td>
<td align="left"><p>SERVICE_DEMAND_START</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000004</p></td>
<td align="left"><p>SERVICE_DISABLED</p></td>
</tr>
</tbody>
</table>

 

For detailed descriptions of these start types, see [What Determines When a Driver Is Loaded](what-determines-when-a-driver-is-loaded.md).

If your driver's start type is SERVICE\_BOOT\_START (that is, the driver is a boot-start driver), you should also ensure that the **LoadOrderGroup** entry is appropriate for the type of filter you are developing. To choose a load order group, see [Load Order Groups for File System Filter Drivers](load-order-groups-for-file-system-filter-drivers.md). Additionally, starting with x64-based Windows Vista systems, the binary image file of a boot-start driver must contain an embedded signature. This requirement ensures optimal system boot performance. For more information, see [Kernel-Mode Code Signing Walkthrough](https://go.microsoft.com/fwlink/p/?linkid=79445).

For information about how the **StartType** and **LoadOrderGroup** entries determine when the driver is loaded, see [What Determines When a Driver Is Loaded](what-determines-when-a-driver-is-loaded.md).

The **ErrorControl** entry specifies the action to be taken if the service fails to start during system startup. The following table lists the possible values for **ErrorControl** and their corresponding error control values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x00000000</p></td>
<td align="left"><p>SERVICE_ERROR_IGNORE (Log the error and continue system startup.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000001</p></td>
<td align="left"><p>SERVICE_ERROR_NORMAL (Log the error, display a message to the user, and continue system startup.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000002</p></td>
<td align="left"><p>SERVICE_ERROR_SEVERE (Switch to the registry's LastKnownGood control set and continue system startup.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000003</p></td>
<td align="left"><p>SERVICE_ERROR_CRITICAL (If system startup is not using the registry's LastKnownGood control set, switch to LastKnownGood and try again. If startup still fails, run a bug-check routine. Only the drivers that are needed for the system to startup should specify this value in their INF files.)</p></td>
</tr>
</tbody>
</table>

 

The **LoadOrderGroup** entry should be set to a load order group that is appropriate for the type of file system filter driver that you are developing. To choose a load order group, see [Load Order Groups for File System Filter Drivers](load-order-groups-for-file-system-filter-drivers.md).

The [**AddReg directive**](../install/inf-addreg-directive.md) refers to one or more INF writer-defined **AddRegistry** sections that contain any information to be stored in the registry for the newly installed service.

**Note**   If the INF file will also be used for upgrading the driver after the initial install, the entries that are contained in the **AddRegistry** section should specify the 0x00000002 (FLG\_ADDREG\_NOCLOBBER) flag. Specifying this flag preserves the registry entries in HKLM\\CurrentControlSet\\Services when subsequent files are installed. For example:

 

```inf
[ExampleFileSystem.AddRegistry]
HKR,Parameters,ExampleParameter,0x00010003,1
```

### <span id="DefaultUninstall_Section__optional_"></span><span id="defaultuninstall_section__optional_"></span><span id="DEFAULTUNINSTALL_SECTION__OPTIONAL_"></span>DefaultUninstall Section (optional)

The **DefaultUninstall** section is optional but recommended if your driver can be uninstalled. It contains [**DelFiles**](../install/inf-delfiles-directive.md) and [**DelReg**](../install/inf-delreg-directive.md) directives to remove files and registry entries.

In the following code example, the [**DelFiles**](../install/inf-delfiles-directive.md) directive removes the files that are listed in the MyLegacyFilter.DriverFiles and MyLegacyFilter.UserFiles sections of the driver's INF file:

```inf
[DefaultUninstall]
DelFiles   = MyLegacyFilter.DriverFiles, MyLegacyFilter.UserFiles
DelReg     = MyLegacyFilter.DelRegistry
```

The [**DelReg**](../install/inf-delreg-directive.md) directive refers to one or more INF writer-defined **DelRegistry** sections that contain any information to be removed from the registry for the service that is being uninstalled.

### <span id="DefaultUninstall.Services_Section__optional_"></span><span id="defaultuninstall.services_section__optional_"></span><span id="DEFAULTUNINSTALL.SERVICES_SECTION__OPTIONAL_"></span>DefaultUninstall.Services Section (optional)

The **DefaultUninstall.Services** section is optional but recommended if your driver can be uninstalled. It contains [**DelService**](../install/inf-delservice-directive.md) directives to remove the file system filter driver's services.

In the following code example, the [**DelService**](../install/inf-delservice-directive.md) directive removes the MyLegacyFilter service from the operating system.

```inf
[DefaultUninstall.Services]
DelService = MyLegacyFilter,0x200
```

**Note**   The [**DelService**](../install/inf-delservice-directive.md) directive should always specify the 0x200 (SPSVCINST\_STOPSERVICE) flag to stop the service before it is deleted.

 

### <span id="Strings_Section__required_"></span><span id="strings_section__required_"></span><span id="STRINGS_SECTION__REQUIRED_"></span>Strings Section (required)

The [**Strings**](../install/inf-strings-section.md) section defines each %strkey% token that is used in the INF file, as shown in the following example.

```inf
[Strings]
Msft                      = "Microsoft Corporation"
MyLegacyFilterServiceDesc = "MyLegacyFilterFilter Driver"
MyLegacyFilterServiceName = "MyLegacyFilter"
MyLegacyFilterRegistry    = "system\currentcontrolset\services\MyLegacyFilter"
MyLegacyFilterMaxRecords  = "MaxRecords"
MyLegacyFilterMaxNames    = "MaxNames"
MyLegacyFilterDebugFlags  = "DebugFlags"
Disk1                     = "MyLegacyFilter Source Media"
```

You can create a single international INF file by creating additional locale-specific [**Strings.**](../install/inf-strings-section.md)*LanguageID* sections in the INF file. For more information about international INF files, see [Creating International INF Files](../install/creating-international-inf-files.md).
