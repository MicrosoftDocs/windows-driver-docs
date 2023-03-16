---
title: Battery Class Driver Functionality
description: Battery Class Driver Functionality
keywords:
- battery class drivers WDK , functionality
ms.date: 04/20/2017
---

# Battery Class Driver Functionality

The kernel-mode battery class driver, battc.sys, provides device-independent battery support and exports support routines for use by all device-specific battery miniclass drivers.

The battery class driver takes care of the following tasks for miniclass drivers:

- Performing a large part of miniclass driver initialization, including allocating system resources and space for the miniclass driver's class data

- Handling device control IRPs ([**IRP\_MJ\_DEVICE\_CONTROL**](../kernel/irp-mj-device-control.md)) that specify battery class IOCTLs. (See the Microsoft Windows SDK for information about these IOCTLs.)

- Serializing requests to the battery device

- Administering DC power policy for the operating system

- Freeing system resources if the miniclass driver is unloaded

- Handling certain standard battery WMI classes

See [Battery Miniclass Driver Routines](/windows-hardware/drivers/ddi/_battery/) for descriptions of the routines that the battery class driver exports to battery miniclass drivers.
