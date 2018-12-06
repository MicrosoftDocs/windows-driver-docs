---
title: Overview of Device Metadata Packages
description: Overview of Device Metadata Packages
ms.assetid: 1b17bdab-44e4-498b-ab80-f28fa94d9821
keywords:
- device metadata packages WDK , about
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Device Metadata Packages


A device metadata package consists of multiple XML documents, and each document specifies various components of the device's attributes.

Starting with Windows 7, a new user interface for devices, Devices and Printers, shows most of the devices that are typically connected to a computer in one window. This window is called the gallery view. For each device that is displayed in the gallery view, Devices and Printers displays device-specific information to the user based on the XML documents from the device's metadata package. By using these XML documents, the OEM can customize which information is included and how this information appears. For example, a device in the gallery view can be represented by a custom icon and descriptive text that the OEM provides.

The XML documents that are contained within device metadata packages specify the information that describes the physical device. The following list shows the type of information that the XML documents can specify:

-   The name of the OEM.

-   The model name and description of the device.

-   One or more functional categories that the device supports.

Each device metadata package consists of the following components:

<a href="" id="packageinfo-xml-document"></a>[PackageInfo XML document](packageinfo-xml-document.md)  
This document contains data that specifies the contents of the device metadata package. The operating system uses this data to install the package and reference its contents.

This data is formatted based on the [PackageInfo XML schema](https://msdn.microsoft.com/library/windows/hardware/ff549614).

<a href="" id="deviceinfo-xml-document"></a>[DeviceInfo XML document](deviceinfo-xml-document.md)  
This document contains data that specifies the device's properties, such as device category and model name. The Devices and Printers user interface uses this data to show detailed information about the device.

This data is formatted based on the [DeviceInfo XML schema](https://msdn.microsoft.com/library/windows/hardware/ff541135).

<a href="" id="device-icon-file"></a>[Device icon file](device-icon-file.md)  
This file contains a photo-realistic image that represents the device in the Devices and Printers user interface.

<a href="" id="windowsinfo-xml-document"></a>[WindowsInfo XML document](windowsinfo-xml-document.md)  
This document contains data that specifies the display actions that the Devices and Printers user interface performs for the specified device in the device metadata package.

This data is formatted based on the [WindowsInfo XML Schema](https://msdn.microsoft.com/library/windows/hardware/ff553992).

Each device metadata package has its components compressed into a single file by using the Cabarc (*Cabarc.exe*) tool. For more information about this tool, see to the [Cabarc Overview](http://go.microsoft.com/fwlink/p/?linkid=145395) website.

The file name of the device metadata package uses the following naming convention:

```cpp
<GUID>.devicemetadata-ms
```

The *&lt;GUID&gt;* file prefix is a globally unique identifier (GUID) that is created for the device metadata package. The GUID for each metadata package file name must be unique. When you create a new or revised metadata package, you must create a new GUID, even if the changes are minor.

For more information, see [Building Device Metadata Packages](building-device-metadata-packages.md).

 

 





