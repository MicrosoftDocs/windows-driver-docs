---
title: '[Optional] Saving a Copy of the Registry Path String'
description: '[Optional] Saving a Copy of the Registry Path String'
keywords:
- RegistryPath string copies
- saving RegistryPath string copies
- copying RegistryPath strings
ms.date: 02/23/2023
---

# \[Optional\] Saving a Copy of the Registry Path String

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

This step is necessary only if the filter driver needs to use the registry path after the **DriverEntry** routine returns.

Save a copy of the *RegistryPath* string that was passed as input to **DriverEntry**. This parameter points to a counted Unicode string that specifies a path to the driver's registry key, **\\Registry\\Machine\\System\\CurrentControlSet\\Services\\***DriverName*, where *DriverName* is the name of the driver. If the *RegistryPath* string will be needed later, **DriverEntry** must save a copy of it, not just a pointer to it, because the pointer is no longer valid after the **DriverEntry** routine returns. You can use the [**RtlCopyUnicodeString**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlcopyunicodestring) routine to copy the *RegistryPath* source string to a destination string.
