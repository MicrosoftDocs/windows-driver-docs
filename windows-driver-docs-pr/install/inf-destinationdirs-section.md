---
title: INF DestinationDirs Section
description: A DestinationDirs section specifies the target destination directory or directories for all copy, delete, and/or rename operations on files referenced by name elsewhere in the INF file.
keywords:
- INF DestinationDirs Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF DestinationDirs Section
api_type:
- NA
ms.date: 04/10/2023
---

# INF DestinationDirs section

A **DestinationDirs** section specifies the target destination directory or directories for all copy, delete, and/or rename operations on files referenced by name elsewhere in the INF file.

```inf
[DestinationDirs]

[DefaultDestDir=dirid[,subdir]] 
[file-list-section=dirid[,subdir]]... 
```

## Entries

**DefaultDestDir=**_dirid_[,_subdir_]  
Specifies the default destination directory for all copy, delete, and/or rename operations on files that are not explicitly listed in a _file-list-section_ referenced by other entries here. To ensure that file operations always occur in the correct directory, an INF file that includes **Include** and **Needs** entries should not specify a default destination directory. For more information, see the following Remarks section.

_file-list-section_**=**_dirid_[,_subdir_]] ...  
Specifies the INF-writer-determined name of a section referenced by a [**CopyFiles**](inf-copyfiles-directive.md), [**RenFiles**](inf-renfiles-directive.md), or [**DelFiles**](inf-delfiles-directive.md) directive elsewhere in the INF file. Such an entry is optional if this section has a **DefaultDestDir** entry and all copy-file operations specified in this INF have the same target destination. However, any _file-list-section_ referenced by a **RenFiles** or **DelFiles** directive elsewhere in the INF must be listed here.

_dirid_  
Specifies the directory identifier of the target directory for operations on files that are referenced by name, possibly within a named _file-list-section_ of the INF. For lists of commonly used _dirids_, see [Using Dirids](using-dirids.md). On Windows 10 version 1709 and later versions of windows, it is recommended that DIRID 13 be used. See [run from Driver Store](../develop/run-from-driver-store.md) for more information.

_subdir_  
Specifies the subdirectory (and the rest of its path, if any, under the directory identified by _dirid_) to be the destination of the file operations in the given _file-list-section_.

## Remarks

The **DestinationDirs** section is required in any INF file that uses an [**INF CopyFiles directive**](inf-copyfiles-directive.md) or that references a _file-list-section_, whether with a **CopyFiles**, [**DelFiles**](inf-delfiles-directive.md), or [**RenFiles**](inf-renfiles-directive.md) directive.

If _Abc.inf_ includes sections from another INF file, _Def.inf_, and both INF files include a **DefaultDestDir** entry for copy-file, rename-file, or delete-file operations, Windows ignores the default destination directory that is specified in Def.inf and performs all the corresponding file operations in the default destination directory that is specified in _Abc.inf_.

To ensure that file operations always occur in the correct directories, an INF file that includes **Include** and **Needs** entries should not include a **DefaultDestDir** entry in a **DestinationDirs** section. Instead, such an INF file should explicitly reference all the _file-list-section_ names that are specified by [**CopyFiles**](inf-copyfiles-directive.md), [**RenFiles**](inf-renfiles-directive.md), and [**DelFiles**](inf-delfiles-directive.md) directives in the **DestinationDirs** section.

If an INF file does not include **Include** and **Needs** entries, the INF can use the **DefaultDestDir** entry to specify a default destination for copy, rename, and delete file operations that appear elsewhere in the INF file:

- [**CopyFiles**](inf-copyfiles-directive.md) directives that use the direct copy (@_filename_) notation must have a **DefaultDestDir** entry in the **DestinationDirs** section of the INF in which the direct-copy entry appears.
- **CopyFiles**, [**RenFiles**](inf-renfiles-directive.md), or [**DelFiles**](inf-delfiles-directive.md) sections that are not directly referenced in the **DestinationDirs** section must have a **DefaultDestDir** entry in the **DestinationDirs** section of the INF in which the copy, rename, and delete file sections appear.

## Examples

This example sets the default target directory for all copy-file, delete-file, and rename-file operations. Such a simple **DestinationDirs** section is common to INF files for new peripheral devices, because such an INF usually just copies a set of source files into a single directory on the target computer.

```inf
[DestinationDirs]
DefaultDestDir = 13
```

This example shows a fragment of the **DestinationDirs** section of the INF for a display/video driver.

```inf
[DestinationDirs]
DefaultDestDir     = 13

; ... 

; list of per-Manufacturer, per-Models, per-DDInstall-section, and
; CopyFiles-referenced xxx.Miniport/xxx.Display sections omitted here
; along with several other miniport/display paired drivers
; ...
vga.Miniport     = 13
vga.Display      = 13
xga.Miniport     = 13
xga.Display      = 13
```

## See also

[**CopyFiles**](inf-copyfiles-directive.md)

[**_DDInstall_**](inf-ddinstall-section.md)

[**DelFiles**](inf-delfiles-directive.md)

[**RenFiles**](inf-renfiles-directive.md)

[**SourceDisksFiles**](inf-sourcedisksfiles-section.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**Using Dirids**](./using-dirids.md)
