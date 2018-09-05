---
title: INF DefaultInstall Section
description: An INF file's DefaultInstall section is accessed if a user selects the "Install" menu item after right-clicking on the INF file name.
ms.assetid: 41412124-38d9-43c0-9954-d34b242a3922
keywords:
- INF DefaultInstall Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DefaultInstall Section
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# INF DefaultInstall Section


**Note**  If you are building a universal or mobile driver package, this section is not valid and should not be used.  Instead, use only the [**INF Manufacturer Section**](inf-manufacturer-section.md).  Using both **DefaultInstall** and **Manufacturer** sections in your INF will cause Universal INF validation failures and can lead to inconsistent installation behaviors.  See [Using a Universal INF File](using-a-universal-inf-file.md).

 

An INF file's **DefaultInstall** section is accessed if a user selects the "Install" menu item after right-clicking on the INF file name.

```
[DefaultInstall] | 
[DefaultInstall.nt] | 
[DefaultInstall.ntx86] | 
[DefaultInstall.ntarm] | (Windows 8 and later versions of Windows)
[DefaultInstall.ntarm64]  (Windows 10 version 1709 and later versions of Windows)
[DefaultInstall.ntia64] | (Windows XP and later versions of Windows)
[DefaultInstall.ntamd64]  (Windows XP and later versions of Windows)
 
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


<a href="" id="copyfiles--filename---file-list-section--file-list-section-----"></a>**CopyFiles=@***filename* | *file-list-section*\[**,***file-list-section*\] ...  
This optional directive either specifies one named file to be copied from the source medium to the destination, or references one or more INF-writer-defined sections that specify files to be transferred from the source media to the destination.

The **DefaultDestDir** entry in the **DestinationDirs** section of the INF specifies the destination for any single file to be copied. The **SourceDisksNames** and **SourceDisksFiles** sections, or an additional INF specified in the **LayoutFile** entry of this INF's **Version** section, provide the location on the distribution media of the driver files.

For more information, see [**INF CopyFiles Directive**](inf-copyfiles-directive.md).

<a href="" id="copyinf-filename1-inf--filename2-inf----"></a>**CopyINF=***filename1***.inf**\[**,***filename2***.inf**\]...  
(Windows XP and later versions of Windows.) This directive causes specified INF files to be copied to the target system.

For more information, see [**INF CopyINF Directive**](inf-copyinf-directive.md).

<a href="" id="addreg-add-registry-section--add-registry-section----"></a>**AddReg=***add-registry-section*\[**,***add-registry-section*\]...  
This directive references one or more INF-writer-defined sections in which new subkeys, possibly with initial value entries, are specified to be written into the registry or in which the value entries of existing keys are modified.

For more information, see [**INF AddReg Directive**](inf-addreg-directive.md).

<a href="" id="include-filename1-inf--filename2-inf----"></a>**Include=***filename1***.inf**\[**,***filename2***.inf**\]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device and/or driver. If this entry is specified, usually so is a **Needs** entry.

For example, the system INF files for device drivers that depend on the system's kernel-streaming support specify this entry as follows:

```
Include= ks.inf[,[kscaptur.inf,][ksfilter.inf]]
```

For more information about the **Include** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="needs-inf-section-name--inf-section-name----"></a>**Needs=***inf-section-name*\[**,***inf-section-name*\]...  
This optional entry specifies sections within system-supplied INF files that must be processed during the installation of this device. Typically, such a named section is a *DDInstall* (or *DDInstall***.***xxx*) section within one of the INF files that are listed in an **Include** entry. However, it can be any section that is referenced within such a *DDInstall* or *DDInstall***.***xxx* section of the included INF.

For example, the INF files for device drivers that have the preceding **Include** entry specify this entry as follows:

```
Needs= KS.Registration[,KSCAPTUR.Registration | 
                        KSCAPTUR.Registration.NT,MSPCLOCK.Installation]
```

**Needs** entries cannot be nested. (For more information about the **Needs** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md)).

<a href="" id="delfiles-file-list-section--file-list-section----"></a>**Delfiles=***file-list-section*\[**,***file-list-section*\]...  
This directive references one or more INF-writer-defined sections listing files on the target to be deleted.

For more information, see [**INF DelFiles Directive**](inf-delfiles-directive.md).

<a href="" id="renfiles-file-list-section--file-list-section----"></a>**Renfiles=***file-list-section*\[**,***file-list-section*\]...  
This directive references one or more INF-writer-defined sections listing files to be renamed on the destination before device-relevant source files are copied to the target computer.

For more information, see [**INF RenFiles Directive**](inf-renfiles-directive.md).

<a href="" id="delreg-del-registry-section--del-registry-section----"></a>**DelReg=***del-registry-section*\[**,***del-registry-section*\]...  
This directive references one or more INF-writer-defined sections in which keys and/or value entries are specified to be removed from the registry during installation of the devices.

Typically, this directive is used to handle upgrades when an INF must clean up old registry entries from a previous installation of this device. An **HKR** specification in such a delete-registry section designates the **..Class\\***SetupClassGUID***\\***device-instance-id* registry path of the user-accessible driver. This type of **HKR** specification is also referred to as a. "software key".

For more information, see [**INF DelReg Directive**](inf-delreg-directive.md).

<a href="" id="bitreg-bit-registry-section--bit-registry-section----"></a>**BitReg=***bit-registry-section*\[**,***bit-registry-section*\]...  
This directive references one or more INF-writer-defined sections in which existing registry value entries of type REG_BINARY are modified. For more information, see [**INF AddReg Directive**](inf-addreg-directive.md).

An **HKR** specification in such a bit-registry section designates the **..Class\\***SetupClassGUID***\\***device-instance-id* registry path of the user-accessible driver. This type of **HKR** specification is also referred to as a. "software key".

For more information, see [**INF BitReg Directive**](inf-bitreg-directive.md).

<a href="" id="profileitems-profile-items-section--profile-items-section----"></a>**ProfileItems=***profile-items-section*\[**,***profile-items-section*\]...  
This directive references one or more INF-writer-defined sections that describe items to be added to, or removed from, the Start menu.

For more information, see [**INF ProfileItems Directive**](inf-profileitems-directive.md).

<a href="" id="updateinis-update-ini-section--update-ini-section----"></a>**UpdateInis=***update-ini-section*\[**,***update-ini-section*\]...  
This rarely used directive references one or more INF-writer-defined sections, specifying a source INI file from which a particular section or line within such a section is to be read into a destination INI file of the same name during installation. Optionally, line-by-line modifications to an existing INI file on the destination from a specified source INI file of the same name can be specified in the update-ini section.

For more information, see [**INF UpdateInis Directive**](inf-updateinis-directive.md).

<a href="" id="updateinifields-update-inifields-section--update-inifields-section----"></a>**UpdateIniFields=***update-inifields-section*\[**,***update-inifields-section*\]...  
This rarely used directive references one or more INF-writer-defined sections in which modifications within the lines of a device-specific INI file are specified.

For more information, see [**INF UpdateIniFields Directive**](inf-updateinifields-directive.md).

<a href="" id="ini2reg-ini-to-registry-section--ini-to-registry-section----"></a>**Ini2Reg=***ini-to-registry-section*\[**,***ini-to-registry-section*\]...  
This rarely used directive references one or more INF-writer-defined sections in which sections or lines from a device-specific INI file, supplied on the source media, are to be moved into the registry.

For more information, see [**INF Ini2Reg Directive**](inf-ini2reg-directive.md).

<a href="" id="registerdlls-register-dll-section--register-dll-section----"></a>**RegisterDlls=***register-dll-section*\[**,***register-dll-section*\]...  
This directive references one or more INF sections used to specify files that are OLE controls and require self-registration.

For more information, see [**INF RegisterDlls Directive**](inf-registerdlls-directive.md).

<a href="" id="unregisterdlls-unregister-dll-section--unregister-dll-section----"></a>**UnregisterDlls=***unregister-dll-section*\[**,***unregister-dll-section*\]...  
This directive references one or more INF sections used to specify files that are OLE controls and require self-unregistration (self-removal).

For more information, see [**INF UnregisterDlls Directive**](inf-unregisterdlls-directive.md).

Remarks
-------

**DefaultInstall** sections must not be used for device installations. Use **DefaultInstall** sections only for the installation of class filter drivers, class co-installers, file system filters, and kernel driver services that are not associated with a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)).

**Note**  The INF file of a [driver package](driver-packages.md) must not contain an INF **DefaultInstall** section if the driver package is to be digitally signed. For more information about signing driver packages, see [Driver Signing](driver-signing.md).

 

Providing a **DefaultInstall** section is optional. If an INF file does not include a **DefaultInstall** section, selecting "Install" after right-clicking on the file name causes an error message to be displayed.

**Note**  Unlike a [***DDInstall***](inf-ddinstall-section.md) section, a **DefaultInstall** section cannot contain [**DriverVer**](inf-driverver-directive.md) or [**LogConfig**](inf-logconfig-directive.md) directives.

 

To install a **DefaultInstall** section from a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application), use the following call to **InstallHinfSection**:

```
InstallHinfSection(NULL,NULL,TEXT("DefaultInstall 132 path-to-inf\infname.inf"),0); 
```

For more information about **InstallHinfSection**, see the Microsoft Windows SDK documentation.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

Examples
--------

The following example shows a typical **DefaultInstall** section:

```
[DefaultInstall]
CopyFiles=MyAppWinFiles, MyAppSysFiles, @SRSutil.exe
AddReg=MyAppRegEntries
```

In this example, the **DefaultInstall** section is executed if a user selects "Install" after right-clicking on the INF file name.

## See also


[***DDInstall***](inf-ddinstall-section.md)

[**DriverVer**](inf-driverver-directive.md)

[**LogConfig**](inf-logconfig-directive.md)

 

 






