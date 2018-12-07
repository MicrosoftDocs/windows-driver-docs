---
title: Porting DriverEntry
description: Porting DriverEntry
ms.assetid: E880A45A-136C-480E-BE66-B61558F98227
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting DriverEntry


In both WDM and framework-based drivers, the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) function is the primary entry point. The function prototype is the same in both models. In a WDM driver, the system calls **DriverEntry** when the driver is first loaded into memory. DriverEntry sets a pointer to the driver’s [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine in the **DriverExtension-&gt;AddDevice** field of the [**DRIVER\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff544174) structure, sets pointers to its I/O dispatch routines in the **MajorFunction** array of the DRIVER\_OBJECT structure, and then returns. In a framework-based driver, the system calls the framework’s internal **FxDriverEntry** function upon loading the driver. This internal function initializes the framework and then calls the driver’s **DriverEntry** function. **DriverEntry** sets a pointer to the driver’s [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback and calls [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) to create the WDFDRIVER object, as the following example shows:

```cpp
NTSTATUS
DriverEntry(
    IN PDRIVER_OBJECT  DriverObject
    IN PUNICODE_STRING RegistryPath
    )
{
    WDF_DRIVER_CONFIG_INIT( &config,
                              ToasterEvtDeviceAdd );
    status = WdfDriverCreate(
                 DriverObject
                 RegistryPath
                 WDF_NO_OBJECT_ATTRIBUTES
                 &config
                 WDF_NO_HANDLE
             );

    return STATUS_SUCCESS;
}
```

**DriverEntry** also initializes any global data or resources that the driver requires, such as creating a lookaside list or initializing tracing. Note that although [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) returns a handle to the WDFDRIVER object, the driver does not retain this handle, just as a WDM driver might not retain the DRIVER\_OBJECT pointer that was passed to its **DriverEntry** routine. The reason is the same: only a few drivers use the pointer to the driver object.

 

 





