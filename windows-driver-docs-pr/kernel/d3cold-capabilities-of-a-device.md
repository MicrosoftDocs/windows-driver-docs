---
title: D3cold Capabilities of a Device
description: Before the driver that is the power policy owner (PPO) for a device enables the device to enter D3cold (when the computer is to remain in S0), the driver must verify that the device will be responsive and continue to operate correctly after the device enters D3cold.
ms.assetid: 5A6CB076-7D97-48EC-B2BF-3204CD093B3E
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# D3cold Capabilities of a Device


Before the driver that is the power policy owner (PPO) for a device enables the device to enter D3cold (when the computer is to remain in S0), the driver must verify that the device will be responsive and continue to operate correctly after the device enters D3cold.

For a Plug and Play (PnP) device, the operating system typically gets information about the D3cold capabilities of the device from the parent bus driver.

For example, if a device is attached to a PCI or PCI Express bus, the device's PCI configuration space contains a Power Management Register Block that indicates the capabilities of the device. Capability flags in this block specify the device power states from which the device can signal a power management event, or PME (the PCI term for a wake event). These states might include D3hot and D3cold. For more information about PCI power management, see the [PCI Bus Power Management Interface Specification](http://www.pcisig.com/specifications/conventional/pci_bus_power_management_interface/).

If a device must be able to signal a wake event from any low-power Dx state that it enters, the device should not enter D3cold unless the device, parent bus controller, and hardware platform support signaling a wake event from D3cold.

The KMDF driver for a device calls the [**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903) method to enable the device to idle in the lowest-powered device power state from which the device can signal a wake event. Starting with KMDF version 1.11, **WdfDeviceAssignS0IdleSettings** includes D3cold in the range of possible low-power Dx states. This method enables a device to idle in D3cold only if the device, the parent bus driver, and the ACPI system firmware support signaling wake events from D3cold.

The WDM driver for a device must decide which low-power Dx state to move the device to when the device is idle. (In contrast, **WdfDeviceAssignS0IdleSettings** automatically selects this Dx state so that the driver does not have to.) If the device must be able to signal a wake event from any low-power Dx state that it enters, the driver can call the [*GetIdleWakeInfo*](https://msdn.microsoft.com/library/windows/hardware/hh967712) routine to determine the lowest-powered device power state from which the device can signal a wake event. To get this information, *GetIdleWakeInfo* queries the underlying bus driver and ACPI system firmware. Based on the information from *GetIdleWakeInfo*, the driver can call the [*SetD3ColdSupport*](https://msdn.microsoft.com/library/windows/hardware/hh967716) routine to enable or disable the device's transitions to D3cold.

A device might not require the ability to signal a wake event from D3cold. The device might instead be required to make the transition from D3cold to D0 only in response to software-initiated actions. For example, the driver might need to wake the device if the driver receives an I/O request for the device. With few exceptions, the driver for such a device can enable the device to enter D3cold. A possible exception is a device that requires a large amount of time to make a transition from D3cold to D0. For example, a display device might contain a large amount of memory that needs to be saved before the device enters D3cold and restored after the device exits D3cold.

For more information about ACPI support for D3cold, see [Firmware Requirements for D3cold](https://msdn.microsoft.com/library/windows/hardware/dn605829).

 

 




