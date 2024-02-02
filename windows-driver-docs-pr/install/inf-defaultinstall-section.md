---
title: INF DefaultInstall Section
description: An INF file's DefaultInstall section is accessed if a user selects the "Install" menu item after selecting and holding (or right-clicking) on the INF file name.
keywords:
- INF DefaultInstall Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF DefaultInstall Section
api_type:
- NA
ms.date: 05/03/2023
---

# INF DefaultInstall section

> [!NOTE]
> If you are building a [universal driver package](using-a-universal-inf-file.md), this section is valid only if it has an architecture decoration, for example `[DefaultInstall.NTAMD64]`.

> [!NOTE]
> Using both **DefaultInstall** and [**Manufacturer**](inf-manufacturer-section.md) sections in your INF will cause Universal INF validation failures and can lead to inconsistent installation behaviors.  See [Using a Universal INF File](using-a-universal-inf-file.md).

An INF file's **DefaultInstall** section is accessed if a user selects the "Install" menu item after selecting and holding (or right-clicking) on the INF file name. On Windows 10 version 1903 and later versions of Windows, an INF with **DefaultInstall** can be used in many [driver package](driver-packages.md) APIs if it meets the requirements of a [primitive driver](../develop/creating-a-primitive-driver.md).

```inf
[DefaultInstall] | 
[DefaultInstall.nt] | 
[DefaultInstall.ntx86] | 
[DefaultInstall.ntia64] | (Windows XP and later versions of Windows)
[DefaultInstall.ntamd64] | (Windows XP and later versions of Windows)
[DefaultInstall.ntarm] | (Windows 8 and later versions of Windows)
[DefaultInstall.ntarm64] (Windows 10 version 1709 and later versions of Windows)
 
[CopyFiles=@filename | file-list-section[,file-list-section] ...]
[CopyINF=filename1.inf[,filename2.inf]...]
[AddReg=add-registry-section[,add-registry-section]...]
[Include=filename1.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...]
[Delfiles=file-list-section[,file-list-section]...]
[Renfiles=file-list-section[,file-list-section]...]
[DelReg=del-registry-section[,del-registry-section]...]
[BitReg=bit-registry-section[,bit-registry-section]...]
[ProfileItems=profile-items-section[,profile-items-section]...]
[UpdateInis=update-ini-section[,update-ini-section]...]
[UpdateIniFields=update-inifields-section[,update-inifields-section]...]
[Ini2Reg=ini-to-registry-section[,ini-to-registry-section]...]
[RegisterDlls=register-dll-section[,register-dll-section]...]
[UnregisterDlls=unregister-dll-section[,unregister-dll-section]...] ...
```

## Entries

Not all valid entries are supported in a [Universal INF](using-a-universal-inf-file.md).  The following lists which directives are valid in a universal INF and which are not.

### Supported in a Universal INF

**CopyFiles=@**_filename_ | _file-list-section_[**,**_file-list-section_] ...  
This optional directive either specifies one named file to be copied from the source medium to the destination, or references one or more INF-writer-defined sections that specify files to be transferred from the source media to the destination.

The **DefaultDestDir** entry in the **DestinationDirs** section of the INF specifies the destination for any single file to be copied. The **SourceDisksNames** and **SourceDisksFiles** sections, or an additional INF specified in the **LayoutFile** entry of this INF's **Version** section, provide the location on the distribution media of the driver files.

For more information, see [**INF CopyFiles Directive**](inf-copyfiles-directive.md).

**CopyINF=**_filename1_**.inf**[**,**_filename2_**.inf**]...  
(Windows XP and later versions of Windows.) This directive causes specified INF files to be copied to the target system.

For more information, see [**INF CopyINF Directive**](inf-copyinf-directive.md).

**AddReg=**_add-registry-section_[**,**_add-registry-section_]...  
This directive references one or more INF-writer-defined sections in which new subkeys, possibly with initial value entries, are specified to be written into the registry or in which the value entries of existing keys are modified.

For more information, see [**INF AddReg Directive**](inf-addreg-directive.md).

**Include=**_filename1_**.inf**[**,**_filename2_**.inf**]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device and/or driver. If this entry is specified, usually so is a **Needs** entry.

For example, the system INF files for device drivers that depend on the system's kernel-streaming support specify this entry as follows:

```inf
Include= ks.inf,kscaptur.inf,ksfilter.inf
```

**Needs=**_inf-section-name_[**,**_inf-section-name_]...  
This optional entry specifies sections within system-supplied INF files that must be processed during the installation of this device. Typically, such a named section is a _DDInstall_ (or _DDInstall_**.**_xxx_) section within one of the INF files that are listed in an **Include** entry. However, it can be any section that is referenced within such a _DDInstall_ or _DDInstall_**.**_xxx_ section of the included INF.

For example, the INF files for device drivers that have the preceding **Include** entry specify this entry as follows:

```inf
Needs= KS.Registration,KSCAPTUR.Registration.NT,MSPCLOCK.Installation
```

### Not supported in a Universal INF

**Delfiles=**_file-list-section_[**,**_file-list-section_]...  
This directive references one or more INF-writer-defined sections listing files on the target to be deleted.

For more information, see [**INF DelFiles Directive**](inf-delfiles-directive.md).

**Renfiles=**_file-list-section_[**,**_file-list-section_]...  
This directive references one or more INF-writer-defined sections listing files to be renamed on the destination before device-relevant source files are copied to the target computer.

For more information, see [**INF RenFiles Directive**](inf-renfiles-directive.md).

**DelReg=**_del-registry-section_[**,**_del-registry-section_]...  
This directive references one or more INF-writer-defined sections in which keys and/or value entries are specified to be removed from the registry during installation of the devices.

For more information, see [**INF DelReg Directive**](inf-delreg-directive.md).

**BitReg=**_bit-registry-section_[**,**_bit-registry-section_]...  
This directive references one or more INF-writer-defined sections in which existing registry value entries of type [REG_BINARY](/windows/desktop/SysInfo/registry-value-types) are modified. For more information, see [**INF AddReg Directive**](inf-addreg-directive.md).

For more information, see [**INF BitReg Directive**](inf-bitreg-directive.md).

**ProfileItems=**_profile-items-section_[**,**_profile-items-section_]...  
This directive references one or more INF-writer-defined sections that describe items to be added to, or removed from, the Start menu.

For more information, see [**INF ProfileItems Directive**](inf-profileitems-directive.md).

**UpdateInis=**_update-ini-section_[**,**_update-ini-section_]...  
This rarely used directive references one or more INF-writer-defined sections, specifying a source INI file from which a particular section or line within such a section is to be read into a destination INI file of the same name during installation. Optionally, line-by-line modifications to an existing INI file on the destination from a specified source INI file of the same name can be specified in the update-ini section.

For more information, see [**INF UpdateInis Directive**](inf-updateinis-directive.md).

**UpdateIniFields=**_update-inifields-section_[**,**_update-inifields-section_]...  
This rarely used directive references one or more INF-writer-defined sections in which modifications within the lines of a device-specific INI file are specified.

For more information, see [**INF UpdateIniFields Directive**](inf-updateinifields-directive.md).

**Ini2Reg=**_ini-to-registry-section_[**,**_ini-to-registry-section_]...  
This rarely used directive references one or more INF-writer-defined sections in which sections or lines from a device-specific INI file, supplied on the source media, are to be moved into the registry.

For more information, see [**INF Ini2Reg Directive**](inf-ini2reg-directive.md).

**RegisterDlls=**_register-dll-section_[**,**_register-dll-section_]...  
This directive references one or more INF sections used to specify files that are OLE controls and require self-registration.

For more information, see [**INF RegisterDlls Directive**](inf-registerdlls-directive.md).

**UnregisterDlls=**_unregister-dll-section_[**,**_unregister-dll-section_]...  
This directive references one or more INF sections used to specify files that are OLE controls and require self-unregistration (self-removal).

For more information, see [**INF UnregisterDlls Directive**](inf-unregisterdlls-directive.md).

## Remarks

**DefaultInstall** sections must not be used for device installations. Use **DefaultInstall** sections only for the installation of class filter drivers, file system filters, and kernel driver services that are not associated with a device node (_devnode_).

If using **DefaultInstall** on Windows 10 version 1903 and later versions of Windows, it is recommended that the INF file meets the requirements of a [primitive driver](../develop/creating-a-primitive-driver.md).

> [!NOTE]
> The INF file of a [driver package](driver-packages.md) that has a [**Manufacturer**](inf-manufacturer-section.md) section must not contain an INF **DefaultInstall** section if the driver package is to be digitally signed. For more information about signing driver packages, see [Driver Signing](driver-signing.md).

> [!NOTE]
> Unlike a [**_DDInstall_**](inf-ddinstall-section.md) section, a **DefaultInstall** section cannot contain [**DriverVer**](inf-driverver-directive.md) or [**LogConfig**](inf-logconfig-directive.md) directives.

To install a **DefaultInstall** section from a _device installation application_, use the following call to [**InstallHinfSection**](/windows/win32/api/setupapi/nf-setupapi-installhinfsectionw):

```cpp
InstallHinfSection(NULL,NULL,TEXT("DefaultInstall 132 path-to-inf\infname.inf"),0); 
```

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

## Examples

The following example shows a typical **DefaultInstall** section:

```inf
[DefaultInstall]
CopyFiles=MyAppWinFiles, MyAppSysFiles, @SRSutil.exe
AddReg=MyAppRegEntries
```

## See also

[**_DDInstall_**](inf-ddinstall-section.md)

[**DriverVer**](inf-driverver-directive.md)

[**LogConfig**](inf-logconfig-directive.md)
