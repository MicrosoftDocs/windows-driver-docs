---
title: Device-Level Thermal Management
description: Starting with Windows 8, Windows supports device-level thermal management for kernel-mode device drivers.
ms.date: 07/21/2021
---

# Device-Level Thermal Management

Starting with Windows 8, Windows supports device-level thermal management for kernel-mode device drivers. Windows thermal management has these goals:

- Prevent devices in a hardware platform from overheating, which can cause them to operate incorrectly or unreliably.

- Avoid making user-accessible surfaces on a computer case too hot to comfortably touch or hold.

Similar to power management, thermal management must be implemented on a platform-wide basis by coordinating device-local thermal constraints in the context of global thermal conditions. By providing global coordination, the operating system can distribute cooling requirements across multiple devices in a way that minimizes interference with tasks that the user is performing. Thermal requirements can be balanced intelligently with other system requirements, such as power management and responsiveness to user actions.

In contrast, a device driver that tries to manage thermal levels for its device locally, in isolation from the other devices in the platform, is more likely to make poor decisions that result in inefficient power usage and an unresponsive user interface (UI).

To participate in global thermal management, a device driver implements a [GUID_THERMAL_COOLING_INTERFACE](global-thermal-mgmt.md) driver interface. During system startup, a system-supplied driver, Acpi.sys, queries the device drivers in the system to determine which of them support this interface. A driver can receive an [**IRP_MN_QUERY_INTERFACE**](./irp-mn-query-interface.md) request for this interface any time after the [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine for the driver's device is called. In response to this request, the driver for a device that has thermal management capabilities can supply a pointer to a [**THERMAL_COOLING_INTERFACE**](/previous-versions/hh698275(v=vs.85)) structure. This structure contains pointers to a set of callback routines that are implemented by the driver. To manage thermal levels in the device, the operating system calls these routines directly.

The two principal routines in this interface are [*ActiveCooling*](/previous-versions/hh698235(v=vs.85)) and [*PassiveCooling*](/previous-versions/hh698270(v=vs.85)). The driver's *ActiveCooling* routine engages or disengages active cooling in the device. For example, this routine might turn a fan on and off. The driver's *PassiveCooling* routine controls the degree to which the performance of the device must be throttled to maintain acceptable thermal levels. For example, this routine might be called to run the device at half speed to prevent it from overheating.

By default, before the first call to the *ActiveCooling* routine, active cooling is disengaged (for example, the fan is turned off). Before the first call to the *PassiveCooling* routine, the driver configures the device to run at full performance, with no cooling restrictions.

A driver can implement one or both of these routines, depending on the capabilities of the device hardware. For more information, see [Passive and Active Cooling Modes](passive-and-active-cooling-modes.md).
