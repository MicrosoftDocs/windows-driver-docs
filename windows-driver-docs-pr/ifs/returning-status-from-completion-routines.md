---
title: Returning Status from Completion Routines
description: Returning Status from Completion Routines
keywords:
- IRP completion routines WDK file system , returning status
- status values WDK file system
- success status values WDK file system
- returning status WDK file system
ms.date: 02/23/2023
---

# Returning Status from Completion Routines

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

A legacy file system filter driver's completion routine normally returns one of the following two NTSTATUS values to the caller:

- STATUS_SUCCESS

- STATUS_MORE_PROCESSING_REQUIRED

STATUS_SUCCESS indicates that the driver is finished with the IRP and allows the I/O Manager to continue completion processing on the IRP.

STATUS_MORE_PROCESSING_REQUIRED halts the I/O Manager's completion processing on the IRP.

If any other NTSTATUS value is returned, the I/O Manager resets it to STATUS_SUCCESS.

For more information about returning STATUS_MORE_PROCESSING_REQUIRED, see [Constraints on Completion Routines](constraints-on-completion-routines.md).
