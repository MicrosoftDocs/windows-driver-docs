---
title: DeviceInfo XML Document
description: DeviceInfo XML Document
ms.date: 04/20/2017
---

# DeviceInfo XML Document


The Devices and Printers user interface displays detailed information about the device that is based on the DeviceInfo XML document from the device's metadata package. This XML document contains data that specifies the device's properties, such as the following:

-   The functional category of the device. This information is specified by a [**DeviceCategory**](/previous-versions/windows/hardware/metadata/ff541101(v=vs.85)) XML element, which is a child element of the [**DeviceCategoryList**](/previous-versions/windows/hardware/metadata/ff541102(v=vs.85)) XML element within the DeviceInfo XML document.

    The first [**DeviceCategory**](/previous-versions/windows/hardware/metadata/ff541101(v=vs.85)) XML element within the [**DeviceCategoryList**](/previous-versions/windows/hardware/metadata/ff541102(v=vs.85)) XML element is considered the *primary functional category* of the device. When the Devices and Printers user interface first displays the gallery view of devices that are connected to the computer, or if the end-user has filtered devices by category, devices are displayed based on their primary functional category.

    For multifunction devices, additional functional categories are specified by a separate [**DeviceCategory**](/previous-versions/windows/hardware/metadata/ff541101(v=vs.85)) XML child element that follows the first **DeviceCategory** element within the [**DeviceCategoryList**](/previous-versions/windows/hardware/metadata/ff541102(v=vs.85)) XML element. Again, if the end-user filters devices within the Devices and Printers user interface based on device category, devices are displayed based on their primary and additional functional categories.

-   The model name of the device. This information is specified by the [**ModelName**](/previous-versions/windows/hardware/metadata/ff549311(v=vs.85)) XML element within the DeviceInfo XML document.

-   The description of the device. This information is specified by the [**DeviceDescription1**](/previous-versions/windows/hardware/metadata/ff541105(v=vs.85)) and [**DeviceDescription2**](/previous-versions/windows/hardware/metadata/ff541108(v=vs.85)) XML elements within the DeviceInfo XML document.

-   The manufacturer of the device. This information is specified by the [**Manufacturer**](/previous-versions/windows/hardware/metadata/ff548710(v=vs.85)) XML elements within the DeviceInfo XML document.

-   An icon that represents the device. This information is specified by the [**DeviceIconFile**](/previous-versions/windows/hardware/metadata/ff541123(v=vs.85)) XML element within the DeviceInfo XML document.

    For more information about device icons, see [Device Icon File](device-icon-file.md).

Each device metadata package must contain only one DeviceInfo XML document. The name of the document must be DeviceInfo.xml.

The data in the DeviceInfo XML document is formatted based on the [DeviceInfo XML schema](/previous-versions/windows/hardware/metadata/ff541135(v=vs.85)).

 

