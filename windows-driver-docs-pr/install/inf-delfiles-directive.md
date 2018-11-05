---
title: INF DelFiles Directive
description: A DelFiles directive references an INF-writer-defined section elsewhere in the INF file, and causes that list of files to be deleted.
ms.assetid: e163f88f-e0ab-41e7-97df-49853ec0836f
keywords:
- INF DelFiles Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DelFiles Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DelFiles Directive


**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

A **DelFiles** directive references an INF-writer-defined section elsewhere in the INF file, and causes that list of files to be deleted in the context of operations on the section in which the referring **DelFiles** directive is specified.

```cpp
[DDInstall] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] |  (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64]  (Windows XP and later versions of Windows) 
  
Delfiles=file-list-section[,file-list-section]... 
```

A **DelFiles** directive can be specified within any of the sections shown in the formal syntax statement. This directive can also be specified within any of the following INF-writer-defined sections:

-   An add-interface-section referenced by the [**AddInterface**](inf-addinterface-directive.md) directive in a [***DDInstall*.Interfaces**](inf-ddinstall-interfaces-section.md) section.
-   An install-interface-section referenced in an [**InterfaceInstall32**](inf-interfaceinstall32-section.md) section

Each named section referenced by a **DelFiles** directive has one or more entries of the following form:

```cpp
[file-list-section]
 
destination-file-name[,,,flag]
...
```

A *file-list-section* can have any number of entries, each on a separate line.

## Entries


<a href="" id="destination-file-name"></a>*destination-file-name*  
Specifies the name of the file to be deleted from the destination.

Do not specify a file that is listed in a [**CopyFiles**](inf-copyfiles-directive.md) directive. If a file is listed in both a **CopyFiles**-referenced and a **DelFiles**-referenced section, and the file is currently present on the system with a valid signature, the operating system might optimize away the copy operation but perform the delete operation. This is very likely *not* what the INF writer intended.

**Note**  You cannot use a %*strkey*% token to specify the destination-file-name entry. For more information about %*strkey*% tokens, see [**INF Strings Section**](inf-strings-section.md).

 

<a href="" id="flag"></a>*flag*  
This optional value can be one of the following, expressed in hexadecimal notation as shown here or as a decimal value:

<a href="" id="0x00000001--delflg-in-use-"></a>**0x00000001** (DELFLG_IN_USE)  
Delete the named file, possibly after it was used during the installation process.

Setting this flag value in an INF queues the file-deletion operation until the system has restarted if the given file cannot be deleted because it is in use while this INF is being processed. Otherwise, such a file will not be deleted.

<a href="" id="0x00010000---delflg-in-use1-"></a>**0x00010000** (DELFLG_IN_USE1)  
(Windows 2000 or later versions of Windows) This flag is a high-word version of the DELFLG_IN_USE flag, and it has the same purpose and effect. This flag should be used in only for installations on NT-based systems.

Setting this flag value in an INF prevents conflicts with the COPYFLG_WARN_IF_SKIP flag in an INF with both **DelFiles** and [**CopyFiles**](inf-copyfiles-directive.md) directives that reference the same *file-list-section*.

Remarks
-------

**Important**  This directive must be used carefully. We highly recommend that you do not use the **DelFiles** directive in the INF file for a Plug and Play (PnP) function driver.

 

Any *file-list-section* name must be unique to the INF file, but it can be referenced by [**CopyFiles**](inf-copyfiles-directive.md), **DelFiles**, or [**RenFiles**](inf-renfiles-directive.md) directives elsewhere in the same INF. Such an INF-writer-defined section name must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

The **DelFiles** directive does not support decorating a *file-list-section* name with a system-defined platform extension (**.nt**, **.ntx86**, **.ntia64**, or **.ntamd64**).

The [**DestinationDirs**](inf-destinationdirs-section.md) section of the INF file controls the destination for all file-deletion operations, regardless of the section that contains a particular **DelFiles** directive. If a named section referenced by a **DelFiles** directive has a corresponding entry in the **DestinationDirs** section of the same INF, that entry explicitly specifies the target destination directory from which all files that are listed in the named section will be deleted. If the named section is not listed in the **DestinationDirs** section, Windows uses the **DefaultDestDir** entry in the INF.

Examples
--------

This example shows how the [**DestinationDirs**](inf-destinationdirs-section.md) section specifies the path for a delete-file operation that occurs in processing a simple device-driver INF.

```cpp
[DestinationDirs]
DefaultDestDir = 12  ; DIRID_DRIVERS 

; ... 

[AHA154X]
CopyFiles=@AHA154x.MPD
DelFiles=ASPIDEV ; defines delete-files section name
; ... some other directives and sections omitted here

[ASPIDEV]
VASPID.SYS ; name of file to be deleted, if it exists on target 
; ...
```

## See also


[**AddInterface**](inf-addinterface-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[**CopyFiles**](inf-copyfiles-directive.md)

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.CoInstallers**](inf-ddinstall-coinstallers-section.md)

[**DestinationDirs**](inf-destinationdirs-section.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

**RenFiles**
[**Strings**](inf-strings-section.md)

 

 






