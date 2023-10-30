---
title: Checking the PendingReturned Flag
description: Checking the PendingReturned Flag
keywords:
- IRP completion routines WDK file system , PendingReturned flag
- PendingReturned flag
ms.date: 02/23/2023
---

# Checking the PendingReturned Flag

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

If a completion routine doesn't signal an event, it must check the **Irp‑>PendingReturned** flag. If this flag is set, the completion routine must mark the IRP pending by calling [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending).
