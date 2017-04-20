---
title: Roadmap for Developing Native 802.11 Wireless LAN Drivers
description: Roadmap for Developing Native 802.11 Wireless LAN Drivers
ms.assetid: bedfa5e7-a5b2-45a4-9bc0-82686b0ecffe
keywords:
- wireless LAN networks WDK , roadmap
- WLAN networks WDK , roadmap
- Native 802.11 WDK networking , roadmap
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Roadmap for Developing Native 802.11 Wireless LAN Drivers


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

To create a Native 802.11 Wireless LAN driver package, follow these steps:

-   Step 1: Learn about Windows architecture and drivers.

    You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and let you streamline your development process. For more information about driver fundamentals, see [Concepts for all driver developers](https://msdn.microsoft.com/library/windows/hardware/ff554731).

-   Step 2: Learn about the Network Driver Interface Specification (NDIS).

    Your Native 802.11 Wireless LAN driver package will include a *miniport driver* that uses Network Driver Interface Specification (NDIS) interfaces. For more information about NDIS and NDIS miniport drivers, see the following topics:

    [Windows Network Architecture and the OSI Model](windows-network-architecture-and-the-osi-model.md)

    [NDIS Miniport Drivers](ndis-miniport-drivers.md)

    [Writing NDIS Miniport Drivers](writing-ndis-miniport-drivers.md)

    [Network Driver Programming Considerations](network-driver-programming-considerations.md)

-   Step 3: Determine additional Windows driver design decisions.

    For information about how to make additional Windows design decisions, see [Creating Reliable Kernel-Mode Drivers](https://msdn.microsoft.com/library/windows/hardware/ff542904), [Programming Issues for 64-Bit Drivers](https://msdn.microsoft.com/library/windows/hardware/ff559923), and [Creating International INF Files](https://msdn.microsoft.com/library/windows/hardware/ff540208).

-   Step 4: Learn about the Windows driver build, test, and debug processes and tools.

    Building a driver differs from building a user-mode application. For information about Windows driver build, debug, and test processes, driver signing, and [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613) testing, see [Building, Debugging, and Testing Drivers](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment). For information about building, testing, verifying, and debugging tools, see [Driver Development Tools](https://msdn.microsoft.com/library/windows/hardware/ff545440).

-   Step 5: Learn about Native 802.11 Wireless LAN.

    For information about how to implement Native 802.11 Wireless LAN, see [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560689).

-   Step 6: Review the [Native Wi-Fi driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617934) available in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507 ) repository on GitHub.

-   Step 7: Develop, build, test, and debug your miniport driver and DLLs.

    You will have to provide a Native 802.11 miniport driver and an IHV Extensions dynamic link library (DLL). Optionally you can also provide an IHV User Interface (UI) Extensions DLL. The DLLs are compiled from user-mode code. For information about these Native 802.11 modules and guidelines for developing them for your device, see the following topics:

    [Native 802.11 Miniport Drivers](https://msdn.microsoft.com/library/windows/hardware/ff560648)

    [Overview of IHV Extensibility](overview-of-ihv-extensibility.md)

    [Native 802.11 IHV Extensions DLL](https://msdn.microsoft.com/library/windows/hardware/ff560614)

    [Native 802.11 IHV UI Extensions DLL](https://msdn.microsoft.com/library/windows/hardware/ff560635)

-   Step 8: Create a driver package for your driver.

    For information about how to install drivers, see [Providing a Driver Package](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_package). For information about how to install a Native 802.11 IHV Extensions DLL and an IHV UI Extensions DLL, see [Installing Native 802.11 IHV Extensions](installing-native-802-11-ihv-extensions.md).

-   Step 9: Sign and distribute your driver.

    The final step is to sign (optional) and distribute the driver. If your driver meets the quality standards that are defined for the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613), you can distribute it through the Microsoft Windows Update program. For more information about how to distribute a driver, see [Distributing a Driver](https://msdn.microsoft.com/windows-drivers/develop/distributing_a_driver_package_win8).

These are the basic steps. Additional steps might be necessary based on the needs of your individual driver.

 

 





