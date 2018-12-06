---
title: INF CopyFiles Directive
description: A CopyFiles directive can do either of the following
ms.assetid: 65756b1c-ea61-4bb4-90ac-4d96ceaf9665
keywords:
- INF CopyFiles Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF CopyFiles Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF CopyFiles Directive


A **CopyFiles** directive can do either of the following:

-   Cause a single file to be copied from the source media to the default destination directory.
-   Reference one or more INF-writer-defined sections in the INF that each specifies a list of files to be copied from the source media to the destination.

```cpp
[DDInstall] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] |  (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64]  (Windows XP and later versions of Windows)
  
CopyFiles=@filename | file-list-section[, file-list-section]... 
```

A **CopyFiles** directive can be specified within any of the sections shown in the formal syntax statement. This directive can also be specified within any of the following INF sections:

-   An *add-interface-section* referenced by the INF [**AddInterface**](inf-addinterface-directive.md) directive in a [***DDInstall*.Interfaces**](inf-ddinstall-interfaces-section.md) section.
-   An *install-interface-section* referenced in an INF [**InterfaceInstall32**](inf-interfaceinstall32-section.md) section

Each named section referenced by a **CopyFiles** directive has one or more entries of the following form:

```cpp
[file-list-section]
destination-file-name[,[source-file-name][,[unused][,flag]]]
...
```

An INF-writer-defined *file-list-section* can have any number of entries, each on a separate line.

Each *file-list-section* can have an optional, associated <em>file-list-section</em>**.security** section of the following form:

```cpp
[file-list-section.security]
"security-descriptor-string"
```

## Entries


<a href="" id="destination-file-name"></a>*destination-file-name*  
Specifies the name of the destination file. If no *source-file-name* is given, this specification is also the name of the source file.

<a href="" id="source-file-name"></a>*source-file-name*  
Specifies the name of the source file. If the source and destination file names for the file copy operation are the same, *source-file-name* can be omitted.

<a href="" id="unused"></a>*unused*  
This entry is no longer supported in Windows 2000 and later versions of Windows.

<a href="" id="flag"></a>*flag*  
These optional flags, expressed in hexadecimal notation or as a decimal value in a section entry, can be used to control how (or whether) a particular source file is copied to the destination. One or more (ORed) values for the following system-defined flags can be specified. However, some of these flags are mutually exclusive:

<a href="" id="0x00000001---copyflg-warn-if-skip--"></a>**0x00000001** (COPYFLG_WARN_IF_SKIP)   
Send a warning if the user chooses not to copy a file. This flag and the next are mutually exclusive, and both are irrelevant to INF files that are digitally signed.

<a href="" id="0x00000002--copyflg-noskip-"></a>**0x00000002** (COPYFLG_NOSKIP)  
Do not allow the user to skip copying a file. This flag is implied if the [driver package](driver-packages.md) is signed.

<a href="" id="0x00000004--copyflg-noversioncheck-"></a>**0x00000004** (COPYFLG_NOVERSIONCHECK)  
Ignore file versions and write over existing files in the destination directory. This flag and the next two are mutually exclusive. This flag is irrelevant to digitally signed INF files.

<a href="" id="0x00000008--copyflg-force-file-in-use-"></a>**0x00000008** (COPYFLG_FORCE_FILE_IN_USE)  
Force file-in-use behavior: do not copy over an existing file of the same name if it is currently open. Instead, copy the given source file with a temporary name so that it can be renamed and used when the next restart occurs.

<a href="" id="0x00000010--copyflg-no-overwrite-"></a>**0x00000010** (COPYFLG_NO_OVERWRITE)  
Do not replace an existing file in the destination directory with a source file of the same name. This flag cannot be combined with any other flags.

<a href="" id="0x00000020--copyflg-no-version-dialog--"></a>**0x00000020** (COPYFLG_NO_VERSION_DIALOG)   
Do not write over a file in the destination directory with the source file if the existing file is newer than the source file.

Beginning with Windows Vista and later operating systems, Windows respects this flag for all INF files, including digitally signed INF files.

Prior to Windows Vista this flag is irrelevant to digitally signed INF files. If a [driver package](driver-packages.md) is digitally signed, Windows installs the package as a whole and does not selectively omit files in the package based on other versions already present on the computer.

<a href="" id="0x00000040---copyflg-overwrite-older-only-"></a>**0x00000040** (COPYFLG_OVERWRITE_OLDER_ONLY)  
Copy the source file to the destination directory only if the file on the destination is superseded by a newer version. This flag is irrelevant to digitally signed INF files.

<a href="" id="0x00000400--copyflg-replaceonly--"></a>**0x00000400** (COPYFLG_REPLACEONLY)   
Copy the source file to the destination directory only if the file is already present in the destination directory.

<a href="" id="0x00000800--copyflg-nodecomp--"></a>**0x00000800** (COPYFLG_NODECOMP)   
(Windows 7 and later) Copy the source file to the destination directory without decompressing the source file if it is compressed.

<a href="" id="0x00001000--copyflg-replace-boot-file-"></a>**0x00001000** (COPYFLG_REPLACE_BOOT_FILE)  
This file is required by the system loader. The system will prompt the user to restart the system.

<a href="" id="0x00002000--copyflg-noprune-"></a>**0x00002000** (COPYFLG_NOPRUNE)  
Do not delete this operation as a result of optimization.

For example, Windows might determine that the file copy operation is not necessary because the file already exists. However, the writer of the INF knows that the operation is required and directs Windows to override its optimization and perform the file operation.

This flag can be used to ensure that files are copied if they are also specified in an INF [**DelFiles**](inf-delfiles-directive.md) directive or an INF [**RenFiles**](inf-renfiles-directive.md) directive.

<a href="" id="0x00004000--copyflg-in-use-rename-"></a>**0x00004000** (COPYFLG_IN_USE_RENAME)  
If the source file cannot be copied because the destination file is being used, rename the destination file, then copy the source file to the destination file, and delete the renamed destination file. If the destination file cannot be renamed, complete the copy operation during the next system restart. If the renamed destination file cannot be deleted, delete the renamed destination file during the next system restart.

<a href="" id="security-descriptor-string"></a>*security-descriptor-string*  
Specifies a security descriptor, to be applied to all files copied by the named *file-list-section*. The *security-descriptor-string* is a string with tokens to indicate the DACL (**D:**) security component.

For information about security descriptor strings, see [Security Descriptor Definition Language (Windows)](https://msdn.microsoft.com/library/windows/desktop/aa379567). For information about the format of security descriptor strings, see Security Descriptor Definition Language (Windows).

If an <em>file-list-section</em>**.security** section is not specified, files inherit the security characteristics of the directory into which the files are copied.

If an <em>file-list-section</em>**.security** section is specified, the following ACE's must be included so that installations and upgrades of devices and system service packs can occur:

-   (A;;GA;;;SY) − Grants all access to the local system.
-   (A;;GA;;;BA) − Grants all access to built-in administrators.

Do *not* specify ACE strings that grant write access to nonprivileged users.

For more information about how to specify security descriptors, see [Creating Secure Device Installations](creating-secure-device-installations.md).

Remarks
-------

Windows only copies a [driver package](driver-packages.md) to its destination location as part of a driver installation if the file has an INF **CopyFiles** directive. When it copies files, the operating system automatically generates temporary file names, when necessary, and renames the copied source files the next time that the operating system is started.

The INF file writer must also supply path specifications for files that are copied from source media by using the INF [**SourceDisksNames**](inf-sourcedisksnames-section.md) section and the INF [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) section to explicitly specify the path of each source file relative to the INF file in the source media.

The destination of copy operations is controlled by the [**INF DestinationDirs section**](inf-destinationdirs-section.md). This section controls the destination for all file-copy operations, as follows:

- If a named section referenced by a **CopyFiles** directive has a corresponding entry in the [**DestinationDirs**](inf-destinationdirs-section.md) section of the same INF, that entry explicitly specifies the target destination directory into which all files that are listed in the named section are copied. If the named section is not listed in the **DestinationDirs** section, Windows uses the **DefaultDestDir** entry in the **DestinationDirs** section of the INF file.
- If a **CopyFiles** directive uses the **@**<em>filename</em> syntax, Windows uses the **DefaultDestDir** entry in the **DestinationDirs** section of the INF file.

The following points apply to the INF **CopyFiles** directive:

- Every *file-list-section* name must be unique to the INF file, but it can be referenced by **CopyFiles**, [**DelFiles**](inf-delfiles-directive.md), or [**RenFiles**](inf-renfiles-directive.md) directives elsewhere in the same INF file. The section name must follow the general rules that are described in [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).
- File names that are specified in either the **@**<em>filename</em> or *file-list-section* entries must be the exact name of a file on the source media. You cannot use a %*strkey*% token to specify the file name. For more information about %*strkey*% tokens, see [**INF Strings Section**](inf-strings-section.md).
- The **CopyFiles** directive does not support decorating a *file-list-section* name with a system-defined platform extension (**.nt**, **.ntx86**, **.ntia64**, or **.ntamd64**).
- Do not use **CopyFiles** directives to copy INF files. For more information, see [Copying INF Files](copying-inf-files.md).

Starting with Windows Vista, the following points also apply to the INF **CopyFiles** directive:

-   When the DIFx tools preinstall a driver package in the [driver store](driver-store.md), they only copy a file from the driver package source to the driver store if the file has a corresponding INF **CopyFiles** directive.
-   As part of a Windows upgrade, Windows only copies a driver package file to the [driver store](driver-store.md) as part of a driver migration if the file has an INF **CopyFiles** directive.

Examples
--------

This example shows how the [**SourceDisksNames**](inf-sourcedisksnames-section.md), [**SourceDisksFiles**](inf-sourcedisksfiles-section.md), and [**DestinationDirs**](inf-destinationdirs-section.md) sections specify the paths for copy-file (and delete-file) operations that occur in processing a simple device-driver INF. (The same INF was also used previously as examples of [**Version**](inf-version-section.md), **SourceDisksNames**, and **SourceDisksFiles** sections.)

```cpp
[SourceDisksNames]
1 = %Floppy_Description%,,,\WinNT


[SourceDisksFiles.x86]
aha154x.sys = 2,\x86 ; on distribution disk 2, in subdir \WinNT\x86

[DestinationDirs]
DefaultDestDir = 12  ; DIRID_DRIVERS 
                     ; == \System32\Drivers on Windows platforms
; ... Manufacturer and Models sections omitted here


DelFiles= AHA154X.DelFiles
 ; defines a delete-files section not shown here
; ... some other directives and sections omitted here

[AHA154X.NTx86]
CopyFiles=@AHA154x.SYS 
; ... some other directives and sections omitted here
; ...
```

This example shows how a **CopyFiles** directive can be used in a [***DDInstall*.CoInstallers**](inf-ddinstall-coinstallers-section.md) section of an INF for a device driver that provides two device-specific co-installers to supplement the INF processing of the system device-type-specific class installer.

```cpp
[DestinationDirs]
XxDev_Coinstallers_CopyFiles = 11  ; DIRID_SYSTEM
; ... other file-list entries and DefaultDestDirs omitted here

; ... Manufacturer, Models, and DDInstall sections omitted here

[XxDev_Install.CoInstallers] 
CopyFiles=XxDev_Coinstallers_CopyFiles
; ... AddReg omitted here

[XxDev_Coinstallers_CopyFiles]
XxPreInst.dll   ; dev-specific co-installer run before class installer
XxPostInst.dll  ; run after class installer (post processing)
```

As the preceding example suggests, the names of new device-specific co-installers can be constructed from the name of the provider (shown here as *Xx*) and the intended use for each such co-installer DLL (shown here as *PreInst* and *PostInst*).

For additional examples of how to use the INF **CopyFiles** directive, see the INF files for the device driver samples that are included in the *src* directory of the Windows Driver Kit (WDK).

## See also


[**AddInterface**](inf-addinterface-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.CoInstallers**](inf-ddinstall-coinstallers-section.md)

[***DDInstall*.Interfaces**](inf-ddinstall-interfaces-section.md)

[**DelFiles**](inf-delfiles-directive.md)

[**DestinationDirs**](inf-destinationdirs-section.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[**RenFiles**](inf-renfiles-directive.md)

[**SourceDisksFiles**](inf-sourcedisksfiles-section.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**Strings**](inf-strings-section.md)

[**Version**](inf-version-section.md)

 

 






