---
title: PackageInfo XML Document
description: PackageInfo XML Document
ms.assetid: 1fa9b8a5-d6ab-4952-8e2d-7cb7ccc88804
---

# PackageInfo XML Document


The PackageInfo XML document contains data that specifies the contents of the device metadata package. The operating system uses this data to install the package and reference its contents.

Components of the device metadata system, such as the [Windows Metadata and Internet Services](windows-metadata-and-internet-services.md) (WMIS) and [Device Metadata Retrieval Client](device-metadata-retrieval-client.md) (DMRC) use the PackageInfo XML document to provide the Devices and Printers user interface with the current and most appropriate information for a device, such as the following:

-   The hardware or model ID of the device. This information is specified by the [**HardwareID**](https://msdn.microsoft.com/library/windows/hardware/ff546114) and [**ModelID**](https://msdn.microsoft.com/library/windows/hardware/ff549295) XML elements within the PackageInfo XML document.

-   A localized version of the device metadata package that matches the locale of the computer. This information is specified by the [**Locale**](https://msdn.microsoft.com/library/windows/hardware/ff548647) XML element within the PackageInfo XML document.

-   The last modified data of the device metadata package that matches the locale of the computer. This information is specified by the [**LastModifiedDate**](https://msdn.microsoft.com/library/windows/hardware/ff548624) XML element within the PackageInfo XML document.

Each device metadata package must contain only one PackageInfo XML document. The name of the document must be *PackageInfo.xml*.

The data in the PackageInfo XML document is formatted based on the [PackageInfo XML schema](https://msdn.microsoft.com/library/windows/hardware/ff549614).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20PackageInfo%20XML%20Document%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




