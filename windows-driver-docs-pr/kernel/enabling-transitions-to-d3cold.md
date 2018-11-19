---
title: Enabling Transitions to D3cold
description: All versions of Windows enable a device to be in D3cold while the computer is sleeping (in one of the system low-power states, S1 through S4).
ms.assetid: C2C6166D-8269-4FCE-81A8-B350626052D4
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Enabling Transitions to D3cold


All versions of Windows enable a device to be in D3cold while the computer is sleeping (in one of the system low-power states, S1 through S4). Before the computer exits S0, the function drivers, bus drivers, and filter drivers work together to move the device to D3hot. When the computer enters the low-power Sx state, this transition has the side effect of moving the device from D3hot to D3cold.

Starting with Windows 8, a device can enter and exit D3cold while the computer remains in S0. The driver that is the power policy owner (PPO) for a device can enable and disable these transitions to D3cold. A driver should not enable its device to enter D3cold unless the device can, if required, wake from D3cold, and then resume normal operation after the transition to D0.

When a device enters D3, it initially enters the D3hot substate of D3. From D3hot, the device can enter either D0 or D3cold. In response to a wake event or I/O request, the device enters D0 from D3hot. Otherwise, the device might remain in D3hot, or it might move from D3hot to D3cold. For more information about these transitions, see the device power state [diagram](device-power-states.md#power-state-diagram) in [Device Power States](device-power-states.md).

The driver does not initiate the device's transition from D3hot to D3cold. Instead, this transition occurs when all the other devices that share a common power source with this device are in D3hot and are prepared to enter D3cold. When the last of these devices enters D3hot, the underlying bus drivers and system firmware remove the power source and the devices enter D3cold in unison.

The PPO driver for a device tells the operating system whether to enable the device's transition from D3hot to D3cold. The driver can supply this information in the INF file that installs the device, or the driver can call the [*SetD3ColdSupport*](https://msdn.microsoft.com/library/windows/hardware/hh967716) routine at run time to dynamically enable or disable the device's transitions to D3cold. For more information, see [Using the GUID\_D3COLD\_SUPPORT\_INTERFACE Driver Interface](using-guid-d3cold-support-interface.md).

By enabling a device to enter D3cold, a driver guarantees the following behavior:

-   The device can tolerate a transition from D3hot to D3cold when the computer is to remain in S0.
-   The device will work properly when it returns to D0 from D3cold.

A device that fails to meet either requirement might, after entering D3cold, be unavailable until the computer is restarted or enters a sleeping state. If the device must be able to signal a wake event from any low-power Dx state that it enters, entry to D3cold must not be enabled unless the driver is certain that the device's wake signal will work in D3cold.

Putting a device in D3cold doesn't necessarily mean that all sources of power to the device have been removed; it means only that the sources of power that allow communication to the device through the bus are gone. The device might still be able to draw enough power to signal a wake event to the processor. For example, an Ethernet network interface card (NIC) whose main power source is removed might draw power from the Ethernet cable.

Because D3cold is a state where the bus cannot be used to communicate with the device, a driver can't put its device into D3cold directly. Instead, the driver first calls the [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) routine to request a D3 power IRP (an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request with target state = **PowerDeviceD3**) to move the device from D0 to D3hot. After entering D3hot, the device may or may not move from D3hot to D3cold. The device enters D3cold only when power to the bus is removed, which occurs if the parent bus driver turns off the bus or if the system firmware turns off power to a section of the hardware platform.

 

 




