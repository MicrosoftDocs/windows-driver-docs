---
title: Device Icon File
description: Device Icon File
ms.assetid: bd1272d5-f673-4138-887d-94653cf41829
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Icon File


A device metadata package can contain one photo-realistic image, or icon, that represents the device in the Devices and Printers user interface. The image is stored in an icon file, and the file name must be specified in the [**DeviceIconFile**](https://msdn.microsoft.com/library/windows/hardware/ff541123) element of the package's [DeviceInfo XML document](deviceinfo-xml-document.md).

If the device metadata package does not contain a device icon file and [**DeviceIconFile**](https://msdn.microsoft.com/library/windows/hardware/ff541123) element, the Devices and Printers user interface displays a default icon for the device. This icon is based on the device's category type that is specified in the [**DeviceCategory**](https://msdn.microsoft.com/library/windows/hardware/ff541101) element of the DeviceInfo XML document.

**Note**  We highly recommend that the device metadata package contain a device icon file, which is used to display the photo-realistic image of the device in the Devices and Printers user interface. For more information about how to create icons that have the same display qualities of Windows graphical elements, refer to [Icons](https://docs.microsoft.com/visualstudio/extensibility/ux-guidelines/images-and-icons-for-visual-studio?view=vs-2017) in the Microsoft SDK.

 

 

 





