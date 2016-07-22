---
title: Writing INF Files
description: Writing INF Files
ms.assetid: 0A31484C-3A61-4a6d-B500-E5C69E2130F9
keywords: ["INF files WDK device installations , writing", "writing INF files WDK device installations"]
---

# Writing INF Files


When you write an [INF file](inf-files.md) for your [driver package](driver-packages.md), you should follow these guidelines:

-   An INF file must use valid structure and syntax to pass driver package validation checks at the beginning of the installation process.

    Use the [ChkINF](https://msdn.microsoft.com/library/windows/hardware/ff543461) tool to validate the structure and syntax of INF files.

-   An INF file must contain valid INF [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) and [**SourceDisksNames**](inf-sourcedisksnames-section.md) sections. Starting with Windows Vista, the operating system does not copy the driver package into the [driver store](driver-store.md) unless these sections are present and filled in correctly.

-   It is sometimes necessary to copy INF files during device installation so that Windows can find them without repetitively displaying user prompts. For example, the base INF file for a multifunction device might copy the INF files for the device's individual functions so that Windows can find these INF files without prompting the user every time that it installs one of the device's functions.

    Starting with Windows XP, if you want to stage other INF files during an installation that is driven by an INF file, use the [**INF CopyINF directive**](inf-copyinf-directive.md).

    **Note**  Do not use the [**INF CopyFiles directive**](inf-copyfiles-directive.md) to copy INF files.

     

-   The components of a driver package must never directly copy or delete INF files directly into a system's *%SystemRoot%/Inf* directory. This results in the driver's digital signature to be invalidated, and this causes the driver not to load successfully.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Writing%20INF%20Files%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




