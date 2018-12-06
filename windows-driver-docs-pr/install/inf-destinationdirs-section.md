---
title: INF DestinationDirs Section
description: A DestinationDirs section specifies the target destination directory or directories for all copy, delete, and/or rename operations on files referenced by name elsewhere in the INF file.
ms.assetid: fadebcb9-da4b-4daf-9e84-822447e5cb2a
keywords:
- INF DestinationDirs Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DestinationDirs Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DestinationDirs Section


A **DestinationDirs** section specifies the target destination directory or directories for all copy, delete, and/or rename operations on files referenced by name elsewhere in the INF file.

```cpp
[DestinationDirs]

[DefaultDestDir=dirid[,subdir]] 
[file-list-section=dirid[,subdir]]... 
```

## Entries


<a href="" id="defaultdestdir-dirid--subdir-"></a>**DefaultDestDir=**<em>dirid</em>\[**,**<em>subdir</em>\]  
Specifies the default destination directory for all copy, delete, and/or rename operations on files that are not explicitly listed in a *file-list-section* referenced by other entries here. To ensure that file operations always occur in the correct directory, an INF file that includes **Include** and **Needs** entries should not specify a default destination directory. For more information, see the following Remarks section.

<a href="" id="file-list-section-dirid--subdir--------------"></a><em>file-list-section</em>**=**<em>dirid</em>\[**,**<em>subdir</em>\]\] ...   
Specifies the INF-writer-determined name of a section referenced by a [**CopyFiles**](inf-copyfiles-directive.md), [**RenFiles**](inf-renfiles-directive.md), or [**DelFiles**](inf-delfiles-directive.md) directive elsewhere in the INF file. Such an entry is optional if this section has a **DefaultDestDir** entry and all copy-file operations specified in this INF have the same target destination. However, any *file-list-section* referenced by a **RenFiles** or **DelFiles** directive elsewhere in the INF must be listed here.

<a href="" id="dirid"></a>*dirid*  
Specifies the directory identifier of the target directory for operations on files that are referenced by name, possibly within a named *file-list-section* of the INF. For lists of commonly used *dirids*, see [Using Dirids](using-dirids.md).

<a href="" id="subdir"></a>*subdir*  
Specifies the subdirectory (and the rest of its path, if any, under the directory identified by *dirid*) to be the destination of the file operations in the given *file-list-section*.

Remarks
-------

The **DestinationDirs** section is required in any INF file that uses an [**INF CopyFiles directive**](inf-copyfiles-directive.md) or that references a *file-list-section*, whether with a **CopyFiles**, [**DelFiles**](inf-delfiles-directive.md), or [**RenFiles**](inf-renfiles-directive.md) directive.

If *Abc.inf* includes sections from another INF file, *Def.inf*, and both INF files include a **DefaultDestDir** entry for copy-file, rename-file, or delete-file operations, Windows ignores the default destination directory that is specified in Def.inf and performs all the corresponding file operations in the default destination directory that is specified in *Abc.inf*.

To ensure that file operations always occur in the correct directories, an INF file that includes **Include** and **Needs** entries should not include a **DefaultDestDir** entry in a **DestinationDirs** section. Instead, such an INF file should explicitly reference all the *file-list-section* names that are specified by [**CopyFiles**](inf-copyfiles-directive.md), [**RenFiles**](inf-renfiles-directive.md), and [**DelFiles**](inf-delfiles-directive.md) directives in the **DestinationDirs** section.

If an INF file does not include **Include** and **Needs** entries, the INF can use the **DefaultDestDir** entry to specify a default destination for copy, rename, and delete file operations that appear elsewhere in the INF file:

-   [**CopyFiles**](inf-copyfiles-directive.md) directives that use the direct copy (@*filename*) notation must have a **DefaultDestDir** entry in the **DestinationDirs** section of the INF in which the direct-copy entry appears.
-   **CopyFiles**, [**RenFiles**](inf-renfiles-directive.md), or [**DelFiles**](inf-delfiles-directive.md) sections that are not directly referenced in the **DestinationDirs** section must have a **DefaultDestDir** entry in the **DestinationDirs** section of the INF in which the copy, rename, and delete file sections appear.

Examples
--------

This example sets the default target directory for all copy-file, delete-file, and rename-file operations. Such a simple **DestinationDirs** section is common to INF files for new peripheral devices, because such an INF usually just copies a set of source files into a single directory on the target computer.

```cpp
[DestinationDirs]
DefaultDestDir = 12 ; dirid = \Drivers on WinNT platforms
```

This example shows a fragment of the **DestinationDirs** section of the INF for display/video drivers.

```cpp
[DestinationDirs]
DefaultDestDir     = 11 ; dirid = \system32 on WinNT platforms

; ... 

; list of per-Manufacturer, per-Models, per-DDInstall-section, and
; CopyFiles-referenced xxx.Miniport/xxx.Display sections omitted here
; along with several other miniport/display paired drivers
; ...
vga.Miniport     = 12
vga.Display      = 11
xga.Miniport     = 12
xga.Display      = 11

; all video miniports copied into \system32\drivers on WinNT platforms
; all paired display drivers copied into \system32
```

## See also


[**ClassInstall32**](inf-classinstall32-section.md)

[**CopyFiles**](inf-copyfiles-directive.md)

[***DDInstall***](inf-ddinstall-section.md)

[**DelFiles**](inf-delfiles-directive.md)

[**RenFiles**](inf-renfiles-directive.md)

[**SourceDisksFiles**](inf-sourcedisksfiles-section.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**Using Dirids**](https://docs.microsoft.com/windows-hardware/drivers/install/using-dirids)

[**Version**](inf-version-section.md)

 

 






