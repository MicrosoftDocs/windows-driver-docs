---
title: Device Installation Application Started through AutoRun
description: Device Installation Application Started through AutoRun
ms.assetid: 9b520d82-2293-4936-99fe-30bf6753ba9f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Installation Application Started through AutoRun


This method builds upon existing [software-first installation](software-first-installation.md) methods to create a [hardware-first installation](hardware-first-installation.md) scenario. This method relies on the [**INF HardwareId directive**](inf-hardwareid-directive.md), which is supported in Windows Vista and later versions of Windows.

In this method, the [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) on the distribution medium is launched as part of the processing of the Autorun.inf file. When the user plugs in the device, the Found New Hardware Wizard parses this file, and looks for an [**INF HardwareId directive**](inf-hardwareid-directive.md) that matches the device that is being installed. If the wizard finds a match, it invokes the AutoRun-enabled device installation application to install the [driver package](driver-packages.md) and device-specific applications.

This method has the following advantages:

-   Independent hardware vendors (IHVs) can easily use this method to an existing AutoRun-compatible distribution medium by adding one or more [**INF HardwareId directives**](inf-hardwareid-directive.md) to the Autorun.inf file. For more information about and AutoRun and AutoRun-enabled applications, see [Creating an AutoRun-Enabled Application](http://go.microsoft.com/fwlink/p/?linkid=133162).

-   Only the [driver package](driver-packages.md) must be digitally signed. The device installation application and associated installation files do not have to be digitally signed. For more information about digital signatures, see [Driver Signing](driver-signing.md).

-   Only the driver package is copied to the [driver store](driver-store.md). The device-specific applications are installed elsewhere on the user's hard drive.

-   The user can be prompted during driver package updates to update the device-specific applications. This occurs through the [finish-install actions](finish-install-actions--windows-vista-and-later-.md) supplied by the package's co-installer. In this way, updates to the driver package and device-specific applications can be synchronized. Also, additional or optional applications, which are not on the distribution medium, can be downloaded from the Internet.

However, this method also has the following disadvantages:

-   This method can be used for installing [driver package](driver-packages.md) and device-specific application installation only on Windows Vista and later versions of Windows.

-   The distribution media must be AutoRun-compatible, such as a CD or DVD. The [**INF HardwareId directive**](inf-hardwareid-directive.md) does not provide any capability for downloading an application installer from the Internet.

 

 





