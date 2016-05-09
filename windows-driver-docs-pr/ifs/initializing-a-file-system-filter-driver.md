---
title: Initializing a File System Filter Driver
author: windows-driver-content
description: Initializing a File System Filter Driver
ms.assetid: 8a487665-0210-49f5-af91-de78de982506
keywords: ["initializing filter drivers", "filter drivers WDK file system , initializing", "file system filter drivers WDK , initializing", "DriverEntry WDK file systems"]
---

# Initializing a File System Filter Driver


## <span id="ddk_initializing_a_file_system_filter_driver_if"></span><span id="DDK_INITIALIZING_A_FILE_SYSTEM_FILTER_DRIVER_IF"></span>


The [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine for initializing a file system filter driver is very similar to the **DriverEntry** routine for initializing a device driver. After a driver is loaded, the same component that loaded the driver also initializes the driver by calling the driver's **DriverEntry** routine. For file system filter drivers, the component that loads the driver is either the I/O Manager (for filters whose start type is SERVICE\_BOOT\_START) or the Service Control Manager (for other start types).

The [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine runs in a system thread context at IRQL = PASSIVE\_LEVEL. This routine can be pageable and should be in an INIT segment so that it will be discarded. For more information about how to make your driver code pageable, see the Remarks section of [**MmLockPagableCodeSection**](https://msdn.microsoft.com/library/windows/hardware/ff554601).

The [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine is defined as follows:

```
NTSTATUS 
(*PDRIVER_INITIALIZE) ( 
    IN PDRIVER_OBJECT DriverObject, 
    IN PUNICODE_STRING RegistryPath 
    ); 
```

This routine has two input parameters. The first, *DriverObject*, is the driver object that was created when the file system filter driver was loaded. The second, *RegistryPath*, is a pointer to a counted Unicode string that contains a path to the driver's registry key.

The [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine for a file system filter driver performs the following steps:

[Creating the Control Device Object](creating-the-control-device-object.md)

[Registering IRP Dispatch Routines](registering-irp-dispatch-routines.md)

[Registering Fast I/O Dispatch Routines](registering-fast-i-o-dispatch-routines.md)

[Registering FsFilter Callback Routines](registering-fsfilter-callback-routines.md)

[Performing Any Other Needed Initialization](performing-any-other-needed-initialization.md)

[\[Optional\] Registering Callback Routines](-optional--registering-callback-routines.md)

[\[Optional\] Saving a Copy of the Registry Path String](-optional--saving-a-copy-of-the-registry-path-string.md)

[Returning Status](returning-status.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Initializing%20a%20File%20System%20Filter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


