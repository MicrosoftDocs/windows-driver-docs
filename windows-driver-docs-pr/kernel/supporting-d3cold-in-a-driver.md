---
title: Supporting D3cold in a Driver
description: Starting with Windows 8, the D3 (off) device power state is divided into two distinct substates, D3hot and D3cold.
ms.date: 07/22/2021
---

# Supporting D3cold in a Driver

Starting with Windows 8, the D3 (off) device power state is divided into two distinct substates, D3hot and D3cold. D3 is the lowest-powered device power state, and D3cold is the lowest-powered substate of D3. Moving idle devices to the D3cold substate can reduce power consumption and extend the time that a mobile hardware platform can run on a battery charge.

In D3hot, the device is mostly turned off. However, the device is not disconnected from its main power source, and the parent bus controller can detect the presence of the device on the bus. In D3cold, the main power source is removed from the device, and the bus controller cannot detect the presence of the device. For more information, see the descriptions of D3hot and D3cold in [Device Low-Power States](device-sleeping-states.md).

In earlier versions of Windows, the D3 device power state is implicitly divided into D3hot and D3cold substates, but a device cannot enter D3cold unless the computer is preparing to exit the S0 system power state and enter one of the sleeping states, S1 through S4. The low-power Dx states that a device can enter when the computer is to remain in S0 are limited to D1 through D3hot.

Windows 8 is the first version of Windows to support device-power-state transitions to the D3cold substate when the computer is in S0 and is not preparing to enter a sleeping state. A device that supports D3cold in this way helps to save power in the following ways:

- The device consumes less power in D3cold than in any other low-power Dx state.
- If this device shares a bus with other devices, and all these devices support D3cold, then after all the devices on the bus enter D3cold, the bus controller can enter a low-power Dx state.
- If this device shares a power source with other devices, and all these devices support D3cold, then when the last of these devices enters D3hot, the power source can be removed, at which time these devices all enter D3cold in unison.

Conversely, a device that cannot idle in D3cold can prevent other devices from entering D3cold or other low-power Dx states.

The following topics contain more information about supporting D3cold in a device driver.

## In this section

| Topic | Description |
|--|--|
| [Enabling Transitions to D3cold](enabling-transitions-to-d3cold.md) | All versions of Windows enable a device to be in D3cold while the computer is sleeping (in one of the system low-power states, S1 through S4). Before the computer exits S0, the function drivers, bus drivers, and filter drivers work together to move the device to D3hot. When the computer enters the low-power Sx state, this transition has the side effect of moving the device from D3hot to D3cold. |
| [D3cold Capabilities of a Device](d3cold-capabilities-of-a-device.md) | Before the driver that is the power policy owner (PPO) for a device enables the device to enter D3cold (when the computer is to remain in S0), the driver must verify that the device will be responsive and continue to operate correctly after the device enters D3cold. |
| [Using the GUID_D3COLD_SUPPORT_INTERFACE Driver Interface](using-guid-d3cold-support-interface.md) | Starting with Windows 8, drivers can call the routines in the [D3COLD_SUPPORT_INTERFACE](/windows-hardware/drivers/ddi/wdm/ns-wdm-_d3cold_support_interface) interface to determine the D3cold capabilities of devices and to enable these devices to use D3cold. The two primary routines in this interface are [*SetD3ColdSupport*](/windows-hardware/drivers/ddi/wdm/nc-wdm-set_d3cold_support) and [*GetIdleWakeInfo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-get_idle_wake_info). |
| [Surprise Wake-Up](surprise-wake-up.md) | A surprise wake-up is an unexpected transition to D0. After a device enters D3cold, it might experience a surprise wake-up as a side effect when the driver for another device on the same power rail requests a transition from D3cold to D0. The driver for the first device must receive notification of the surprise wake-up to prevent the device from remaining in an uninitialized D0 state. |
