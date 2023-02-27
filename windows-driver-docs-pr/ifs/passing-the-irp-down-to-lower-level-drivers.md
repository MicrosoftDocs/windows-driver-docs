---
title: Passing the IRP Down to Lower-Level Drivers
description: Passing the IRP Down to Lower-Level Drivers
keywords:
- IRP dispatch routines WDK file system , passing IRP down
- passing IRPs down device stack WDK
ms.date: 02/23/2023
---

# Passing the IRP Down to Lower-Level Drivers

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

By default, after checking the IRP's target device object, every dispatch routine must pass the IRP down to the next-lower-level device driver by calling [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver). It's especially important that your legacy filter driver passes down any IRPs that it doesn't recognize instead of simply failing them. Failing unfamiliar IRPs can cause the operating system itself to fail in unexpected ways. For example, failing IRP_MJ_PNP requests in a file system filter driver can interfere with power management by preventing system hibernation. This interference is true even though file system filter drivers aren't involved in power management and don't receive [**IRP_MJ_POWER**](../kernel/irp-mj-power.md) requests.
