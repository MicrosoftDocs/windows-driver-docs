---
title: Summary of INF Directives
description: Summary of INF Directives
ms.assetid: 6212502c-183c-4abb-9e56-59dba15fc685
keywords:
- INF files WDK device installations , directives
- directives WDK INF files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of INF Directives





The following list summarizes many (but not all) of the directives that can be used in INF files. INF directive names are case-insensitive. For example, **Addreg**, **addReg**, and **AddReg** are equally valid as directive specifications within an INF file.

This section lists the most commonly used directives first, together with their reciprocal or related directives. The most rarely used directives are toward the end of the list.

<a href="" id="addreg-directive"></a>[**AddReg Directive**](inf-addreg-directive.md)  
This directive references one or more *add-registry-section*s, which are INF sections used to add or modify subkeys and value entries in the registry.

The particular INF section in which an **AddReg** (or **DelReg**) directive resides determines the default, relative registry location that will receive modifications specified in the referenced *add-registry-section* (or *delete-registry-section*). These default registry locations are typically device-specific or driver-specific subkeys somewhere under the HKEY_LOCAL_MACHINE registry tree. For more information, see [Registry Trees and Keys for Devices and Drivers](registry-trees-and-keys.md).

Additional *add-registry-sections* can set up registry information for vendor-supplied co-installers, for system-defined device interfaces (such as kernel streaming interfaces) exported to higher level drivers, for new device interfaces exported by an installed component for a given class of devices, for driver services, or (rarely) for a new setup class of devices if the INF has a **ClassInstall32** section.

<a href="" id="delreg-directive"></a>[**DelReg Directive**](inf-delreg-directive.md)  
**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This directive references one or more *del-registry-section*s used to remove obsolete subkeys and/or value entries from the registry. For example, such a section might appear in an INF that upgrades a previous installation.

<a href="" id="copyfiles-directive"></a>[**CopyFiles Directive**](inf-copyfiles-directive.md)  
This directive references one or more *file-list-section*s specifying transfers of model/device-specific driver images and any other necessary files from the distribution media to the destination directory for each such file. Alternatively, this directive can specify a single file to be copied from the distribution media to the default destination directory.

<a href="" id="delfiles-directive"></a>[**DelFiles Directive**](inf-delfiles-directive.md)  
**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This rarely used directive references one or more *file-list-section*s specifying files to be deleted from the target of the installation.

<a href="" id="renfiles-directive"></a>[**RenFiles Directive**](inf-renfiles-directive.md)  
**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This rarely used directive references one or more *file-list-section*s specifying INF-associated source files to be renamed on the destination.

<a href="" id="addservice-directive"></a>[**AddService Directive**](inf-addservice-directive.md)  
This directive references at least a *service-install-section*, possibly with an additional *event-log-install-section*.

INF files for most kinds of devices (those that install drivers) have an INF-writer-defined *service-install-section* to specify any dependencies on system-supplied drivers or services, during which stage of the system initialization process the supplied drivers should be loaded, and so forth. Many INF files for device drivers also have an INF-writer-defined *event-log-install-section* that is referenced by the **AddService** directive to set up event logging by the device driver.

<a href="" id="delservice-directive"></a>[**DelService Directive**](inf-delservice-directive.md)  
**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This rarely used directive deletes a previously installed service.

<a href="" id="addinterface-directive"></a>[**AddInterface Directive**](inf-addinterface-directive.md)  
This directive references an *add-interface-section* in which one or more **AddReg** directives are specified referencing sections that set up the registry entries for the device interfaces supported by this device/driver. Optionally, such an *add-interface-section* can reference one or more additional sections that specify delete-registry, file-transfer, file-delete, and/or file-rename operations.

<a href="" id="bitreg-directive"></a>[**BitReg Directive**](inf-bitreg-directive.md)  
**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This rarely used directive references one or more *bit-registry-section*s specifying existing [REG_BINARY](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types)-type value entries in the registry for which particular bits in the values are to be modified.

<a href="" id="logconfig-directive"></a>[**LogConfig Directive**](inf-logconfig-directive.md)  
**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This directive references one or more *log-config-section*s that specify acceptable bus-relative and device-specific hardware configurations in an INF for devices that are detected (by PnP device enumerators) or manually installed. For example, INF files for non-PnP ISA, EISA, and MCA devices, which are manually installed, use this directive. (Also see [**INF DDInstall.LogConfigOverride Section**](inf-ddinstall-logconfigoverride-section.md).)

<a href="" id="updateinis-directive"></a>[**UpdateInis Directive**](inf-updateinis-directive.md)  
**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This rarely used directive references one or more *update-ini-section*s specifying parts of a supplied INI file to be read during installation and, possibly specifying line-by-line modifications to be made in that INI file.

<a href="" id="updateinifields-directive"></a>[**UpdateIniFields Directive**](inf-updateinifields-directive.md)  
**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This rarely used directive references one or more *update-inifields-section*s specifying modifications to be made on fields within the lines of an INI file.

<a href="" id="ini2reg-directive"></a>[**Ini2Reg Directive**](inf-ini2reg-directive.md)  
**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This rarely used directive references one or more *ini-to-registry-section*s specifying lines or sections of an INI file to be written into the registry.

The sections under which any of the directives in the previous list can be specified is system-determined. The basic form of each directive is shown in the formal syntax of the reference for each section, as for example:

```cpp
[DDInstall] | [DDInstall.HW] | [DDInstall.CoInstallers] | 
[ClassInstall32] | [ClassInstall32.ntx86] | [ClassInstall32.ntia64] | [ClassInstall32.ntamd64]

AddReg=add-registry-section[,add-registry-section] ...
```

The rest of this section describes the formal syntax and meaning for each system-defined named section, standard INF-writer-defined section, and directives that can be specified in an INF file.

 

 





