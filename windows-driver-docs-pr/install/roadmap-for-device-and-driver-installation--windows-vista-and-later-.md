---
title: Roadmap for Device and Driver Installation
description: Roadmap for Device and Driver Installation
ms.assetid: d6cb6d8c-226f-4b6f-989a-36184236f826
---

# Roadmap for Device and Driver Installation


![figure of a compass, a map, and a finger pointing at the map](images/map-hand-sml.png)

To install a device and driver in Windows 7 and later versions of Windows, follow these steps:

-   Step 1: Learn the fundamentals of device and driver installation in Windows.

    You must understand the fundamentals of device and driver installation in the Windows family of operating systems. This will help you to make appropriate design decisions and will allow you to streamline your development process. For more information, see [Overview of Device and Driver Installations](overview-of-device-and-driver-installation.md).

-   Step 2: Learn about driver packages and their components.

    A driver package consists of all the components that you must supply to install your device and support it under Windows.

    To install a device or a driver, you must have system-supplied and vendor-supplied components. The system provides generic installation software for all device classes. Vendors must supply one or more device-specific components within the driver package.

    For more information, see [Driver Packages](driver-packages.md).

-   Step 3: Learn about information (INF) files.

    An INF file contains the information and device settings which the system-provided [device installation components](https://msdn.microsoft.com/library/windows/hardware/ff541277) use to install your [driver package](driver-packages.md), such as the driver for the device and any device-specific applications.

    For more information, see [INF Files](inf-files.md).

-   Step 4: Create a driver package for your device and drivers.

    Your driver package must provide an INF file, the device's driver files, as well as optionally provide additional software components. You may refer to the sample Toaster driver package to determine which components are needed for your driver package.

    For more information about the components of a driver package, see [Creating a Driver Package](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_package).

    For more information about driver packages, see the [Toaster Sample](http://go.microsoft.com/fwlink/p/?linkid=256195).

-   Step 5: Test-sign your driver package during development and testing.

    Test-signing refers to using a test certificate to sign a prerelease version of a [driver package](driver-packages.md) for use on test computers. In particular, this allows developers to sign driver packages by using self-signed certificates, such as those the [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) tool generates. This capability allows developers to install and test driver packages in Windows with driver signature verification enabled.

    For more information, see [Signing Drivers during Development and Test](signing-drivers-during-development-and-test--windows-vista-and-later-.md).

-   Step 6: Release-sign your driver package for distribution.

    After you have tested and verified your [driver package](driver-packages.md), you should release-sign the driver package. Release-signing identifies the publisher of a driver package. While this step is optional, driver packages should be release-signed for the following reasons:

    -   Ensure the authenticity, integrity, and reliability of driver packages. Windows uses digital signatures to verify the identity of the publisher and to verify that the driver has not been altered since it was published.
    -   Provide the best user experience by facilitating automatic driver installation.
    -   Run kernel-mode drivers on 64-bit versions of Windows Vista and later versions of Windows.
    -   Playback certain types of next-generation premium content.

    [Driver packages](driver-packages.md) are release-signed through either:

    -   A [WHQL Release Signature](whql-release-signature.md) obtained through the [Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=227016).
    -   A release signature created through a [Software Publisher Certificate (SPC)](software-publisher-certificate.md).

    For more information, see [Signing Drivers for Public Release](signing-drivers-for-public-release--windows-vista-and-later-.md).

-   Step 7: Distribute your driver package.

    The final step is to distribute the [driver package](driver-packages.md). If your driver package meets the quality standards that are defined in the HCK, you can distribute it through Microsoft Windows Update program. For more information, see [Distributing a Driver Package](https://msdn.microsoft.com/windows-drivers/develop/distributing_a_driver_package_win8).

These are the basic steps. Additional steps might be necessary based on the installation needs of your individual device and driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Roadmap%20for%20Device%20and%20Driver%20Installation%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




