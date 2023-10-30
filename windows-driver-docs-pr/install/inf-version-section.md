---
title: INF Version section
description: By convention, the Version section appears first in INF files. Every INF file must have this section.
keywords:
- INF Version Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF Version Section
api_type:
- NA
ms.date: 04/10/2023
---

# INF Version section

By convention, the **Version** section appears first in INF files. Every INF file must have this section.

```inf
[Version]
 
Signature="signature-name"
[Class=class-name]
[ClassGuid={nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn}]
[Provider=%INF-creator%]
[ExtensionId={xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}]
[LayoutFile=filename.inf [,filename.inf]... ]  (Windows 2000 and Windows XP)
[CatalogFile=filename.cat]
[CatalogFile.nt=unique-filename.cat]
[CatalogFile.ntx86=unique-filename.cat]
[CatalogFile.ntia64=unique-filename.cat]  (Windows XP and later versions of Windows)
[CatalogFile.ntamd64=unique-filename.cat]  (Windows XP and later versions of Windows)
[CatalogFile.ntarm=unique-filename.cat]  (Windows 8 and later versions of Windows)
[CatalogFile.ntarm64=unique-filename.cat]  (Windows 10 version 1709 and later versions of Windows)

DriverVer=mm/dd/yyyy,w.x.y.z
[PnpLockDown=0|1] (Windows Vista and later versions of Windows)
[DriverPackageDisplayName=%driver-package-description%]
[DriverPackageType=PackageType]
```

## Entries

**Signature="**_signature-name_**"**  
Must be **$Windows NT$** or **$Chicago$**. This indicates the operating systems for which this INF is valid. These signature values have the following meanings.

| Signature value | Meaning |
|--|--|
| **$Windows NT$** | All Windows operating systems |
| **$Chicago$** | All Windows operating systems |

The enclosing dollar sign characters ($) are required but these strings are case-insensitive. If _signature-name_ is none of these string values, the file is not accepted as a valid INF.

Generally, Windows does not differentiate among these signature values. One of them must be specified, but it does not matter which one. You should specify the appropriate value so that someone reading an INF file can determine the operating systems for which it is intended.

Some class installers put additional requirements on how the signature value must be specified. Such requirements, if they exist, are discussed in device type-specific sections of this Windows Driver Kit (WDK).

An INF must supply OS-specific installation information by appending system-defined extensions to its _DDInstall_ sections, whether the _signature-name_ is **$Windows NT$** or **$Chicago$**. (See [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md) for a discussion of these extensions.)

**Class=**_class-name_  
For any standard type of device, this specifies the name of the [device setup class](./overview-of-device-setup-classes.md) for the type of device that is installed by using this INF file. This name is usually one of the system-defined class names, such as **Net** or **Display,** which are listed in _Devguid.h_. For more information, see [System-Supplied Device Setup Classes](./system-defined-device-setup-classes-reserved-for-system-use.md).

If an INF specifies a **Class**, it should also specify the corresponding system-defined GUID value for its **ClassGUID** entry. Specifying the matching GUID value for a device of any predefined device setup class can install the device and its drivers faster because this helps the system setup code to optimize its INF searching.

If an INF adds a new setup class of devices to the system, it should supply a unique, case-insensitive _class-name_ value that differs from any of the system-supplied classes in _Devguid.h_. The length of the _class-name_ string must be 32 characters or less. The INF must specify a newly generated GUID value for the **ClassGUID** entry. Also see [**INF ClassInstall32 Section**](inf-classinstall32-section.md).

This entry is irrelevant to an INF that installs neither a new device driver under a predefined device setup class nor a new device setup class.

> [!NOTE]
> This entry is required for device drivers that are installed through the Plug and Play (PnP) manager.

**ClassGuid={**_nnnnnnnn_**-**_nnnn_**-**_nnnn_**-**_nnnn_**-**_nnnnnnnnnnnn_**}**  
Specifies the [device setup class](./overview-of-device-setup-classes.md) GUID. The GUID value is formatted as shown here, where each _n_ is a hexadecimal digit.

This GUID value specifies the device setup class to assign to devices that are installed from this INF file. This class-specific GUID value also identifies the device class installer for the type of device and class-specific property page provider, if any.

For a new [device setup class](./overview-of-device-setup-classes.md), the INF must specify a newly generated **ClassGUID** value. For more information about how to create GUIDs, see [Using GUIDs in Drivers](../kernel/using-guids-in-drivers.md). Also see Device Setup Classes.

> [!NOTE]
> This entry is required for device drivers that are installed through the PnP manager.

**ExtensionId**={xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}  
Specifies the extension ID GUID when authoring an [extension INF](using-an-extension-inf-file.md). The GUID value is formatted as shown here, where each _x_ is a hexadecimal digit.

When creating the initial version of an extension INF, the INF must specify a newly generated **ExtensionId** value. However, when updating an existing extension INF, the **ExtensionId** must remain the same so that multiple related versions of the extension INF are versioned against each other instead of being treated as independent extension INFs that may be simultaneously installed on the same device instance. For more information about how to author extension INFs, see [Using an Extension INF File](using-an-extension-inf-file.md).

> [!NOTE]
> This entry is only required when creating an extension INF, as identified by specifying `Class = Extension` and `ClassGuid = {e2f84ce7-8efa-411c-aa69-97454ca4cb57}`.

**ClassVer=**_major_**.**_minor_  
Reserved for system use unless explicitly required by a device class such as Printer. For example, see [V4 Driver INF](../print/v4-driver-inf.md).

**Provider=%**_INF-creator_**%**  
Identifies the provider of the INF file. Typically, this is specified as an **%**_OrganizationName_**%** token that is expanded later in the INF file's [**Strings**](inf-strings-section.md) section. The maximum length, in characters, of a provider name is LINE_LEN.

For example, INF files supplied with the system typically specify the _INF-creator_ as **%**Msft**%** and define **%**Msft**% = "**Microsoft**"** in their [**Strings**](inf-strings-section.md) sections.

> [!NOTE]
> This entry is required for device drivers that are installed through the PnP manager.

**CatalogFile=**_filename_**.cat**  
Specifies a catalog (._cat_) file to be included on the distribution media of a driver package.

When a [driver package](driver-packages.md) is submitted to Microsoft for digital signing, WHQL provides a [catalog file](catalog-files.md) for the driver package after WHQL has tested and assigned digital signatures to the package. For more information about the testing and signing of IHV or OEM driver packages, see [WHQL Release Signature](whql-release-signature.md). Catalog files are not listed in the [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) section or [**CopyFiles**](inf-copyfiles-directive.md) directive of the INF. Windows assumes that the catalog file is in the same location as the INF file.

System-supplied INF files never have **CatalogFile=** entries because the operating system validates the signature for such an INF against all system-supplied _xxx.cat_ files.

**CatalogFile.nt=**_unique-filename_**.cat** |  
**CatalogFile.ntx86=**_unique-filename_**.cat** |  
**CatalogFile.ntia64=**_unique-filename_**.cat** |  
**CatalogFile.ntamd64=**_unique-filename_**.cat**  
**CatalogFile.ntarm=**_unique-filename_**.cat**  
**CatalogFile.ntarm64=**_unique-filename_**.cat**  

Specifies another INF-writer-determined, unique file name, with the ._cat_ extension, of a catalog file. If these optional entries are omitted, a given **CatalogFile=**_filename.cat_ is used for validating WDM device/driver installations.

If any decorated **CatalogFile._xxx_=** entry exists in an INF's **Version** section together with an undecorated **CatalogFile=** entry, the undecorated entry is assumed to identify a _filename.cat_ for validating device installations, driver installations, or both on those platforms for which a decorated entry is not specified.

Any cross-platform device driver INF file that has **CatalogFile=** and **CatalogFile.**_xxx_**=** entries must supply a unique IHV/OEM-determined name for each such .cat file.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

> [!NOTE]
> Because the same .cat file can be used across all supported platforms, the use of this entry is not required or recommended. However, you must use this entry if you want to create platform-specific .cat files for your driver package.

**DriverVer=** **mm/dd/yyyy**,**w.x.y.z**  
This entry specifies version information for drivers that are installed by this INF file. Starting with Windows 2000, this entry is required.

For information about how to specify this entry, see [**INF DriverVer Directive**](inf-driverver-directive.md).

**PnpLockDown=0**|**1**  
Specifies whether Plug and Play (PnP) prevents applications from directly modifying the files that a [driver package's](driver-packages.md) INF file specifies. If the **PnpLockDown** directive is set to 1, PnP prevents applications from directly modifying the files that are copied by INF **CopyFiles** directives. Otherwise, if the directive is not included in an INF file or the value of the directive is set to zero, an application that has administrator privileges can directly modify these files. Driver files that are protected in this manner are referred to as _third-party protected driver files_.

To ensure the integrity of a PnP driver installation, applications should not directly modify driver files that are copied by the driver package INF file. Applications should only use the device installation mechanisms provided by Windows to update PnP drivers.

Starting with Windows Vista, a driver package should set **PnpLockDown** to 1 to prevent an application from directly modifying driver files. However, some existing applications that uninstall driver packages do directly delete driver files. To maintain compatibility with these applications, the **PnpLockDown** directive for such driver package should be set to zero.

> [!NOTE]
> Although PnP on Windows Vista and later versions of Windows does not require that an INF file include a **PnpLockDown** directive in order to install a driver, PnP in a future version of Windows might require that INF files for PnP [driver packages](driver-packages.md) include the **PnpLockDown** directive.

**DriverPackageDisplayName=%**driver-package-description**%**  
Deprecated. Was previously used by Driver Install Frameworks (DIFx). For info about the DIFx deprecation, see [DIFx Guidelines](difx-guidelines.md).

**DriverPackageType=** _PackageType_  
Deprecated. Was previously used by Driver Install Frameworks (DIFx). For info about the DIFx deprecation, see [DIFx Guidelines](difx-guidelines.md).

## Remarks

When a [driver package](driver-packages.md) passes Microsoft Windows Hardware Quality Lab (WHQL) testing, WHQL returns _.cat_ catalog files to the IHV or OEM. Each _.cat_ file contains a digitally encrypted signature for the driver package. The IHV or OEM must list these _.cat_ files in the INF **Version** section and must supply the files on the distribution media, in the same location as the INF file. The _.cat_ files must be uncompressed.

> [!NOTE]
> If an INF **Version** section does not include at least one **CatalogFile** or **CatalogFile.nt**_xxx_ entry, the driver is treated as unsigned, and the dates listed in the [**DriverVer**](inf-driverver-directive.md) directive are not displayed by Windows.

For more information, see [Driver Signing](signing-drivers-for-public-release--windows-vista-and-later-.md).

## Examples

The following example shows a **Version** section typical of a simple driver package INF, followed by the required [**SourceDisksNames**](inf-sourcedisksnames-section.md) and [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections implied by the entries specified in this sample **Version** section:

```inf
[Version]
Signature="$Windows NT$"
Class=SCSIAdapter
ClassGUID={4D36E97B-E325-11CE-BFC1-08002BE10318}
Provider=%INF_Provider%
CatalogFile=example.cat
DriverVer=01/29/2010,1.2.3.4
PnpLockdown=1

[SourceDisksNames]
;
; diskid = description[, [tagfile] [, <unused>, subdir]]
;
1 = %Disk_Description%,,,\WinNT

[SourceDisksFiles.x86]
;
; filename_on_source = diskID[, [subdir][, size]]
;
exampleDriver.sys = 1,\x86

; ...

[Strings]
INF_Provider="Contoso"
Disk_Description = "Contoso Drivers Disk"
; ...
```

## See also

[**_DDInstall_**](inf-ddinstall-section.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**SourceDisksFiles**](inf-sourcedisksfiles-section.md)

[**Strings**](inf-strings-section.md)
