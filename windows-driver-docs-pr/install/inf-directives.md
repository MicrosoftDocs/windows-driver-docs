---
title: INF Directives
description: INF Directives
ms.assetid: 4cce21d3-08e9-4c8e-ac98-d43aa692621d
---

# INF Directives


This section describes the syntax of the directives that can appear within the sections of INF files. The following topics provide detailed information about the INF directives, and are listed in alphabetical order.

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
<td align="left"><p>[<strong>INF AddInterface Directive</strong>](inf-addinterface-directive.md)</p></td>
<td align="left"><p>One or more <strong>AddInterface</strong> directives can be specified within an [<strong>INF DDInstall.Interfaces section</strong>](inf-ddinstall-interfaces-section.md). This directive installs device-specific support for [device interface classes](device-interface-classes.md) exported to higher level components, such as other drivers or applications. The directive typically references an <em>add-interface-section</em> , which sets up registry information for the device-specific instance of the device interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF AddPowerSetting Directive</strong>](inf-addpowersetting-directive.md)</p></td>
<td align="left"><p>An <strong>AddPowerSetting</strong> directive references one or more sections that are used to modify or create power setting information. Each <em>add-power-setting-section</em> defines a power setting, the allowed values for the power setting, the friendly name of the power setting, and the description of the power setting. An <em>add-power-setting-section</em> also specifies the default value for each power scheme personality. For more information about power settings and power scheme personalities, see [Managing Device Performance States](https://msdn.microsoft.com/library/windows/hardware/ff554353).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF AddProperty Directive</strong>](inf-addproperty-directive.md)</p></td>
<td align="left"><p>An <strong>AddProperty</strong> directive references one or more INF file sections that modify the [device properties](device-properties.md) that are set for a device instance, a [device setup class](device-setup-classes.md), a [device interface class](device-interface-classes.md), or a device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF AddReg Directive</strong>](inf-addreg-directive.md)</p></td>
<td align="left"><p>An <strong>AddReg</strong> directive references one or more INF-writer-defined <em>add-registry-sections</em> that are used to modify or create registry information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF AddService Directive</strong>](inf-addservice-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  This directive is not used in INF files that install devices that do not require any drivers, such as modems or display monitors.
</div>
<div>
 
</div>
<p>An <strong>AddService</strong> directive is used within an [<strong>INF <em>DDInstall</em>.Services section</strong>](inf-ddinstall-services-section.md) or [<strong>INF DefaultInstall.Services section</strong>](inf-defaultinstall-services-section.md). It specifies characteristics of the services associated with drivers, such as how and when the services are loaded, and any dependencies on other underlying legacy drivers or services. Optionally, this directive also sets up event-logging services for the device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF BitReg Directive</strong>](inf-bitreg-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>BitReg</strong> directive references one or more INF-writer-defined sections used to set or clear bits within an existing REG_BINARY-type value entry in the registry. However, this directive is very rarely used in device/driver INF files.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF CopyFiles Directive</strong>](inf-copyfiles-directive.md)</p></td>
<td align="left"><p>A <strong>CopyFiles</strong> directive can do either of the following:</p>
<ul>
<li>Cause a single file to be copied from the source media to the default destination directory.</li>
<li>Reference one or more INF-writer-defined sections in the INF that each specifies a list of files to be copied from the source media to the destination.</li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF CopyINF Directive</strong>](inf-copyinf-directive.md)</p></td>
<td align="left"><p>A <strong>CopyINF</strong> directive causes specified INF files to be copied to the target system. The <strong>CopyINF</strong> directive is supported in Windows XP and later versions of Windows.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF DelFiles Directive</strong>](inf-delfiles-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>DelFiles</strong> directive references an INF-writer-defined section elsewhere in the INF file, and causes that list of files to be deleted in the context of operations on the section in which the referring <strong>DelFiles</strong> directive is specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF DelProperty Directive</strong>](inf-delproperty-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>DelProperty</strong> directive references one or more INF file sections that delete [device properties](device-properties.md) for a device instance, a [device setup class](device-setup-classes.md), a [device interface class](device-interface-classes.md), or a device interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF DelReg Directive</strong>](inf-delreg-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>DelReg</strong> directive references one or more INF-writer-defined sections describing keys and/or value entries to be removed from the registry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF DelService Directive</strong>](inf-delservice-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>DelService</strong> directive is used in a [<strong><em>DDInstall</em>.Services</strong>](inf-ddinstall-services-section.md) section to remove one or more previously installed device/driver services from the target computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF DriverVer Directive</strong>](inf-driverver-directive.md)</p></td>
<td align="left"><p>A <strong>DriverVer</strong> directive specifies version information for drivers installed by this INF.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF FeatureScore Directive</strong>](inf-featurescore-directive.md)</p></td>
<td align="left"><p>The <strong>FeatureScore</strong> directive provides an additional ranking criterion for drivers based on the features that a driver supports. For example, feature scores might be defined for a [device setup class](device-setup-classes.md) that distinguishes between drivers that are based on class-specific criteria.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF HardwareId Directive</strong>](inf-hardwareid-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  The <strong>HardwareId</strong> directive is only supported within an <em>Autorun.inf</em> file. This directive must not be used within the INF files that are used for PnP device installations.
</div>
<div>
 
</div>
<p>Starting with Windows Vista, the Found New Hardware Wizard and Hardware Update Wizard support INF <strong>HardwareId</strong> directives in the <strong>[DeviceInstall]</strong> section of an <em>Autorun.inf</em> file. The author of <em>Autorun.inf</em> can use these <strong>HardwareId</strong> directives to specify Plug and Play (PnP) hardware identifiers (IDs) of the devices for which the AutoRun-enabled application provides and installs drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF Ini2Reg Directive</strong>](inf-ini2reg-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>An <strong>Ini2Reg</strong> directive references one or more named sections in which lines or sections from a supplied INI file are moved into the registry. This creates or replaces one or more value entries under a specified key.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF LogConfig Directive</strong>](inf-logconfig-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>LogConfig</strong> directive references one or more INF-writer-defined sections, each of which specifies a logical configuration of hardware resources − the interrupt request lines, memory ranges, I/O ports, and DMA channels that can be used by the device. Each <em>log-config-section</em> specifies an alternative set of bus-relative hardware resources that can be used by the device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF ProfileItems Directive</strong>](inf-profileitems-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>ProfileItems</strong> directive is used in an [<strong>INF <em>DDInstall</em> section</strong>](inf-ddinstall-section.md) to list one or more <em>profile-items-sections</em> that contain items or groups to be added to, or removed from, the Start menu.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF Reboot Directive</strong>](inf-reboot-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>Reboot</strong> directive indicates that the caller should be notified to reboot the system after installation is complete.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF RegisterDlls Directive</strong>](inf-registerdlls-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>RegisterDlls</strong> directive references one or more INF sections used to specify files that are OLE controls and require self-registration.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF RenFiles Directive</strong>](inf-renfiles-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>A <strong>RenFiles</strong> directive references an INF-writer-defined section elsewhere in the INF file, which causes that list of files to be renamed in the context of operations on the section in which the referring <strong>RenFiles</strong> directive is specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF UnregisterDlls Directive</strong>](inf-unregisterdlls-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>An <strong>UnregisterDlls</strong> directive references one or more INF sections used to specify files that are OLE controls and require self-unregistration (self-removal).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>INF UpdateIniFields Directive</strong>](inf-updateinifields-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>An <strong>UpdateIniFields</strong> directive references one or more named sections in which fine-grained modifications within the lines of an INI file can be specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>INF UpdateInis Directive</strong>](inf-updateinis-directive.md)</p></td>
<td align="left"><div class="alert">
<strong>Note</strong>  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).
</div>
<div>
 
</div>
<p>An <strong>UpdateInis</strong> directive references one or more named sections, specifying an INI file from which a particular section or line is to be read and applied to an existing INI file of the same name on the target computer. Optionally, line-by-line modifications from and to such INI files can be specified in the <em>update-ini-section</em>.</p></td>
</tr>
</tbody>
</table>

 

For more information about the syntax rules for INF directives, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

 

 





