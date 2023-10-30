---
title: '[Optional] Registering Callback Routines'
description: '[Optional] Registering Callback Routines'
keywords:
- registering callback routines
- callback routines WDK file system
ms.date: 02/23/2023
---

# \[Optional\] Registering Callback Routines

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

Legacy filter drivers can call [**IoRegisterFsRegistrationChange**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ioregisterfsregistrationchange) to register a callback routine to be called whenever a file system driver calls [**IoRegisterFileSystem**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ioregisterfilesystem) or [**IoUnregisterFileSystem**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iounregisterfilesystem) to register or unregister itself. Filter drivers register this callback routine so they can see new file systems enter the system and choose whether to attach to them.

File system filter drivers must never call [**IoRegisterFileSystem**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ioregisterfilesystem) or [**IoUnregisterFileSystem**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iounregisterfilesystem). These routines are only for file systems.

Filter drivers that attach to volumes only when explicitly directed (for example, by a user-mode application) shouldn't call [**IoRegisterFsRegistrationChange**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ioregisterfsregistrationchange). Note, however, that a filter that uses this routine has the ability to attach to any given volume immediately after that volume is mounted. Using this routine doesn't guarantee that the filter attaches directly to the volume device object. It does ensure that such a filter attaches before (and thus below) any filter that instead waits for a command from a user-mode application. This is because filters can attach only at the top of the current file system volume device stack.
