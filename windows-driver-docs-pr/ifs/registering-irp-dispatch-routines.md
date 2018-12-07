---
title: Registering IRP Dispatch Routines
description: Registering IRP Dispatch Routines
ms.assetid: 096f4bb7-2326-4e6c-b3db-a2d95ca4982b
keywords:
- registering IRP dispatch routines
- dispatch routines WDK file system
- IRP dispatch routines WDK file system , registering
- IRPs WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering IRP Dispatch Routines


## <span id="ddk_registering_irp_dispatch_routines_if"></span><span id="DDK_REGISTERING_IRP_DISPATCH_ROUTINES_IF"></span>


The *DriverObject* parameter of the filter driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine supplies a pointer to the filter driver's [**driver object**](https://msdn.microsoft.com/library/windows/hardware/ff544174). To register I/O request packet (IRP) dispatch routines, you must store the entry points of these routines into the **MajorFunction** member of the driver object. For example, a hypothetical "MyLegacyFilter" driver can set the entry points for its dispatch routine as follows:

```cpp
for (i = 0; i <= IRP_MJ_MAXIMUM_FUNCTION; i++) {
    DriverObject->MajorFunction[i] = MyLegacyFilterDispatch;
}
DriverObject->MajorFunction[IRP_MJ_CREATE] = MyLegacyFilterCreate;
DriverObject->MajorFunction[IRP_MJ_CLOSE] = MyLegacyFilterClose;
DriverObject->MajorFunction[IRP_MJ_FILE_SYSTEM_CONTROL] = MyLegacyFilterFsControl;
```

Note that the above **FOR** loop assigns a default dispatch routine for all IRP major function codes. This assignment is good practice, because otherwise the I/O Manager completes any unrecognized IRP with STATUS\_INVALID\_DEVICE\_REQUEST by default. File system filter drivers should not reject unfamiliar IRPs in this way, because such requests are usually intended for another driver that is lower in the driver stack. For this reason, the default dispatch routine normally just passes the IRP down to the next-lower-level driver.

 

 




