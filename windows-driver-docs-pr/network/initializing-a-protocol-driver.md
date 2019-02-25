---
title: Initializing a Protocol Driver
description: Initializing a Protocol Driver
ms.assetid: 1479d59b-7c8b-495b-86c7-72f1b7e334e4
keywords:
- protocol drivers WDK networking , initializing
- NDIS protocol drivers WDK , initializing
- initializing protocol drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a Protocol Driver




The system calls a protocol driver's [DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine after it loads the driver. Protocol drivers load as system services. They can load at any time before, during, or after the miniport drivers load.

Protocol drivers allocate driver resources and register *ProtocolXxx* functions in **DriverEntry**. This includes CoNDIS clients and stand-alone call managers. To register its *ProtocolXxx* functions with NDIS, a protocol driver calls the [NdisRegisterProtocolDriver](https://msdn.microsoft.com/library/windows/hardware/ff564520) function.

[DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113) returns STATUS_SUCCESS, or its equivalent NDIS_STATUS_SUCCESS, if the driver registered as an NDIS protocol driver successfully. If **DriverEntry** fails initialization by propagating an error status that was returned by an **NdisXxx** function or by a kernel-mode support routine, the driver will not remain loaded. **DriverEntry** must execute synchronously; that is, it cannot return STATUS_PENDING or its equivalent NDIS_STATUS_PENDING.

The [DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113) function of an NDIS protocol driver must call the [NdisRegisterProtocolDriver](https://msdn.microsoft.com/library/windows/hardware/ff564520) function. To register the driver's *ProtocolXxx* entry points with the NDIS library, a protocol driver initializes an [**NDIS_PROTOCOL_DRIVER_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566825) structure and passes it to **NdisRegisterProtocolDriver**.

Drivers that call NdisRegisterProtocolDriver must be prepared for an immediate call to any of their ProtocolXxx functions.

NDIS protocol drivers provide the following *ProtocolXxx* functions, which are updated versions of the functions that legacy drivers provide:

[*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269)

[*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220)

[*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278)

[*ProtocolOpenAdapterCompleteEx*](https://msdn.microsoft.com/library/windows/hardware/ff570265)

[*ProtocolCloseAdapterCompleteEx*](https://msdn.microsoft.com/library/windows/hardware/ff570236)

[*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263)

[*ProtocolUninstall*](https://msdn.microsoft.com/library/windows/hardware/ff570279)

NDIS protocol drivers provide the following *ProtocolXxx* functions for send and receive operations:

[**ProtocolReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff570267)

[**ProtocolSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570268)

All types of NDIS protocol drivers should register fully functional [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) and [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) functions to support Plug and Play (PnP). In general, a [DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113) function should call [NdisRegisterProtocolDriver](https://msdn.microsoft.com/library/windows/hardware/ff564520) immediately before it returns control with a status value of STATUS_SUCCESS or NDIS_STATUS_SUCCESS.

Any protocol driver that exports a set of standard kernel-mode driver routines in addition to its NDIS-defined *ProtocolXxx* functions must set the entry points for those driver routines in the given driver object that is passed in to its [DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113) function. For more information about the functionality of such a protocol driver's **DriverEntry** function, see [Writing a DriverEntry Routine](../kernel/writing-a-driverentry-routine.md).

If an attempt to allocate resources that the driver needs to carry out network I/O operations fails, [DriverEntry](https://msdn.microsoft.com/library/windows/hardware/ff544113) should release all resources that it already allocated before it returns control with a status other than STATUS_SUCCESS or NDIS_STATUS_SUCCESS.

If an error occurs after a successful call to [NdisRegisterProtocolDriver](https://msdn.microsoft.com/library/windows/hardware/ff564520), the driver must call the [NdisDeregisterProtocolDriver](https://msdn.microsoft.com/library/windows/hardware/ff561743) function before **DriverEntry** returns.

To allow a protocol driver to configure optional services, NDIS calls the *ProtocolSetOptions* function within the context of the protocol driver's call to **NdisRegisterProtocolDriver**. For more information about optional services, see [Configuring Optional Protocol Driver Services](configuring-optional-protocol-driver-services.md).

CoNDIS client drivers must call the [NdisSetOptionalHandlers](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from the [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function. The driver initializes an [**NDIS_CO_CLIENT_OPTIONAL_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564884) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

CoNDIS stand-alone call managers must also call the [NdisSetOptionalHandlers](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from the [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function. The driver initializes an [**NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564883) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

MCMs are not protocol drivers. Therefore, they must call the [NdisSetOptionalHandlers](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from the [MiniportSetOptions](https://msdn.microsoft.com/library/windows/hardware/ff559443) function. The MCM initializes an [**NDIS_CO_CALL_MANAGER_OPTIONAL_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564883) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

To unregister with NDIS, a protocol driver calls [NdisDeregisterProtocolDriver](https://msdn.microsoft.com/library/windows/hardware/ff561743) from its [Unload](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine.

To perform cleanup operations before a protocol driver is uninstalled, a protocol driver can register a [*ProtocolUninstall*](https://msdn.microsoft.com/library/windows/hardware/ff570279) function. The *ProtocolUninstall* function is optional. For example, the protocol lower edge of an intermediate driver might require a *ProtocolUninstall* function. The intermediate driver can release its protocol edge resources in *ProtocolUninstall* before NDIS calls its [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) function.

 

 





