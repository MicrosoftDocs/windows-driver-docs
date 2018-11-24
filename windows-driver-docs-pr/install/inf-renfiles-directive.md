---
title: INF RenFiles Directive
description: A RenFiles directive references an INF-writer-defined section elsewhere in the INF file, which causes that list of files to be renamed in the context of operations on the section in which the referring RenFiles directive is specified.
ms.assetid: 269171f7-88f6-47bb-9997-8fdcbe3fa688
keywords:
- INF RenFiles Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF RenFiles Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF RenFiles Directive


**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

A **RenFiles** directive references an INF-writer-defined section elsewhere in the INF file, which causes that list of files to be renamed in the context of operations on the section in which the referring **RenFiles** directive is specified.

```cpp
[DDInstall] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] |  (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64]  (Windows XP and later versions of Windows)
  
Renfiles=file-list-section[,file-list-section]...
```

A **RenFiles** directive can be specified within any of the sections shown in the formal syntax statement. This directive can also be specified within any of the following INF-writer-defined sections:

-   An *add-interface-section* referenced by the [**AddInterface**](inf-addinterface-directive.md) directive in a [***DDInstall*.Interfaces**](inf-ddinstall-interfaces-section.md) section.
-   An *install-interface-section* referenced in an [**InterfaceInstall32**](inf-interfaceinstall32-section.md) section.

Each named section referenced by a **RenFiles** directive has one or more entries of the following form:

```cpp
[file-list-section]
 
new-dest-file-name,old-source-file-name 
...
```

A *file-list-section* can have any number of entries, each on a separate line.

## Entries


<a href="" id="new-dest-file-name"></a>*new-dest-file-name*  
Specifies the new name to be given to the file on the destination.

<a href="" id="old-source-file-name"></a>*old-source-file-name*  
Specifies the old name of the file.

Remarks
-------

**Important**  This directive must be used carefully. We highly recommend that you do not use the **RenFiles** directive in the INF file for a Plug and Play (PnP) function driver.

 

Any *file-list-section* name must be unique to the INF file, but it can be referenced by [**CopyFiles**](inf-copyfiles-directive.md), **DelFiles**, or **RenFiles** directives elsewhere in the same INF. Such an INF-writer-defined section name must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

The **RenFiles** directive does not support decorating a *file-list-section* name with a system-defined platform extension (**.nt**, **.ntx86**, **.ntia64**, or **.ntamd64**).

The [**DestinationDirs**](inf-destinationdirs-section.md) section of the INF file controls the destination for all file-rename operations, regardless of the section that contains a particular **RenFiles** directive. The following rules describe the file-rename operation:

-   If a named section referenced by a **RenFiles** directive has a corresponding entry in the [**DestinationDirs**](inf-destinationdirs-section.md) section in the same INF, that entry explicitly specifies the target destination directory. All files that are listed in the named section are renamed on the destination before these source files are copied.
-   If a named section is not listed in the **DestinationDirs** section, Windows uses the *DefaultDestDir* entry in the **DestinationDirs** section of the INF.

**Note**  You cannot use a %*strkey*% token to specify the new or old file names. For more information about %*strkey*% tokens, see [**INF Strings Section**](inf-strings-section.md).

 

Examples
--------

This example shows a section referenced by a **RenFiles** directive.

```cpp
[RenameOldFilesSec]
devfile41.sav, devfile41.sys
```

## See also


[**AddInterface**](inf-addinterface-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[**CopyFiles**](inf-copyfiles-directive.md)

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.CoInstallers**](inf-ddinstall-coinstallers-section.md)

**DelFiles**
[**DestinationDirs**](inf-destinationdirs-section.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[**SourceDisksFiles**](inf-sourcedisksfiles-section.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**Strings**](inf-strings-section.md)

[**Version**](inf-version-section.md)

 

 






