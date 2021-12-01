---
title: Roadmap for Device and Driver Installation
description: Roadmap for Device and Driver Installation
ms.date: 12/01/2021
ms.localizationpriority: medium
---

# Roadmap for Device and Driver Installation


![figure of a compass, a map, and a finger pointing at the map.](images/map-hand-sml.png)

To install a device and driver in the Windows operating system, follow these steps:

-   Step 1: Learn the fundamentals of device and driver installation in Windows.

    You must understand the fundamentals of device and driver installation in the Windows family of operating systems. This will help you to make appropriate design decisions and will allow you to streamline your development process. For more information, see [Overview of Device and Driver Installations](overview-of-device-and-driver-installation.md).

-   Step 2: Learn about driver packages and their components.

    A driver package consists of all the components that you must supply to install your device and support it under Windows.  This includes an INF file and all the files that the INF file references.

    For more information, see [Driver Packages](driver-packages.md) and [INF Files](overview-of-inf-files.md).

-   Step 3: Create a driver package for your device and drivers.

    Your driver package must provide an INF file and optionally driver files or additional software components.

    For more information about the components of a driver package, see [Creating a Driver Package](../develop/creating-a-driver-package.md).

    For example driver packages, see the [Toaster Sample](../wdf/sample-kmdf-drivers.md).

-   Step 4: Test-sign your driver package during development and testing.

    Test-signing refers to using a test certificate to sign a prerelease version of a [driver package](driver-packages.md) for use on test computers. In particular, this allows developers to sign driver packages by using self-signed certificates, such as those the [**MakeCert**](../devtest/makecert.md) tool generates. This capability allows developers to install and test driver packages in Windows with driver signature verification enabled.

    For more information, see [Signing Drivers during Development and Test](./introduction-to-test-signing.md).

-   Step 5: Release-sign your driver package for distribution.

    After you have tested and verified your [driver package](driver-packages.md), you should release-sign the driver package. Release-signing identifies the publisher of a driver package. While this step is optional, driver packages should be release-signed for the following reasons:

    - Ensure the authenticity, integrity, and reliability of driver packages. Windows uses digital signatures to verify the identity of the publisher and to verify that the driver has not been altered since it was published.
    - Provide the best user experience by facilitating automatic driver installation.
    - Run kernel-mode drivers on 64-bit versions of Windows Vista and later versions of Windows.
    - Playback certain types of next-generation premium content.

    [Driver packages](driver-packages.md) are release-signed through either:

    - A [WHQL Release Signature](whql-release-signature.md) obtained through the [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility/) (for Windows 10/11), or the [Windows Hardware Certification Program](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) (for Windows 8/8.1 and older operating systems).
    - A release signature created through a [Software Publisher Certificate (SPC)](/windows-hardware/drivers/install/deprecation-of-software-publisher-certificates-and-commercial-release-certificates).

    For more information, see [Signing Drivers for Public Release](signing-drivers-for-public-release--windows-vista-and-later-.md).

-   Step 6: Distribute your driver package.

    The final step is to distribute the [driver package](driver-packages.md). If your driver package meets the quality standards that are defined in the the [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility/) (for Windows 10/11), or the [Windows Hardware Certification Program](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) (for Windows 8/8.1 and older operating systems), you can distribute it through Microsoft Windows Update program. For more information, see [Publishing a driver to Windows Update](../dashboard/publish-a-driver-to-windows-update.md).

These are the basic steps. Additional steps might be necessary based on the installation needs of your individual device and driver.