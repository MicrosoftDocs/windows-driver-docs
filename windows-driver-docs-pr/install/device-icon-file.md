---
title: Device Icon File
description: Device Icon File
ms.assetid: bd1272d5-f673-4138-887d-94653cf41829
---

# Device Icon File


A device metadata package can contain one photo-realistic image, or icon, that represents the device in the Devices and Printers user interface. The image is stored in an icon file, and the file name must be specified in the [**DeviceIconFile**](https://msdn.microsoft.com/library/windows/hardware/ff541123) element of the package's [DeviceInfo XML document](deviceinfo-xml-document.md).

If the device metadata package does not contain a device icon file and [**DeviceIconFile**](https://msdn.microsoft.com/library/windows/hardware/ff541123) element, the Devices and Printers user interface displays a default icon for the device. This icon is based on the device's category type that is specified in the [**DeviceCategory**](https://msdn.microsoft.com/library/windows/hardware/ff541101) element of the DeviceInfo XML document.

**Note**  We highly recommend that the device metadata package contain a device icon file, which is used to display the photo-realistic image of the device in the Devices and Printers user interface. For more information about how to create icons that have the same display qualities of Windows graphical elements, refer to [Icons](http://go.microsoft.com/fwlink/p/?linkid=145422) in the Microsoft SDK.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Icon%20File%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




