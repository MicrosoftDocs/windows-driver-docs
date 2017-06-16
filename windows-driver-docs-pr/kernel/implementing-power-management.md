---
title: Power Management for Windows Drivers
author: windows-driver-content
description: Kernel-mode drivers should manage their hardware devices so that they are turned on and available for use when needed, but operate in a low-power mode and generate no unnecessary system activity when they are not being used.
ms.assetid: ed422428-8a87-4a2d-830d-e156ef949b13
keywords: ["power management WDK kernel", "kernel-mode drivers WDK , power management", "energy WDK power management", "startup power management WDK kernel", "shutdown power management WDK kernel", "device power management WDK kernel", "restoring power WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Power Management for Windows Drivers


Kernel-mode drivers should manage their hardware devices so that they are turned on and available for use when needed, but operate in a low-power mode and generate no unnecessary system activity when they are not being used. The [*power manager*](power-manager.md) is the Windows kernel component that is responsible for coordinating the power states of the devices in the hardware platform.

## <a href="" id="ddk-power-management-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Power%20Management%20for%20Windows%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


