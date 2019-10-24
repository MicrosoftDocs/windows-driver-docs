---
title: Enabling and Disabling Interrupts
description: Enabling and Disabling Interrupts
ms.assetid: 52846461-4F08-4546-93F5-F2469C6E3AD8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling and Disabling Interrupts


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

If your driver handles device interrupts, it must provide [*OnInterruptEnable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_enable) and [*OnInterruptDisable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_disable) callback functions that enable and disable the interrupts. These callback functions must do whatever is necessary to enable and disable a device's interrupt mechanism.

If your driver must perform additional operations that are related to enabling or disabling interrupts, the driver can also provide [**IPnpCallbackHardwareInterrupt::OnD0EntryPostInterruptsEnabled**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardwareinterrupt-ond0entrypostinterruptsenabled) and [**IPnpCallbackHardwareInterrupt::OnD0ExitPreInterruptsDisabled**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardwareinterrupt-ond0exitpreinterruptsdisabled) callback functions.

The framework calls the driver's [*OnInterruptEnable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_enable) and [**IPnpCallbackHardwareInterrupt::OnD0EntryPostInterruptsEnabled**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardwareinterrupt-ond0entrypostinterruptsenabled) callback functions each time the device enters its working (D0) state, after the framework has called the driver's [**OnD0Entry**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallback-ond0entry) callback function. The framework calls the driver's [**IPnpCallbackHardwareInterrupt::OnD0ExitPreInterruptsDisabled**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardwareinterrupt-ond0exitpreinterruptsdisabled) and [*OnInterruptDisable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_disable) callback functions each time the device leaves its working state, before the framework calls the driver's [**OnD0Exit**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallback-ond0exit) callback function. For more information about when the framework calls a driver's callback functions, see [PnP and Power Management in UMDF-based Drivers](pnp-and-power-management-in-umdf-drivers.md).

You must not assume that a device will use the same interrupt resources each time the framework calls your driver's [*OnInterruptEnable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_enable) callback function. Sometimes the PnP manager redistributes system resources, and it might assign new interrupt resources to your device.

The driver can call [**IWDFInterrupt::GetInfo**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-getinfo) to determine a device's interrupt resources. The driver can call [**IWDFInterrupt::GetDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-getdevice) to determine the device that an interrupt object belongs to.

To enable and disable interrupts directly, the driver can call the interrupt object's [**IWDFInterrupt::Enable**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-enable) and [**IWDFInterrupt::Disable**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfinterrupt-disable) methods, which call the driver's [*OnInterruptEnable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_enable) and [*OnInterruptDisable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_disable) event callback functions. However, most drivers should just allow the framework to call the *OnInterruptEnable* and *OnInterruptDisable* callback functions at the proper times.

 

 





