---
title: Road Map for the Windows Display Driver Model (WDDM)
description: Road map for Developing Drivers for the Windows Display Driver Model (WDDM)
ms.date: 04/24/2025
ms.topic: concept-article
---

# WDDM development road map

:::image type="content" source="images/wdkroadmap-th.png" alt-text="Illustration of a roadmap with the acronym 'WDK' superimposed on a highway.":::

The Windows Display Driver Model (WDDM) requires that a graphics hardware vendor supply a paired user-mode display driver (UMD) and kernel-mode display miniport driver (KMD).

The following steps are a starting point:

- Step 1: Learn about Windows architecture and drivers.

  It's important to understand the fundamentals of how drivers work in Windows operating systems. Knowing the fundamentals helps you make appropriate design decisions and allows you to streamline your development process. See [Getting started with drivers on Windows](../gettingstarted/index.md).

- Step 2: Learn implementation fundamentals of WDDM display drivers by reading through this WDDM documentation.

  Graphics drivers are complex. The WDDM documentation covers a considerable amount of material about concepts such as:

  - [Driver initialization](initializing-display-miniport-and-user-mode-display-drivers.md)
  - [WDDM operation flow](windows-vista-and-later-display-driver-model-operation-flow.md)
  - [Threading and synchronization](windows-vista-display-driver-threading-and-synchronization-model.md)
  - [Memory management and GPU scheduling](video-memory-management-and-gpu-scheduling.md)

  WDDM versions are tied to Windows releases. For example, WDDM 1.0 was introduced with Windows Vista, WDDM 2.0 was introduced with Windows 10, and WDDM 3.0 was introduced with Windows 11. Most features introduced in each WDDM version are documented under sections titled "WDDM *x.y* features"; for example, WDDM 3.2 features.

- Step 3: Review the [display driver samples](display-samples.md).

- Step 4: Learn about the Windows driver build, test, and debug processes and tools.

  Building a driver isn't the same as building a user-mode application. See [Developing, Testing, and Deploying Drivers](../develop/get-started-developing-windows-drivers.md) for information about Windows driver build, debug, and test processes, driver signing, and driver verification. See [Driver Development Tools](../devtest/index.md) for information about building, testing, verifying, and debugging tools.

- Step 5: Make graphics display driver design decisions.

  For information about making design decisions, see [Implementation Tips and Requirements for WDDM](implementation-tips-and-requirements-for-the-windows-vista-display-dri.md) and [Tasks in WDDM](tasks-in-the-windows-vista-display-driver-model.md).

- Step 6: Develop, build, test, and debug your display drivers.

  - For introductory information about how to develop display drivers for your graphics adapter, see [Initializing Display Miniport and User-Mode Display Drivers](initializing-display-miniport-and-user-mode-display-drivers.md) and [WDDM Operation Flow](windows-vista-and-later-display-driver-model-operation-flow.md).
  - For information about iterative building, testing, and debugging, see [Developing, Testing, and Deploying Drivers](/windows-hardware/drivers/develop).
  - For debugging tips that are specific to display drivers, see [Debugging tips for WDDM drivers](debugging-tips-for-wddm-drivers.md).

- Step 7: [Create a driver package](../develop/creating-a-driver-package.md) for your display drivers.

  For information about how to install display drivers for a graphics adapter, see [Installation Requirements for Display Miniport and User-Mode Display Drivers](installing-display-miniport-and-user-mode-display-drivers.md).

- Step 8: Sign and distribute your display drivers.

  The final step is to [sign](../develop/signing-a-driver.md) and [distribute](../develop/distributing-a-driver-package.md) the driver. If your driver meets the quality standards defined in the [Windows Hardware Lab Kit](/windows-hardware/test/hlk/) (WHLK), you can distribute it through the Windows Update program.

These steps are a starting point. Other steps are likely necessary based on the needs of your individual driver.
