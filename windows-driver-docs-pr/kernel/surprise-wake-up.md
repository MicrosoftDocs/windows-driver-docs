---
title: Surprise Wake-Up
description: A surprise wake-up is an unexpected transition to D0.
ms.assetid: 07D3EC05-A1C9-40C5-90FC-E25B5A66B064
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Surprise Wake-Up


A surprise wake-up is an unexpected transition to D0. After a device enters D3cold, it might experience a surprise wake-up as a side effect when the driver for another device on the same power rail requests a transition from D3cold to D0. The driver for the first device must receive notification of the surprise wake-up to prevent the device from remaining in an uninitialized D0 state.

When a device moves from D3hot to D3cold, it probably does so because the power source that it shares with some number of other devices was turned off. Some time after these devices enter D3cold, the driver for one of the devices might request a transition to D0. In response to this request, the parent bus driver or ACPI filter driver turns on the power source, and all the devices that share the power source enter their default, power-on hardware states.

The only device driver that expects this power state change is the driver that requested the change. The drivers for the other devices must receive notification of this change so that they can properly initialize their devices to operate in D0. Only a driver that can receive this notification should enable its device to enter D3cold. Otherwise, the driver will not know when the device enters D0.

When a device is turned on, it enters a default, uninitialized hardware state. For example, the [PCI Express Base 3.0 Specification](http://www.pcisig.com/specifications/pciexpress/specifications/) defines a *D0 uninitialized* state that a device enters when it first receives power. The definition of this state is specific to PCI and PCI Express devices, but devices that connect to other buses are designed to enter similar hardware states when they are turned on.

In the case of a PCI or PCI Express device that implements multiple functions, these device functions probably share the same power rail. However, each function might have a separate driver and the drivers for these functions are unlikely to communicate directly with each other. When the driver for one of these functions requests a power state change from D3cold to D0, the drivers for the other functions do not expect this change. When these other functions receive power, their drivers must be notified so that they can configure the functions to operate correctly in D0.

A bus driver detects when power to a child device is being turned on. If this device's function driver did not request a transition to D0, the bus driver prompts the device driver to send itself a D0 power IRP (an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request with target state = **PowerDeviceD0**) to initialize the device to operate in D0. From this initialized D0 state, the device driver can then initiate the device's transition to D3hot. Device drivers can receive notifications of surprise transitions to D0 from bus drivers in the following ways:

-   Device drivers that directly or indirectly register themselves as clients of the [run-time power management framework](overview-of-the-power-management-framework.md) (PoFx) receive notification callbacks.
-   Drivers for devices that arm their devices for wake have their pending [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) requests completed by the bus drivers.

Starting with Windows 8, a device's function driver, acting as the power policy owner, can register itself as a client of PoFx. When the bus driver notifies PoFx that the device experienced a surprise transition to D0, PoFx helps the device to move to an initialized D0 state, and then to D3hot. First, PoFx calls the driver's [*DevicePowerRequiredCallback*](https://msdn.microsoft.com/library/windows/hardware/hh450949) routine to prompt the device driver to send a D0 power IRP down the device stack. Next, PoFx calls the driver's [*DevicePowerNotRequiredCallback*](https://msdn.microsoft.com/library/windows/hardware/hh450946) routine to notify the device driver that the device is not required to stay in the D0 state.

Starting with Kernel-Mode Driver Framework (KMDF) version 1.11, the KMDF driver for a single-component device can indirectly register itself with PoFx by calling the [**WdfDeviceWdmAssignPowerFrameworkSettings**](https://msdn.microsoft.com/library/windows/hardware/hh451097) method. In this call, the driver supplies pointers to callback routines that notify the driver of surprise transitions to D0. For more information, see [Supporting Functional Power States](https://msdn.microsoft.com/library/windows/hardware/hh451017).

A driver that does not register its device with PoFx can still be notified of a surprise transition to D0 if the device is armed for wake. When the bus drivers turn on the power to the device, they complete the driver's **IRP\_MN\_WAIT\_WAKE** request. In response, the driver initializes its device to operate in D0. The device is likely to be idle, in which case the driver, after some time, will move this device to D3hot.

A function driver that does not register with PoFx and that does not arm its device for wake receives no notification of a surprise transition from D3cold to D0. The device might spend large amounts of time in an uninitialized D0 state. In this state, all of the components in the device are typically turned on. To reduce power consumption by idle devices, drivers should enable entry to D3cold only if they can receive notifications of surprise transitions to D0.

 

 




