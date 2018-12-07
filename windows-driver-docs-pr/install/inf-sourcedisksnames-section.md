---
title: INF SourceDisksNames Section
description: A SourceDisksNames section identifies the distribution disks or CD-ROM discs that contain the source files to be transferred to the target computer during installation.
ms.assetid: ad69521c-5185-4c7b-a851-eb825b468459
keywords:
- INF SourceDisksNames Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF SourceDisksNames Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF SourceDisksNames Section


A **SourceDisksNames** section identifies the distribution disks or CD-ROM discs that contain the source files to be transferred to the target computer during installation.

```cpp
[SourceDisksNames] |
[SourceDisksNames.x86] | 
[SourceDisksNames.arm] | (Windows 8 and later versions of Windows)
[SourceDisksNames.arm64] | (Windows 10 version 1709 and later versions of Windows)
[SourceDisksNames.ia64] | (Windows XP and later versions of Windows)
[SourceDisksNames.amd64] (Windows XP and later versions of Windows)

diskid = disk-description[,tag-or-cab-file] |
diskid = disk-description[,[tag-or-cab-file][,[unused][,path]]] |
diskid = disk-description[,[tag-or-cab-file],[unused],[path][,flags]] |
diskid = disk-description[,[tag-or-cab-file],[unused],[path],[flags][,tag-file]]  (Windows XP and later versions of Windows)
...
```

## Entries


<a href="" id="diskid"></a>*diskid*  
Specifies a nonnegative integer, in decimal format, that identifies a source disk. This value cannot require more than 4 bytes of storage. If there is more than one source disk for the distribution, each *diskid* entry in this section must have a unique value, such as **1**, **2**, **3**, and so forth.

<a href="" id="disk-description"></a>*disk-description*  
Specifies a %*strkey*% token or a **"**<em>quoted string</em>**"** that describes the contents and/or purpose of the disk identified by *diskid*. The installer can display the value of this string to the end-user during installation, for example, to identify a source disk to be inserted into a drive at a particular stage of the installation process.

Every %*strkey*% specification in this section must be defined in the INF's **Strings** section. Any *disk-description* that is not a %*strkey*% token is a user-visible string that must be delimited by double quotation marks characters (**"**) if it has any leading or trailing spaces.

<a href="" id="tag-or-cab-file"></a>*tag-or-cab-file*  
This optional value specifies the name of a [*tag file*](https://msdn.microsoft.com/library/windows/hardware/ff556341#wdkgloss-tag-file) or [*cabinet (.cab) file*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-cabinet-file) supplied on the distribution disk, either in the [*installation root*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-installation-root) or in the subdirectory specified by *path*, if any. The value should specify only the file name and extension, not any directory or subdirectory.

Windows uses a tag file to verify that the user inserted the correct installation disk. Tag files are required for removable media, and are optional for fixed media.

If Windows cannot find installation files by name on the installation medium, and if *tag-or-cab-file* has the extension **.**<em>cab</em>, Windows uses it as the name of a cabinet file that contains the installation files.

If a .*cab* extension is specified, Windows treats the file as both a tag file and a cabinet file, as explained in the following **Remarks** section.

For Windows XP and later versions of Windows, also see the *flags* and *tag-file* entry values.

<a href="" id="unused"></a>*unused*  
This entry is no longer supported for Windows 2000 and later versions of Windows.

<a href="" id="path"></a>*path*  
This optional value specifies the directory path on the distribution disk that contains source files. The *path* is relative to the [*installation root*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-installation-root) and is expressed as **\\**<em>dirname1</em>**\\**<em>dirname2</em>... and so forth. If this value is omitted from an entry, files are assumed to be in the installation root of the distribution disk.

You can use an [**INF SourceDisksFiles section**](inf-sourcedisksfiles-section.md) to specify subdirectories, relative to a given path directory, that contain source files. However, tag files and [*cabinet file*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-cabinet-file) must reside either in the given path directory or in the installation root.

<a href="" id="flags"></a>*flags*  
Starting with Windows XP, setting this to **0x10** forces Windows to use *tag-or-cab-file* as a cabinet file name, and to use *tag-file* as a tag file name. Otherwise, *flags* is for internal use only.

<a href="" id="tag-file"></a>*tag-file*  
Starting with Windows XP, if *flags* is set to **0x10**, this optional value specifies the name of a [*tag file*](https://msdn.microsoft.com/library/windows/hardware/ff556341#wdkgloss-tag-file) supplied on the distribution medium, either in the [*installation root*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-installation-root) or in the subdirectory specified by *path*. The value should specify the file name and extension without path information. For more information, see the Remarks section.

Remarks
-------

A **SourceDisksNames** section can have any number of entries, one for each distribution disk. Any INF with a **SourceDisksNames** section must also have an [**INF SourceDisksFiles section**](inf-sourcedisksfiles-section.md). (By convention, **SourceDisksNames** and **SourceDisksFiles** sections follow the [**INF Version section**](inf-version-section.md).)

These sections never appear in system-supplied INF files. Instead, system-supplied INF files specify **LayoutFile** entries in their **Version** sections.

Entries in a **SourceDisksNames** section can have either of two formats, one of which is supported only in Windows XP and later versions of Windows.

In the first format, the *tag-or-cab-file* parameter can specify either a [*tag file*](https://msdn.microsoft.com/library/windows/hardware/ff556341#wdkgloss-tag-file) or a [*cabinet file*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-cabinet-file). When encountering this format, Windows uses the following algorithm:

1.  Treat the *tag-or-cab-file* value as a tag file name and look for the file on the installation medium. If the medium is removable and the tag file is not found, prompt the user for the correct medium. If the medium is fixed and neither the tag file nor the first file to be installed can be found, prompt the user for the correct medium.
2.  Attempt to copy installation files directly from the medium.
3.  Treat the *tag-or-cab-file* value as a .cab file and look for the file.
4.  Attempt to copy installation files from the *.cab* file.
5.  Prompt the user for files not found.

The second format is supported in Windows XP and later versions of Windows. With this format, you can use the *tag-or-cab-file*, *flags*, and *tag-file* entries to specify both a *.cab* file and a tag file. When encountering this format, Windows uses the following algorithm:

1.  If the installation medium is removable, look for a tag file that matches the file name that is specified by *tag-file*. If the file is not found, prompt the user for the correct medium. If the medium is fixed, look for either the tag file or the cabinet file. If neither file is found, prompt the user for the correct medium.
2.  Attempt to copy installation files from the *.cab* file specified by *tag-or-cab-file*.
3.  Prompt the user for files not found.

For either format, you must provide a different tag file, with a different file name, for each version of the driver files.

To support distribution of driver files on multiple system architectures, you can specify an architecture-specific **SourceDisksNames** section by adding an **.x86**, **.ia64**, or **.amd64** extension to **SourceDisksNames**.

Be aware that, unlike other sections such as a *DDInstall* section, the platform extensions for a **SourceDisksNames** section are not **.ntx86**, **.ntia64**, or **.ntamd64**. For example, to specify a source disk names section for an x86-based system, use a **SourceDisksNames.x86** section, not a **SourceDisksNames.ntx86** section. Similarly, use a **SourceDisksNames.ia64** section to specify an Itanium-based system and a **SourceDisksNames.amd64** section to specify an x64-based system.

During installation, SetupAPI functions look for architecture-specific **SourceDisksNames** sections before using the generic section. For example, if, during installation on an x86-based platform, an INF file references disk "2", the [SetupAPI](setupapi.md) functions will look for an entry for disk "2" in **SourceDisksNames.x86** before looking in **SourceDisksNames**.

SetupAPI functions use the **SourceDisksNames** and **SourceDisksNames.**<em>architecture</em> sections that are in the same INF file as the relevant [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) section.

Examples
--------

In the following example, the *write.exe* file is the same for all Windows platforms and is located in the *\\common* subdirectory, under the installation root, on a CD-ROM distribution disc. The *cmd.exe* file is a platform-specific file that is only used on x86-based platforms.

```cpp
[SourceDisksNames]
1 = "Windows NT CD-ROM",file.tag,,\common

[SourceDisksNames.x86]
2 = "Windows NT CD-ROM",file.tag,,\x86

[SourceDisksFiles]
write.exe = 1
cmd.exe = 2
```

The following example uses entries that contain separate specifications for *.tag* files and *.cab* files.

```cpp
[Version]
signature = "$Windows NT$"
Provider = %Msft%

[SourceDisksNames]
1 = "Dajava","Dajava.cab",,,0x10,"Dajava.tag"
2 = "Osc","Osc.cab",,,0x10,"OSC.tag"
3 = "Win","Win.cab",,,0x10,"Win.tag"
4 = "XMLDSO","XMLDSO.cab",,,0x10,"XMLDSO.tag"

[SourceDisksFiles]
ArrayBvr.class=1
BvrCallback.class=1
BvrsToRun.class=1
choice.osc=2
custom.osc=2
login.osc=2
mwcload.exe=3
mwcloadw.exe=3
mwclw32.dll=3
Atom.class=4
DTD.class=4
Entity.class=4
Entry.class=4

[DestinationDirs]
Test = 16430,InfTest    ; %SystemRoot%\System32

[DefaultInstall]
CopyFiles = Test

[Test]
ArrayBvr.class
mwcloadw.exe
Entity.class
custom.osc
BvrCallback.class
BvrsToRun.class
choice.osc
login.osc
mwcload.exe
mwclw32.dll
Atom.class
DTD.class
Entry.class

[Strings]
Msft = "Microsoft"
```

## See also


[**DestinationDirs**](inf-destinationdirs-section.md)

[**SourceDisksFiles**](inf-sourcedisksfiles-section.md)

[**Version**](inf-version-section.md)

 

 






