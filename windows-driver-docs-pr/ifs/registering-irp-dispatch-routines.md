---
title: Registering IRP Dispatch Routines
description: Registering IRP Dispatch Routines
keywords:
- registering IRP dispatch routines
- dispatch routines WDK file system
- IRP dispatch routines WDK file system , registering
- IRPs WDK file system
ms.date: 02/23/2023
---

# Registering IRP Dispatch Routines

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

The **DriverObject** parameter of the legacy filter driver's [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine supplies a pointer to the filter driver's [**driver object**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_driver_object). To register I/O request packet (IRP) dispatch routines, you must store the entry points of these routines into the **MajorFunction** member of the driver object. For example, a hypothetical "MyLegacyFilter" driver can set the entry points for its dispatch routine as follows:

```cpp
for (i = 0; i <= IRP_MJ_MAXIMUM_FUNCTION; i++) {
    DriverObject->MajorFunction[i] = MyLegacyFilterDispatch;
}
DriverObject->MajorFunction[IRP_MJ_CREATE] = MyLegacyFilterCreate;
DriverObject->MajorFunction[IRP_MJ_CLOSE] = MyLegacyFilterClose;
DriverObject->MajorFunction[IRP_MJ_FILE_SYSTEM_CONTROL] = MyLegacyFilterFsControl;
```

The ```for``` loop assigns a default dispatch routine for all IRP major function codes. This assignment is good practice, because otherwise the I/O Manager completes any unrecognized IRP with STATUS_INVALID_DEVICE_REQUEST by default. File system filter drivers shouldn't reject unfamiliar IRPs in this way, because such requests are usually intended for another driver that is lower in the driver stack. For this reason, the default dispatch routine normally just passes the IRP down to the next-lower-level driver.
