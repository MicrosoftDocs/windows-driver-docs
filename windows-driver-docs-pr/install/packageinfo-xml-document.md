---
title: PackageInfo XML Document
description: PackageInfo XML Document
ms.date: 04/20/2017
---

# PackageInfo XML Document


The PackageInfo XML document contains data that specifies the contents of the device metadata package. The operating system uses this data to install the package and reference its contents.

Components of the device metadata system, such as the [Windows Metadata and Internet Services](windows-metadata-and-internet-services.md) (WMIS) and [Device Metadata Retrieval Client](device-metadata-retrieval-client.md) (DMRC) use the PackageInfo XML document to provide the Devices and Printers user interface with the current and most appropriate information for a device, such as the following:

-   The hardware or model ID of the device. This information is specified by the [**HardwareID**](/previous-versions/windows/hardware/metadata/ff546114(v=vs.85)) and [**ModelID**](/previous-versions/windows/hardware/metadata/ff549295(v=vs.85)) XML elements within the PackageInfo XML document.

-   A localized version of the device metadata package that matches the locale of the computer. This information is specified by the [**Locale**](/previous-versions/windows/hardware/metadata/ff548647(v=vs.85)) XML element within the PackageInfo XML document.

-   The last modified data of the device metadata package that matches the locale of the computer. This information is specified by the [**LastModifiedDate**](/previous-versions/windows/hardware/metadata/ff548624(v=vs.85)) XML element within the PackageInfo XML document.

Each device metadata package must contain only one PackageInfo XML document. The name of the document must be *PackageInfo.xml*.

The data in the PackageInfo XML document is formatted based on the [PackageInfo XML schema](/previous-versions/windows/hardware/metadata/ff549614(v=vs.85)).

 

