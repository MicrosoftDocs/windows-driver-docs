---
title: Device Icon File
description: Device Icon File
ms.date: 04/20/2017
---

# Device Icon File


A device metadata package can contain one photo-realistic image, or icon, that represents the device in the Devices and Printers user interface. The image is stored in an icon file, and the file name must be specified in the [**DeviceIconFile**](/previous-versions/windows/hardware/metadata/ff541123(v=vs.85)) element of the package's [DeviceInfo XML document](deviceinfo-xml-document.md).

If the device metadata package does not contain a device icon file and [**DeviceIconFile**](/previous-versions/windows/hardware/metadata/ff541123(v=vs.85)) element, the Devices and Printers user interface displays a default icon for the device. This icon is based on the device's category type that is specified in the [**DeviceCategory**](/previous-versions/windows/hardware/metadata/ff541101(v=vs.85)) element of the DeviceInfo XML document.

**Note**  We highly recommend that the device metadata package contain a device icon file, which is used to display the photo-realistic image of the device in the Devices and Printers user interface. For more information about how to create icons that have the same display qualities of Windows graphical elements, refer to [Icons](/visualstudio/extensibility/ux-guidelines/images-and-icons-for-visual-studio) in the Microsoft SDK.

 

 

