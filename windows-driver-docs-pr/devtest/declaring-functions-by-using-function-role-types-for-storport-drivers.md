---
title: Declaring Functions by Using Function Role Types for Storport Drivers
description: To enable SDV to analyze a Storport driver, you must declare your functions by using the function role type declarations that are defined for Storport. The function role types are defined in Storport.h.
ms.assetid: 40BD11CD-A559-4F90-BF39-4ED2FB800392
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 





