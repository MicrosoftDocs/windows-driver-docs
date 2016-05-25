---
title: Roadmap for Developing Storport Miniport Drivers
author: windows-driver-content
description: Roadmap for Developing Storport Miniport Drivers
ms.assetid: 43a8f1ee-b2d3-4f97-b7e5-d59790ca6754
---

# Roadmap for Developing Storport Miniport Drivers


![figure of a roadmap with the text "wdk" superimposed on a highway](images/wdkroadmap-th.png)To create a storport miniport driver, perform the following steps:

1.  **Learn about Windows architecture and drivers.**

    You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and allow you to streamline your development process. See [Concepts for all driver developers](https://msdn.microsoft.com/library/windows/hardware/ff554731).

2.  **Learn the fundamentals of storport miniport drivers.**

    To learn storport miniport driver fundamentals, see [Windows Storage Driver Architecture](storage-driver-architecture.md), [Capabilities Provided by Storport](capabilities-provided-by-storport.md), and [Storport's Interface with Storport Miniport Drivers](storport-s-interface-with-storport-miniport-drivers.md).

3.  **Determine additional storport miniport driver design decisions.**

    For information about how to make design decisions, see [Capabilities Provided by Storport](capabilities-provided-by-storport.md), [Storport's Interface with the Storage Class Driver](storport-s-interface-with-the-storage-class-driver.md), [Storage Virtual Miniport Drivers: When Are They Appropriate?](storage-virtual-miniport-drivers--when-are-they-appropriate-.md), and [Making SCSI Port Miniport Drivers Work with Storport](making-scsi-port-miniport-drivers-work-with-storport.md).

4.  **Learn about storport miniport drivers in Windows Vista and later operating systems.**

    See [History of Storport](history-of-storport.md) in the Windows Driver Kit (WDK).

5.  **Learn about the Windows driver build, test, and debug processes and tools.**

    Building a driver is not the same as building a user-mode application. See [Developing, Testing, and Deploying Drivers](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment) for information about Windows driver build, debug, and test processes, driver signing, and Windows Logo testing. See [Driver Development Tools](https://msdn.microsoft.com/library/windows/hardware/ff545440) for information about building, testing, verifying, and debugging tools.

6.  **Review storport miniport driver samples.**

    To access and review the storport miniport driver samples see the [MSDN Code Gallery](http://go.microsoft.com/fwlink/p/?LinkId=618052).

7.  **Develop, build, test, and debug your storport miniport driver.**

    See [Building a Driver](https://msdn.microsoft.com/windows-drivers/develop/building_a_driver), [Testing a Driver](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver), and [Debugging a Driver](https://msdn.microsoft.com/windows-drivers/develop/debugging_a_driver) for information about iterative building, testing, and debugging. This process will help ensure that you build a driver that works.

8.  **Create a driver package for your storport miniport driver.**

    For more information, see [Creating a Driver Package](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_package).

9.  **Sign and distribute your storport miniport** **driver.**

    The final step is to sign (optional) and distribute the driver. If your driver meets the quality standards that are defined for Windows Hardware Certification, you can distribute it through the Microsoft Windows Update program. For more information, see [Distributing a Driver Package](https://msdn.microsoft.com/windows-drivers/develop/distributing_a_driver_package_win8).

These are the basic steps. Additional steps might be necessary based on the needs of your individual driver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Roadmap%20for%20Developing%20Storport%20Miniport%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


