---
title: Guidelines for Writing Device Installation Applications
description: Guidelines for Writing Device Installation Applications
ms.assetid: 7f364b95-98ca-479a-8cdb-5e5e77c70cfa
keywords: ["installation applications WDK , guidelines", "device installation applications WDK , guidelines"]
---

# Guidelines for Writing Device Installation Applications


[*Device installation applications*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application)   *must* do the following:

-   Support removal of all device-specific applications that they install. As part of that uninstall process, the device installation application should check whether any associated devices are still present on the system and, if so, warn the user.

-   Follow the guidelines for [installing devices on 64-bit systems](device-installations-on-64-bit-systems.md).

-   Starting with Windows Vista, list all the applications that were installed by using Microsoft Windows Installer (MSI), and that are available in **Programs and Features** in Control Panel. You can then uninstall these items if necessary.

-   In versions of Windows earlier than Windows Vista, list all the applications that were installed by using Microsoft Windows Installer (MSI), and that are available in **Add Or Remove Programs** in Control Panel. You can then uninstall these items if necessary.

-   Follow the guidelines for Microsoft Windows applications. See the [Microsoft Developer Network (MSDN)](http://go.microsoft.com/fwlink/p/?linkid=8714) website for more information.

Device installation applications *can* do the following:

-   [Install device-specific applications](installing-device-specific-applications.md)

    **Note**  We highly recommend that you submit device-specific applications to the appropriate [Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=227016) for software. See the [MSDN](http://go.microsoft.com/fwlink/p/?linkid=8714) website for more information.

     

-   [Preload driver packages](preloading-driver-packages.md)

-   [Preinstall driver packages](preinstalling-driver-packages.md)

Device installation applications *must not* do the following:

-   Instruct the user to copy or overwrite any files, especially .*inf* and .*sys* files.

-   Delete the installed driver files from the system during the uninstall operation, even if the hardware is removed.

-   Force any unnecessary system restarts. Restarts are generally not required for installing PnP devices or software applications. The *bRebootRequired* parameter of the [**UpdateDriverForPlugAndPlayDevices**](https://msdn.microsoft.com/library/windows/hardware/ff553534) function indicates the need for a restart.

-   Use [RunOnce registry keys](runonce-registry-key.md) to start [*device installation applications*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application), because this requires a system restart.

-   Use a device or class co-installer, or a class installer, to start a device installation application, because the state of the system during device installation cannot be guaranteed to be safe for installing software applications. Specifically, if the device installation application runs during a server-side installation, the system will stop responding.

    After the device is installed, device installation applications can be started safely by using [finish-install actions](finish-install-actions--windows-vista-and-later-.md) that are supplied by class installers or co-installers.

    For more information about co-installers, see [Writing a Co-installer](writing-a-co-installer.md).

-   Use the Startup Group to start [*device installation applications*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application).

-   Use *win.ini* entries to start device installation applications.

-   Force the user to install any device-specific applications, unless the device will not operate without the application. Examples might include utilities for setting configurable keyboard keys or for setting a modem's country/region code, if an inbox application does not support such a capability.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Guidelines%20for%20Writing%20Device%20Installation%20Applications%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




