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


If your driver handles device interrupts, it must provide [*EvtInterruptEnable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable) and [*EvtInterruptDisable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable) callback functions that enable and disable the interrupts. Typically, these callback functions run at the device's DIRQL and must do whatever is necessary to enable and disable a device's interrupt mechanism. For [passive-level interrupts](supporting-passive-level-interrupts.md), these callback functions run at IRQL = PASSIVE_LEVEL while holding the passive-level interrupt lock.

If your driver must perform additional operations that are related to enabling or disabling interrupts, and if these additional operations cannot be performed at IRQL = DIRQL, the driver can also provide [*EvtDeviceD0EntryPostInterruptsEnabled*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry_post_interrupts_enabled) and [*EvtDeviceD0ExitPreInterruptsDisabled*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled) callback functions. These two callback functions run at IRQL = PASSIVE\_LEVEL with no interrupt lock held, and can call framework object methods that are unavailable at IRQL = DIRQL.

The framework calls the driver's [*EvtInterruptEnable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable) and [*EvtDeviceD0EntryPostInterruptsEnabled*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry_post_interrupts_enabled) callback functions each time the device enters its working (D0) state, after the framework has called the driver's [*EvtDeviceD0Entry*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback function.

The framework calls the driver's [*EvtDeviceD0ExitPreInterruptsDisabled*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled) and [*EvtInterruptDisable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable) callback functions each time the device leaves its working state, before the framework calls the driver's [*EvtDeviceD0Exit*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit) callback function. For more information about when the framework calls a driver's callback functions, see [PnP and Power Management Scenarios](pnp-and-power-management-scenarios.md).

You must not assume that a device will use the same interrupt resources each time the framework calls your driver's [*EvtInterruptEnable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable) callback function. Sometimes the PnP manager [redistributes system resources](the-pnp-manager-redistributes-system-resources.md), and it might assign new interrupt resources to your device.

The driver can call [**WdfInterruptGetInfo**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nf-wdfinterrupt-wdfinterruptgetinfo) to determine a device's interrupt resources. The driver can call [**WdfInterruptGetDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nf-wdfinterrupt-wdfinterruptgetdevice) to determine the device that an interrupt object belongs to. (A few drivers might call [**WdfInterruptWdmGetInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nf-wdfinterrupt-wdfinterruptwdmgetinterrupt).)

To enable and disable interrupts directly, the driver can call the interrupt object's [**WdfInterruptEnable**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nf-wdfinterrupt-wdfinterruptenable) and [**WdfInterruptDisable**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nf-wdfinterrupt-wdfinterruptdisable) methods, which call the driver's [*EvtInterruptEnable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable) and [*EvtInterruptDisable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable) event callback functions. However, most drivers should just allow the framework to call the *EvtInterruptEnable* and *EvtInterruptDisable* callback functions at the proper times.

 

 





