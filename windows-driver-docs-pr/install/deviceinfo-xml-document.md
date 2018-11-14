---
title: DeviceInfo XML Document
description: DeviceInfo XML Document
ms.assetid: b6b859cf-de30-4df0-bec1-0cd7d8c55ea6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DeviceInfo XML Document


The Devices and Printers user interface displays detailed information about the device that is based on the DeviceInfo XML document from the device's metadata package. This XML document contains data that specifies the device's properties, such as the following:

-   The functional category of the device. This information is specified by a [**DeviceCategory**](https://msdn.microsoft.com/library/windows/hardware/ff541101) XML element, which is a child element of the [**DeviceCategoryList**](https://msdn.microsoft.com/library/windows/hardware/ff541102) XML element within the DeviceInfo XML document.

    The first [**DeviceCategory**](https://msdn.microsoft.com/library/windows/hardware/ff541101) XML element within the [**DeviceCategoryList**](https://msdn.microsoft.com/library/windows/hardware/ff541102) XML element is considered the *primary functional category* of the device. When the Devices and Printers user interface first displays the gallery view of devices that are connected to the computer, or if the end-user has filtered devices by category, devices are displayed based on their primary functional category.

    For multifunction devices, additional functional categories are specified by a separate [**DeviceCategory**](https://msdn.microsoft.com/library/windows/hardware/ff541101) XML child element that follows the first **DeviceCategory** element within the [**DeviceCategoryList**](https://msdn.microsoft.com/library/windows/hardware/ff541102) XML element. Again, if the end-user filters devices within the Devices and Printers user interface based on device category, devices are displayed based on their primary and additional functional categories.

-   The model name of the device. This information is specified by the [**ModelName**](https://msdn.microsoft.com/library/windows/hardware/ff549311) XML element within the DeviceInfo XML document.

-   The description of the device. This information is specified by the [**DeviceDescription1**](https://msdn.microsoft.com/library/windows/hardware/ff541105) and [**DeviceDescription2**](https://msdn.microsoft.com/library/windows/hardware/ff541108) XML elements within the DeviceInfo XML document.

-   The manufacturer of the device. This information is specified by the [**Manufacturer**](https://msdn.microsoft.com/library/windows/hardware/ff548710) XML elements within the DeviceInfo XML document.

-   An icon that represents the device. This information is specified by the [**DeviceIconFile**](https://msdn.microsoft.com/library/windows/hardware/ff541123) XML element within the DeviceInfo XML document.

    For more information about device icons, see [Device Icon File](device-icon-file.md).

Each device metadata package must contain only one DeviceInfo XML document. The name of the document must be DeviceInfo.xml.

The data in the DeviceInfo XML document is formatted based on the [DeviceInfo XML schema](https://msdn.microsoft.com/library/windows/hardware/ff541135).

 

 





