---
title: Power Management for Windows Drivers
description: Kernel-mode drivers should manage their hardware devices so that they are turned on and available for use when needed, but operate in a low-power mode and generate no unnecessary system activity when they are not being used.
ms.assetid: ed422428-8a87-4a2d-830d-e156ef949b13
keywords: ["power management WDK kernel", "kernel-mode drivers WDK , power management", "energy WDK power management", "startup power management WDK kernel", "shutdown power management WDK kernel", "device power management WDK kernel", "restoring power WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Power Management for Windows Drivers


Kernel-mode drivers should manage their hardware devices so that they are turned on and available for use when needed, but operate in a low-power mode and generate no unnecessary system activity when they are not being used. The [*power manager*](power-manager.md) is the Windows kernel component that is responsible for coordinating the power states of the devices in the hardware platform.




The power manager instructs drivers when to prepare their devices to enter a low-power mode, and drivers receive notification from the power manager when their devices are turned back on. Drivers are responsible for reporting their power capabilities to the power manager. Drivers have the option of detecting when their devices are idle (and can be switched to a low-power mode) or relying on the power manager for such detection.

## In this section


-   [Introduction to Power Management](introduction-to-power-management.md)
-   [Kernel-Mode Power Management Components](kernel-mode-power-management-components.md)
-   [Power Management Responsibilities for Drivers](power-management-responsibilities-for-drivers.md)
-   [Rules for Handling Power IRPs](rules-for-handling-power-irps.md)
-   [Managing Power for Individual Devices](managing-power-for-individual-devices.md)
-   [Handling System Power State Requests](handling-system-power-state-requests.md)
-   [Overview of the Power Management Framework](overview-of-the-power-management-framework.md)
-   [Platform Extension Plug-ins (PEPs)](platform-extension-plug-ins--peps-.md)
-   [Supporting Devices that Have Wake-Up Capabilities](supporting-devices-that-have-wake-up-capabilities.md)
-   [Improving System Startup Performance](improving-system-startup-performance.md)
-   [Device-Level Thermal Management](device-level-thermal-management.md)

 

 




