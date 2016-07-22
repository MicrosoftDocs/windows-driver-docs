---
title: Supplying an INF File
description: Supplying an INF File
ms.assetid: 208726d9-6f62-46a4-84a1-6fab3895bbe3
keywords: ["driver packages WDK , INF files", "packages WDK , INF files", "INF files WDK , about INF files", "information files WDK", ".inf files", "device installations WDK , INF files", "installing devices WDK , INF files", "device installations WDK , INF files", "INF files"]
---

# Supplying an INF File


## <a href="" id="ddk-supplying-an-inf-file-pg"></a>


Every driver package must include an INF file, which the [device installation components](https://msdn.microsoft.com/library/windows/hardware/ff541277) read when installing the device. An INF file is not an installation script. It is an ASCII or Unicode text file that provides device and driver information, including the driver files, registry entries, device IDs, [catalog files](catalog-files.md), and version information that is required to install the device or driver. The INF is used not only when the device or driver is first installed, but also when the user requests a driver update through Device Manager.

The exact contents and format of the INF file depend on the [device setup classes](device-setup-classes.md). [Summary of INF Sections](summary-of-inf-sections.md) describes the information that is required in each type of INF. In general, per-manufacturer information is located in an [**INF *Models* section**](inf-models-section.md). Entries in the **Models** section refer to [**INF *DDInstall* sections**](inf-ddinstall-section.md) that contain model-specific details.

The [ChkINF](https://msdn.microsoft.com/library/windows/hardware/ff543461) tool, which is provided in the *\\tools* directory of the Microsoft Windows Driver Kit (WDK), checks the syntax and structure of all cross-class INF sections and directives, together with the class-specific extensions for all setup classes except for Printers.

Starting with Windows 2000, you can use a single INF file for installation on all versions of the Windows operating system. For more information, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md). If your device will be sold in the international market, you should [create an international INF file](creating-international-inf-files.md). Depending on the localities involved, an international INF file might have to be a Unicode file instead of ASCII.

A good way to create an INF file for your driver is to modify one of the samples that the WDK provides. Most of the WDK sample drivers include INF files in the same directory as the sample driver.

For more information about INF files, see [Creating an INF File](overview-of-inf-files.md), the documentation for [ChkINF](https://msdn.microsoft.com/library/windows/hardware/ff543461), the device-specific documentation in the WDK, and the INF files that are supplied with sample drivers for devices similar to yours.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Supplying%20an%20INF%20File%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




