---
title: Combining Platform Extensions with Operating System Versions
description: Combining Platform Extensions with Operating System Versions
ms.assetid: ef3b7138-b68a-4dba-b011-fcb93e3072a3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Combining Platform Extensions with Operating System Versions


Within the [**INF Manufacturer section**](inf-manufacturer-section.md) of an INF file, you can supply [**INF *Models* sections**](inf-models-section.md) that are specific to various versions of the Windows operating system. These version-specific *Models* sections are identified by using the *TargetOSVersion* decoration.

Within the same INF file, different [**INF *Models* sections**](inf-models-section.md) can be specified for different versions of the operating system. The specified versions indicate target operating system versions with which the INF *Models* sections will be used. If no versions are specified, Windows uses a *Models* section without the *TargetOSVersion* decoration for all versions of all operating systems.

### *TargetOSVersion* decoration format

The following example shows the correct format of the *TargetOSVersion* decoration for Windows XP through Windows 10, version 1511:

**nt**\[*Architecture*\]\[**.**\[*OSMajorVersion*\]\[**.**\[*OSMinorVersion*\]\[**.**\[*ProductType*\]\[**.**\[*SuiteMask*\]\]\]\]\]

Starting with Windows 10, version 1607 (Build 14310 and later), the correct format of the *TargetOSVersion* decoration includes *BuildNumber*:

**nt**\[*Architecture*\]\[**.**\[*OSMajorVersion*\]\[**.**\[*OSMinorVersion*\]\[**.**\[*ProductType*\]\[**.**\[*SuiteMask*\]\]\[**.**\[*BuildNumber*\]\]\]\]\]

Each field is defined as follows:

<a href="" id="nt"></a>**nt**  
Specifies that the target operating system is NT-based. Windows 2000 and later versions of Windows are all NT-based.

<a href="" id="architecture"></a>*Architecture*  
Identifies the hardware platform. If specified, this must be **x86**, **ia64**, or **amd64**. If not specified, the associated INF *Models* section can be used with any hardware platform.

<a href="" id="osmajorversion"></a>*OSMajorVersion*  
A number that represents the major version number for the operating system. The following table defines the major version for the Windows operating systems.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Windows version</th>
<th align="left">Major version</th>
</tr>
</thead>
<tbody>
<tr class="even">
<td align="left"><p>Windows 10</p></td>
<td align="left"><p>10</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2012 R2</p></td>
<td align="left"><p>6</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 8.1</p></td>
<td align="left"><p>6</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2012</p></td>
<td align="left"><p>6</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 8</p></td>
<td align="left"><p>6</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2008 R2</p></td>
<td align="left"><p>6</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 7</p></td>
<td align="left"><p>6</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2008</p></td>
<td align="left"><p>6</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows Vista</p></td>
<td align="left"><p>6</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2003</p></td>
<td align="left"><p>5</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows XP</p></td>
<td align="left"><p>5</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="osminorversion"></a>*OSMinorVersion*  
A number that represents the minor version number for the operating system. The following table defines the minor version for the Windows operating systems.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Windows version</th>
<th align="left">Minor version</th>
</tr>
</thead>
<tbody>
<tr class="even">
<td align="left"><p>Windows 10</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2012 R2</p></td>
<td align="left"><p>3</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 8.1</p></td>
<td align="left"><p>3</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2012</p></td>
<td align="left"><p>2</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 8</p></td>
<td align="left"><p>2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2008 R2</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows 7</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2008</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows Vista</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Server 2003</p></td>
<td align="left"><p>2</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows XP</p></td>
<td align="left"><p>1</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="producttype"></a>*ProductType*

A number that represents *one* of the VER_NT_*xxxx* flags defined in *Winnt.h*, such as the following:

**0x0000001** (VER_NT_WORKSTATION)

**0x0000002** (VER_NT_DOMAIN_CONTROLLER)

**0x0000003** (VER_NT_SERVER)

If a product type is specified, the INF file will be used only if the operating system matches the specified product type. If the INF file supports multiple product types for a single operating system version, multiple *TargetOSVersion* entries are required.

*SuiteMask*

A number that represents *a combination of* one or more of the VER_SUITE_*xxxx* flags defined in *Winnt.h*. These flags include the following:

**0x00000001** (VER_SUITE_SMALLBUSINESS)  
**0x00000002** (VER_SUITE_ENTERPRISE)  
**0x00000004** (VER_SUITE_BACKOFFICE)  
**0x00000008** (VER_SUITE_COMMUNICATIONS)  
**0x00000010** (VER_SUITE_TERMINAL)  
**0x00000020** (VER_SUITE_SMALLBUSINESS_RESTRICTED)  
**0x00000040** (VER_SUITE_EMBEDDEDNT)  
**0x00000080** (VER_SUITE_DATACENTER)  
**0x00000100** (VER_SUITE_SINGLEUSERTS)  
**0x00000200** (VER_SUITE_PERSONAL)  
**0x00000400** (VER_SUITE_SERVERAPPLIANCE)  

If one or more suite mask values are specified, the INF file will be used only if the operating system matches all the specified product suites. If the INF file supports multiple product suite combinations for a single operating system version, multiple *TargetOSVersion* entries are required.

*BuildNumber*

Specifies the minimum OS build number of the Windows 10 release to which the section applies, starting with build 14310 or later.

The build number is assumed to be relative to some specific OS major/minor version only, and may be reset for some future OS major/minor version.

Any build number specified by the *TargetOSVersion* decoration is evaluated only when the OS major/minor version of the *TargetOSVersion* matches the current OS (or AltPlatformInfo) version exactly.  If the current OS version is greater than the OS version specified by the *TargetOSVersion* decoration (OSMajorVersion,OSMinorVersion), the section is considered applicable regardless of the build number specified. Likewise, if the current OS version is less than the OS version specified by the TargetOSVersion decoration, the section is not applicable.

If build number is supplied, the OS version and BuildNumber of the *TargetOSVersion* decoration must both be greater than the OS version and build number of the Windows 10 build 14310 where this decoration was first introduced.  Earlier versions of the operating system without these changes (for example, Windows 10 build 10240) will not parse unknown decorations, so an attempt to target these earlier builds will actually prevent that OS from considering the decoration valid at all.

### <a href="" id="how-setup-processes-targetosversion-decorations"></a>How Windows processes *TargetOSVersion* decorations

When you install a device or driver on a host operating system, Windows follows these steps to process the [**INF *Models* sections**](inf-models-section.md) within an INF file:

1.  If one or more [**INF *Models* sections**](inf-models-section.md) have the *TargetOS* decoration, Windows selects the INF *Models* section that is closest to the attributes for the host operating system.

    For example, if an INF *Models* section has a *TargetOS* decoration of **ntx86.5.1**, Windows selects that section if the host operating system is running Windows XP or later version of Windows on an x86-based system.

    Similarly, if an [**INF *Models* section**](inf-models-section.md) has a *TargetOS* decoration of **nt.6.0**, Windows selects that section if the host operating system is Windows Vista or later version of Windows on any supported hardware platform.

    If an INF *Models* section has a *TargetOS* decoration of **nt.10.0...14393**, Windows selects that section if the host operating system is running a Windows 10 build equal to or greater than 14393 on any supported hardware platform.

2.  If none of the [**INF *Models* sections**](inf-models-section.md) have a *TargetOS* decoration that matches the host operating system, Windows selects the *Models* section that has either a matching platform extension or no platform extension.

    For example, if an INF *Models* section has a platform extension of **ntx86**, Windows selects that section if the host operating system is Microsoft Windows 2000 or later version of Windows on an x86-based system.

    Similarly, if an [**INF *Models* sections**](inf-models-section.md) has no platform extension, Windows selects that section if the host operating system is Windows 2000 or later version of Windows on any supported hardware platform.

3.  If Windows cannot find a matching [**INF *Models* section**](inf-models-section.md), it will not use the INF file to install the device or driver.

### Sample INF *Models* sections with*TargetOSVersion* decorations

The following topics provide samples of how to decorate platform extensions for target operating systems within an [**INF *Models* section**](inf-models-section.md):

[Sample INF *Models* Sections for One or More Target Operating Systems](sample-inf-models-sections-for-one-or-more-target-operating-system.md)

[Sample INF *Models* Sections for Only One Target Operating System](sample-inf-models-sections-for-only-one-target-operating-system.md)

[Sample INF File for Device Installation on Multiple Versions of Windows](sample-inf-file-for-device-installation-on-multiple-versions-of-windows.md)

 

 





