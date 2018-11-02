---
title: INF File Platform Extensions and x86-Based Systems
description: INF File Platform Extensions and x86-Based Systems
ms.assetid: d0e1c6ba-32c4-413d-b0d9-620e3617a62b
keywords:
- x86 INF file platform extensions WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF File Platform Extensions and x86-Based Systems


The following table summarizes Windows support for platform extensions for x86-based systems that run Windows 2000 and later versions of Windows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Platform extension</th>
<th align="left">Platform extension support (Windows 2000 and later)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>.ntamd64</strong></p></td>
<td align="left"><p>Not supported.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>.ntia64</strong></p></td>
<td align="left"><p>Not supported.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>.ntarm</strong></p></td>
<td align="left"><p>Not supported.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>.ntarm64</strong></p></td>
<td align="left"><p>Not supported.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>.ntx86</strong></p></td>
<td align="left"><p>Optional on sections that support extensions.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>.nt</strong></p></td>
<td align="left"><p>Optional on sections that support extensions.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>(No platform extension)</p></td>
<td align="left"><p>Supported by default on all sections.</p></td>
</tr>
</tbody>
</table>

 

For more information about how to use platform extensions with x86-based systems, see the following sections:

[Platform Extensions and x86-Based Systems (Windows 2000 and Later)](#platform-extensions-and-x86-based-systems--windows-2000-and-later-)

[Creating INF Files for x86-Based Systems (Windows 2000 and Later)](#creating-inf-files-for-x86-based-systems--windows-2000-and-later-)

### <a href="" id="platform-extensions-and-x86-based-systems--windows-2000-and-later-"></a> Platform Extensions and x86-Based Systems

Windows XP and later versions of Windows support an optional **.nt** or **.ntx86** platform extension on a *Models* section name and the names of other sections that support platform extensions.

Windows 2000 does not support platform extensions on an [**INF *Models* section**](inf-models-section.md) name, but does support an optional **.nt** or **.ntx86** platform extension on the names of other sections that support platform extensions.

For sections that support optional platform extensions, Windows selects which section to process, as follows:

1. Windows checks for a <em>section-name</em>**.ntx86** section and, if one exists, processes it. Windows checks for the **.ntx86** extension in the INF file that is being processed and in any included INF files (that is, any INF files that are included with **Include** entries).

2. If a <em>section-name</em>**.ntx86** section does not exist, Windows checks for a <em>section-name</em>**.nt** section in the INF file or any included INF files. If one exists, Windows processes the <em>section-name</em>**.nt** section.

3. If a <em>section-name</em>**.nt** section does not exist, Windows processes a *section-name* section that does not include a platform extension.

### <a href="" id="creating-inf-files-for-x86-based-systems--windows-2000-and-later-"></a> Creating INF Files for x86-Based Systems

In general, you cannot use a single INF file that differentiates between device installations that are based on the operating system version. For example, if the files or registry settings that support a device differ between versions of x86-based operating systems, you must create an operating system-specific INF file for each version.

However, if a device does not require operating system-specific installation, you can create a single cross-operating system INF file for x86-based systems that run Windows 2000 and later versions of Windows.

Because **.nt** and **.ntx86** platform extensions are optional, the simplest approach to create and to maintain a cross-operating system INF file for x86-based systems is not to use platform extensions on section names.

To create a single cross-operating system INF file for x86-based systems that run Windows 2000 and later versions of Windows, do the following:

1.  Create a valid INF file that contains the generic entries that are required in all INF files, as described in [General Guidelines for INF Files](general-guidelines-for-inf-files.md).

2.  Include an INF **Manufacturer** section that includes a *manufacturer-identifier* that specifies the *Models* section name for the device, but does not specify an optional **.nt** or **.ntx86** platform extension. For example, the following **Manufacturer** section specifies a *Models* section name of "AbcModelSection" for an Abc device.

    ```cpp
    [Manufacturer]
    ; The manufacturer-identifier for the Abc device.
    %ManufacturerName%=AbcModelSection
    ```

3.  Include a *Models* section whose name matches the *Models* section name that is specified by the *manufacturer-identifier* in the **Manufacturer** section. For example, the following AbcModelSection section for an Abc device includes a *device-description* that specifies an *install-section-name* of "AbcInstallSection."

    ```cpp
    [AbcModelSection]
    %AbcDeviceName%=AbcInstallSection,Abc-hw-id
    ```

4.  Include a *DDInstall* section whose name matches the *install-section-name* that is specified by the *Models* section. For example, the *device-description* in the AbcModelSection section specifies the following AbcInstallSection section for an Abc device. Windows processes this section to install the Abc device on x86-based systems that run Windows 2000 and later versions of Windows.

    ```cpp
    [AbcInstallSection]
    ; Install section entries go here.
    ...
    ```

5.  Include other device-specific sections that are required to install the device, but do not include an **.nt** or **.ntx86** platform extension on the names of these sections. Windows processes these sections to install the Abc device on x86-based systems that run Windows 2000 and later versions of Windows.

For more information about INF file sections and directives, see [Summary of INF Sections](summary-of-inf-sections.md) and [Summary of INF Directives](summary-of-inf-directives.md).

For information about how to create a single cross-platform INF file for all platform types, see [Cross-Platform INF Files](cross-platform-inf-files.md).

 

 





