---
title: Device Metadata Package Structure
description: Device Metadata Package Structure
ms.assetid: 37614100-0a56-4a32-8e45-3161994e503a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Metadata Package Structure


Each device metadata package has the following directory structure:

PackageInfo.xml

DeviceInformation
DeviceInfo.xml
*DeviceIcon*.ico

WindowsInformation
WindowsInfo.xml

DeviceStage
When you create a device metadata package, XML documents and icon files are stored in the following directories:

-   The [PackageInfo XML document](packageinfo-xml-document.md) is at the root of the directory. The name of this XML document must be PackageInfo.xml.

-   The DeviceInformation subdirectory contains the [DeviceInfo XML document](deviceinfo-xml-document.md) and the optional device icon file. The name of the XML document must be DeviceInfo.xml.

    If your device metadata package includes a device icon file, it can have any name but must end with a suffix of *.ico*. For more information, see [Device Icon File](device-icon-file.md).

-   The WindowsInformation subdirectory contains the [WindowsInfo XML document](windowsinfo-xml-document.md). The name of the XML document must be WindowsInfo.xml.

-   The DeviceStage subdirectory contains the specific files that are used by Windows Device Stage to present the Device Stage experience. Device Stage is a rich platform for developing and distributing device-specific experiences. With Device Stage, a device maker can create experiences that match the branding, functionality, and services of its device by defining only a few XML files and graphics.

    If the device maker uses the Device Stage experience for the device, Windows requires the DeviceStage directory to be in the device metadata package. Otherwise, Windows ignores the directory if it is in the package.

    **Note**  Device Stage is supported for a limited number of device classes.




More information about Windows Device Experience, Device Stage, and the Device Stage XML schema can be found in the [Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?linkid=192621).


When you create a device metadata package, you should follow these guidelines:

-   Each XML document must be saved by using UTF-8 encoding.

-   The device metadata package is not required to include a device icon. However, we highly recommend that the device metadata package contain a [device icon file](device-icon-file.md). This is used to display the photo-realistic image of the device in Devices and Printers.

Starting with the Windows 7 version of the Windows Driver Kit (WDK), the [Toaster Sample](http://go.microsoft.com/fwlink/p/?linkid=256195) provides a sample device metadata package. The XML documents for this package are located in the *src\\general\\toaster\\devicemetadatapackage* subdirectory of the WDK.









