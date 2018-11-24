---
title: Summary of INF Sections
description: Summary of INF Sections
ms.assetid: a9d4691b-4429-456b-a5d2-482ccd0a2845
keywords:
- INF files WDK device installations , sections
- sections WDK INF files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of INF Sections





The following summarizes the system-defined sections that can be used in INF files. System-defined section names are case-insensitive. For example, **version**, **VERSION**, and **Version** are equally valid section-names within an INF file.

This section describes the INF file sections in the same order that they generally appear in most device INF files. However, these sections actually can be specified in any arbitrary order. Windows finds all sections within each INF file by section name, not by sequential order, whether system-defined or INF-writer-defined.

<a href="" id="version-section"></a>[**Version Section**](inf-version-section.md)  
This is a required section for every INF file. For installation on Windows 2000 and later versions of Windows, this section must have a valid **Signature** entry.

<a href="" id="signatureattributes-section"></a>[**SignatureAttributes Section**](inf-signatureattributes-section.md)  
This section of the INF defines a set of files to be embedded-signed as part of Hardware Certification. These additional signatures are required for devices with certain special needs. Examples are Protected Environment media playback, Early Launch Antimalware, and third party HAL extensions.

<a href="" id="sourcedisksnames-section"></a>[**SourceDisksNames Section**](inf-sourcedisksnames-section.md)  
This section is required if the INF file has a corresponding **SourceDisksFiles** section. This section is required to install IHV/OEM-supplied devices and their drivers from distribution media included in packaged products. It is also required in such an INF file that installs either of the following:

- A co-installer DLL to supplement the operations of a system-supplied device class installer or co-installers (see also <em>DDInstall</em>**.CoInstallers** later in this list)

- A new class installer DLL to supplement the operations of the OS's device installer (see also **ClassInstall32**)

This section identifies the individual source distribution disks or CD-ROM discs for the installation. By contrast, the system-supplied INF files each specify a **LayoutFile** entry in their **Version** sections and provide at least one other INF file detailing the source distribution contents and layout of all software components to be installed.

<a href="" id="sourcedisksfiles-section"></a>[**SourceDisksFiles Section**](inf-sourcedisksfiles-section.md)  
This section identifies the locations of files to be installed from the distribution media to the destinations on the target computer. An INF file that has this section must also have a **SourceDisksNames** section.

<a href="" id="destinationdirs-section"></a>[**DestinationDirs Section**](inf-destinationdirs-section.md)  
Device/driver INF files have a **DestinationDirs** section to specify a default destination directory for INF-specified copies of the files supplied on the distribution media or listed in the INF layout files. This section is required unless the INF file installs a device, such as a modem or display monitor, that has no files except its INF to be installed with it.

<a href="" id="controlflags-section"></a>[**ControlFlags Section**](inf-controlflags-section.md)  
This section controls whether an INF file is used only to transfer files from the distribution media.

Generally, most INF files for device drivers and for the system class installers have this section so they can exclude at least a subset of *Models* entries from the list of manually installable devices to be displayed to end-users. INF files that only install PnP devices suppress the display of all model-specific information.

<a href="" id="manufacturer-section"></a>[**Manufacturer Section**](inf-manufacturer-section.md)  
This section is required in INF files for devices and their drivers.

The **Manufacturer** section of a system device class INF is sometimes called a "Table of Contents," because each of its entries references an INF-writer-defined *Models* section, which, in turn, references additional INF-writer-defined sections, such as a per-models-entry *DDInstall* section, <em>DDInstall</em>**.Services** section, and so forth.

<a href="" id="models-section--per-manufacturer-entry--"></a>[**Models Section**](inf-models-section.md) (per **Manufacturer** entry)   
This section is required to identify the devices for which the INF file installs drivers. It specifies a set of mappings between the generic name (string) for a device, the device ID, and the name of the *DDInstall* section, elsewhere in the INF file that contains the installation instructions for the device.

An INF file that installs one or more devices and drivers for a single provider would have only one *Models* section, but system INF files for device classes can have many INF-writer-defined *Models* sections.

<a href="" id="ddinstall-section--per-models-entry--"></a>[***DDInstall* Section**](inf-ddinstall-section.md) (per *Models* entry)   
This section is required to actually install any devices that are listed in a *Models* section in the INF file, along with the drivers for each such device. A *DDInstall* section can be shared by more than one *Models* section.

<a href="" id="ddinstall-services-section"></a>[***DDInstall*.Services Section**](inf-ddinstall-services-section.md)  
Starting with Microsoft Windows 2000, this section is required as an expansion of the *DDInstall* section for most kernel-mode device drivers. This includes any WDM drivers (exceptions are INF files for modems and display monitors). It controls how and when the services of a particular driver are started, its dependencies (if any) on underlying legacy, and so forth. This section also sets up event-logging services by a device driver if it supports event logging.

<a href="" id="ddinstall-hw-section"></a>[***DDInstall*.HW Section**](inf-ddinstall-hw-section.md)  
This optional section adds device-specific (and typically, driver-independent) information to the registry or removes such information from the registry, possibly for a multifunction device or to install one or more PnP filter drivers.

<a href="" id="ddinstall-coinstallers-section"></a>[***DDInstall*.CoInstallers Section**](inf-ddinstall-coinstallers-section.md)  
**Note**  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This optional section registers one or more device-specific co-installers supplied on the distribution media to supplement the operations of the system's device installer or of an existing device class installer.

A co-installer is an IHV/OEM-provided Win32 DLL that typically writes additional configuration information to the registry or performs other installation tasks that require dynamically generated, machine-specific information that is not available when the device's INF file is created. For more information, see [Writing a Co-installer](writing-a-co-installer.md).

<a href="" id="ddinstall-factdef-section"></a>[***DDInstall*.FactDef Section**](inf-ddinstall-factdef-section.md)  
**Note**  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This section should be included in the INF file of any manually installed non-PnP device. It specifies the factory default hardware configuration settings, such as the bus-relative I/O ports, IRQ (if any), and so forth, for the card.

<a href="" id="ddinstall-logconfigoverride-section"></a>[***DDInstall*.LogConfigOverride Section**](inf-ddinstall-logconfigoverride-section.md)  
**Note**  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This section is used to create an [override configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#logical-configuration-types-for-resource-requirements-lists), which overrides the hardware resource requirements that a Plug and Play device's bus driver reports.

<a href="" id="ddinstall-interfaces-section"></a>[***DDInstall*.Interfaces Section**](inf-ddinstall-interfaces-section.md)  
If a driver exports the functionality of a device interface class, therefore creating a new instance of the interface class, such as kernel-streaming still-image capture or data decompression, its INF file can have this section.

<a href="" id="interfaceinstall32-section"></a>[**InterfaceInstall32 Section**](inf-interfaceinstall32-section.md)  
If a to-be-installed component, such as a new class driver, provides one or more new [device interface classes](device-interface-classes.md) to higher-level components, its INF file has this section. In effect, this section bootstraps a set of device interfaces for a new class by setting up whatever is needed to use the functionality that the interface class provides.

<a href="" id="defaultinstall-section"></a>[**DefaultInstall Section**](inf-defaultinstall-section.md)  
An INF file's **DefaultInstall** section will be accessed if a user selects the "Install" menu item after right-clicking on the INF file name.

<a href="" id="defaultinstall-services-section"></a>[**DefaultInstall.Services Section**](inf-defaultinstall-services-section.md)  
This section is the same as the [**INF DDInstall.Services section**](inf-ddinstall-services-section.md), and is used in association with an [**INF DefaultInstall section**](inf-defaultinstall-section.md).

<a href="" id="strings-section"></a>[**Strings Section**](inf-strings-section.md)  
This section is required in every INF file to define each **%**<em>strkey</em>**%** token specified in the INF. By convention, the **Strings** section (or sections if the INF provides a set of locale-specific **Strings** sections) appears last in all system-supplied INF files for ease of maintenance and localization.

Some sections listed here, especially those with *Install* in their names, can contain directives that reference additional INF-writer-defined sections. Each directive causes particular operations to be performed on the items listed under the appropriate type of INF-writer-defined section during the installation process.

The set of valid entries and directives for any particular section in the previous list is section-specific and shown in the formal syntax of the reference for each of these sections. Additionally, see [Summary of INF Directives](summary-of-inf-directives.md) for a summary of the most commonly used directives.

Optional entries and directives within each such section are shown enclosed in unbolded brackets, as for example:

**\[Version\]**
...
\[**Provider=%**<em>INF-creator</em>**%**\]
...
The **Provider** entry in a **\[Version\]** section is optional in the sense that it is not a mandatory entry in every INF file.

 

 





