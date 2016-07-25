---
title: Device Metadata Package Structure
description: Device Metadata Package Structure
ms.assetid: 37614100-0a56-4a32-8e45-3161994e503a
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

-   The DeviceStage subdirectory contains the specific files that are used by Windows Device Stage™ to present the Device Stage experience. Device Stage is a rich platform for developing and distributing device-specific experiences. With Device Stage, a device maker can create experiences that match the branding, functionality, and services of its device by defining only a few XML files and graphics.

    If the device maker uses the Device Stage experience for the device, Windows requires the DeviceStage directory to be in the device metadata package. Otherwise, Windows ignores the directory if it is in the package.

    **Note**  Device Stage is supported for a limited number of device classes.

     

    More information about Windows Device Experience, Device Stage, and the Device Stage XML schema can be found in the [Microsoft Device Experience Development Kit](http://go.microsoft.com/fwlink/p/?linkid=192621).

When you create a device metadata package, you should follow these guidelines:

-   Each XML document must be saved by using UTF-8 encoding.

-   The device metadata package is not required to include a device icon. However, we highly recommend that the device metadata package contain a [device icon file](device-icon-file.md). This is used to display the photo-realistic image of the device in Devices and Printers.

Starting with the Windows 7 version of the Windows Driver Kit (WDK), the [Toaster Sample](http://go.microsoft.com/fwlink/p/?linkid=256195) provides a sample device metadata package. The XML documents for this package are located in the *src\\general\\toaster\\devicemetadatapackage* subdirectory of the WDK.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Metadata%20Package%20Structure%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




