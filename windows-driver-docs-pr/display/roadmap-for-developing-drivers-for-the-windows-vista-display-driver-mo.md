---
title: Road map for the Windows Display Driver Model (WDDM)
description: Road map for Developing Drivers for the Windows Display Driver Model (WDDM)
ms.date: 03/20/2023
---

# WDDM development road map

:::image type="content" source="images/wdkroadmap-th.png" alt-text="Illustration of a roadmap with the acronym 'WDK' superimposed on a highway.":::

The Windows Display Driver Model (WDDM) requires that a graphics hardware vendor supply a paired user-mode display driver (UMD) and kernel-mode display driver (KMD; also referred to as a display miniport driver).

To create these display drivers, perform the following steps:

- Step 1: Learn about Windows architecture and drivers.

  You must understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals will help you make appropriate design decisions and allow you to streamline your development process. See [Concepts for all driver developers](../gettingstarted/concepts-and-knowledge-for-all-driver-developers.md).

- Step 2: Learn the fundamentals of WDDM display drivers by reading this design guide.

  For a description of the major new features in recent Windows releases, start with [What's new for Windows 11 display and graphics drivers](./what-s-new-for-windows-11-display-and-graphics-drivers.md)

- Step 3: Learn about UMDs and issues with KMDs from the [User-Mode Display Drivers](user-mode-display-drivers.md) and [Multiple Monitors and Video Present Networks](multiple-monitors-and-video-present-networks.md) sections.

- Step 4: Learn about the Windows driver build, test, and debug processes and tools.

  Building a driver is not the same as building a user-mode application. See [Developing, Testing, and Deploying Drivers](../develop/getting-started-with-windows-drivers.md) for information about Windows driver build, debug, and test processes, driver signing, and driver verification. See [Driver Development Tools](../devtest/index.md) for information about building, testing, verifying, and debugging tools.

- Step 5: Make additional graphics display driver design decisions.

  For information about making design decisions, see [Implementation Tips and Requirements for WDDM](implementation-tips-and-requirements-for-the-windows-vista-display-dri.md) and [Tasks in WDDM](tasks-in-the-windows-vista-display-driver-model.md).

- Step 6: Access and review the [display driver samples](display-samples.md).

- Step 7: Develop, build, test, and debug your display drivers.

  For information about how to develop display drivers for your graphics adapter, see [Initializing Display Miniport and User-Mode Display Drivers](initializing-display-miniport-and-user-mode-display-drivers.md) and [WDDM Operation Flow](windows-vista-and-later-display-driver-model-operation-flow.md). See [Developing, Testing, and Deploying Drivers](/windows-hardware/drivers) for information about iterative building, testing, and debugging. For debugging tips that are specific to display drivers, see [Debugging tips for WDDM drivers](debugging-tips-for-wddm-drivers.md). This process will help ensure that you build a driver that works.

- Step 8: Create a driver package for your display drivers.

  For more information, see [Distributing a driver package](../develop/distributing-a-driver-package-win8.md). For information about how to install display drivers for a graphics adapter, see [Installation Requirements for Display Miniport and User-Mode Display Drivers](installing-display-miniport-and-user-mode-display-drivers.md).

- Step 9: Sign and distribute your display drivers.

  The final step is to sign (optional) and distribute the driver. If your driver meets the quality standards that are defined in the [Windows Hardware Lab Kit](/windows-hardware/test/hlk/) (formerly Windows Logo Kit or WLK), you can distribute it through the Microsoft Windows Update program. For more information, see [Distributing a driver package](../develop/distributing-a-driver-package-win8.md).

These are the basic steps. Additional steps might be necessary based on the needs of your individual driver.
