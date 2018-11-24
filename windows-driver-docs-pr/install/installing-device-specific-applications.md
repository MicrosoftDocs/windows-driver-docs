---
title: Installing Device-Specific Applications
description: Installing Device-Specific Applications
ms.assetid: 47e54ea6-f391-420a-aa69-caf7225b1147
keywords:
- installation applications WDK , device-specific applications
- device installation applications WDK , device-specific applications
- device-specific applications WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Device-Specific Applications





If your distribution medium includes device-specific applications, you can use the following methods to install those applications:

-   Use a device co-installer to install the applications by using [finish-install actions](finish-install-actions--windows-vista-and-later-.md).

    If the user plugs in the device before inserting the distribution medium, this is referred to as a [hardware-first installation](hardware-first-installation.md). If the device is not supported by inbox drivers, Windows calls the co-installer that is supplied by the medium during the installation process.

    The co-installer should determine whether the device-specific applications have already been installed. If they have not, the co-installer should do one of the following

    1.  Start a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) on the distribution medium to install the device-specific applications.
    2.  Prompt the user to download a newer version of the device installation application from the Internet.

    Independent hardware vendors (IHVs) can use various methods to provide [hardware-first installation](hardware-first-installation.md) solutions for installing device-specific applications. For more information about these methods, see [Hardware-First Installation of Device-Specific Applications](hardware-first-installation-of-device-specific-applications.md).

    For more information about co-installers, see [Writing a Co-installer](writing-a-co-installer.md).

-   Use a device installation application that uses Windows Installer to install the device-specific applications.

    If the user inserts the distribution medium before plugging in the device, this is referred to as a [software-first installation](software-first-installation.md). The medium's AutoRun-invoked device installation application should determine whether the device-specific applications have already been installed and if they have not, it should install them by using Windows Installer. For more information, see the Windows SDK documentation.

 

 





