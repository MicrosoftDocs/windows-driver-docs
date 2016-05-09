---
title: Writing a DriverEntry Routine for a Minifilter Driver
description: Writing a DriverEntry Routine for a Minifilter Driver
ms.assetid: 949b4087-47de-4145-87dd-d618db44a15b
keywords: ["file system minifilter drivers WDK , DriverEntry routine", "minifilter drivers WDK , DriverEntry routine", "DriverEntry WDK file systems", "global initialization WDK file system minifilter"]
---

# Writing a DriverEntry Routine for a Minifilter Driver


## <span id="ddk_writing_a_driverentry_routine_for_a_minifilter_driver_if"></span><span id="DDK_WRITING_A_DRIVERENTRY_ROUTINE_FOR_A_MINIFILTER_DRIVER_IF"></span>


Every file system minifilter driver must have a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. The **DriverEntry** routine is called when the minifilter driver is loaded.

The **DriverEntry** routine performs global initialization, registers the minifilter driver, and initiates filtering. This routine runs in a system thread context at IRQL PASSIVE\_LEVEL.

The **DriverEntry** routine is defined as follows:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Writing%20a%20DriverEntry%20Routine%20for%20a%20Minifilter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




