---
title: Roadmap for Developing Drivers for the Windows Display Driver Model (WDDM)
description: Roadmap for Developing Drivers for the Windows Display Driver Model (WDDM)
ms.assetid: 4f7ea2f4-ca2f-4b1d-97be-fb22e81c8080
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Roadmap for Developing Drivers for the Windows Display Driver Model (WDDM)


![wdk roadmap for developing wddm display drivers](images/wdkroadmap-th.png)The Windows Display Driver Model (WDDM) requires that a graphics hardware vendor supply a paired user-mode display driver and kernel-mode display driver (or *display miniport driver*).

To create these display drivers, perform the following steps:

-   Step 1: Learn about Windows architecture and drivers.

    You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and allow you to streamline your development process. See [Concepts for all driver developers](https://msdn.microsoft.com/library/windows/hardware/ff554731).

-   Step 2: Learn the fundamentals of WDDM display drivers.

    To learn the fundamentals, see [Introduction to the Windows Display Driver Model (WDDM))](introduction-to-the-windows-vista-and-later-display-driver-model.md), [Video Memory Management and GPU Scheduling](video-memory-management-and-gpu-scheduling.md), and [Threading and Synchronization Model of Display Miniport Driver](threading-and-synchronization-model-of-display-miniport-driver.md).

    For a description of the major new features in recent Windows releases, see:

    -   [What's new for Windows 8.1 display drivers (WDDM 1.3)](what-s-new-for-windows-8-1-display-drivers--wddm-1-3-.md)
    -   [What's new for Windows 8 display drivers (WDDM 1.2)](what-s-new-for-windows-8-display-drivers.md)
    -   [Windows Display Driver Model Enhancements (WDDM 1.2)](http://go.microsoft.com/fwlink/p/?LinkId=226814)
-   Step 3: Learn about user-mode display drivers and issues with display miniport drivers from the [User-Mode Display Drivers](user-mode-display-drivers.md) and [Multiple Monitors and Video Present Networks](multiple-monitors-and-video-present-networks.md) sections.

-   Step 4: Learn about the Windows driver build, test, and debug processes and tools.

    Building a driver is not the same as building a user-mode application. See [Developing, Testing, and Deploying Drivers](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment) for information about Windows driver build, debug, and test processes, driver signing, and driver verification. See [Driver Development Tools](https://msdn.microsoft.com/library/windows/hardware/ff545440) for information about building, testing, verifying, and debugging tools.

-   Step 5: Make additional display driver design decisions.

    For information about making design decisions, see [Implementation Tips and Requirements for the Windows Display Driver Model (WDDM)](implementation-tips-and-requirements-for-the-windows-vista-display-dri.md) and [Tasks in the Windows Display Driver Model (WDDM)](tasks-in-the-windows-vista-display-driver-model.md).

-   Step 6: Access and review the display driver samples in the WDK at [Display Samples](display-samples.md).

-   Step 7: Develop, build, test, and debug your display drivers.

    For information about how to develop display drivers for your graphics adapter, see [Initializing Display Miniport and User-Mode Display Drivers](initializing-display-miniport-and-user-mode-display-drivers.md) and [Windows Display Driver Model (WDDM) Operation Flow](windows-vista-and-later-display-driver-model-operation-flow.md). See [Developing, Testing, and Deploying Drivers](https://msdn.microsoft.com/windows-drivers/develop/visual_studio_driver_development_environment) for information about iterative building, testing, and debugging. For debugging tips that are specific to display drivers, see [Debugging Tips for the Windows Display Driver Model (WDDM)](debugging-tips-for-the-windows-vista-display-driver-model.md). This process will help ensure that you build a driver that works.

-   Step 8: Create a driver package for your display drivers.

    For more information, see [Distributing a driver package](https://msdn.microsoft.com/windows-drivers/develop/distributing_a_driver_package_win8). For information about how to install display drivers for a graphics adapter, see [Installation Requirements for Display Miniport and User-Mode Display Drivers](installing-display-miniport-and-user-mode-display-drivers.md).

-   Step 9: Sign and distribute your display drivers.

    The final step is to sign (optional) and distribute the driver. If your driver meets the quality standards that are defined in the [Windows Hardware Certification Kit](http://go.microsoft.com/fwlink/p/?linkid=248337) (formerly Windows Logo Kit or WLK), you can distribute it through the Microsoft Windows Update program. For more information, see [Distributing a driver package](https://msdn.microsoft.com/windows-drivers/develop/distributing_a_driver_package_win8).

These are the basic steps. Additional steps might be necessary based on the needs of your individual driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Roadmap%20for%20Developing%20Drivers%20for%20the%20Windows%20Display%20Driver%20Model%20%28WDDM%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




