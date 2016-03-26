---
title: Porting DriverEntry
description: Porting DriverEntry
ms.assetid: E880A45A-136C-480E-BE66-B61558F98227
---

# Porting DriverEntry


In both WDM and framework-based drivers, the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) function is the primary entry point. The function prototype is the same in both models. In a WDM driver, the system calls **DriverEntry** when the driver is first loaded into memory. DriverEntry sets a pointer to the driver’s [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine in the **DriverExtension-&gt;AddDevice** field of the [**DRIVER\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff544174) structure, sets pointers to its I/O dispatch routines in the **MajorFunction** array of the DRIVER\_OBJECT structure, and then returns. In a framework-based driver, the system calls the framework’s internal **FxDriverEntry** function upon loading the driver. This internal function initializes the framework and then calls the driver’s **DriverEntry** function. **DriverEntry** sets a pointer to the driver’s [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback and calls [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) to create the WDFDRIVER object, as the following example shows:

```
NTSTATUS
DriverEntry(
    IN PDRIVER_OBJECT  DriverObject
    IN PUNICODE_STRING RegistryPath
    )
{
    WDF_DRIVER_CONFIG_INIT( &amp;config,
                              ToasterEvtDeviceAdd );
    status = WdfDriverCreate(
                 DriverObject
                 RegistryPath
                 WDF_NO_OBJECT_ATTRIBUTES
                 &amp;config
                 WDF_NO_HANDLE
             );

    return STATUS_SUCCESS;
}
```

**DriverEntry** also initializes any global data or resources that the driver requires, such as creating a lookaside list or initializing tracing. Note that although [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) returns a handle to the WDFDRIVER object, the driver does not retain this handle, just as a WDM driver might not retain the DRIVER\_OBJECT pointer that was passed to its **DriverEntry** routine. The reason is the same: only a few drivers use the pointer to the driver object.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Porting%20DriverEntry%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




