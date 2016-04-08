---
title: Device and Driver Technologies
description: This section contains information about each of the supported Windows driver technologies.
ms.assetid: 1ef3e216-1322-42c3-b070-94cddfb2133c
---

# Device and Driver Technologies


This section contains information about each of the supported Windows driver technologies. The majority of the driver technology information is the same for all editions of Windows 10. When you must make special considerations for a particular edition of Windows, such as for Windows 10 Mobile, we explicitly called these out in each technology area. For general information about developing drivers see [Write your first driver](https://msdn.microsoft.com/library/windows/hardware/ff554811).

**Universal Windows drivers**

You can create a Universal Windows driver—a driver that uses a subset of the interfaces that are available to a Windows driver—to run on all editions of Windows 10. Where possible, use a Universal Windows driver to enable deployment of your drivers on multiple devices. For more information about how to build, install, deploy, and debug a Universal Windows driver for Windows 10, see [Getting Started with Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers) and [Deploying a Driver to a Test Computer](https://msdn.microsoft.com/windows-drivers/develop/deploying_a_driver_to_a_test_computer).

**Device drivers and Windows 10 for desktop computers**

For information about the tools used to develop desktop drivers, see [Device and Driver Development Tools](https://msdn.microsoft.com/en-us/library/windows/hardware/ff557553) and [Tools for Verifying Drivers](https://msdn.microsoft.com/library/windows/hardware/ff552969). For information about deploying drivers to Windows 10 on a desktop, see [Device and Driver Installation](https://msdn.microsoft.com/library/windows/hardware/dn653558). For information about troubleshooting driver installation, see [Troubleshoot Driver Configuration](https://msdn.microsoft.com/windows-drivers/develop/troubleshooting_configuration_of_driver_deployment__testing_and_debugging).

**Device drivers and Windows 10 Mobile**

Windows 10 Mobile is optimized for the unique needs of mobile devices. Instead of copying the driver to the desktop or installing it using Device Manager, you add a driver to the OS on a mobile device by using a package. For more information about working with packages see [Creating mobile packages](https://msdn.microsoft.com/library/dn756642). Also, a driver on a mobile device needs to be signed using a specific process to maintain integrity of the OS, as explained in [Mobile code signing](https://msdn.microsoft.com/library/windows/hardware/dn756634). For a walkthrough of adding a device driver to a mobile device such as a phone, see [Adding a driver to a test image](https://msdn.microsoft.com/library/windows/hardware/mt131832).

## In this section


-   [Audio Devices](https://msdn.microsoft.com/library/windows/hardware/ff537760)
-   [Battery Devices](https://msdn.microsoft.com/library/windows/hardware/ff536301)
-   [Biometric Devices](https://msdn.microsoft.com/library/windows/hardware/ff536448)
-   [Bluetooth Devices](https://msdn.microsoft.com/library/windows/hardware/ff536768)
-   [Bus and Port Drivers](https://msdn.microsoft.com/en-us/library/windows/hardware/ff557547)
-   [Display Devices (Adapters and Monitors)](https://msdn.microsoft.com/library/windows/hardware/ff569172)
-   [Human Input Devices](https://msdn.microsoft.com/library/windows/hardware/ff543301)
-   [Hardware Indicators](https://msdn.microsoft.com/library/windows/hardware/dn957503)
-   [Imaging Devices (Scanner)](https://msdn.microsoft.com/library/windows/hardware/ff546215)
-   [Infrared Devices](https://msdn.microsoft.com/library/windows/hardware/ff539583)
-   [Installable File System Drivers](https://msdn.microsoft.com/library/windows/hardware/ff551834)
-   [Modem Devices](https://msdn.microsoft.com/library/windows/hardware/ff542573)
-   [Multifunction Devices](https://msdn.microsoft.com/library/windows/hardware/ff542743)
-   [Network Devices](https://msdn.microsoft.com/en-us/library/windows/hardware/ff557563)
-   [Point of Service](https://msdn.microsoft.com/library/windows/hardware/mt269579)
-   [Print Devices](https://msdn.microsoft.com/library/windows/hardware/ff559887)
-   [Proximity Devices](https://msdn.microsoft.com/library/windows/hardware/dn905575)
-   [Radio Management](https://msdn.microsoft.com/library/windows/hardware/hh406615)
-   [Sensor Devices](https://msdn.microsoft.com/library/windows/hardware/ff545682)
-   [Smart Card Reader Devices](https://msdn.microsoft.com/library/windows/hardware/ff548914)
-   [Storage Devices](https://msdn.microsoft.com/library/windows/hardware/ff563893)
-   [Streaming Media Devices](https://msdn.microsoft.com/library/windows/hardware/ff567782)
-   [System Technologies](https://msdn.microsoft.com/en-us/library/windows/hardware/ff557564)
-   [Windows Portable Devices](https://msdn.microsoft.com/library/windows/hardware/ff597729)
-   [Windows SideShow Devices](https://msdn.microsoft.com/library/windows/hardware/ff548077)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdknodes\wdknodes%5D:%20Device%20and%20Driver%20Technologies%20%20RELEASE:%20%284/6/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




