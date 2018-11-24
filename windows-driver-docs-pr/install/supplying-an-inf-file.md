---
title: Supplying an INF File
description: Supplying an INF File
ms.assetid: 208726d9-6f62-46a4-84a1-6fab3895bbe3
keywords:
- driver packages WDK , INF files
- packages WDK , INF files
- INF files WDK , about INF files
- information files WDK
- .inf files
- device installations WDK , INF files
- installing devices WDK , INF files
- device installations WDK , INF files
- INF files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supplying an INF File





Every driver package must include an INF file, which the [device installation components](https://msdn.microsoft.com/library/windows/hardware/ff541277) read when installing the device. An INF file is not an installation script. It is an ASCII or Unicode text file that provides device and driver information, including the driver files, registry entries, device IDs, [catalog files](catalog-files.md), and version information that is required to install the device or driver. The INF is used not only when the device or driver is first installed, but also when the user requests a driver update through Device Manager.

The exact contents and format of the INF file depend on the [device setup classes](device-setup-classes.md). [Summary of INF Sections](summary-of-inf-sections.md) describes the information that is required in each type of INF. In general, per-manufacturer information is located in an [**INF *Models* section**](inf-models-section.md). Entries in the **Models** section refer to [**INF *DDInstall* sections**](inf-ddinstall-section.md) that contain model-specific details.

The [ChkINF](https://msdn.microsoft.com/library/windows/hardware/ff543461) tool, which is provided in the *\\tools* directory of the Microsoft Windows Driver Kit (WDK), checks the syntax and structure of all cross-class INF sections and directives, together with the class-specific extensions for all setup classes except for Printers.

Starting with Windows 2000, you can use a single INF file for installation on all versions of the Windows operating system. For more information, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md). If your device will be sold in the international market, you should [create an international INF file](creating-international-inf-files.md). Depending on the localities involved, an international INF file might have to be a Unicode file instead of ASCII.

A good way to create an INF file for your driver is to modify one of the samples that the WDK provides. Most of the WDK sample drivers include INF files in the same directory as the sample driver.

For more information about INF files, see [Creating an INF File](overview-of-inf-files.md), the documentation for [ChkINF](https://msdn.microsoft.com/library/windows/hardware/ff543461), the device-specific documentation in the WDK, and the INF files that are supplied with sample drivers for devices similar to yours.

 

 





