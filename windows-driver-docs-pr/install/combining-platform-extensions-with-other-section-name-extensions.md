---
title: Combining Platform Extensions with Other Section Name Extensions
description: Combining Platform Extensions with Other Section Name Extensions
ms.assetid: ca82ba0f-0d65-47ca-826a-4f78435b1442
keywords: ["INF files WDK device installations , platform extensions", "platform extensions WDK INF files", "extensions WDK INF platform", "combining platform extensions WDK INF files", "install-section-name WDK INF files", "decorated INF WDK", "operating systems WDK"]
---

# Combining Platform Extensions with Other Section Name Extensions


An INF file that contains INF *DDInstall* sections with platform extensions can also contain additional per-device sections, such as the required *DDInstall***.Services** and optional *DDInstall***.HW**, *DDInstall***.CoInstallers**, *DDInstall***.LogConfigOverride**, and *DDInstall***.Interfaces** sections. In cross-operating system and cross-platform INF files, you should specify the appropriate platform extension immediately after the INF-writer-defined section name (for example, *install-section-name***.ntx86.HW**).

If a cross-operating system INF file contains decorated *install-section-name***.nt**, *install-section-name***.ntx86**, *install-section-name***.ntia64**, or *install-section-name***.ntamd64** sections, it must also have additional parallel decorated and undecorated per-device sections. That is, if the INF file has both *install-section-name* and *install-section-name***.nt** sections and it has a *DDInstall*.**HW** section, it must also have a parallel *install-section-name***.nt.HW** section (if the device or driver requires a **.HW** section for Windows 2000 and later versions of Windows).

The topics in the [INF File Sections and Directives](inf-file-sections-and-directives.md) section show the **nt***xxx***.HW** extensions as part of the formal syntax statements in the appropriate section references, such as in the following example:

**\[***install-section-name***.HW\]** |
**\[***install-section-name***.nt.HW\]** |
**\[***install-section-name***.ntx86.HW\]** |
**\[***install-section-name***.ntia64.HW\]** |
**\[***install-section-name***.ntamd64.HW\]**
Such a formal syntax statement indicates that these extensions are valid alternatives to the basic section. This type of statement does *not* indicate that any INF file that has an *install-section-name***.nt.HW** section must also include every other platform-specific *install-section-name***.nt***xxx***.HW** section. You can use any subset of these extensions to specify the decorated sections that are required for a particular cross-platform installation.

INF files that contain *install-section-name* platform extensions can also include platform extensions with their [**INF SourceDisksNames section**](inf-sourcedisksnames-section.md) and [**INF SourceDisksFiles section**](inf-sourcedisksfiles-section.md) entries, to specify installation file locations in a platform-specific manner.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Combining%20Platform%20Extensions%20with%20Other%20Section%20Name%20Extensions%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




