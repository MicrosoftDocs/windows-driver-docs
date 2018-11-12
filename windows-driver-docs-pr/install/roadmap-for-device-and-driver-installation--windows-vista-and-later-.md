---
title: Roadmap for Device and Driver Installation
description: Roadmap for Device and Driver Installation
ms.assetid: d6cb6d8c-226f-4b6f-989a-36184236f826
ms.date: 04/20/2017
ms.localizationpriority: medium
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

    For more information, see [Signing Drivers during Development and Test](signing-drivers-during-development-and-test.md).

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

 

 





