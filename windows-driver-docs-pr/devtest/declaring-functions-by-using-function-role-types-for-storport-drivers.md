---
title: Declaring Functions by Using Function Role Types for Storport Drivers
description: To enable SDV to analyze a Storport driver, you must declare your functions by using the function role type declarations that are defined for Storport. The function role types are defined in Storport.h.
ms.assetid: 40BD11CD-A559-4F90-BF39-4ED2FB800392
---

# Declaring Functions by Using Function Role Types for Storport Drivers


To enable SDV to analyze a Storport driver, you must declare your functions by using the function role type declarations that are defined for Storport. The function role types are defined in Storport.h.

You must declare each callback function in a Storport driver by specifying the corresponding role type.

The following code example shows the function role type declaration for DriverIntialize callback function. The function role type is sp\_DRIVER\_INITIALIZE.

```
sp_DRIVER_INITIALIZE DriverEntry;
```

If a callback function has a function prototype declaration, you must replace the function prototype with the function role type declaration.

| Function role type                        | Storport routine                                                                                                               |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| sp\_DRIVER\_INITIALIZE                    | DriverEntry                                                                                                                    |
| HW\_INITIALIZE                            | [**HwStorInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff557396)                                                                               |
| HW\_BUILDIO                               | [**HwStorBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557369)                                                                                     |
| HW\_STARTIO                               | [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423)                                                                                     |
| HW\_INTERRUPT                             | [**HwStorInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff557403)                                                                                 |
| HW\_TIMER                                 | [**HwStorTimer**](https://msdn.microsoft.com/library/windows/hardware/ff557426)                                                                                         |
| HW\_FIND\_ADAPTER                         | [**HwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff557390)                                                                             |
| HW\_RESET\_BUS                            | [**HwStorResetBus**](https://msdn.microsoft.com/library/windows/hardware/ff557415)                                                                                   |
| HW\_ADAPTER\_CONTROL                      | [**HwStorAdapterControl**](https://msdn.microsoft.com/library/windows/hardware/ff557365)                                                                       |
| HW\_PASSIVE\_INITIALIZE\_ROUTINE          | [**HwStorPassiveInitializeRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff557407)                                                   |
| HW\_DPC\_ROUTINE                          | [**HwStorDpcRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff557383)                                                                               |
| HW\_FREE\_ADAPTER\_RESOURCES              | HwFreeAdapterResources part of the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568010) structure.  |
| HW\_PROCESS\_SERVICE\_REQUEST             | HwProcessServiceRequest part of the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568010) structure. |
| HW\_COMPLETE\_SERVICE\_IRP                | HwCompleteServiceIrp part of the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568010) structure.    |
| HW\_INITIALIZE\_TRACING                   | HwInitializeTracing part of the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568010) structure.     |
| HW\_CLEANUP\_TRACING                      | HwCleanupTracing part of the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568010) structure.        |
| VIRTUAL\_HW\_FIND\_ADAPTER                | HwFindAdapter part of the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568010) structure.           |
| HW\_MESSAGE\_SIGNALED\_INTERRUPT\_ROUTINE | [**HwMSInterruptRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff557268)                                                                       |

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Declaring%20Functions%20by%20Using%20Function%20Role%20Types%20for%20Storport%20Drivers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




