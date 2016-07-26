---
title: General Guidelines for INF Files
description: General Guidelines for INF Files
ms.assetid: a0394708-46ed-47f8-a629-0c7d3088df3b
keywords: ["INF files WDK device installations , general guidelines"]
---

# General Guidelines for INF Files


## <a href="" id="ddk-general-guidelines-for-inf-files-dg"></a>


INF files have many common parts and follow a single set of syntax rules. However, they are also as different as the variety of devices that are supported by Microsoft Windows. When you write an INF file, refer to the following sources of information:

-   This section and the [INF File Sections and Directives](inf-file-sections-and-directives.md) reference material.

-   The documentation for your class of device.

    For example, if your device is a printer, see [Installing and Configuring Printer Drivers](https://msdn.microsoft.com/library/windows/hardware/ff551648).

-   WDK tools for INF files.

    For more information, see [Tools for INF Files](https://msdn.microsoft.com/library/windows/hardware/ff552956). These tools are included in the \\Tools subdirectory of the WDK.

-   Sample INF files and INF files for similar devices.

    The WDK includes INF files for its sample drivers. Look through the sample drivers to see whether there are INF files for devices similar to your device.

You can create or modify an INF file by using any text editor in which you can control the insertion of line breaks. If your INF contains non-ASCII characters, save the file as a Unicode file.

INF files that ship with Windows 7 and earlier operating systems must have a file name of *xxxxxxxx***.inf**, where "*xxxxxxxx*" does not exceed eight characters. The name of an INF file that ships separately from the operating system is not limited to eight characters.

Beginning with Windows 8, INF file names are not limited to eight characters, regardless if they ship with the operating system or not.

Do not arbitrarily modify the time stamps of your INF files, as a version control mechanism. Version control of INF files should be based on a date and version number that is specified in an [**INF Version section**](inf-version-section.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20General%20Guidelines%20for%20INF%20Files%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




