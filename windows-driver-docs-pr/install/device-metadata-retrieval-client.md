---
title: Device Metadata Retrieval Client
description: Device Metadata Retrieval Client
ms.assetid: fdcf3459-0fd4-4cf6-a9f5-13337fbd604b
keywords: ["DMRC WDK", "Device Metadata Retrieval Client WDK"]
---

# Device Metadata Retrieval Client


The Device Metadata Retrieval Client (DMRC) is the operating system component that matches devices to device metadata packages. When the user opens the gallery view window of the Devices and Printers user interface, the DMRC tries to obtain device metadata for the devices that Devices and Printers will display. First, it checks the local computer's [device metadata cache](device-metadata-cache.md) and [device metadata store](device-metadata-store.md). If the device is newly installed, or if the device is scheduled for a periodic metadata update, DMRC queries the [Windows Metadata and Internet Services](windows-metadata-and-internet-services.md) (WMIS) website to determine whether a device metadata package is available for the device. If a device metadata package is available, DMRC automatically downloads the package from WMIS, extracts the package's device metadata components, and saves them within the device metadata cache.

The [PackageInfo XML document](packageinfo-xml-document.md) (Packageinfo.xml), which is a component of a device metadata package, contains the information that the DMRC needs in order to match a device to the package. The file includes a [**MetadataKey**](https://msdn.microsoft.com/library/windows/hardware/ff548740) XML element that specifies the device-matching information, which comes from one of the following sources:

-   A list of one or more hardware IDs that identifies a hardware function that is supported by the device. The list of hardware IDs is specified in the [**HardwareIDList**](https://msdn.microsoft.com/library/windows/hardware/ff546121) child XML element.

-   A list of one or more model IDs that identifies a hardware function that is supported by the device. Each model ID is a globally unique identifier (GUID), and the list of model IDs is specified in the [**ModelIDList**](https://msdn.microsoft.com/library/windows/hardware/ff549303) child XML element.

For more information about the XML schema that is referenced by the [PackageInfo XML document](packageinfo-xml-document.md), see [PackageInfo XML Schema](https://msdn.microsoft.com/library/windows/hardware/ff549614).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Metadata%20Retrieval%20Client%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




