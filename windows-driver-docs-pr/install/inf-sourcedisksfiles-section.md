---
title: INF SourceDisksFiles Section
description: The SourceDisksFiles section names source files, installation disks, and directory paths used during installation.
ms.assetid: 4a20b2e7-3371-47c1-8f51-bcc7af044382
keywords:
- INF SourceDisksFiles Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF SourceDisksFiles Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF SourceDisksFiles Section


The **SourceDisksFiles** section names the source files that are used during installation, identifies the installation disks that contain those files, and provides the directory paths, if any, on the distribution disks that contain individual files.

In order for a driver file or an application file to be included as part of a signed [driver package](driver-packages.md), the file must have a corresponding INF **SourceDisksFiles** section entry and a corresponding [**INF CopyFiles directive**](inf-copyfiles-directive.md).

```cpp
[SourceDisksFiles] | 
[SourceDisksFiles.x86] | 
[SourceDisksFiles.arm] | (Windows 8 and later versions of Windows)
[SourceDisksFiles.arm64] | (Windows 10 version 1709 and later versions of Windows)
[SourceDisksFiles.ia64] | (Windows XP and later versions of Windows)
[SourceDisksFiles.amd64] (Windows XP and later versions of Windows)

filename=diskid[,[ subdir][,size]]
...  
```

## Entries


<a href="" id="filename"></a>*filename*  
Specifies the name of the file on the source disk.

<a href="" id="diskid"></a>*diskid*  
Specifies the integer identifying the source disk that contains the file. This value, along with the initial *subdir*(ectory) path (if any) that contains the named file, must be defined in a [**SourceDisksNames**](inf-sourcedisksnames-section.md) section of the same INF.

<a href="" id="subdir"></a>*subdir*  
This optional value specifies the subdirectory (relative to the *path* value of the **SourceDisksNames** section, if any) on the source disk where the named file resides.

If this value is omitted from an entry, the named source file is assumed to be in the *path* directory that was specified in the **SourceDisksFiles** section for the given disk or, if no *path* directory was specified, in the [*installation root*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-installation-root).

<a href="" id="size"></a>*size*  
This optional value specifies the uncompressed size, in bytes, of the given file.

Remarks
-------

A **SourceDisksFiles** section can have any number of entries, one for each file on the distribution disks. Any INF with a **SourceDisksFiles** section must also have an [**INF SourceDisksNames section**](inf-sourcedisksnames-section.md). By convention, **SourceDisksNames** and **SourceDisksFiles** sections follow the [**INF Version section**](inf-version-section.md). (These sections are omitted from a system-supplied INF, which instead specifies a **LayoutFile** entry in its **Version** section.)

Each *filename* entry must specify the exact name of a file on the source disk. You cannot use a %*strkey*% token to specify the file name. For more information about %*strkey*% tokens, see [**INF Strings Section**](inf-strings-section.md).

To support distribution of driver files on multiple system architectures, you can specify an architecture-specific **SourceDisksFiles** section by adding an **.x86**, **.ia64**, or **.amd64** extension to **SourceDisksFiles**. Be aware that, unlike other sections such as a ***DDInstall*** section, the platform extensions for a **SourceDisksFiles** section are not **.ntx86**, **.ntia64**, or **.ntamd64**.

For example, to specify a source disk names section for an x86-based system, use a **SourceDisksFiles.x86** section, not a **SourceDisksFiles.ntx86** section. Similarly, use a **SourceDisksFiles.ia64** section to specify an Itanium-based system and a **SourceDisksFiles.amd64** section to specify an x64-based system.

During installation, SetupAPI functions look for architecture-specific **SourceDisksFiles** sections before using the generic section. For example, if, during installation on an x86-based platform, Windows is copying a file that is named *driver.sys*, it will look for the file's description in [**SourceDisksFiles.x86**] before looking in [**SourceDisksFiles**].

**Important**  Do not use a **SourceDisksFiles** section to copy INF files. For more information about how to copy INF files, see [Copying INFs](copying-inf-files.md).

 

Examples
--------

The following example shows a [**SourceDisksNames**](inf-sourcedisksnames-section.md) section and a corresponding SourceDisksFiles section.  Note that this example has only a **SourceDisksFiles.x86** section, specifying the files for the x86 architecture.  An INF that supports another architecture will need a corresponding **SourceDisksFiles** section for that architecture, or the use of an undecorated [**SourceDisksFiles**] section, which supports all architectures.

```cpp
[SourceDisksNames]
;
; diskid = description[, [tagfile] [, <unused>, subdir]]
;
1 = %Floppy_Description%,,,\WinNT

[SourceDisksFiles.x86]
aha154x.sys = 1,\x86 ; on distribution disk 1, in subdir \WinNT\x86

; ...
```

## See also


[**CopyFiles,**](inf-copyfiles-directive.md)

[**DestinationDirs**](inf-destinationdirs-section.md)

[**RenFiles**](inf-renfiles-directive.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**Strings**](inf-strings-section.md)

[**Version**](inf-version-section.md)

 

 






