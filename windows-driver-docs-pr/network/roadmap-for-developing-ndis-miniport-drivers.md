---
title: Roadmap for Developing NDIS Miniport Drivers
description: Roadmap for Developing NDIS Miniport Drivers
ms.assetid: 7cb56c08-3578-49d7-a0aa-a89dc6b139ca
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Roadmap for Developing NDIS Miniport Drivers


To create a Network Driver Interface Specification (NDIS) miniport driver package, follow these steps:

- Step 1: Learn about Windows architecture and drivers.

  You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and let you streamline your development process. For more information about driver fundamentals, see [Concepts for all driver developers](https://msdn.microsoft.com/library/windows/hardware/ff554731).

- Step 2: Learn about NDIS.

  For general information about NDIS and NDIS drivers, see the following topics:

  [Windows Network Architecture and the OSI Model](windows-network-architecture-and-the-osi-model.md)

  [Network Driver Programming Considerations](network-driver-programming-considerations.md)

  [Driver Stack Management](driver-stack-management.md)

  [NET\_BUFFER Architecture](net-buffer-architecture.md)

- Step 3: Determine additional Windows driver design decisions.

  For more information about how to make additional Windows design decisions, see [Creating Reliable Kernel-Mode Drivers](https://msdn.microsoft.com/library/windows/hardware/ff542904), [Programming Issues for 64-Bit Drivers](https://msdn.microsoft.com/library/windows/hardware/ff559923), and [Creating International INF Files](https://msdn.microsoft.com/library/windows/hardware/ff540208).

- Step 4: Learn about the Windows driver build, test, and debug processes and tools.

  Building a driver differs from building a user-mode application. For more information about Windows driver build, debug, and test processes, driver signing, and [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613) testing, see [Building, Debugging, and Testing Drivers](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment). For more information about building, testing, verifying, and debugging tools, see [Driver Development Tools](https://msdn.microsoft.com/library/windows/hardware/ff545440).

- Step 5: Read the miniport driver introduction topics.
  [Types of NDIS Miniport Drivers](types-of-ndis-miniport-drivers.md)
  [Network Interface Card Support](network-interface-card-support.md)
  [Important Features of Miniport Driver Code](important-features-of-miniport-driver-code.md)
  [Sample NDIS Miniport Drivers](sample-ndis-miniport-drivers.md)
- Step 6: Read the [writing miniport drivers section](writing-ndis-miniport-drivers.md).

  This section provides an overview of the primary miniport driver interfaces. These interfaces included functions that miniport drivers provide (*MiniportXxx* functions) and NDIS calls to initiate operations. NDIS provides **Ndis*Xxx*** functions that miniport drivers call to perform NDIS operations.

- Step 7: Review the [NDIS miniport driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617918) in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

- Step 8: (optional reading) Additional considerations for Miniport Drivers.

  Additional considerations include topics that expand on the primary interfaces that are described in the [writing miniport drivers section](writing-ndis-miniport-drivers.md).

  [Obtaining and Setting Miniport Driver Information and NDIS Support for WMI](obtaining-and-setting-miniport-driver-information-and-ndis-support-for.md)

  [NDIS MSI-X](ndis-msi-x.md)

  [NDIS Scatter/Gather DMA](ndis-scatter-gather-dma.md)

  [NDIS Power Management](ndis-power-management.md)

  [Plug and Play for NDIS Miniport Drivers](plug-and-play-for-ndis-miniport-drivers.md)

  [Reset, Halt, and Shutdown Functions](reset--halt--and-shutdown-functions.md)

  [Miniport Driver with a WDM Lower Interface](https://msdn.microsoft.com/library/windows/hardware/ff560532)

  [WAN Miniport Drivers](wan-miniport-drivers.md)

  [Scalable Networking](https://msdn.microsoft.com/library/windows/hardware/ff570735)

- Step 9: Develop (or port), build, test, and debug your NDIS driver.

  See the porting guides if you are porting an existing driver:

  -   [Porting NDIS 5.x Drivers to NDIS 6.0](porting-ndis-5-x-drivers-to-ndis-6-0.md)
  -   [Porting NDIS 6.x Drivers to NDIS 6.20](porting-ndis-6-x-drivers-to-ndis-6-20.md)
  -   [Porting NDIS 6.x Drivers to NDIS 6.30](porting-ndis-6-x-drivers-to-ndis-6-30.md)

  For more information about iterative building, testing, and debugging, see [Overview of Build, Debug, and Test Process](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment). This process will help ensure that you build a driver that works.

- Step 10: Create a driver package for your driver.

  For more information about how to install drivers, see [Providing a Driver Package](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_package). For more information about how to install an NDIS driver, see [Installing and Upgrading Network Components](installing-and-upgrading-network-components.md).

- Step 11: Sign and distribute your driver.

  The final step is to sign (optional) and distribute the driver. If your driver meets the quality standards that are defined for the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613), you can distribute it through the Microsoft Windows Update program. For more information about how to distribute a driver, see [Distributing a Driver](https://msdn.microsoft.com/windows-drivers/develop/distributing_a_driver_package_win8).

These are the basic steps. Additional steps might be necessary based on the needs of your individual driver.

 

 





