---
title: Summary of INF Directives
description: Summary of INF Directives
keywords:
- INF files WDK device installations , directives
- directives WDK INF files
ms.date: 01/14/2022
---

# Summary of INF Directives

The following list summarizes many (but not all) of the directives that can be used in INF files. INF directive names are case-insensitive. For example, **Addreg**, **addReg**, and **AddReg** are equally valid as directive specifications within an INF file.

This section lists the most commonly used directives first, together with their reciprocal or related directives. The most rarely used directives are toward the end of the list.

<a href="" id="addreg-directive"></a>[**AddReg Directive**](inf-addreg-directive.md)  
This directive references one or more *add-registry-section*s, which are INF sections used to add or modify subkeys and value entries in the registry.

The particular INF section in which an **AddReg** directive resides determines the default, relative registry location that will receive modifications specified in the referenced *add-registry-section*. These default registry locations are typically device-specific or driver-specific subkeys.

Additional *add-registry-sections* can set up registry information for system-defined device interfaces (such as kernel streaming interfaces) exported to higher level drivers, for new device interfaces exported by an installed component for a given class of devices, or for driver services.

<a href="" id="copyfiles-directive"></a>[**CopyFiles Directive**](inf-copyfiles-directive.md)  
This directive references one or more *file-list-section*s specifying transfers of model/device-specific driver images and any other necessary files from the distribution media to the destination directory for each such file.

<a href="" id="addservice-directive"></a>[**AddService Directive**](inf-addservice-directive.md)  
This directive references at least a *service-install-section*, possibly with an additional *event-log-install-section*.

INF files for most kinds of devices (those that install drivers) have an INF-writer-defined *service-install-section* to specify any dependencies on system-supplied drivers or services, during which stage of the system initialization process the supplied drivers should be loaded, and so forth. Many INF files for device drivers also have an INF-writer-defined *event-log-install-section* that is referenced by the **AddService** directive to set up event logging by the device driver.

<a href="" id="addinterface-directive"></a>[**AddInterface Directive**](inf-addinterface-directive.md)  
This directive references an *add-interface-section* in which one or more **AddReg** directives are specified referencing sections that set up the registry entries for the device interfaces supported by this device/driver.

<a href="" id="delreg-directive"></a>[**DelReg Directive**](inf-delreg-directive.md)  
**Note** If you are building a universal or ["Windows Driver"](../develop/getting-started-with-windows-drivers.md) driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

This directive references one or more *del-registry-section*s used to remove obsolete subkeys and/or value entries from the registry. For example, such a section might appear in an INF that upgrades a previous installation.

<a href="" id="delfiles-directive"></a>[**DelFiles Directive**](inf-delfiles-directive.md)  
**Note** If you are building a universal or ["Windows Driver"](../develop/getting-started-with-windows-drivers.md) driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

This rarely used directive references one or more *file-list-section*s specifying files to be deleted from the target of the installation.

<a href="" id="delservice-directive"></a>[**DelService Directive**](inf-delservice-directive.md)  
**Note** If you are building a universal or ["Windows Driver"](../develop/getting-started-with-windows-drivers.md) driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

This rarely used directive deletes a previously installed service.

<a href="" id="logconfig-directive"></a>[**LogConfig Directive**](inf-logconfig-directive.md)  
**Note** If you are building a universal or ["Windows Driver"](../develop/getting-started-with-windows-drivers.md) driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

This directive references one or more *log-config-section*s that specify acceptable bus-relative and device-specific hardware configurations in an INF for devices that are detected (by PnP device enumerators) or manually installed. For example, INF files for non-PnP ISA, EISA, and MCA devices, which are manually installed, use this directive. (Also see [**INF DDInstall.LogConfigOverride Section**](inf-ddinstall-logconfigoverride-section.md).)
