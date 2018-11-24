---
title: Enabling and Disabling Interrupts
description: Enabling and Disabling Interrupts
ms.assetid: 432907e7-05a3-4a99-a291-33bd1eefa94c
keywords:
- hardware interrupts WDK KMDF , enabling
- interrupts WDK KMDF , enabling
- hardware interrupts WDK KMDF , disabling
- interrupts WDK KMDF , disabling
- status information WDK KMDF , enabling interrupts
- status information WDK KMDF , disabling interrupts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling and Disabling Interrupts


If your driver handles device interrupts, it must provide [*EvtInterruptEnable*](https://msdn.microsoft.com/library/windows/hardware/ff541730) and [*EvtInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541714) callback functions that enable and disable the interrupts. Typically, these callback functions run at the device's DIRQL and must do whatever is necessary to enable and disable a device's interrupt mechanism. For [passive-level interrupts](supporting-passive-level-interrupts.md), these callback functions run at IRQL = PASSIVE_LEVEL while holding the passive-level interrupt lock.

If your driver must perform additional operations that are related to enabling or disabling interrupts, and if these additional operations cannot be performed at IRQL = DIRQL, the driver can also provide [*EvtDeviceD0EntryPostInterruptsEnabled*](https://msdn.microsoft.com/library/windows/hardware/ff540853) and [*EvtDeviceD0ExitPreInterruptsDisabled*](https://msdn.microsoft.com/library/windows/hardware/ff540856) callback functions. These two callback functions run at IRQL = PASSIVE\_LEVEL with no interrupt lock held, and can call framework object methods that are unavailable at IRQL = DIRQL.

The framework calls the driver's [*EvtInterruptEnable*](https://msdn.microsoft.com/library/windows/hardware/ff541730) and [*EvtDeviceD0EntryPostInterruptsEnabled*](https://msdn.microsoft.com/library/windows/hardware/ff540853) callback functions each time the device enters its working (D0) state, after the framework has called the driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function.

The framework calls the driver's [*EvtDeviceD0ExitPreInterruptsDisabled*](https://msdn.microsoft.com/library/windows/hardware/ff540856) and [*EvtInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541714) callback functions each time the device leaves its working state, before the framework calls the driver's [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback function. For more information about when the framework calls a driver's callback functions, see [PnP and Power Management Scenarios](pnp-and-power-management-scenarios.md).

You must not assume that a device will use the same interrupt resources each time the framework calls your driver's [*EvtInterruptEnable*](https://msdn.microsoft.com/library/windows/hardware/ff541730) callback function. Sometimes the PnP manager [redistributes system resources](the-pnp-manager-redistributes-system-resources.md), and it might assign new interrupt resources to your device.

The driver can call [**WdfInterruptGetInfo**](https://msdn.microsoft.com/library/windows/hardware/ff547367) to determine a device's interrupt resources. The driver can call [**WdfInterruptGetDevice**](https://msdn.microsoft.com/library/windows/hardware/ff547358) to determine the device that an interrupt object belongs to. (A few drivers might call [**WdfInterruptWdmGetInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff547393).)

To enable and disable interrupts directly, the driver can call the interrupt object's [**WdfInterruptEnable**](https://msdn.microsoft.com/library/windows/hardware/ff547354) and [**WdfInterruptDisable**](https://msdn.microsoft.com/library/windows/hardware/ff547351) methods, which call the driver's [*EvtInterruptEnable*](https://msdn.microsoft.com/library/windows/hardware/ff541730) and [*EvtInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541714) event callback functions. However, most drivers should just allow the framework to call the *EvtInterruptEnable* and *EvtInterruptDisable* callback functions at the proper times.

 

 





