---
title: Installing Device-Specific Applications
description: Installing Device-Specific Applications
ms.assetid: 47e54ea6-f391-420a-aa69-caf7225b1147
keywords: ["installation applications WDK , device-specific applications", "device installation applications WDK , device-specific applications", "device-specific applications WDK device installations"]
---

# Installing Device-Specific Applications


## <a href="" id="ddk-installing-device-specific-applications-dg"></a>


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20Device-Specific%20Applications%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




