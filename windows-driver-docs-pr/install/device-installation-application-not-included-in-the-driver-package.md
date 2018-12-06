---
title: Device Installation Application Not Included in Driver Package
description: Device Installation Application Not Included in the Driver Package
ms.assetid: 3c8fd504-50c9-4a61-9cca-cd8cee4e2bd7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Installation Application Not Included in the Driver Package


This method describes a way through which a co-installer, by using [finish-install actions](finish-install-actions--windows-vista-and-later-.md), can start a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) to install device-specific applications.

In this method, the device installation application is not part of the [driver package](driver-packages.md), and the driver package's INF file is not used to copy this file to the user's hard drive. Instead, the co-installer starts the device installation application directly from the distribution medium, or prompts the user to download the device installation application from the Internet.

This method has the following advantages:

-   If the co-installer supplies [finish-install actions](finish-install-actions--windows-vista-and-later-.md), this method can be used to install [driver packages](driver-packages.md) and device-specific applications on Windows Vista and later versions of Windows.

-   Only the driver package must be digitally signed. The device installation application and associated installation files do not have to be digitally signed. For more information about digital signatures, see [Driver Signing](driver-signing.md).

-   Only the driver package is copied to the driver store. When the device installation application is launched, the device-specific applications are installed elsewhere on the user's hard drive.

-   The user can be prompted during [driver package](driver-packages.md) updates to update the device-specific applications. This occurs through the [finish-install actions](finish-install-actions--windows-vista-and-later-.md) supplied by the package's co-installer. In this way, synchronizing versions of the driver package and device-specific applications is optional. Also, additional device-specific applications, which are not on the distribution medium, can be downloaded from the Internet.

-   The independent hardware vendor (IHV) has greater flexibility with the distribution medium. The device installation application and device-specific applications can be on the medium or can be downloaded from the Internet.

If you use this method, the following will occur whenever the user installs the device before inserting the distribution medium, or Windows Updates detects a new driver for the device:

1.  The [driver package](driver-packages.md) for the device is installed as described in [hardware-first installation](hardware-first-installation.md).

2.  If the driver package's co-installer supplies [finish-install actions](finish-install-actions--windows-vista-and-later-.md), one of the following occurs at the end of the driver package installation:

    -   The device installation application on the distribution medium is launched to install the device-specific applications.
    -   The user is prompted to download a newer version of the device installation application from the Internet. Through this, the IHV can provide additional device-specific applications which are not on the distribution medium.

        The co-installer then starts the device installation application as soon as it is downloaded from the Internet.

**Note**  Since the [driver package](driver-packages.md) has already been installed before the device installation application is launched, the application must detect that the drivers are already installed and only install the device-specific applications.

 

For more information about co-installers, see [Writing a Co-installer](writing-a-co-installer.md).

For more information about starting device installation application through co-installers, see [Guidelines for Starting Device Installation Applications through Co-installers](guidelines-for-starting-device-installation-applications-through-co-in.md).

 

 





