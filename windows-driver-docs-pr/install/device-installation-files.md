---
title: Device Installation Files
description: Device Installation Files
ms.assetid: a4a53040-ff53-49ba-a4a5-aba5f13119ef
keywords: ["Device setup WDK device installations , files", "device installations WDK , files", "installing devices WDK , files", "files WDK device installations"]
---

# Device Installation Files


## <a href="" id="ddk-device-installation-files-dg"></a>


The software that is required to support a particular device depends on the kind of device and the ways in which the device is used. Typically, a vendor provides the following software in a [driver package](driver-packages.md) to support a device:

<a href="" id="a-device-setup-information-file--inf-file-"></a>A device setup information file (INF file)  
An INF file contains information that the system Windows components use to install support for the device. Windows copies this file to the %*SystemRoot*%\\*inf* directory when it installs the driver. This file is required.

For more information, see [Creating an INF File](overview-of-inf-files.md).

<a href="" id="one-or-more-drivers-for-the-device"></a>One or more drivers for the device  
A .*sys* file is the driver's image file. Windows copies this file to the *%SystemRoot%\\system32\\drivers* directory when the driver is installed. Drivers are required for most devices.

For more information, see [Choosing a Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff554652).

<a href="" id="digital-signatures-for-the-driver-package--a-driver-catalog-file-"></a>Digital signatures for the [driver package](driver-packages.md) (a driver catalog file)  
A driver catalog file contains digital signatures. All driver packages should be signed.

A vendor obtains digital signatures by submitting its driver package to the Windows Hardware Quality Lab (WHQL) for testing and signing. WHQL returns the package with a catalog file (.*cat* file).

For more information, see [WHQL release signatures](whql-release-signature.md).

<a href="" id="other-files"></a>Other files  
A [driver package](driver-packages.md) can contain other files, such as a custom device installation application, a device icon, or a driver library file (such as for video drivers).

For more information, see [Providing Device Property Pages](providing-device-property-pages.md) and [Drivers with Special Installation Requirements](drivers-with-special-installation-requirements.md).

Also, see the device-type-specific documentation in the WDK.

The WDK includes various sample installation files. For more information, see [Sample Device Installation Files](sample-device-installation-files.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Installation%20Files%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




