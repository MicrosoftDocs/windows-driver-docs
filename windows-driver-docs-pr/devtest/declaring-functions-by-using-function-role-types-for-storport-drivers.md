---
title: Declaring Functions by Using Function Role Types for Storport Drivers
description: To enable SDV to analyze a Storport driver, you must declare your functions by using the function role type declarations that are defined for Storport. The function role types are defined in Storport.h.
ms.date: 04/20/2017
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
| HW\_INITIALIZE                            | [**HwStorInitialize**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_initialize)                                                                               |
| HW\_BUILDIO                               | [**HwStorBuildIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_buildio)                                                                                     |
| HW\_STARTIO                               | [**HwStorStartIo**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_startio)                                                                                     |
| HW\_INTERRUPT                             | [**HwStorInterrupt**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_interrupt)                                                                                 |
| HW\_TIMER                                 | [**HwStorTimer**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_timer)                                                                                         |
| HW\_FIND\_ADAPTER                         | [**HwStorFindAdapter**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_find_adapter)                                                                             |
| HW\_RESET\_BUS                            | [**HwStorResetBus**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_reset_bus)                                                                                   |
| HW\_ADAPTER\_CONTROL                      | [**HwStorAdapterControl**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_adapter_control)                                                                       |
| HW\_PASSIVE\_INITIALIZE\_ROUTINE          | [**HwStorPassiveInitializeRoutine**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_passive_initialize_routine)                                                   |
| HW\_DPC\_ROUTINE                          | [**HwStorDpcRoutine**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_dpc_routine)                                                                               |
| HW\_FREE\_ADAPTER\_RESOURCES              | HwFreeAdapterResources part of the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_virtual_hw_initialization_data) structure.  |
| HW\_PROCESS\_SERVICE\_REQUEST             | HwProcessServiceRequest part of the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_virtual_hw_initialization_data) structure. |
| HW\_COMPLETE\_SERVICE\_IRP                | HwCompleteServiceIrp part of the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_virtual_hw_initialization_data) structure.    |
| HW\_INITIALIZE\_TRACING                   | HwInitializeTracing part of the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_virtual_hw_initialization_data) structure.     |
| HW\_CLEANUP\_TRACING                      | HwCleanupTracing part of the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_virtual_hw_initialization_data) structure.        |
| VIRTUAL\_HW\_FIND\_ADAPTER                | HwFindAdapter part of the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](/windows-hardware/drivers/ddi/storport/ns-storport-_virtual_hw_initialization_data) structure.           |
| HW\_MESSAGE\_SIGNALED\_INTERRUPT\_ROUTINE | [**HwMSInterruptRoutine**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_message_signaled_interrupt_routine)                                                                       |

 

 

