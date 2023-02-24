---
title: Performing Any Other Needed Initialization
description: Performing Any Other Needed Initialization
ms.date: 02/23/2023
---

# Performing Any Other Needed Initialization

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

After registering IRP and fast I/O dispatch routines, your file system filter driver's **DriverEntry** routine can initialize other global driver variables and data structures as needed.
