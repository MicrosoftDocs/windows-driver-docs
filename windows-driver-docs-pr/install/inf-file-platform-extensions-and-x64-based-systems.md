---
title: INF File Platform Extensions and x64-Based Systems
description: INF File Platform Extensions and x64-Based Systems
ms.assetid: 062c58f7-3519-4835-9597-ab6be5ff5fe8
keywords:
- x64 INF file platform extensions WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF File Platform Extensions and x64-Based Systems


### <a href="" id="platform-extensions-and-x64-based-systems--windows-xp-and-later-"></a> Platform Extensions and x64-Based Systems (Windows XP and later)

On Windows Server 2003 Service Pack 1 (SP1) and later, an **.ntamd64** platform extension is required on an [**INF Models section**](inf-models-section.md). An **.ntamd64** or **.nt** platform extension is optional on all other sections that support platform extensions.

For sections that support optional platform extensions, Windows selects which section to process, as follows:

1. Windows checks for a <em>section-name</em>**.ntamd64** section and, if one exists, processes it. Windows checks for the **.ntamd64** extension in the INF file that is being processed and in any included INF files (that is, any INF files that are included with **Include** entries).

2. If a <em>section-name</em>**.ntamd64** section does not exist, Windows checks for a <em>section-name</em>**.nt** section in the INF file or any included INF files. If one exists, Windows processes the <em>section-name</em>**.nt** section.

3. If a <em>section-name</em>**.nt** section does not exist, Windows processes a *section-name* section that does not include a platform extension.

### <a href="" id="testing-installation-on-x64-based-systems--windows-server-2003-sp1-and"></a> Testing Installation on x64-Based Systems (Windows Server 2003 SP1 and Later)

For testing purposes only, the requirement that an [**INF Models section**](inf-models-section.md) name include an **.ntamd64** extension can be suppressed. To suppress this requirement, create the following registry value entry under the subkey **HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Setup** and set this value entry to one:

```cpp
DisableDecoratedModelsRequirement:REG_DWORD
```

After setting the **DisableDecoratedModelsRequirement** value entry to one, restart the system and then install the device.

To restore the platform extension requirement, delete the **DisableDecoratedModelsRequirement** value entry or set it to zero, and then restart the system.

### <a href="" id="creating-inf-files-for-x64-based-systems--windows-xp-and-later-"></a> Creating INF Files for x64-Based Systems (Windows XP and later)

In general, you cannot use a single INF file that differentiates between device installations that are based on the operating system version. For example, if the files or registry settings that support a device differ between versions of x64-based operating systems, you must create an operating system-specific INF file for each version.

However, if a device does not require an operating system-specific installation, you can create a single cross-operating system INF file for x64-based systems that run Windows XP and later.

Because Windows Server 2003 SP1 and later require an **.ntamd64** platform extension on an [**INF Models section**](inf-models-section.md) name, but do not require this extension on other section names, the simplest approach to create and to maintain a cross-operating system INF file for x64-based systems is to include the **.ntamd64** extension only on the names of *Models* sections.

To create such a cross-operating system INF file, do the following:

1. Create a valid INF file that contains the generic entries that are required in all INF files, as described in [General Guidelines for INF Files](general-guidelines-for-inf-files.md).

2. Include an INF **Manufacturer** section that includes a *manufacturer-identifier* that specifies the [**INF Models section**](inf-models-section.md) name for the device and that specifies the **.ntamd64** platform extension. For example, the following **Manufacturer** section specifies an INF *Models* section name of "AbcModelSection" for an Abc device and the **.ntamd64** platform extension.

   ```cpp
   [Manufacturer]
   ; The manufacturer-identifier for the Abc device.
   %ManufacturerName%=AbcModelSection,ntamd64
   ```

3. Include a <em>Models</em>**.ntamd64** section whose name matches the *Models* section name that is specified by the *manufacturer-identifier* in the **Manufacturer** section. For example, the following AbcModelSection<strong>.ntamd64</strong> section for an Abc device includes a *device-description* that specifies an *install-section-name* of "AbcInstallSection."

   ```cpp
   [AbcModelSection.ntamd64]
   %AbcDeviceName%=AbcInstallSection,Abc-hw-id
   ```

4. Include a *DDInstall* section whose name matches the *install-section-name* that is specified by the *Models* section. For example, the *device-description* in an AbcModelSection section specifies the following AbcInstallSection section for an Abc device.

   ```cpp
   [AbcInstallSection]
   ; Install section entries go here.
   ...
   ```

5. Include other device-specific sections that are required to install the device, but do not include an **.ntamd64** platform extension on names of these sections. For more information about INF file sections and directives, see [Summary of INF Sections](summary-of-inf-sections.md) and [Summary of INF Directives](summary-of-inf-directives.md).

For information about how to create a single cross-operating system INF for all platform types, see [Cross-Platform INF Files](cross-platform-inf-files.md).

 

 





