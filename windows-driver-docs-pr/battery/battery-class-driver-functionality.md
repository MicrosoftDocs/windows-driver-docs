---
title: Battery Class Driver Functionality
description: Discover the functionality of the kernel-mode battery class driver and the tasks it performs for miniclass drivers.
ms.date: 10/04/2023
---

# Battery class driver functionality

The kernel-mode battery class driver, battc.sys, provides device-independent battery support and exports support routines for all device-specific battery miniclass drivers.

## Tasks performed by the battery class driver

The battery class driver handles the following tasks for miniclass drivers:

- Completing a significant portion of miniclass driver initialization, including allocating system resources and space for the miniclass driver's class data

- Processing device control IRPs ([**IRP_MJ_DEVICE_CONTROL**](../kernel/irp-mj-device-control.md)) that specify battery class IOCTLs (refer to the Microsoft Windows SDK for information about these IOCTLs)

- Serializing requests to the battery device

- Managing DC power policy for the operating system

- Releasing system resources when the miniclass driver is unloaded

- Handling specific standard battery WMI classes

For descriptions of the routines that the battery class driver exports to battery miniclass drivers, see [Battery miniclass driver routines](/windows-hardware/drivers/ddi/_battery/).
