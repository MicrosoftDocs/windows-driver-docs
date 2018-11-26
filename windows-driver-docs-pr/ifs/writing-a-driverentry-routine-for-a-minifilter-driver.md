---
title: Writing a DriverEntry Routine for a Minifilter Driver
description: Writing a DriverEntry Routine for a Minifilter Driver
ms.assetid: 949b4087-47de-4145-87dd-d618db44a15b
keywords:
- file system minifilter drivers WDK , DriverEntry routine
- minifilter drivers WDK , DriverEntry routine
- DriverEntry WDK file systems
- global initialization WDK file system minifilter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing a DriverEntry Routine for a Minifilter Driver


## <span id="ddk_writing_a_driverentry_routine_for_a_minifilter_driver_if"></span><span id="DDK_WRITING_A_DRIVERENTRY_ROUTINE_FOR_A_MINIFILTER_DRIVER_IF"></span>


Every file system minifilter driver must have a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. The **DriverEntry** routine is called when the minifilter driver is loaded.

The **DriverEntry** routine performs global initialization, registers the minifilter driver, and initiates filtering. This routine runs in a system thread context at IRQL PASSIVE\_LEVEL.

The **DriverEntry** routine is defined as follows:

```cpp
NTSTATUS 
(*PDRIVER_INITIALIZE) ( 
    IN PDRIVER_OBJECT DriverObject, 
    IN PUNICODE_STRING RegistryPath 
    ); 
```

**DriverEntry** has two input parameters. The first, *DriverObject*, is the driver object that was created when the minifilter driver was loaded. The second, *RegistryPath*, is a pointer to a counted Unicode string that contains a path to the minifilter driver's registry key.

A minifilter driver's **DriverEntry** routine must perform the following steps, in order:

1.  Perform any needed global initialization for the minifilter driver.

2.  Register the minifilter driver by calling [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305).

3.  Initiate filtering by calling [**FltStartFiltering**](https://msdn.microsoft.com/library/windows/hardware/ff544569).

4.  Return an appropriate NTSTATUS value.

This section includes:

[Registering the Minifilter Driver](registering-the-minifilter-driver.md)

[Initiating Filtering](initiating-filtering.md)

[Returning Status from a Minifilter DriverEntry Routine](returning-status.md)

 

 




