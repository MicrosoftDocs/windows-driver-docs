---
title: Device Metadata Retrieval Client
description: Device Metadata Retrieval Client
ms.assetid: fdcf3459-0fd4-4cf6-a9f5-13337fbd604b
keywords:
- DMRC WDK
- Device Metadata Retrieval Client WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Metadata Retrieval Client


The Device Metadata Retrieval Client (DMRC) is the operating system component that matches devices to device metadata packages. When the user opens the gallery view window of the Devices and Printers user interface, the DMRC tries to obtain device metadata for the devices that Devices and Printers will display. First, it checks the local computer's [device metadata cache](device-metadata-cache.md) and [device metadata store](device-metadata-store.md). If the device is newly installed, or if the device is scheduled for a periodic metadata update, DMRC queries the [Windows Metadata and Internet Services](windows-metadata-and-internet-services.md) (WMIS) website to determine whether a device metadata package is available for the device. If a device metadata package is available, DMRC automatically downloads the package from WMIS, extracts the package's device metadata components, and saves them within the device metadata cache.

The [PackageInfo XML document](packageinfo-xml-document.md) (Packageinfo.xml), which is a component of a device metadata package, contains the information that the DMRC needs in order to match a device to the package. The file includes a [**MetadataKey**](https://msdn.microsoft.com/library/windows/hardware/ff548740) XML element that specifies the device-matching information, which comes from one of the following sources:

-   A list of one or more hardware IDs that identifies a hardware function that is supported by the device. The list of hardware IDs is specified in the [**HardwareIDList**](https://msdn.microsoft.com/library/windows/hardware/ff546121) child XML element.

-   A list of one or more model IDs that identifies a hardware function that is supported by the device. Each model ID is a globally unique identifier (GUID), and the list of model IDs is specified in the [**ModelIDList**](https://msdn.microsoft.com/library/windows/hardware/ff549303) child XML element.

For more information about the XML schema that is referenced by the [PackageInfo XML document](packageinfo-xml-document.md), see [PackageInfo XML Schema](https://msdn.microsoft.com/library/windows/hardware/ff549614).

 

 





