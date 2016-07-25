---
title: Device Installation Application that is Included in the Driver Package
description: Device Installation Application that is Included in the Driver Package
ms.assetid: bd6e182c-6b7a-4cde-bcc7-637ae6bf39be
---

# Device Installation Application that is Included in the Driver Package


This method describes a way through which a co-installer, using [finish-install actions](finish-install-actions--windows-vista-and-later-.md), can start a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) to install device-specific applications.

In this method, the device installation application and associated installation files are part of the [driver package](driver-packages.md), and the driver package's INF file is used to copy the application and installation files to the driver store. As a result, the application and driver are both installed in all scenarios.

This method has the following advantages:

-   If the co-installer supplies [finish-install actions](finish-install-actions--windows-vista-and-later-.md), this method can be used to install driver packages, including device-specific applications, on Windows Vista and later versions of Windows.

-   Since the device installation application, associated installation files, and driver are part of the same driver package, they will be installed or updated at the same time. This synchronizes the versions of all components in the driver package.

However, this method also has the following disadvantages:

-   The device installation application and associated installation files must be digitally signed if it is part of the [driver package](driver-packages.md). For more information about digital signatures, see [Driver Signing](driver-signing.md).

    In addition, the driver, device installation application, and associated installation files must be submitted to Windows Hardware Quality Labs (WHQL) as a single driver package whenever these components are modified. For more information about this process, see [WHQL release signatures](whql-release-signature.md).

-   The device installation application and associated installation files are copied to two places on the user's hard drive: the driver store as well as the directory that is specified in the INF file's [**INF DestinationDirs Section**](inf-destinationdirs-section.md).

-   Optional device-specific applications, which are not installed through the device installation application, cannot be installed from the distribution medium or downloaded from the Internet.

    Since the device installation application and associated installation files are signed as part of the [driver package](driver-packages.md), only applications installed through the device installation application are allowed in order to ensure the integrity of the driver package.

If you use this method, the following will occur whenever the user installs the device before inserting the distribution medium, or Windows Updates detects a new driver for the device:

1.  The driver package for the device is installed as described in [hardware-first installation](hardware-first-installation.md).

2.  The [driver package's](driver-packages.md) INF file copies the device installation application and associated installation files to a directory on the user's hard drive, which is typically the Program Files directory. This is done as part of the processing of the [**INF CopyFiles directive**](inf-copyfiles-directive.md) in the INF file.

3.  If the driver package's co-installer supplies [finish-install actions](finish-install-actions--windows-vista-and-later-.md), the co-installer starts the device installation application on the distribution medium to install the device-specific applications.

**Note**  Since the [driver package](driver-packages.md) has already been installed before the device installation application is launched, the application must detect that the drivers are already installed and only install the device-specific applications.

 

For more information about co-installers, see [Writing a Co-installer](writing-a-co-installer.md).

For more information about starting device installation applications through co-installers, see [Guidelines for Starting Device Installation Applications through Co-installers](guidelines-for-starting-device-installation-applications-through-co-in.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Installation%20Application%20that%20is%20Included%20in%20the%20Driver%20Package%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




