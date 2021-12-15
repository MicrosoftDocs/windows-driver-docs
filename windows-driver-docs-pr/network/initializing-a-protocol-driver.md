---
title: Initializing a Protocol Driver
description: Initializing a Protocol Driver
keywords:
- protocol drivers WDK networking , initializing
- NDIS protocol drivers WDK , initializing
- initializing protocol drivers
ms.date: 04/20/2017
---

# Initializing a Protocol Driver




The system calls a protocol driver's [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine after it loads the driver. Protocol drivers load as system services. They can load at any time before, during, or after the miniport drivers load.

Protocol drivers allocate driver resources and register *ProtocolXxx* functions in **DriverEntry**. This includes CoNDIS clients and stand-alone call managers. To register its *ProtocolXxx* functions with NDIS, a protocol driver calls the [NdisRegisterProtocolDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver) function.

[DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) returns STATUS_SUCCESS, or its equivalent NDIS_STATUS_SUCCESS, if the driver registered as an NDIS protocol driver successfully. If **DriverEntry** fails initialization by propagating an error status that was returned by an **NdisXxx** function or by a kernel-mode support routine, the driver will not remain loaded. **DriverEntry** must execute synchronously; that is, it cannot return STATUS_PENDING or its equivalent NDIS_STATUS_PENDING.

The [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function of an NDIS protocol driver must call the [NdisRegisterProtocolDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver) function. To register the driver's *ProtocolXxx* entry points with the NDIS library, a protocol driver initializes an [**NDIS_PROTOCOL_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_driver_characteristics) structure and passes it to **NdisRegisterProtocolDriver**.

Drivers that call NdisRegisterProtocolDriver must be prepared for an immediate call to any of their ProtocolXxx functions.

NDIS protocol drivers provide the following *ProtocolXxx* functions, which are updated versions of the functions that legacy drivers provide:

[*ProtocolSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options)

[*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex)

[*ProtocolUnbindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_unbind_adapter_ex)

[*ProtocolOpenAdapterCompleteEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_open_adapter_complete_ex)

[*ProtocolCloseAdapterCompleteEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_close_adapter_complete_ex)

[*ProtocolNetPnPEvent*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_net_pnp_event)

[*ProtocolUninstall*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_uninstall)

NDIS protocol drivers provide the following *ProtocolXxx* functions for send and receive operations:

[**ProtocolReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_receive_net_buffer_lists)

[**ProtocolSendNetBufferListsComplete**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_send_net_buffer_lists_complete)

All types of NDIS protocol drivers should register fully functional [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) and [*ProtocolUnbindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_unbind_adapter_ex) functions to support Plug and Play (PnP). In general, a [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function should call [NdisRegisterProtocolDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver) immediately before it returns control with a status value of STATUS_SUCCESS or NDIS_STATUS_SUCCESS.

Any protocol driver that exports a set of standard kernel-mode driver routines in addition to its NDIS-defined *ProtocolXxx* functions must set the entry points for those driver routines in the given driver object that is passed in to its [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function. For more information about the functionality of such a protocol driver's **DriverEntry** function, see [Writing a DriverEntry Routine](../kernel/writing-a-driverentry-routine.md).

If an attempt to allocate resources that the driver needs to carry out network I/O operations fails, [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) should release all resources that it already allocated before it returns control with a status other than STATUS_SUCCESS or NDIS_STATUS_SUCCESS.

If an error occurs after a successful call to [NdisRegisterProtocolDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver), the driver must call the [NdisDeregisterProtocolDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisderegisterprotocoldriver) function before **DriverEntry** returns.

To allow a protocol driver to configure optional services, NDIS calls the *ProtocolSetOptions* function within the context of the protocol driver's call to **NdisRegisterProtocolDriver**. For more information about optional services, see [Configuring Optional Protocol Driver Services](configuring-optional-protocol-driver-services.md).

CoNDIS client drivers must call the [NdisSetOptionalHandlers](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function from the [*ProtocolSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function. The driver initializes an [**NDIS_CO_CLIENT_OPTIONAL_HANDLERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_co_client_optional_handlers) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

CoNDIS stand-alone call managers must also call the [NdisSetOptionalHandlers](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function from the [*ProtocolSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function. The driver initializes an [**NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_co_call_manager_optional_handlers) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

MCMs are not protocol drivers. Therefore, they must call the [NdisSetOptionalHandlers](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function from the [MiniportSetOptions](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function. The MCM initializes an [**NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_co_call_manager_optional_handlers) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

To unregister with NDIS, a protocol driver calls [NdisDeregisterProtocolDriver](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisderegisterprotocoldriver) from its [Unload](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine.

To perform cleanup operations before a protocol driver is uninstalled, a protocol driver can register a [*ProtocolUninstall*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_uninstall) function. The *ProtocolUninstall* function is optional. For example, the protocol lower edge of an intermediate driver might require a *ProtocolUninstall* function. The intermediate driver can release its protocol edge resources in *ProtocolUninstall* before NDIS calls its [*MiniportDriverUnload*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_unload) function.

 

