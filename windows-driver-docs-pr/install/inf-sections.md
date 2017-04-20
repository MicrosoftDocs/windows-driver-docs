---
title: INF Sections
description: INF Sections
ms.assetid: 0eeab13d-9255-4faa-9cf2-de6a8f93d8dc
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# INF Sections


The topics in this section describe the syntax of the sections that can appear in INF files. These topics provide detailed information about the INF sections, and are listed in the order in which they typically appear within an INF file.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>INF ClassInstall32 Section</strong>](inf-classinstall32-section.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>ClassInstall32</strong> section installs a new [device setup class](device-setup-classes.md) (and possibly a class installer) for devices in the new class.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF ClassInstall32.Services Section</strong>](inf-classinstall32-services-section.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>ClassInstall32</strong> section installs a new [device setup class](device-setup-classes.md) (and possibly a class installer) for devices in the new class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF ControlFlags Section</strong>](inf-controlflags-section.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>ControlFlags</strong> section identifies devices for which Windows should take certain unique actions during installation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF DDInstall Section</strong>](inf-ddinstall-section.md)</p></td>
<td align="left"><p>Each per-Models <em>DDInstall</em> section contains an optional <strong>DriverVer</strong> directive and one or more directives referencing additional named sections in the INF file, shown here with the most frequently specified INF directives, <strong>CopyFiles</strong> and <strong>AddReg</strong>, listed first.</p>
<p>The sections referenced by these directives contain instructions for installing driver files and writing any device-specific and/or driver-specific information into the registry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF DDInstall.CoInstallers Section</strong>](inf-ddinstall-coinstallers-section.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>This optional section registers one or more device-specific co-installers supplied on the distribution media to supplement the operations of existing device class installers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF DDInstall.FactDef Section</strong>](inf-ddinstall-factdef-section.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>This section should be used in an INF for any manually installed non-PnP device that an end-user might install. This section specifies the factory-default hardware configuration settings, such as the bus-relative I/O ports and IRQ (if any), for such a card.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF DDInstall.HW Section</strong>](inf-ddinstall-hw-section.md)</p></td>
<td align="left"><p><em>DDInstall</em> <strong>.HW</strong> sections are typically used for installing multifunction devices, for installing PnP filter drivers, and for setting up any user-accessible device-specific but driver-independent information in the registry, whether with explicit [<strong>AddReg</strong>](inf-addreg-directive.md) directives or with <strong>Include</strong> and <strong>Needs</strong> entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF DDInstall.Interfaces Section</strong>](inf-ddinstall-interfaces-section.md)</p></td>
<td align="left"><p>Each per-Models <em>DDInstall</em><strong>.Interfaces</strong> section can have one or more [<strong>AddInterface</strong>](inf-addinterface-directive.md) directives, depending on how many device interfaces a particular device/driver supports.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF DDInstall.LogConfigOverride Section</strong>](inf-ddinstall-logconfigoverride-section.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p><em>DDInstall</em> <strong>.LogConfigOverride</strong> sections are used to create an [override configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#logical-configuration-types-for-resource-requirements-lists), which overrides the hardware resource requirements that a Plug and Play device's bus driver reports.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF DDInstall.Services Section</strong>](inf-ddinstall-services-section.md)</p></td>
<td align="left"><p>Each per-Models <em>DDInstall</em><strong>.Services</strong> section contains one or more [<strong>INF AddService directives</strong>](inf-addservice-directive.md) that reference additional INF-writer-defined sections in an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF DDInstall.WMI Section</strong>](inf-ddinstall-wmi-section.md)</p></td>
<td align="left"><p>An INF <em>DDInstall</em>.<strong>WMI</strong> section contains one or more <strong>WMIInterface</strong> directives that specify characteristics for each WMI class that the driver provides.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF DefaultInstall Section</strong>](inf-defaultinstall-section.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>An INF file's <strong>DefaultInstall</strong> section is accessed if a user selects the &quot;Install&quot; menu item after right-clicking on the INF file name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF DefaultInstall.Services Section</strong>](inf-defaultinstall-services-section.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>DefaultInstall.Services</strong> section contains one or more [<strong>AddService</strong>](inf-addservice-directive.md) directives referencing additional INF-writer-defined sections in an INF file. This section is equivalent to the [<strong>INF <em>DDInstall</em>.Services</strong>](inf-ddinstall-services-section.md) section, and is used in association with an [<strong>INF DefaultInstall</strong>](inf-defaultinstall-section.md) section.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF DestinationDirs Section</strong>](inf-destinationdirs-section.md)</p></td>
<td align="left"><p>A <strong>DestinationDirs</strong> section specifies the target destination directory or directories for all copy, delete, and/or rename operations on files referenced by name elsewhere in the INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF InterfaceInstall32 Section</strong>](inf-interfaceinstall32-section.md)</p></td>
<td align="left"><p>This section creates one or more new [device interface classes](device-interface-classes.md). After a new class is created, subsequently installed devices/drivers can be registered to support the new device interface class by using [<strong>INF <em>DDInstall</em>.Interfaces sections</strong>](inf-ddinstall-interfaces-section.md) in their respective INF files, or by calling [<strong>IoRegisterDeviceInterface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549506).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF Manufacturer Section</strong>](inf-manufacturer-section.md)</p></td>
<td align="left"><p>The <strong>Manufacturer</strong> section identifies the manufacturer of one or more devices that can be installed by using the INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF Models Section</strong>](inf-models-section.md)</p></td>
<td align="left"><p>A per-manufacturer <em>Models</em> section identifies at least one device, references the <em>DDInstall</em> section of the INF file for that device, and specifies a unique-to-the-model-section [hardware identifier (ID)](hardware-ids.md) for that device.</p>
<p>Any entry in the per-manufacturer <em>Models</em> section can also specify one or more additional device IDs for models that are compatible with the device designated by the initial hardware ID and are controlled by the same drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF SignatureAttributes Section</strong>](inf-signatureattributes-section.md)</p></td>
<td align="left"><p>This section allows users to request additional signatures as required by certain certification scenarios. Examples of these scenarios are: Protected Environment media playback, Early Launch Antimalware, and third party HAL extensions. These additional signatures will only be applied if your Hardware Certification Kit package contains the proper Features and passing Tests.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF SourceDisksFiles Section</strong>](inf-sourcedisksfiles-section.md)</p></td>
<td align="left"><p>The <strong>SourceDisksFiles</strong> section names the source files that are used during installation, identifies the installation disks that contain those files, and provides the directory paths, if any, on the distribution disks that contain individual files.</p>
<p>In order for a driver file or an application file to be included as part of a signed [driver package](driver-packages.md), the file must have a corresponding INF <strong>SourceDisksFiles</strong> section entry and a corresponding [<strong>INF CopyFiles directive</strong>](inf-copyfiles-directive.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF SourceDisksNames Section</strong>](inf-sourcedisksnames-section.md)</p></td>
<td align="left"><p>A <strong>SourceDisksNames</strong> section identifies the distribution disks or CD-ROM discs that contain the source files to be transferred to the target computer during installation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF Strings Section</strong>](inf-strings-section.md)</p></td>
<td align="left"><p>An INF file must have at least one <strong>Strings</strong> section to define every %<em>strkey</em>% token specified elsewhere in that INF.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF Version Section</strong>](inf-version-section.md)</p></td>
<td align="left"><p>By convention, the <strong>Version</strong> section appears first in INF files. Every INF file must have this section.</p></td>
</tr>
</tbody>
</table>

 

For more information about the syntax rules for INF sections, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

 

 





