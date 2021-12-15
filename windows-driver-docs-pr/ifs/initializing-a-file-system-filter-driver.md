---
title: Initializing a File System Filter Driver
description: Initializing a File System Filter Driver
keywords:
- initializing filter drivers
- filter drivers WDK file system , initializing
- file system filter drivers WDK , initializing
- DriverEntry WDK file systems
ms.date: 04/20/2017
---

# Initializing a File System Filter Driver


## <span id="ddk_initializing_a_file_system_filter_driver_if"></span><span id="DDK_INITIALIZING_A_FILE_SYSTEM_FILTER_DRIVER_IF"></span>


The [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine for initializing a file system filter driver is very similar to the **DriverEntry** routine for initializing a device driver. After a driver is loaded, the same component that loaded the driver also initializes the driver by calling the driver's **DriverEntry** routine. For file system filter drivers, the component that loads the driver is either the I/O Manager (for filters whose start type is SERVICE\_BOOT\_START) or the Service Control Manager (for other start types).

The [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine runs in a system thread context at IRQL = PASSIVE\_LEVEL. This routine can be pageable and should be in an INIT segment so that it will be discarded. For more information about how to make your driver code pageable, see the Remarks section of [**MmLockPagableCodeSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmlockpagablecodesection).

The [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine is defined as follows:

```cpp
NTSTATUS 
(*PDRIVER_INITIALIZE) ( 
    IN PDRIVER_OBJECT DriverObject, 
    IN PUNICODE_STRING RegistryPath 
    ); 
```

This routine has two input parameters. The first, *DriverObject*, is the driver object that was created when the file system filter driver was loaded. The second, *RegistryPath*, is a pointer to a counted Unicode string that contains a path to the driver's registry key.

The [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine for a file system filter driver performs the following steps:

[Creating the Control Device Object](creating-the-control-device-object.md)

[Registering IRP Dispatch Routines](registering-irp-dispatch-routines.md)

[Registering Fast I/O Dispatch Routines](registering-fast-i-o-dispatch-routines.md)

[Registering FsFilter Callback Routines](registering-fsfilter-callback-routines.md)

[Performing Any Other Needed Initialization](performing-any-other-needed-initialization.md)

[\[Optional\] Registering Callback Routines](-optional--registering-callback-routines.md)

[\[Optional\] Saving a Copy of the Registry Path String](-optional--saving-a-copy-of-the-registry-path-string.md)

[Returning Status](returning-status.md)

 

