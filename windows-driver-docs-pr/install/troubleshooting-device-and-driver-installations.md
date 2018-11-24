---
title: Troubleshooting Device and Driver Installations
description: Troubleshooting Device and Driver Installations
ms.assetid: 1ffad62b-140d-4a0a-9174-245e0344e605
keywords:
- Device setup WDK device installations , troubleshooting
- device installations WDK , troubleshooting
- installing devices WDK , troubleshooting
- troubleshooting device installations WDK
- Device setup WDK device installations , SetupAPI
- installing devices WDK , SetupAPI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Troubleshooting Device and Driver Installations





You can use the following guidelines to either verify that your device is installed correctly or diagnose problems with your device installation:

-   Follow the steps that are described in [Using Device Manager](using-device-manager.md) to view system information about the device.

-   Follow the steps that are described in [SetupAPI Logging (Windows Vista and Later)](setupapi-logging--windows-vista-and-later-.md) or [SetupAPI Logging (Windows Server 2003, Windows XP, and Windows 2000)](setupapi-logging--windows-server-2003--windows-xp--and-windows-2000-.md) to identify installation errors.

-   On Windows Vista and later versions of Windows, follow the steps that are described in [Debugging Device Installations (Windows Vista and Later)](debugging-device-installations--windows-vista-and-later-.md) to debug [co-installers](writing-a-co-installer.md) during the core stages of device installation.

-   On Windows Vista and later versions of Windows, follow the steps that are described in [Troubleshooting Install and Load Problems with Test-signed Drivers](troubleshooting-install-and-load-problems-with-signed-driver-packages.md) to diagnose problems related to the installation and loading of test-signed drivers.

-   Run test programs to exercise the device. This includes the testing and debugging tools that are supplied with the Windows Driver Kit (WDK).

Additionally, in Windows Server 2003, Windows XP, and Windows 2000, a [co-installer](writing-a-co-installer.md) can provide a troubleshooter that helps users diagnose problems with your device. See [**DIF_TROUBLESHOOTER**](https://msdn.microsoft.com/library/windows/hardware/ff543726) for more information.

 

 





