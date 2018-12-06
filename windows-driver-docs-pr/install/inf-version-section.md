---
title: INF Version Section
description: By convention, the Version section appears first in INF files. Every INF file must have this section.
ms.assetid: 53e30950-28a3-4ae3-a351-a917b02c84a5
keywords:
- INF Version Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF Version Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF Version Section


By convention, the **Version** section appears first in INF files. Every INF file must have this section.

```cpp
[Version]
 
Signature="signature-name"
[Class=class-name]
[ClassGuid={nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn}]
[Provider=%INF-creator%]
[LayoutFile=filename.inf [,filename.inf]... ]  (Windows 2000 and Windows XP)
[CatalogFile=filename.cat]
[CatalogFile.nt=unique-filename.cat]
[CatalogFile.ntx86=unique-filename.cat]
[CatalogFile.ntia64=unique-filename.cat]  (Windows XP and later versions of Windows)
[CatalogFile.ntamd64=unique-filename.cat]  (Windows XP and later versions of Windows)
DriverVer=mm/dd/yyyy,w.x.y.z
[DontReflectOffline=1] (Windows Vista and later versions of Windows)
[PnpLockDown=0|1] (Windows Vista and later versions of Windows)
[DriverPackageDisplayName=%driver-package-description%]
[DriverPackageType=PackageType]
```

## Entries


<a href="" id="signature--signature-name-"></a>**Signature="**<em>signature-name</em>**"**  
Must be **$Windows NT$** or **$Chicago$**. This indicates the operating systems for which this INF is valid. These signature values have the following meanings.

| Signature value  | Meaning                       |
|------------------|-------------------------------|
| **$Windows NT$** | All Windows operating systems |
| **$Chicago$**    | All Windows operating systems |

 

The enclosing dollar sign characters ($) are required but these strings are case-insensitive. If *signature-name* is none of these string values, the file is not accepted as a valid INF.

Generally, Windows does not differentiate among these signature values. One of them must be specified, but it does not matter which one. You should specify the appropriate value so that someone reading an INF file can determine the operating systems for which it is intended.

Some class installers put additional requirements on how the signature value must be specified. Such requirements, if they exist, are discussed in device type-specific sections of this Windows Driver Kit (WDK).

An INF must supply OS-specific installation information by appending system-defined extensions to its *DDInstall* sections, whether the *signature-name* is <strong>$Windows NT$</strong>or **$Chicago$**. (See [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md) for a discussion of these extensions.)

<a href="" id="class-class-name"></a>**Class=**<em>class-name</em>  
For any standard type of device, this specifies the name of the [device setup class](device-setup-classes.md) for the type of device that is installed by using this INF file. This name is usually one of the system-defined class names, such as **Net** or **Display,** which are listed in *Devguid.h*. For more information, see [System-Supplied Device Setup Classes](https://msdn.microsoft.com/library/windows/hardware/ff553419).

If an INF specifies a **Class,** it should also specify the corresponding system-defined GUID value for its **ClassGUID** entry. Specifying the matching GUID value for a device of any predefined device setup class can install the device and its drivers faster because this helps the system setup code to optimize its INF searching.

If an INF adds a new setup class of devices to the system, it should supply a unique, case-insensitive *class-name* value that differs from any of the system-supplied classes in *Devguid.h*. The length of the *class-name* string must be 32 characters or less. The INF must specify a newly generated GUID value for the **ClassGUID** entry. Also see [**INF ClassInstall32 Section**](inf-classinstall32-section.md).

This entry is irrelevant to an INF that installs neither a new device driver under a predefined device setup class nor a new device setup class.

**Note**  This entry is required for device drivers that are installed through the Plug and Play (PnP) manager.

 

<a href="" id="classguid--nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn-"></a>**ClassGuid={**<em>nnnnnnnn</em>**-***nnnn***-***nnnn***-***nnnn***-**<em>nnnnnnnnnnnn</em>**}**  
Specifies the [device setup class](device-setup-classes.md) GUID. The GUID value is formatted as shown here, where each *n* is a hexadecimal digit.

This GUID value specifies the device setup class subkey in the registry **...\\Class** tree under which to write registry information for the drivers of devices that are installed from this INF file. This class-specific GUID value also identifies the device class installer for the type of device and class-specific property page provider, if any.

For a new [device setup class](device-setup-classes.md), the INF must specify a newly generated **ClassGUID** value. For more information about how to create GUIDs, see [Using GUIDs in Drivers](https://msdn.microsoft.com/library/windows/hardware/ff565392). Also see Device Setup Classes.

**Note**  This entry is required for device drivers that are installed through the PnP manager.

 

<a href="" id="provider--inf-creator-"></a>**Provider=%**<em>INF-creator</em>**%**  
Identifies the provider of the INF file. Typically, this is specified as an **%**<em>OrganizationName</em>**%** token that is expanded later in the INF file's [**Strings**](inf-strings-section.md) section. The maximum length, in characters, of a provider name is LINE_LEN.

For example, INF files supplied with the system typically specify the *INF-creator* as <strong>%</strong>Msft<strong>%</strong> and define <strong>%</strong>Msft<strong>% = "</strong>Microsoft<strong>"</strong> in their [**Strings**](inf-strings-section.md) sections.

**Note**  This entry is required for device drivers that are installed through the PnP manager.

 

<a href="" id="catalogfile-filename-cat"></a>**CatalogFile=**<em>filename</em>**.cat**  
Specifies a catalog (.*cat*) file to be included on the distribution media of a device/driver.

When a [driver package](driver-packages.md) is submitted to Microsoft for digital signing, WHQL provides a [catalog file](catalog-files.md) for the driver package after WHQL has tested and assigned digital signatures to the package. For more information about the testing and signing of IHV or OEM driver packages, see [WHQL Release Signature](whql-release-signature.md). Catalog files are not listed in the [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) section or [**CopyFiles**](inf-copyfiles-directive.md) directive of the INF. Windows assumes that the catalog file is in the same location as the INF file.

System-supplied INF files never have **CatalogFile=** entries because the operating system validates the signature for such an INF against all system-supplied *xxx.cat* files.

<a href="" id="catalogfile-nt-unique-filename-cat--"></a>**CatalogFile.nt=**<em>unique-filename</em>**.cat** |  

<a href="" id="catalogfile-ntx86-unique-filename-cat--"></a>**CatalogFile.ntx86=**<em>unique-filename</em>**.cat** |  

<a href="" id="catalogfile-ntia64-unique-filename-cat--"></a>**CatalogFile.ntia64=**<em>unique-filename</em>**.cat** |  

<a href="" id="catalogfile-ntamd64-unique-filename-cat"></a>**CatalogFile.ntamd64=**<em>unique-filename</em>**.cat**  
Specifies another INF-writer-determined, unique file name, with the .*cat* extension, of a catalog file. If these optional entries are omitted, a given **CatalogFile=**<em>filename.cat</em> is used for validating WDM device/driver installations.

If any decorated **CatalogFile.*xxx*=** entry exists in an INF's **Version** section together with an undecorated **CatalogFile=** entry, the undecorated entry is assumed to identify a *filename.cat* for validating device installations, driver installations, or both on those platforms for which a decorated entry is not specified.

Any cross-platform device driver INF file that has **CatalogFile=** and **CatalogFile.**<em>xxx</em>**=** entries must supply a unique IHV/OEM-determined name for each such .cat file.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

**Note**  Because the same .cat file can be used across all supported platforms, the use of this entry is not required or recommended. However, you must use this entry if you want to create platform-specific .cat files for your driver package.

 

<a href="" id="driverver-mm-dd-yyyy--w-x-y-z-"></a>**DriverVer=** **mm/dd/yyyy**,**w.x.y.z**  
This entry specifies version information for drivers that are installed by this INF file. Starting with Windows 2000, this entry is required.

For information about how to specify this entry, see [**INF DriverVer Directive**](inf-driverver-directive.md).

<a href="" id="dontreflectoffline-1"></a>**DontReflectOffline=1**  
This directive is for internal use only on Windows Vista and later versions of Windows. This directive must not be used for any reason in a third-party INF file.

**Note**  This directive is present in some of the INF files for inbox drivers. The INF file writer must be careful not to copy this directive along with other INF Version directives that the writer might copy from an inbox INF file.

 

<a href="" id="pnplockdown-0-1"></a>**PnpLockDown=0**|**1**  
Specifies whether Plug and Play (PnP) prevents applications from directly modifying the files that a [driver package's](driver-packages.md) INF file specifies. If the **PnpLockDown** directive is set to 1, PnP prevents applications from directly modifying the files that are copied by INF **CopyFiles** directives. Otherwise, if the directive is not included in an INF file or the value of the directive is set to zero, an application that has administrator privileges can directly modify these files. Driver files that are protected in this manner are referred to as *third-party protected driver files*.

To ensure the integrity of a PnP driver installation, applications should not directly modify driver files that are copied by the driver package INF file. Applications should only use the device installation mechanisms provided by Windows to update PnP drivers.

Starting with Windows Vista, a driver package should set **PnpLockDown** to 1 to prevent an application from directly modifying driver files. However, some existing applications that uninstall driver packages do directly delete driver files. To maintain compatibility with these applications, the **PnpLockDown** directive for such driver package should be set to zero.

**Note**  Although PnP on Windows Vista and later versions of Windows does not require that an INF file include a **PnpLockDown** directive in order to install a driver, PnP in a future version of Windows might require that INF files for PnP [driver packages](driver-packages.md) include the **PnpLockDown** directive.

 

<a href="" id="driverpackagedisplayname--driver-package-description-"></a><strong>DriverPackageDisplayName=%</strong>driver-package-description<strong>%</strong>  
Specifies a string token that corresponds to a string key entry in an INF [**Strings**](inf-strings-section.md) section. The string key entry supplies the [driver package](driver-packages.md) display name. Driver Install Frameworks (DIFx) uses the driver package display name to describe the purpose of driver package to end-users.

<a href="" id="driverpackagetype-packagetype"></a>**DriverPackageType=** *PackageType*  
Specifies the [driver package](driver-packages.md) type. Driver Install Frameworks (DIFx) uses the driver package type to determine the type of driver package.

Remarks
-------

When a [driver package](driver-packages.md) passes Microsoft Windows Hardware Quality Lab (WHQL) testing, WHQL returns *.cat* catalog files to the IHV or OEM. Each *.cat* file contains a digitally encrypted signature for the driver package. The IHV or OEM must list these *.cat* files in the INF **Version** section and must supply the files on the distribution media, in the same location as the INF file. The *.cat* files must be uncompressed.

**Note**   If an INF **Version** section does not include at least one **CatalogFile** or **CatalogFile.nt***xxx* entry, the driver is treated as unsigned, and the dates listed in the [**DriverVer**](inf-driverver-directive.md) directive are not displayed by Windows.

 

For more information, see [Driver Signing](signing-drivers-for-public-release--windows-vista-and-later-.md).

Examples
--------

The following example shows a **Version** section typical of a simple device-driver INF, followed by the required [**SourceDisksNames**](inf-sourcedisksnames-section.md) and [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections implied by the entries specified in this sample **Version** section:

```cpp
[Version]
Signature="$Windows NT$"
Class=SCSIAdapter
ClassGUID={4D36E97B-E325-11CE-BFC1-08002BE10318}
Provider=%INF_Provider%
CatalogFile=aha154_ntx86.cat
DriverVer=01/29/2010

[SourceDisksNames]
;
; diskid = description[, [tagfile] [, <unused>, subdir]]
;
1 = %Floppy_Description%,,,\WinNT

[SourceDisksFiles.x86]
;
; filename_on_source = diskID[, [subdir][, size]]
;
aha154x.sys = 1,\x86

; ...

[Strings]
INF_Provider="Adaptec"
Floppy_Description = "Adaptec Drivers Disk"
; ...
```

## See also


[***DDInstall***](inf-ddinstall-section.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**SourceDisksFiles**](inf-sourcedisksfiles-section.md)

[**Strings**](inf-strings-section.md)

 

 






