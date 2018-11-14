---
title: Initializing a Filter Driver
description: Initializing a Filter Driver
ms.assetid: e24b18b5-76d3-4d56-bf60-0dea91ba014e
keywords:
- filter drivers WDK networking , initializing
- NDIS filter drivers WDK , initializing
- initializing filter drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a Filter Driver



Filter driver initialization occurs immediately after the system loads the driver. Filter drivers load as system services. The system can load the filter drivers at any time before, during, or after the miniport drivers load. NDIS can attach a filter module to a miniport adapter after a miniport adapter of the type supported by the filter driver becomes available and the filter driver initialization is complete.

While a driver stack is starting, the system loads the filter drivers if they are not already loaded. For more information about starting a driver stack that includes filter modules, see [Starting a Driver Stack](starting-a-driver-stack.md).

After a filter driver loads, the system calls the driver's [DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. 

The system passes two arguments to [DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113):

-   A pointer to the driver object, which was created by the I/O system.

-   A pointer to the registry path, which specifies where driver-specific parameters are stored.

[DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113) returns STATUS_SUCCESS, or its equivalent NDIS_STATUS_SUCCESS, if the driver successfully registered as an NDIS filter driver. If **DriverEntry** fails initialization by propagating an error status returned by an **NdisXxx** function or by a kernel-mode support routine, the driver will not remain loaded. **DriverEntry** must execute synchronously; that is, it cannot return STATUS_PENDING or its equivalent NDIS_STATUS_PENDING.

The filter driver passes the driver object to the [NdisFRegisterFilterDriver](https://msdn.microsoft.com/library/windows/hardware/ff562608) function when it registers with NDIS as a filter driver. The driver can use the registry path to obtain configuration information. For more information about how to access filter driver configuration information, see [Accessing Configuration Information for a Filter Driver](accessing-configuration-information-for-a-filter-driver.md).

A filter driver calls **NdisFRegisterFilterDriver** from its **DriverEntry** routine. Filter drivers export a set of *FilterXxx* functions by passing an [**NDIS\_FILTER\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565515) structure to **NdisFRegisterFilterDriver** at the *FilterCharacteristics* parameter.

The NDIS\_FILTER\_DRIVER\_CHARACTERISTICS structure specifies entry points for mandatory and optional *FilterXxx* functions. Some optional functions can be bypassed. For more information about bypassing functions, see [Data Bypass Mode](data-bypass-mode.md).

Drivers that call [NdisFRegisterFilterDriver](https://msdn.microsoft.com/library/windows/hardware/ff562608) must be prepared for an immediate call to any of their *FilterXxx* functions.

The NDIS\_FILTER\_DRIVER\_CHARACTERISTICS structure specifies the entry points for these mandatory *FilterXxx* functions:

[*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905)

[*FilterDetach*](https://msdn.microsoft.com/library/windows/hardware/ff549918)

[*FilterRestart*](https://msdn.microsoft.com/library/windows/hardware/ff549962)

[*FilterPause*](https://msdn.microsoft.com/library/windows/hardware/ff549957)

The NDIS\_FILTER\_DRIVER\_CHARACTERISTICS structure specifies the entry points for these optional, and not changeable at run-time, *FilterXxx* functions:

[*FilterSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff549972)

[*FilterSetModuleOptions*](https://msdn.microsoft.com/library/windows/hardware/ff549970)

[*FilterOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff549954)

[*FilterOidRequestComplete*](https://msdn.microsoft.com/library/windows/hardware/ff549956)

[*FilterStatus*](https://msdn.microsoft.com/library/windows/hardware/ff549973)

[*FilterNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff549952)

[*FilterDevicePnPEventNotify*](https://msdn.microsoft.com/library/windows/hardware/ff549926)

[*FilterCancelSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549915)

The NDIS\_FILTER\_DRIVER\_CHARACTERISTICS structure specifies the default entry points for these optional, and changeable at run-time, *FilterXxx* functions:

[*FilterSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549966)

[*FilterSendNetBufferListsComplete*](https://msdn.microsoft.com/library/windows/hardware/ff549967)

[*FilterReturnNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549964)

[*FilterReceiveNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549960)

The preceding four functions are also defined in the [**NDIS\_FILTER\_PARTIAL\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565544) structure. This structure specifies the functions that can be changed at a run time by calling the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from the [*FilterSetModuleOptions*](https://msdn.microsoft.com/library/windows/hardware/ff549970) function. If a filter driver will change these partial characteristics at runtime, it must provide the entry point for *FilterSetModuleOptions*. The partial characteristics can be different for each filter module. For more information, see [Starting a Filter Module](starting-a-filter-module.md).

NDIS calls the *FilterSetOptions* function within the context of the call to **NdisFRegisterFilterDriver**. *FilterSetOptions* registers optional services with NDIS. For more information, see [Configuring Optional Filter Driver Services](configuring-optional-filter-driver-services.md).

If the call to **NdisFRegisterFilterDriver** succeeds, NDIS fills the variable at *NdisFilterDriverHandle* with a filter driver handle. The filter driver saves this handle and later passes this handle to NDIS functions, such as [**NdisFDeregisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561800), that require a filter driver handle as an input parameter. When the driver unloads, it must call the **NdisFDeregisterFilterDriver** function to release the driver resources allocated by **NdisFRegisterFilterDriver**.

After *FilterSetOptions* returns, the filter modules are in the *Detached* state. NDIS can call the filter driver's [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function at any time after the call to *FilterSetOptions* returns. The driver performs filter module-specific initialization in the *FilterAttach* function. For more information about attaching a filter module to a driver stack, see [Attaching a Filter Module](attaching-a-filter-module.md).

A filter driver also performs any other driver-specific initialization that it requires in **DriverEntry**. The filter driver must release the driver-specific resources that it allocates in its [*FilterDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff549936) routine. For more information, see [Unloading a Filter Driver](unloading-a-filter-driver.md).

 

 





