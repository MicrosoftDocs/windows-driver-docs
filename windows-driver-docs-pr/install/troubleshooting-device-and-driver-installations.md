---
title: Troubleshooting Device and Driver Installations
description: Troubleshooting Device and Driver Installations
ms.assetid: 1ffad62b-140d-4a0a-9174-245e0344e605
keywords: ["Device setup WDK device installations , troubleshooting", "device installations WDK , troubleshooting", "installing devices WDK , troubleshooting", "troubleshooting device installations WDK", "Device setup WDK device installations , SetupAPI", "installing devices WDK , SetupAPI"]
---

# Troubleshooting Device and Driver Installations


## <a href="" id="ddk-troubleshooting-device-installation-dg"></a>


You can use the following guidelines to either verify that your device is installed correctly or diagnose problems with your device installation:

-   Follow the steps that are described in [Using Device Manager](using-device-manager.md) to view system information about the device.

-   Follow the steps that are described in [SetupAPI Logging (Windows Vista and Later)](setupapi-logging--windows-vista-and-later-.md) or [SetupAPI Logging (Windows Server 2003, Windows XP, and Windows 2000)](setupapi-logging--windows-server-2003--windows-xp--and-windows-2000-.md) to identify installation errors.

-   On Windows Vista and later versions of Windows, follow the steps that are described in [Debugging Device Installations (Windows Vista and Later)](debugging-device-installations--windows-vista-and-later-.md) to debug [co-installers](writing-a-co-installer.md) during the core stages of device installation.

-   On Windows Vista and later versions of Windows, follow the steps that are described in [Troubleshooting Install and Load Problems with Test-signed Drivers](troubleshooting-install-and-load-problems-with-signed-driver-packages.md) to diagnose problems related to the installation and loading of test-signed drivers.

-   Run test programs to exercise the device. This includes the testing and debugging tools that are supplied with the Windows Driver Kit (WDK).

Additionally, in Windows Server 2003, Windows XP, and Windows 2000, a [co-installer](writing-a-co-installer.md) can provide a troubleshooter that helps users diagnose problems with your device. See [**DIF\_TROUBLESHOOTER**](https://msdn.microsoft.com/library/windows/hardware/ff543726) for more information.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Troubleshooting%20Device%20and%20Driver%20Installations%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




