---
title: Returning Status
description: Returning Status
keywords:
- status values WDK file system
- success status values WDK file system
- returning status WDK file system
ms.date: 02/23/2023
---

# Returning Status

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

A legacy file system filter driver's **DriverEntry** routine normally returns STATUS_SUCCESS. However, if driver initialization fails, the **DriverEntry** routine should return an appropriate error status value.

If the **DriverEntry** routine returns a status value that isn't a success status value, the system responds by unloading the driver. For this reason, the **DriverEntry** routine must always free any memory that was allocated for system resources, such as device objects, before returning a status value that isn't a success status value.
