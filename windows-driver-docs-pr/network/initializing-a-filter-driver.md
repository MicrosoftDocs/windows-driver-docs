---
title: Initializing a Filter Driver
description: Initializing a Filter Driver
keywords:
- filter drivers WDK networking , initializing
- NDIS filter drivers WDK , initializing
- initializing filter drivers
ms.date: 04/20/2017
---

# Initializing a Filter Driver



Filter driver initialization occurs immediately after the system loads the driver. Filter drivers load as system services. The system can load the filter drivers at any time before, during, or after the miniport drivers load. NDIS can attach a filter module to a miniport adapter after a miniport adapter of the type supported by the filter driver becomes available and the filter driver initialization is complete.

While a driver stack is starting, the system loads the filter drivers if they are not already loaded. For more information about starting a driver stack that includes filter modules, see [Starting a Driver Stack](starting-a-driver-stack.md).

After a filter driver loads, the system calls the driver's [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine. 

The system passes two arguments to [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize):

-   A pointer to the driver object, which was created by the I/O system.

-   A pointer to the registry path, which specifies where driver-specific parameters are stored.

[DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) returns STATUS_SUCCESS, or its equivalent NDIS_STATUS_SUCCESS, if the driver successfully registered as an NDIS filter driver. If **DriverEntry** fails initialization by propagating an error status returned by an **NdisXxx** function or by a kernel-mode support routine, the driver will not remain loaded. **DriverEntry** must execute synchronously; that is, it cannot return STATUS_PENDING or its equivalent NDIS_STATUS_PENDING.

The filter driver passes the driver object to the [NdisFRegisterFilterDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfregisterfilterdriver) function when it registers with NDIS as a filter driver. The driver can use the registry path to obtain configuration information. For more information about how to access filter driver configuration information, see [Accessing Configuration Information for a Filter Driver](accessing-configuration-information-for-a-filter-driver.md).

A filter driver calls **NdisFRegisterFilterDriver** from its **DriverEntry** routine. Filter drivers export a set of *FilterXxx* functions by passing an [**NDIS\_FILTER\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics) structure to **NdisFRegisterFilterDriver** at the *FilterCharacteristics* parameter.

The NDIS\_FILTER\_DRIVER\_CHARACTERISTICS structure specifies entry points for mandatory and optional *FilterXxx* functions. Some optional functions can be bypassed. For more information about bypassing functions, see [Data Bypass Mode](data-bypass-mode.md).

Drivers that call [NdisFRegisterFilterDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfregisterfilterdriver) must be prepared for an immediate call to any of their *FilterXxx* functions.

The NDIS\_FILTER\_DRIVER\_CHARACTERISTICS structure specifies the entry points for these mandatory *FilterXxx* functions:

[*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach)

[*FilterDetach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_detach)

[*FilterRestart*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_restart)

[*FilterPause*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_pause)

The NDIS\_FILTER\_DRIVER\_CHARACTERISTICS structure specifies the entry points for these optional, and not changeable at run-time, *FilterXxx* functions:

[*FilterSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options)

[*FilterSetModuleOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_set_module_options)

[*FilterOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request)

[*FilterOidRequestComplete*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_oid_request_complete)

[*FilterStatus*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_status)

[*FilterNetPnPEvent*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_net_pnp_event)

[*FilterDevicePnPEventNotify*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_device_pnp_event_notify)

[*FilterCancelSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_send_net_buffer_lists)

The NDIS\_FILTER\_DRIVER\_CHARACTERISTICS structure specifies the default entry points for these optional, and changeable at run-time, *FilterXxx* functions:

[*FilterSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_send_net_buffer_lists)

[*FilterSendNetBufferListsComplete*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_send_net_buffer_lists_complete)

[*FilterReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_return_net_buffer_lists)

[*FilterReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists)

The preceding four functions are also defined in the [**NDIS\_FILTER\_PARTIAL\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_partial_characteristics) structure. This structure specifies the functions that can be changed at a run time by calling the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function from the [*FilterSetModuleOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_set_module_options) function. If a filter driver will change these partial characteristics at runtime, it must provide the entry point for *FilterSetModuleOptions*. The partial characteristics can be different for each filter module. For more information, see [Starting a Filter Module](starting-a-filter-module.md).

NDIS calls the *FilterSetOptions* function within the context of the call to **NdisFRegisterFilterDriver**. *FilterSetOptions* registers optional services with NDIS. For more information, see [Configuring Optional Filter Driver Services](configuring-optional-filter-driver-services.md).

If the call to **NdisFRegisterFilterDriver** succeeds, NDIS fills the variable at *NdisFilterDriverHandle* with a filter driver handle. The filter driver saves this handle and later passes this handle to NDIS functions, such as [**NdisFDeregisterFilterDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfderegisterfilterdriver), that require a filter driver handle as an input parameter. When the driver unloads, it must call the **NdisFDeregisterFilterDriver** function to release the driver resources allocated by **NdisFRegisterFilterDriver**.

After *FilterSetOptions* returns, the filter modules are in the *Detached* state. NDIS can call the filter driver's [*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach) function at any time after the call to *FilterSetOptions* returns. The driver performs filter module-specific initialization in the *FilterAttach* function. For more information about attaching a filter module to a driver stack, see [Attaching a Filter Module](attaching-a-filter-module.md).

A filter driver also performs any other driver-specific initialization that it requires in **DriverEntry**. The filter driver must release the driver-specific resources that it allocates in its [*FilterDriverUnload*](./unloading-a-filter-driver.md) routine. For more information, see [Unloading a Filter Driver](unloading-a-filter-driver.md).

 

