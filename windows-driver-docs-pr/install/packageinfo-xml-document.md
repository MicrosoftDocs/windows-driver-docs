---
title: PackageInfo XML Document
description: PackageInfo XML Document
ms.assetid: 1fa9b8a5-d6ab-4952-8e2d-7cb7ccc88804
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PackageInfo XML Document


The PackageInfo XML document contains data that specifies the contents of the device metadata package. The operating system uses this data to install the package and reference its contents.

Components of the device metadata system, such as the [Windows Metadata and Internet Services](windows-metadata-and-internet-services.md) (WMIS) and [Device Metadata Retrieval Client](device-metadata-retrieval-client.md) (DMRC) use the PackageInfo XML document to provide the Devices and Printers user interface with the current and most appropriate information for a device, such as the following:

-   The hardware or model ID of the device. This information is specified by the [**HardwareID**](https://msdn.microsoft.com/library/windows/hardware/ff546114) and [**ModelID**](https://msdn.microsoft.com/library/windows/hardware/ff549295) XML elements within the PackageInfo XML document.

-   A localized version of the device metadata package that matches the locale of the computer. This information is specified by the [**Locale**](https://msdn.microsoft.com/library/windows/hardware/ff548647) XML element within the PackageInfo XML document.

-   The last modified data of the device metadata package that matches the locale of the computer. This information is specified by the [**LastModifiedDate**](https://msdn.microsoft.com/library/windows/hardware/ff548624) XML element within the PackageInfo XML document.

Each device metadata package must contain only one PackageInfo XML document. The name of the document must be *PackageInfo.xml*.

The data in the PackageInfo XML document is formatted based on the [PackageInfo XML schema](https://msdn.microsoft.com/library/windows/hardware/ff549614).

 

 





