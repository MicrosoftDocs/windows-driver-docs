---
title: Creating an INF File for a File System Driver
description: Creating an INF File for a File System Driver
ms.assetid: 4b67159f-a5a5-46da-9500-a9c6b6995da4
keywords:
- INF files WDK file system , creating
- SetupAPI WDK file system
- Strings section WDK file system
- DefaultUninstall section WDK file system
- ServiceInstall section WDK file system
- DefaultInstall section WDK file system
- SourceDisksNames section WDK file system
- DestinationDirs section WDK file system
- Version section WDK file system
- creating INF files WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating an INF File for a File System Driver


## <span id="ddk_creating_an_inf_file_for_a_file_system_filter_driver_if"></span><span id="DDK_CREATING_AN_INF_FILE_FOR_A_FILE_SYSTEM_FILTER_DRIVER_IF"></span>


The Windows Setup and Device Installer Services, known collectively as [SetupAPI](https://msdn.microsoft.com/library/windows/hardware/ff550855), provide the functions that control Windows setup and driver installation. The installation process is controlled by INF files.

A file system driver's INF file provides instructions that SetupAPI uses to install the driver. The INF file is a text file that specifies the files that must be present for your driver to run and the source and destination directories for the driver files. An INF file also contains driver configuration information that SetupAPI stores in the registry, such as the driver's start type and load order group.

For more information about INF files and how they are created, see [Creating an INF File](https://msdn.microsoft.com/library/windows/hardware/ff549520) and [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433). For general information about signing drivers, see [Driver Signing](https://msdn.microsoft.com/library/windows/hardware/ff544865).

You can create a single INF file to install your driver on multiple versions of the Windows operating system. For more information about creating such an INF file, see [Creating INF Files for Multiple Platforms and Operating Systems](https://msdn.microsoft.com/library/windows/hardware/ff540206) and [Creating International INF Files](https://msdn.microsoft.com/library/windows/hardware/ff540208).

Starting with 64-bit versions of Windows Vista, all kernel-mode components, including non-PnP (Plug and Play) drivers such as file system drivers (file system, legacy filter, and minifilter drivers), must be signed in order to load and execute. For these versions of the Windows operating system, the following list contains information that is relevant to file system drivers.

-   INF files for non-PnP drivers, including file system drivers, are not required to contain \[Manufacturer\] or \[Models\] sections.

-   The [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command-line tool, located in the \\bin\\SelfSign directory of the WDK installation directory, can be used to directly "embed sign" a driver SYS executable file. For performance reasons, boot-start drivers must contain an embedded signature.

-   Given an INF file, the [**Inf2Cat**](https://msdn.microsoft.com/library/windows/hardware/ff547089) command-line tool can be used to create a catalog (.cat) file for a driver package. Only catalog files can receive [WHQL](http://go.microsoft.com/fwlink/p/?linkid=8705) logo signatures.

-   With Administrator privileges, an unsigned driver can still be installed on x64-based systems starting with Windows Vista. However, the driver will fail to load (and thus execute) because it is unsigned.

-   For detailed information about the driving signing process, including the driving signing process for 64-bit versions of Windows Vista, see [Kernel-Mode Code Signing Walkthrough](http://go.microsoft.com/fwlink/p/?linkid=79445).

-   All kernel-mode components, including custom kernel-mode development tools, must be signed. For more information, see [Signing Drivers during Development and Test (Windows Vista and Later)](https://msdn.microsoft.com/library/windows/hardware/ff552275).

INF files cannot be used to read information from the registry or to launch a user-mode application.

After creating an INF file, you will typically write the source code for your setup application. The setup application calls user-mode setup functions to access the information in the INF file and perform installation operations.

To construct your own file system driver INF file, use the following information as a guide. You can use the [ChkINF](https://msdn.microsoft.com/library/windows/hardware/ff543461) tool to check the syntax of your INF file.

An INF file for a file system driver generally contains the following sections.

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

The [**Version**](https://msdn.microsoft.com/library/windows/hardware/ff547502) section specifies the driver version information, as shown in the following code example.

```cpp
[Version]
Signature   = "$WINDOWS NT$"
Provider    = %Msft%
DriverVer   = 08/28/2000,1.0.0.1
CatalogFile = 
```

The following table shows the values that file system filter drivers should specify in the [**Version**](https://msdn.microsoft.com/library/windows/hardware/ff547502) section.

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
<td align="left"><p>&quot;$WINDOWS NT$&quot;</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Provider</strong></p></td>
<td align="left"><p>In your own INF file, you should specify a provider other than Microsoft.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>DriverVer</strong></p></td>
<td align="left"><p>See <a href="https://msdn.microsoft.com/library/windows/hardware/ff547394" data-raw-source="[&lt;strong&gt;INF DriverVer directive&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547394)"><strong>INF DriverVer directive</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CatalogFile</strong></p></td>
<td align="left"><p>Leave this entry blank. In the future, it will contain the name of a WHQL-supplied catalog file for signed drivers.</p></td>
</tr>
</tbody>
</table>

 

### <span id="DestinationDirs_Section__optional_but_recommended_"></span><span id="destinationdirs_section__optional_but_recommended_"></span><span id="DESTINATIONDIRS_SECTION__OPTIONAL_BUT_RECOMMENDED_"></span>DestinationDirs Section (optional but recommended)

The [**DestinationDirs**](https://msdn.microsoft.com/library/windows/hardware/ff547383) section specifies the directories where the file system driver files will be copied.

In this section and in the **ServiceInstall** section, you can specify well-known system directories by using system-defined numeric values. For a list of these values, see [**INF DestinationDirs Section**](https://msdn.microsoft.com/library/windows/hardware/ff547383). In the following code example, the value "12" refers to the Drivers directory (%windir%\\system32\\drivers).

```cpp
[DestinationDirs]
DefaultDestDir = 12
ExampleFileSystem.DriverFiles = 12
```

### <span id="SourceDisksNames_Section__required_"></span><span id="sourcedisksnames_section__required_"></span><span id="SOURCEDISKSNAMES_SECTION__REQUIRED_"></span>SourceDisksNames Section (required)

The [**SourceDisksNames**](https://msdn.microsoft.com/library/windows/hardware/ff547478) section specifies the distribution media to be used.

In the following code example, the [**SourceDisksNames**](https://msdn.microsoft.com/library/windows/hardware/ff547478) section lists a single distribution media for the file system driver. The unique identifier for the media is 1. The name of the media is specified by the %Disk1% token, which is defined in the **Strings** section of the INF file.

```cpp
[SourceDisksNames]
1 = %Disk1%
```

### <span id="SourceDisksFiles_Section__required_"></span><span id="sourcedisksfiles_section__required_"></span><span id="SOURCEDISKSFILES_SECTION__REQUIRED_"></span>SourceDisksFiles Section (required)

The [**SourceDisksFiles**](https://msdn.microsoft.com/library/windows/hardware/ff547472) section specifies the location and names of the files to be copied.

In the following code example, the [**SourceDisksFiles**](https://msdn.microsoft.com/library/windows/hardware/ff547472) section lists the file to be copied for the file system driver and specifies that the files can be found on the media whose unique identifier is 1 (This identifier is defined in the [**SourceDisksNames**](https://msdn.microsoft.com/library/windows/hardware/ff547478) section of the INF file.)

```cpp
[SourceDisksFiles]
examplefilesystem.sys = 1
```

### <span id="DefaultInstall_Section__required_"></span><span id="defaultinstall_section__required_"></span><span id="DEFAULTINSTALL_SECTION__REQUIRED_"></span>DefaultInstall Section (required)

In the [**DefaultInstall**](https://msdn.microsoft.com/library/windows/hardware/ff547356) section, a [**CopyFiles**](https://msdn.microsoft.com/library/windows/hardware/ff546346) directive copies the file system driver's driver files to the destination that is specified in the [**DestinationDirs**](https://msdn.microsoft.com/library/windows/hardware/ff547383) section.

**Note**   The [**CopyFiles**](https://msdn.microsoft.com/library/windows/hardware/ff546346) directive should not refer to the catalog file or the INF file itself; SetupAPI copies these files automatically.

 

You can create a single INF file to install your driver on multiple versions of the Windows operating system. This type of INF file is created by creating additional [**DefaultInstall**](https://msdn.microsoft.com/library/windows/hardware/ff547356), [**DefaultInstall.Services**](https://msdn.microsoft.com/library/windows/hardware/ff547360), **DefaultUninstall**, and **DefaultUninstall.Services** sections for each operating system version. Each section is labeled with a *decoration* (for example, .ntx86, .ntia64, or .nt) that specifies the operating system version to which it applies. For more information about creating this type of INF file, see [Creating INF Files for Multiple Platforms and Operating Systems](https://msdn.microsoft.com/library/windows/hardware/ff540206).

In the following code example, the [**CopyFiles**](https://msdn.microsoft.com/library/windows/hardware/ff546346) directive copies the files that are listed in the ExampleFileSystem.DriverFiles section of the INF file.

```cpp
[DefaultInstall]
OptionDesc = %ServiceDesc%
CopyFiles = ExampleFileSystem.DriverFiles

[ExampleFileSystem.DriverFiles]
examplefilesystem.sys
```

### <span id="DefaultInstall.Services_Section__required_"></span><span id="defaultinstall.services_section__required_"></span><span id="DEFAULTINSTALL.SERVICES_SECTION__REQUIRED_"></span>DefaultInstall.Services Section (required)

The [**DefaultInstall.Services**](https://msdn.microsoft.com/library/windows/hardware/ff547360) section contains an [**AddService**](https://msdn.microsoft.com/library/windows/hardware/ff546326) directive that controls how and when the services of a particular driver are loaded.

In the following code example, the [**AddService**](https://msdn.microsoft.com/library/windows/hardware/ff546326) directive adds the file system service to the operating system. The %ServiceName% token contains the service name string, which is defined in the **Strings** section of the INF file. ExampleFileSystem.Service is the name of the file system driver's **ServiceInstall** section.

```cpp
[DefaultInstall.Services]
AddService = %ServiceName%,,ExampleFileSystem.Service
```

### <span id="ddk_serviceinstall_section_if"></span><span id="DDK_SERVICEINSTALL_SECTION_IF"></span>ServiceInstall Section (required)

The **ServiceInstall** section adds subkeys or value names to the registry and sets values. The name of the **ServiceInstall** section must appear in an [**AddService directive**](https://msdn.microsoft.com/library/windows/hardware/ff546326) in the [**DefaultInstall.Services section**](https://msdn.microsoft.com/library/windows/hardware/ff547360).

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

 

The **ServiceType** entry should always be set to SERVICE\_FILE\_SYSTEM\_DRIVER for a file system driver.

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

 

For detailed descriptions of these start types to determine which one is appropriate for your file system driver, see [What Determines When a Driver Is Loaded](what-determines-when-a-driver-is-loaded.md).

Starting with x64-based Windows Vista systems, the binary image file of a boot-start driver (a driver that has a start type of SERVICE\_BOOT\_START) must contain an embedded signature. This requirement ensures optimal system boot performance. For more information, see [Kernel-Mode Code Signing Walkthrough](http://go.microsoft.com/fwlink/p/?linkid=79445).

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
<td align="left"><p>SERVICE_ERROR_SEVERE (Switch to the registry&#39;s LastKnownGood control set and continue system startup.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000003</p></td>
<td align="left"><p>SERVICE_ERROR_CRITICAL (If system startup is not using the registry&#39;s LastKnownGood control set, switch to LastKnownGood and try again. If startup still fails, run a bug-check routine. Only the drivers that are needed for the system to startup should specify this value in their INF files.)</p></td>
</tr>
</tbody>
</table>

 

The **LoadOrderGroup** entry must always be set to "File System" for a file system driver. This is different from what is specified for a file system filter driver or file system minifilter driver where the **LoadOrderGroup** entry is set to one of the file system filter load order groups. For more information about the load order groups that are used for file system filter drivers and file system minifilter drivers, see [Load Order Groups for File System Filter Drivers](load-order-groups-for-file-system-filter-drivers.md) and [Load Order Groups and Altitudes for Minifilter Drivers](load-order-groups-and-altitudes-for-minifilter-drivers.md).

The [**AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) refers to one or more INF writer-defined **AddRegistry** sections that contain any information to be stored in the registry for the newly installed service.

**Note**   If the INF file will also be used for upgrading the driver after the initial install, the entries that are contained in the **AddRegistry** section should specify the 0x00000002 (FLG\_ADDREG\_NOCLOBBER) flag. Specifying this flag preserves the registry entries in HKLM\\CurrentControlSet\\Services when subsequent files are installed. For example:

 

```cpp
[ExampleFileSystem.AddRegistry]
HKR,Parameters,ExampleParameter,0x00010003,1
```

### <span id="DefaultUninstall_Section__optional_"></span><span id="defaultuninstall_section__optional_"></span><span id="DEFAULTUNINSTALL_SECTION__OPTIONAL_"></span>DefaultUninstall Section (optional)

The **DefaultUninstall** section is optional but recommended if your driver can be uninstalled. It contains [**DelFiles**](https://msdn.microsoft.com/library/windows/hardware/ff547363) and [**DelReg**](https://msdn.microsoft.com/library/windows/hardware/ff547374) directives to remove files and registry entries.

In the following code example, the [**DelFiles**](https://msdn.microsoft.com/library/windows/hardware/ff547363) directive removes the files that are listed in the ExampleFileSystem.DriverFiles section of the INF file.

```cpp
[DefaultUninstall]
DelFiles   = ExampleFileSystem.DriverFiles
DelReg     = ExampleFileSystem.DelRegistry
```

The [**DelReg**](https://msdn.microsoft.com/library/windows/hardware/ff547374) directive refers to one or more INF writer-defined **DelRegistry** sections that contain any information to be removed from the registry for the service that is being uninstalled.

### <span id="DefaultUninstall.Services_Section__optional_"></span><span id="defaultuninstall.services_section__optional_"></span><span id="DEFAULTUNINSTALL.SERVICES_SECTION__OPTIONAL_"></span>DefaultUninstall.Services Section (optional)

The **DefaultUninstall.Services** section is optional but recommended if your driver can be uninstalled. It contains [**DelService**](https://msdn.microsoft.com/library/windows/hardware/ff547377) directives to remove the file system driver's services.

In the following code example, the [**DelService**](https://msdn.microsoft.com/library/windows/hardware/ff547377) directive removes the file system driver's service from the operating system.

```cpp
[DefaultUninstall.Services]
DelService = %ServiceName%,0x200
```

**Note**   The [**DelService**](https://msdn.microsoft.com/library/windows/hardware/ff547377) directive should always specify the 0x200 (SPSVCINST\_STOPSERVICE) flag to stop the service before it is deleted.

 

**Note**   There are certain classes of file system products that cannot be completely uninstalled. In this situation, it is acceptable to just uninstall the components of the product that can be uninstalled and leave installed the components of the product that cannot be uninstalled. An example of such a product is the Microsoft Single Instance Store (SIS) feature.

 

### <span id="Strings_Section__required_"></span><span id="strings_section__required_"></span><span id="STRINGS_SECTION__REQUIRED_"></span>Strings Section (required)

The [**Strings**](https://msdn.microsoft.com/library/windows/hardware/ff547485) section defines each %strkey% token that is used in the INF file.

For example, the file system driver defines the following strings in its INF file.

```cpp
[Strings]
Msft        = "Microsoft Corporation"
ServiceDesc = "Example File System Driver"
ServiceName = "ExampleFileSystem"
ParameterPath = "SYSTEM\CurrentControlSet\Services\ExampleFileSystem\Parameters"
Disk1       = "Example File System Driver CD"
```

You can create a single international INF file by creating additional locale-specific **Strings.**<em>LanguageID</em> sections in the INF file. For more information about international INF files, see [Creating International INF Files](https://msdn.microsoft.com/library/windows/hardware/ff540208).

 

 




