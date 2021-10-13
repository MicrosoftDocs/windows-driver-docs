---
title: Power management for HID over SPI
description: Describes power management for devices that support HID over SPI.
ms.date: 06/22/2021
ms.localizationpriority: medium
---

# HID over SPI power management

This article identifies the details around host and device power management over SPI.

## Device initiated power optimizations

The device is responsible for optimizing its power utilization in the absence of any power settings from the host. This enables the device to enter its lowest power state without host intervention, while ensuring that the device is able to continue to communicate with the host in a timely manner.

To correctly comply with device initiated power optimizations:

- The device is responsible for preserving its state across its low power modes.
- All device power optimizations must be transparent to the host and end users.
- The device must respond to all requests from host in a timely manner. The device is responsible for bringing itself to higher power modes on user or system interactions in a timely manner.
- The device must notify the host on any input report changes in a lossless manner. No events should be lost, or deleted by the device.
- The power states described in [Host initiated power optimizations](#host-initiated-power-optimizations) don't apply to device initiated power optimizations.

Scenarios where device initiated power optimizations are generally deployed include the following:

1. The device is idle for a short interval of time. The device determines that it is idle and puts itself in to its lowest power state where it reduces its internal sensing frequency until motion is re-initiated. As soon as motion starts, data is immediately sent to the host.
1. The device reduces its sensing frequency. The device reduces the frequency at which it scans for data.

## Host initiated power optimizations

The host is responsible for optimizing the power of the overall system and the device. This method of power optimization is to be used when the host wishes to provide power optimization notifications to devices.

The following power states are defined for host initiated power optimizations and are not to be confused with vendor specific device initiated power optimizations states.

- ON
- SLEEP (The device may wake the system)
- OFF (the device cannot wake the system, power may be removed from the device)

In the ON state, the device behaves normally and may use device initiated power optimizations to reduce power consumption. The device is responsible for being in the ON state when HIDSPI communications are initiated, after a host initiated reset.

The host instructs the device to enter a low power state from the ON state by issuing the defined `Set Power` command. The host will choose to do this based on the operating system power policy for the device.

The host places the device into the SLEEP state when the platform power policy allows the device to wake either itself or the system. Support for SLEEP is optional and is indicated to the host operating system through ACPI, or in a manner appropriate to the bus for a platform specific controller. Upon receiving a `SET POWER  SLEEP` command, the device must immediately enter a lower-power state, where it will wait for user interaction and must not assert interrupts, except to initiate a wake. If the device detects input, it asserts an interrupt, and waits for the host to send a `SET POWER  ON` command. The device responds to the `SET POWER  ON` command and resumes sending input to the host.

The host places the device into the OFF state when communication with the device is no longer required. ACPI (or platform specific controller) must be configured to provide a cold OFF state. Upon receiving a `SET POWER  OFF` command, the device immediately enters its lowest-power state and stops communication with the host. To bring the device to the ON state, the host initiates a reset, at which point the initialization process begins.

For ACPI enumerated devices, the following power states are required to be implemented:

- D0 – Normal working state
- D2 – Used for the SLEEP state if supported. The device should indicate wake support from this power state.
- D3 – This should be used for the OFF state. The device should not indicate wake support from this power state.

For platform specific controllers, alternate D-state mappings may be used in order to account for the power requirements of the controller hardware.

The platform level D-state mappings are not visible or communicated to the device.

## Host and device power state responsibilities

The table below identifies the properties a device and a host must follow:

| Power state | Host responsibility | Device responsibility |
|---|---|---|
| **ON** | - Address interrupts and IO issues to the device as necessary. | - Being in the ON power state after a reset </br>- Process, but not provide a response to a `SET POWER SLEEP` or `SET POWER OFF` command from the host. |
| **SLEEP** | - Instructing the device to enter the SLEEP state. </br>- Setting the device into the ON state if the device alerts via the interrupt line. </br>- If a host needs to communicate with the device it issues a `SET POWER` command (to ON) before any other command. | - De-assert the interrupt line if asserted, before host initiated power optimizations. </br>- Send an interrupt to the host to request servicing. The device must then not reassert the interrupt until the host has sent a `SET POWER` command to enter the ON state, to which the device has responded, at which point the device should assert the interrupt again to notify the host of any pending input report. </br>- Reduce the power draw to an absolute minimum to maintain state and optionally support remote wake. </br>- Respond to a `SET POWER ON` commands from the host.
| **OFF** | - Instructing the device to enter the OFF state. </br>- Direct the platform to put the device into the OFF state. </br>- Put the device into this state when it should not be capable of waking itself. | - De-assert the interrupt line if asserted, before host initiated power optimizations. </br>- The device will not be able to initiate wake or provide interrupts in this state. </br>- Reduce the power draw to an absolute minimum. It is not required to maintain state. </br>- Treat an OFF -> ON transition as it would a regular power up. |

## See also

[Device Power States](../kernel/device-power-states.md)
