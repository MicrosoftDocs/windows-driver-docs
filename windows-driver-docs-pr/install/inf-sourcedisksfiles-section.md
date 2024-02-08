---
title: INF SourceDisksFiles Section
description: The SourceDisksFiles section names source files, installation disks, and directory paths used during installation.
keywords:
- INF SourceDisksFiles Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF SourceDisksFiles Section
api_type:
- NA
ms.date: 06/06/2022
---

# INF SourceDisksFiles section

The **SourceDisksFiles** section names the source files that are used during installation, identifies the installation disks that contain those files, and provides the directory paths, if any, on the distribution disks that contain individual files.

In order for a driver file or an application file to be included as part of a signed [driver package](driver-packages.md), the file must have a corresponding INF **SourceDisksFiles** section entry and a corresponding [**INF CopyFiles directive**](inf-copyfiles-directive.md).

```inf
[SourceDisksFiles] | 
[SourceDisksFiles.x86] | 
[SourceDisksFiles.ia64] | (Windows XP and later versions of Windows)
[SourceDisksFiles.amd64] | (Windows XP and later versions of Windows)
[SourceDisksFiles.arm] | (Windows 8 and later versions of Windows)
[SourceDisksFiles.arm64] (Windows 10 version 1709 and later versions of Windows)

filename=diskid[,[ subdir][,size]]
...  
```

## Entries

_filename_  
Specifies the name of the file on the source disk.

_diskid_  
Specifies the integer identifying the source disk that contains the file. This value, along with the initial _subdir_ (subdirectory) path (if any) that contains the named file, must be defined in a [**SourceDisksNames**](inf-sourcedisksnames-section.md) section of the same INF.

_subdir_  
This optional value specifies the subdirectory (relative to the _path_ value of the **SourceDisksNames** section, if any) on the source disk where the named file resides.

If this value is omitted from an entry, the named source file is assumed to be in the _path_ directory that was specified in the **SourceDisksFiles** section for the given disk or, if no _path_ directory was specified, in the _installation root_.

_size_  
This optional value specifies the uncompressed size, in bytes, of the given file.

## Remarks

A **SourceDisksFiles** section can have any number of entries, one for each file on the distribution disks. Any INF with a **SourceDisksFiles** section must also have an [**INF SourceDisksNames section**](inf-sourcedisksnames-section.md). By convention, **SourceDisksNames** and **SourceDisksFiles** sections follow the [**INF Version section**](inf-version-section.md). (These sections are omitted from a system-supplied INF, which instead specifies a **LayoutFile** entry in its **Version** section.)

Each _filename_ entry must specify the exact name of a file on the source disk. You cannot use a %_strkey_% token to specify the file name. For more information about %_strkey_% tokens, see [**INF Strings Section**](inf-strings-section.md).

To support distribution of driver files on multiple system architectures, you can specify an architecture-specific **SourceDisksFiles** section by adding an **.x86**, **.ia64**, **.amd64**, **.arm**, or **.arm64** extension to **SourceDisksFiles**. Be aware that, unlike other sections such as a **_DDInstall_** section, the platform extensions for a **SourceDisksFiles** section are not **.ntx86**, **.ntia64**, **.ntamd64**, etc.

For example, to specify a source disk names section for an x86-based system, use a **SourceDisksFiles.x86** section, not a **SourceDisksFiles.ntx86** section. Similarly, use a **SourceDisksFiles.ia64** section to specify an Itanium-based system and a **SourceDisksFiles.amd64** section to specify an x64-based system.

During installation, device installation functions look for architecture-specific **SourceDisksFiles** sections before using the generic section. For example, if, during installation on an x86-based platform, Windows is copying a file that is named _driver.sys_, it will look for the file's description in [**SourceDisksFiles.x86**] before looking in [**SourceDisksFiles**].

> [!IMPORTANT]
> Do not use a **SourceDisksFiles** section to copy INF files. For more information about how to copy INF files, see [Copying INFs](copying-inf-files.md).

## Examples

The following example shows a [**SourceDisksNames**](inf-sourcedisksnames-section.md) section and a corresponding SourceDisksFiles section.  Note that this example has only a **SourceDisksFiles.x86** section, specifying the files for the x86 architecture.  An INF that supports another architecture will need a corresponding **SourceDisksFiles** section for that architecture, or the use of an undecorated [**SourceDisksFiles**] section, which supports all architectures.

```inf
[SourceDisksNames]
;
; diskid = description[, [tagfile] [, <unused>, subdir]]
;
1 = %Floppy_Description%,,,\WinNT

[SourceDisksFiles.x86]
aha154x.sys = 1,\x86 ; on distribution disk 1, in subdir \WinNT\x86
```

## See also

[**CopyFiles**](inf-copyfiles-directive.md)

[**DestinationDirs**](inf-destinationdirs-section.md)

[**RenFiles**](inf-renfiles-directive.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**Strings**](inf-strings-section.md)

[**Version**](inf-version-section.md)
