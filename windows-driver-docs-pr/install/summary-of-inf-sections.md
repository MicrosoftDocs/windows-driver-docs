---
title: Summary of INF Sections
description: Summary of INF Sections
keywords:
- INF files WDK device installations , sections
- sections WDK INF files
ms.date: 01/14/2022
---

# Summary of INF Sections

The following summarizes the system-defined sections that can be used in INF files. System-defined section names are case-insensitive. For example, **version**, **VERSION**, and **Version** are equally valid section-names within an INF file.

This section describes the INF file sections in the same order that they generally appear in most device INF files. However, these sections actually can be specified in any arbitrary order. Windows finds all sections within each INF file by section name, not by sequential order, whether system-defined or INF-writer-defined.

<a href="" id="version-section"></a>[**Version Section**](inf-version-section.md)  
This is a required section for every INF file. For installation on Windows 2000 and later versions of Windows, this section must have a valid **Signature** entry.

<a href="" id="signatureattributes-section"></a>[**SignatureAttributes Section**](inf-signatureattributes-section.md)  
This section of the INF defines a set of files to be embedded-signed as part of Hardware Certification. These additional signatures are required for devices with certain special needs. Examples are Protected Environment media playback, Early Launch Antimalware, and third party HAL extensions.

<a href="" id="sourcedisksnames-section"></a>[**SourceDisksNames Section**](inf-sourcedisksnames-section.md)  
This section is required if the INF file has a corresponding **SourceDisksFiles** section. 

<a href="" id="sourcedisksfiles-section"></a>[**SourceDisksFiles Section**](inf-sourcedisksfiles-section.md)  
This section identifies the locations of files to be installed from the distribution media to the destinations on the target computer. An INF file that has this section must also have a **SourceDisksNames** section.

<a href="" id="destinationdirs-section"></a>[**DestinationDirs Section**](inf-destinationdirs-section.md)  
INF files have a **DestinationDirs** section to specify destination directories for any files that the INF references with a *CopyFiles* directive. This section is required if the INF uses *CopyFiles*.

<a href="" id="controlflags-section"></a>[**ControlFlags Section**](inf-controlflags-section.md)  
Generally, most INF files for device drivers and for the system class installers have this section so they can exclude, via the *ExcludeFromSelect* directive, at least a subset of *Models* entries from the list of manually installable devices to be displayed to end-users. INF files that only install PnP devices suppress the display of all model-specific information.

<a href="" id="manufacturer-section"></a>[**Manufacturer Section**](inf-manufacturer-section.md)  
This section is required in INF files for devices and their drivers.

The **Manufacturer** section of an INF file is sometimes called a "Table of Contents," because each of its entries references an INF-writer-defined *Models* section, which, in turn, references additional INF-writer-defined sections, such as a per-models-entry *DDInstall* section, <em>DDInstall</em>**.Services** section, and so forth.

<a href="" id="models-section--per-manufacturer-entry--"></a>[**Models Section**](inf-models-section.md) (per **Manufacturer** entry)   
This section is required to identify the devices for which the INF file installs drivers. It specifies a set of mappings between the generic name (string) for a device, the device ID, and the name of the *DDInstall* section, elsewhere in the INF file that contains the installation instructions for the device.

An INF file that installs one or more devices and drivers for a single provider would have only one *Models* section, but system INF files for device classes can have many INF-writer-defined *Models* sections.

<a href="" id="ddinstall-section--per-models-entry--"></a>[***DDInstall* Section**](inf-ddinstall-section.md) (per *Models* entry)   
This section is required to actually install any devices that are listed in a *Models* section in the INF file, along with the drivers for each such device. A *DDInstall* section can be shared by more than one *Models* section.

<a href="" id="ddinstall-services-section"></a>[***DDInstall*.Services Section**](inf-ddinstall-services-section.md)  
This section is required if the INF file needs to create any services on the system as part of installing a device. This section controls how and when the services being created are started, its dependencies (if any) on other services, and so forth. This section also sets up event-logging services by a device driver if it supports event logging.

<a href="" id="ddinstall-hw-section"></a>[***DDInstall*.HW Section**](inf-ddinstall-hw-section.md)  
This optional section adds device-specific (and typically, driver-independent) information to the registry.

<a href="" id="ddinstall-events-section"></a>[***DDInstall*.Events Section**](inf-ddinstall-events-section.md)  

This optional section allows the INF to registry ETW providers and create AutoLogger registrations.

<a href="" id="ddinstall-components-section"></a>[***DDInstall*.Components Section**](inf-ddinstall-components-section.md)  

This optional section allows for one or more *AddComponent* directives to be specified to create child component devices.

<a href="" id="ddinstall-software-section"></a>[***DDInstall*.Software Section**](inf-ddinstall-software-section.md)  

This optional section allows for one or more *AddSoftware* directives to be specified to install standalone software.

<a href="" id="ddinstall-interfaces-section"></a>[***DDInstall*.Interfaces Section**](inf-ddinstall-interfaces-section.md)  
If a driver exports the functionality of a device interface class, therefore creating a new instance of the interface class, such as kernel-streaming still-image capture or data decompression, its INF file can have this section. This section can be used to pre-create the device interface as a disabled interface with some initial state provided by the INF file.

<a href="" id="interfaceinstall32-section"></a>[**InterfaceInstall32 Section**](inf-interfaceinstall32-section.md)  
If a to-be-installed component, such as a new class driver, provides one or more new [device interface classes](./overview-of-device-interface-classes.md) to higher-level components, its INF file can have this section. This can be used to pre-create the device interface class before any interfaces are registered in that class. Pre-creation of the class is not required for an interface to be registered in the class, but having this section in the INF allows the INF to associate some state with the device interface class.

<a href="" id="ddinstall-factdef-section"></a>[***DDInstall*.FactDef Section**](inf-ddinstall-factdef-section.md)  
**Note** If you are building a universal or ["Windows Driver"](../develop/getting-started-with-windows-drivers.md) driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

This section should be included in the INF file of any manually installed non-PnP device. It specifies the factory default hardware configuration settings, such as the bus-relative I/O ports, IRQ (if any), and so forth, for the card.

<a href="" id="ddinstall-logconfigoverride-section"></a>[***DDInstall*.LogConfigOverride Section**](inf-ddinstall-logconfigoverride-section.md)  
**Note** If you are building a universal or ["Windows Driver"](../develop/getting-started-with-windows-drivers.md) driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

This section is used to create an [override configuration](../kernel/hardware-resources.md#logical-configuration-types-for-resource-requirements-lists), which overrides the hardware resource requirements that a Plug and Play device's bus driver reports.

<a href="" id="defaultinstall-section"></a>[**DefaultInstall Section**](inf-defaultinstall-section.md)  
An INF file's **DefaultInstall** section will be accessed if a user selects the "Install" menu item after selecting and holding (or right-clicking) on the INF file name.

<a href="" id="defaultinstall-services-section"></a>[**DefaultInstall.Services Section**](inf-defaultinstall-services-section.md)  
This section is the same as the [**INF DDInstall.Services section**](inf-ddinstall-services-section.md), and is used in association with an [**INF DefaultInstall section**](inf-defaultinstall-section.md).

<a href="" id="strings-section"></a>[**Strings Section**](inf-strings-section.md)  
This section is required in every INF file to define each **%**<em>strkey</em>**%** token specified in the INF. By convention, the **Strings** section (or sections if the INF provides a set of locale-specific **Strings** sections) appears last in all system-supplied INF files for ease of maintenance and localization.

Some sections listed here, especially those with *Install* in their names, can contain directives that reference additional INF-writer-defined sections. Each directive causes particular operations to be performed on the items listed under the appropriate type of INF-writer-defined section during the installation process.

The set of valid entries and directives for any particular section in the previous list is section-specific and shown in the formal syntax of the reference for each of these sections. Additionally, see [Summary of INF Directives](summary-of-inf-directives.md) for a summary of the most commonly used directives.

Optional entries and directives within each such section are shown enclosed in brackets, as for example:

```
[Version]
...
[ExtensionId={nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn}]
...
```
The **ExtensionID** entry in a **\[Version\]** section is optional in the sense that it is required for [Extension INFs](using-an-extension-inf-file.md) but not present in other types of driver packages.

 

