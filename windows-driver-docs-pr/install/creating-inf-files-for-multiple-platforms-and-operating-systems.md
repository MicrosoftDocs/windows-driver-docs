---
title: Creating INF Files for Multiple Platforms and Operating Systems
description: Creating INF Files for Multiple Platforms and Operating Systems
keywords:
- INF files WDK device installations , multiple platforms and operating systems
- multiple operating systems WDK , INF files
- cross-platform INF files WDK
- operating systems WDK , cross-operating system INF files
ms.date: 02/02/2022
---

# Creating INF Files for Multiple Platforms and Operating Systems

By using system-defined platform extensions to [INF file sections and directives](./index.md), you can create a single INF file for cross-platform installations. The extensions enable you to create *decorated* section names, which specify which sections and directives are relevant to each target platform and operating system. For example, you can create an INF file that installs a device only on x64-based systems, only on Itanium-based systems, only on x86-based systems, or on all systems that are supported by Windows 2000 and later versions of Windows.

The following table summarizes the system-supported platform extensions that can be added to the names of sections that support extensions.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Platform extension</th>
<th align="left">Use</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>.ntamd64</strong></p></td>
<td align="left"><p>The section contains instructions for installing a device or set of device-compatible models on x64-based systems that are supported by Windows XP and later.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>.ntia64</strong></p></td>
<td align="left"><p>The section contains instructions for installing a device or set of device-compatible models on Itanium-based systems that are supported by Windows XP and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>.ntx86</strong></p></td>
<td align="left"><p>The section contains instructions for installing a device or set of device-compatible models on x86-based systems that are supported by Windows XP and later.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>.ntarm</strong></p></td>
<td align="left"><p>The section contains instructions for installing a device or set of device-compatible models on ARM-based systems that are supported by Windows 8 and later.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>.ntarm64</strong></p></td>
<td align="left"><p>The section contains instructions for installing a device or set of device-compatible models on ARM64-based systems that are supported by Windows 10 version 1709 and later.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>.nt</strong></p></td>
<td align="left"><p>In versions of Windows earlier than Windows Server 2003 SP1, the section contains instructions for installing a device or set of device-compatible models on all systems that are supported by the operating system.</p>
<p>Starting with Windows Server 2003 SP1, the section contains instructions for installing a device or set of device-compatible models on x86-based systems that are supported by the operating system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>(no platform extension)</p></td>
<td align="left"><p>In versions of Windows earlier than Windows Server 2003 SP1, the section contains instructions for installing a device or set of device-compatible models on all systems that are supported by the operating system.</p>
<p>Starting with Windows Server 2003 SP1, the section contains instructions for installing a device or set of device-compatible models on x86-based systems that are supported by the operating system.</p></td>
</tr>
</tbody>
</table>

On Windows Server 2003 Service Pack 1 (SP1) and later, INF files must *decorate* entries in the [**INF Models section**](inf-models-section.md) with **.ntia64**, **.ntarm**, **.ntarm64** or **.ntamd64** platform extensions to specify non-x86 target operating system versions. These platform extensions are not required in INF files for x86-based target operating system versions, but are strongly recommended. The same platform extension decoration or **.nt** platform extension is optional on all other sections that support platform extensions.

> [!NOTE] We highly recommend that you always decorate entries in the [**INF Models section**](inf-models-section.md) with platform extensions for target operating systems of Windows XP and later versions of Windows. For x86-based hardware platforms, you should avoid the use of the **.nt** platform extension and use **.ntx86** instead.

For sections that support optional platform extensions, Windows selects which section to process, as follows:

1. Windows checks for a <em>section-name</em>**.nt<em>\<architecture></em>** section and, if one exists, processes it. Windows checks for the **.nt<em>\<architecture></em>** extension in the INF file that is being processed and in any included INF files (that is, any INF files that are included with **Include** entries).

2. If a <em>section-name</em>**.nt<em>\<architecture></em>** section does not exist, Windows checks for a <em>section-name</em>**.nt** section in the INF file or any included INF files. If one exists, Windows processes the <em>section-name</em>**.nt** section.

3. If a <em>section-name</em>**.nt** section does not exist, Windows processes a *section-name* section that does not include a platform extension.

For sections where **.nt** and **.nt<em>\<architecture></em>** platform extensions are optional, the simplest approach to create and to maintain a cross-platform system INF file is not to use platform extensions on those section names and include the **.nt<em>\<architecture></em>** extension only on the names of [**INF Models section**](inf-models-section.md) sections. However, this assumes that the INF file does not need to copy architecture specific versions of files and that install settings are the same across architectures. For more advanced scenarios for cross-platform INFs, see [Combining Platform Extensions with Other Section Name Extensions](combining-platform-extensions-with-other-section-name-extensions.md).

To create such a simple cross-platform INF file, do the following:

1. Create a valid INF file that contains the generic entries that are required in all INF files, as described in [General Guidelines for INF Files](general-guidelines-for-inf-files.md).

2. Include an INF **Manufacturer** section that includes a *manufacturer-identifier* that specifies the [**INF Models section**](inf-models-section.md) name for the device and that specifies the **.nt<em>\<architecture></em>** platform extension. For example, the following **Manufacturer** section specifies an INF *Models* section name of "AbcModelSection" for an Abc device and the **.nt<em>\<architecture></em>** platform extension.

   ```inf
   [Manufacturer]
   ; The manufacturer-identifier for the Abc device.
   %ManufacturerName%=AbcModelSection,nt<architecture>
   ```

3. Include a <em>Models</em>**.nt<em>\<architecture></em>** section whose name matches the *Models* section name that is specified by the *manufacturer-identifier* in the **Manufacturer** section. For example, the following AbcModelSection<strong>.nt<em>\<architecture></em></strong> section for an Abc device includes a *device-description* that specifies an *install-section-name* of "AbcInstallSection."

   ```inf
   [AbcModelSection.nt<architecture>]
   %AbcDeviceName%=AbcInstallSection,Abc-hw-id
   ```

4. Include a *DDInstall* section whose name matches the *install-section-name* that is specified by the *Models* section. For example, the *device-description* in an AbcModelSection section specifies the following AbcInstallSection section for an Abc device.

   ```inf
   [AbcInstallSection]
   ; Install section entries go here.
   ...
   ```

5. Include other device-specific sections that are required to install the device, but do not include an **.nt<em>\<architecture></em>** platform extension on names of these sections. For more information about INF file sections and directives, see [Summary of INF Sections](summary-of-inf-sections.md) and [Summary of INF Directives](summary-of-inf-directives.md).

## See also

-   [Cross-Platform INF Files](cross-platform-inf-files.md)
-   [Combining Platform Extensions with Other Section Name Extensions](combining-platform-extensions-with-other-section-name-extensions.md)
-   [Combining Platform Extensions with Operating System Versions](combining-platform-extensions-with-operating-system-versions.md)
