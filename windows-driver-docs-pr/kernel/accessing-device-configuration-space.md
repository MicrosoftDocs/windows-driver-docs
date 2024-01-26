---
title: Accessing Device Configuration Space
description: Accessing Device Configuration Space
keywords: ["I/O WDK kernel , device configuration space", "device configuration space WDK I/O", "configuration space WDK I/O", "space WDK I/O", "resource information WDK I/O", "driver stacks WDK configuration info"]
ms.date: 01/17/2024
---

# Accessing Device Configuration Space

This article explains how a driver can get information from a target device's configuration space, provided the driver is loaded in the same driver stack as the driver for the target device, either as a function driver or a filter driver.

The configuration space for a device contains a description of the device and its resource requirements. Typically, a driver receives resources from the Plug and Play (PnP) manager in [**IRP_MN_START_DEVICE**](./irp-mn-start-device.md), and does not need to query a device to find resources.  If the driver does need to access the configuration space:

* Use [BUS_INTERFACE_STANDARD](/windows-hardware/drivers/ddi/wdm/ns-wdm-_bus_interface_standard) provided by the bus driver. For sample code, see [Obtaining Device Configuration Information at IRQL = DISPATCH_LEVEL](obtaining-device-configuration-information-at-irql---dispatch-level.md).
* Use [**IRP_MN_READ_CONFIG**](./irp-mn-read-config.md) and [**IRP_MN_WRITE_CONFIG**](./irp-mn-write-config.md). For sample code, see [Obtaining Device Configuration Information at IRQL = PASSIVE_LEVEL](obtaining-device-configuration-information-at-irql---passive-level.md).

If you need the configuration space of a device whose driver is on a stack other than the one that your driver is on, see [Obtaining Configuration Information from Other Driver Stacks](obtaining-configuration-information-from-other-driver-stacks.md).
