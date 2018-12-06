---
title: Creating an INF File for a Minifilter Driver
description: Creating an INF File for a Minifilter Driver
ms.assetid: 2ae41287-e3c5-4df5-8dec-8575343d5319
keywords:
- INF files WDK file system , minifilter drivers
- DestinationDirs section WDK file system
- Version section WDK file system
- Strings section WDK file system
- DefaultUninstall section WDK file system
- ServiceInstall section WDK file system
- DefaultInstall section WDK file system
- AddRegistry section WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating an INF File for a Minifilter Driver


## <span id="ddk_creating_an_inf_file_for_a_minifilter_driver_if"></span><span id="DDK_CREATING_AN_INF_FILE_FOR_A_MINIFILTER_DRIVER_IF"></span>


An INF file for a file system minifilter driver generally contains the following sections:

Version (required)

DestinationDirs (optional but recommended)

DefaultInstall (required)

DefaultInstall.Services (required)

ServiceInstall (required)

AddRegistry (required)

DefaultUninstall (optional)

DefaultUninstall.Services (optional)

Strings (required)

**Note**  Starting with x64-based Windows Vista systems, all kernel-mode components, including non-PnP (Plug and Play) drivers, such as file system drivers (file system, legacy filter, and minifilter drivers), must be signed in order to load and execute. For this scenario, the following list contains information relevant to file system drivers:
-   INF files for non-PnP drivers, including file system drivers, are not required to contain \[Manufacturer\] or \[Models\] sections.

-   The [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command-line tool, located in the \\bin\\SelfSign directory of the WDK installation directory, can be used to directly "embed sign" a driver SYS executable file. For performance reasons, boot-start drivers must contain an embedded signature.

-   Given an INF file, the [Inf2cat](http://go.microsoft.com/fwlink/p/?linkid=79443) command-line tool can be used to create a catalog (.cat) file for a driver package. Only catalog files can receive [WHQL](http://go.microsoft.com/fwlink/p/?linkid=8705) logo signatures.

-   With Administrator privileges, an unsigned driver can still be installed on x64-based systems starting with Windows Vista. However, the driver will fail to load (and thus execute) because it is unsigned.

-   For general information about signing drivers, see [Driver Signing](https://msdn.microsoft.com/library/windows/hardware/ff544865).

-   For detailed information on the driving signing process, see [Kernel-Mode Code Signing Walkthrough](http://go.microsoft.com/fwlink/p/?linkid=79445).

-   All kernel-mode components, including custom kernel-mode development tools, must be signed. For more information, see [Signing Drivers during Development and Test (Windows Vista and Later)](https://msdn.microsoft.com/library/windows/hardware/ff552275).

 

### <span id="Version_Section__required_"></span><span id="version_section__required_"></span><span id="VERSION_SECTION__REQUIRED_"></span>Version Section (required)

The [**Version**](https://msdn.microsoft.com/library/windows/hardware/ff547502) section specifies a class and GUID that are determined by the type of minifilter driver, as shown in the following code example.

```cpp
[Version]
Signature   = "$WINDOWS NT$"
Class       = "ActivityMonitor"
ClassGuid   = {b86dff51-a31e-4bac-b3cf-e8cfe75c9fc2}
Provider    = %Msft%
DriverVer   = 10/09/2001,1.0.0.0
CatalogFile = 
```

The following table shows the values that file system minifilter drivers should specify in the [**Version**](https://msdn.microsoft.com/library/windows/hardware/ff547502) section.

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
<td align="left"><p>See <a href="https://msdn.microsoft.com/library/windows/hardware/ff547394" data-raw-source="[&lt;strong&gt;INF DriverVer directive&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547394)"><strong>INF DriverVer directive</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>CatalogFile</strong></p></td>
<td align="left"><p>For antivirus minifilter drivers that are signed, this entry contains the name of a WHQL-supplied catalog file. All other minifilter drivers should leave this entry blank. For more information, see the description of the <strong>CatalogFile</strong> entry in <a href="https://msdn.microsoft.com/library/windows/hardware/ff547502" data-raw-source="[&lt;strong&gt;INF Version Section&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547502)"><strong>INF Version Section</strong></a>.</p></td>
</tr>
</tbody>
</table>

 

### <span id="DestinationDirs_Section__optional_but_recommended_"></span><span id="destinationdirs_section__optional_but_recommended_"></span><span id="DESTINATIONDIRS_SECTION__OPTIONAL_BUT_RECOMMENDED_"></span>DestinationDirs Section (optional but recommended)

The [**DestinationDirs**](https://msdn.microsoft.com/library/windows/hardware/ff547383) section specifies the directories where minifilter driver and application files will be copied.

In this section and in the **ServiceInstall** section, you can specify well-known system directories by system-defined numeric values. For a list of these values, see [**INF DestinationDirs Section**](https://msdn.microsoft.com/library/windows/hardware/ff547383). In the following code example, the value 12 refers to the Drivers directory (%windir%\\system32\\drivers), and the value 10 refers to the Windows directory (%windir%).

```cpp
[DestinationDirs]
DefaultDestDir = 12
Minispy.DriverFiles = 12
Minispy.UserFiles   = 10,FltMgr
```

### <span id="DefaultInstall_Section__required_"></span><span id="defaultinstall_section__required_"></span><span id="DEFAULTINSTALL_SECTION__REQUIRED_"></span>DefaultInstall Section (required)

In the [**DefaultInstall**](https://msdn.microsoft.com/library/windows/hardware/ff547356) section, a [**CopyFiles**](https://msdn.microsoft.com/library/windows/hardware/ff546346) directive copies the minifilter driver's driver files and user-application files to the destinations that are specified in the [**DestinationDirs**](https://msdn.microsoft.com/library/windows/hardware/ff547383) section.

**Note**   The [**CopyFiles**](https://msdn.microsoft.com/library/windows/hardware/ff546346) directive should not refer to the catalog file or the INF file itself. SetupAPI copies these files automatically.

 

You can create a single INF file to install your driver on multiple versions of the Windows operating system. You can create this type of INF file by creating additional [**DefaultInstall**](https://msdn.microsoft.com/library/windows/hardware/ff547356), [**DefaultInstall.Services**](https://msdn.microsoft.com/library/windows/hardware/ff547360), **DefaultUninstall**, and **DefaultUninstall.Services** sections for each operating system version. Each section is labeled with a *decoration* (for example, .ntx86, .ntia64, or .nt) that specifies the operating system version to which it applies. For more information about creating this type of INF file, see [Creating INF Files for Multiple Platforms and Operating Systems](https://msdn.microsoft.com/library/windows/hardware/ff540206).

The following code example shows a typical [**DefaultInstall**](https://msdn.microsoft.com/library/windows/hardware/ff547356) section.

```cpp
[DefaultInstall]
OptionDesc = %MinispyServiceDesc%
CopyFiles = Minispy.DriverFiles, Minispy.UserFiles
```

### <span id="DefaultInstall.Services_Section__required_"></span><span id="defaultinstall.services_section__required_"></span><span id="DEFAULTINSTALL.SERVICES_SECTION__REQUIRED_"></span>DefaultInstall.Services Section (required)

The [**DefaultInstall.Services**](https://msdn.microsoft.com/library/windows/hardware/ff547360) section contains an [**AddService**](https://msdn.microsoft.com/library/windows/hardware/ff546326) directive that controls how and when the services of a particular driver are loaded, as shown in the following code example.

```cpp
[DefaultInstall.Services]
AddService = %MinispyServiceName%,,Minispy.Service
```

### <span id="ServiceInstall_Section__required_"></span><span id="serviceinstall_section__required_"></span><span id="SERVICEINSTALL_SECTION__REQUIRED_"></span>ServiceInstall Section (required)

The **ServiceInstall** section contains information used for loading the driver service. In the MiniSpy sample driver, this section is named "Minispy.Service", as shown in the following code example. The name of the **ServiceInstall** section must appear in an [**AddService**](https://msdn.microsoft.com/library/windows/hardware/ff546326) directive in the [**DefaultInstall.Services**](https://msdn.microsoft.com/library/windows/hardware/ff547360) section.

```cpp
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

The **ServiceType** entry specifies the type of service. Minifilter drivers should specify a value of 2 (SERVICE\_FILE\_SYSTEM\_DRIVER). For more information about the **ServiceType** entry, see [**INF AddService Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546326).

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

 

For more information about these start types, see "Driver Start Types" in [What Determines When a Driver Is Loaded](what-determines-when-a-driver-is-loaded.md).

The **LoadOrderGroup** entry provides the filter manager with information that it needs to ensure interoperability between minifilter drivers and legacy file system filter drivers. You should specify a **LoadOrderGroup** value that is appropriate for the type of minifilter driver that you are developing. To choose a load order group, see [Load Order Groups and Altitudes for Minifilter Drivers](load-order-groups-and-altitudes-for-minifilter-drivers.md).

Note that you must specify a **LoadOrderGroup** value, even if your minifilter driver's start type is not SERVICE\_BOOT\_START. In this way, minifilter drivers are different from legacy file system filter drivers.

**Note**   The filter manager's **StartType** value is SERVICE\_BOOT\_START, and its **LoadOrderGroup** value is FSFilter Infrastructure. These values ensure that the filter manager is always loaded before any minifilter drivers are loaded.

 

For more information about how the **StartType** and **LoadOrderGroup** entries determine when the driver is loaded, see [What Determines When a Driver Is Loaded](what-determines-when-a-driver-is-loaded.md).

**Note**   For minifilter drivers, unlike legacy file system filter drivers, the **StartType** and **LoadOrderGroup** values do not determine where the minifilter driver attaches in the minifilter instance stack. This location is determined by the altitude that is specified for the minifilter instance.

 

The **ErrorControl** entry specifies the action to be taken if the service fails to start during system startup. Minifilter drivers should specify a value of 1 (SERVICE\_ERROR\_NORMAL). For more information about the **ErrorControl** entry, see [**INF AddService Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546326).

The [**AddReg**](https://msdn.microsoft.com/library/windows/hardware/ff546320) directive refers to one or more INF writer-defined **AddRegistry** sections that contain information to be stored in the registry for the newly installed service. Minifilter drivers use **AddRegistry** sections to define minifilter driver instances and to specify a default instance.

The **Dependencies** entry specifies the names of any services or load order groups on which the driver depends. All minifilter drivers must specify FltMgr, which is the service name of the filter manager.

### <span id="AddRegistry_Section__required_"></span><span id="addregistry_section__required_"></span><span id="ADDREGISTRY_SECTION__REQUIRED_"></span>AddRegistry Section (required)

The **AddRegistry** section adds keys and values to the registry. Minifilter drivers use an **AddRegistry** section to define minifilter instances and to specify a default instance. This information is used whenever the filter manager creates a new instance for the minifilter driver.

In the MiniSpy sample driver, the following **AddRegistry** section, together with the %strkey% token definitions in the [**Strings**](https://msdn.microsoft.com/library/windows/hardware/ff547485) section, defines three instances, one of which is named as the MiniSpy sample driver's default instance.

```cpp
[Minispy.AddRegistry]
HKR,%RegInstancesSubkeyName%,%RegDefaultInstanceValueName%,0x00000000,%DefaultInstance%
HKR,%RegInstancesSubkeyName%"\"%Instance1.Name%,%RegAltitudeValueName%,0x00000000,%Instance1.Altitude%
HKR,%RegInstancesSubkeyName%"\"%Instance1.Name%,%RegFlagsValueName%,0x00010001,%Instance1.Flags%
HKR,%RegInstancesSubkeyName%"\"%Instance2.Name%,%RegAltitudeValueName%,0x00000000,%Instance2.Altitude%
HKR,%RegInstancesSubkeyName%"\"%Instance2.Name%,%RegFlagsValueName%,0x00010001,%Instance2.Flags%
HKR,%RegInstancesSubkeyName%"\"%Instance3.Name%,%RegAltitudeValueName%,0x00000000,%Instance3.Altitude%
HKR,%RegInstancesSubkeyName%"\"%Instance3.Name%,%RegFlagsValueName%,0x00010001,%Instance3.Flags%
```

### <span id="DefaultUninstall_Section__optional_"></span><span id="defaultuninstall_section__optional_"></span><span id="DEFAULTUNINSTALL_SECTION__OPTIONAL_"></span>DefaultUninstall Section (optional)

The **DefaultUninstall** section is optional but recommended if your driver can be uninstalled. It contains [**DelFiles**](https://msdn.microsoft.com/library/windows/hardware/ff547363) and [**DelReg**](https://msdn.microsoft.com/library/windows/hardware/ff547374) directives to remove files and registry entries, as shown in the following code example.

```cpp
[DefaultUninstall]
DelFiles   = Minispy.DriverFiles, Minispy.UserFiles
DelReg     = Minispy.DelRegistry
```

### <span id="DefaultUninstall.Services_Section__optional_"></span><span id="defaultuninstall.services_section__optional_"></span><span id="DEFAULTUNINSTALL.SERVICES_SECTION__OPTIONAL_"></span>DefaultUninstall.Services Section (optional)

The **DefaultUninstall.Services** section is optional but recommended if your driver can be uninstalled. It contains [**DelService**](https://msdn.microsoft.com/library/windows/hardware/ff547377) directives to remove the minifilter driver's services, as shown in the following code example from the MiniSpy sample driver.

**Note**   The [**DelService**](https://msdn.microsoft.com/library/windows/hardware/ff547377) directive should always specify the SPSVCINST\_STOPSERVICE flag (0x00000200) to stop the service before it is deleted.

 

```cpp
[DefaultUninstall.Services]
DelService = Minispy,0x200
```

### <span id="Strings_Section__required_"></span><span id="strings_section__required_"></span><span id="STRINGS_SECTION__REQUIRED_"></span>Strings Section (required)

The [**Strings**](https://msdn.microsoft.com/library/windows/hardware/ff547485) section defines each %strkey% token that is used in the INF file.

You can create a single international INF file by creating additional locale-specific **Strings.**<em>LanguageID</em> sections in the INF file. For more information about international INF files, see [Creating International INF Files](https://msdn.microsoft.com/library/windows/hardware/ff540208).

The following code example shows a typical [**Strings**](https://msdn.microsoft.com/library/windows/hardware/ff547485) section.

```cpp
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

 

 




