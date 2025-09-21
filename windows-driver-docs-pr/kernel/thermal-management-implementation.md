---
title: Thermal Management Implementation
description: Learn how to implement thermal management in your device driver using the GUID_THERMAL_COOLING_INTERFACE.
ms.date: 09/19/2025
ms.topic: how-to
---

# Thermal management implementation

Starting with Windows 8, devices that have [thermal management capabilities](device-level-thermal-management.md) can implement the  `GUID_THERMAL_COOLING_INTERFACE` driver interface. They can then participate in global thermal management by exposing this interface to the operating system.

The operating system calls the driver's routines to dynamically manage thermal levels in the platform in response to changes in user activity and environmental conditions.

## Implementation overview

To participate in Windows thermal management, your device driver must:

1. Support the thermal cooling interface by responding to `IRP_MN_QUERY_INTERFACE` requests.
2. Implement callback routines for active cooling, passive cooling, or both.
3. Provide the interface structure with pointers to your callback implementations.
4. Handle thermal management requests from the operating system.

## The GUID_THERMAL_COOLING_INTERFACE

The `GUID_THERMAL_COOLING_INTERFACE` enables device drivers to participate in global thermal management across the hardware platform. When you implement this interface, the operating system can coordinate thermal management across multiple devices for optimal system performance.

### Interface discovery

During system startup, the system-supplied driver *Acpi.sys* queries device drivers to determine which ones support thermal management. Specifically, it sends an [**IRP_MN_QUERY_INTERFACE**](irp-mn-query-interface.md) request for the `GUID_THERMAL_COOLING_INTERFACE`.

In response to this request, the driver for a device that has thermal management capabilities can supply a pointer to a [**THERMAL_COOLING_INTERFACE**](/previous-versions/hh698275(v=vs.85)) structure. This structure contains pointers to a set of callback routines that the driver implements. To manage thermal levels in the device, the OS calls these routines directly.

Your driver can receive an [**IRP_MN_QUERY_INTERFACE**](irp-mn-query-interface.md) request for this interface any time after your [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine is called.

## Callback routine implementations

The two principal driver-implemented callback routines in this interface are:

- [*PassiveCooling*](/previous-versions/hh698270(v=vs.85))
- [*ActiveCooling*](/previous-versions/hh698235(v=vs.85)).

You can implement one or both of these routines, depending on your device's capabilities. For more information about these cooling modes, see [Device-level thermal management](device-level-thermal-management.md).

### PassiveCooling callback

The driver's [*PassiveCooling*](/previous-versions/hh698270(v=vs.85)) routine controls the degree to which the performance of the device must be throttled to maintain acceptable thermal levels. This routine:

- Adjusts device performance to maintain acceptable thermal levels.
- Takes a percentage parameter indicating the level of cooling required (0-100%).
- Implements performance scaling appropriate for your device type.

Before the OS's first call to [*PassiveCooling*](/previous-versions/hh698270(v=vs.85)), configure your device to run at full performance with no cooling restrictions.

### ActiveCooling callback

The [*ActiveCooling*](/previous-versions/hh698235(v=vs.85)) routine controls active cooling devices in your hardware. This routine:

- Engages or disengages active cooling based on the operating system's request.
- Controls cooling hardware such as fans, pumps, or other thermal management devices. For example, this routine might turn a fan on and off.
- Takes a boolean parameter indicating whether to turn on cooling (TRUE) or off (FALSE).

By default, before the first call to [*ActiveCooling*](/previous-versions/hh698235(v=vs.85)), active cooling is disengaged (for example, the fan is turned off).
