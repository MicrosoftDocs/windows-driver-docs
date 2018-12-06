---
title: Intermediate Driver DriverEntry Function
description: Intermediate Driver DriverEntry Function
ms.assetid: 85b4d5c0-8ec9-41a9-a34e-578a85d411e3
keywords:
- intermediate drivers WDK networking , entry points
- NDIS intermediate drivers WDK , entry points
- entry points WDK networking
- DriverEntry WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Intermediate Driver DriverEntry Function





An intermediate driver's initial required entry point must be explicitly named [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) so that the loader can properly identify it. All other exported driver functions, which are described in this section as *MiniportXxx* and *ProtocolXxx*, can have any vendor-specified name because they are passed as addresses to NDIS.

In an intermediate driver, **DriverEntry** must at a minimum:

1.  Call [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) and save the handle that is returned in the *NdisMiniportDriverHandle* parameter.

2.  Call [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520) to register the driver's *ProtocolXxx* functions if the driver subsequently binds itself to an underlying NDIS driver.

3.  Call [**NdisIMAssociateMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff562717) to inform NDIS about the association between the driver's miniport upper edge and protocol lower edge.

An intermediate driver must register a [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) unload handler. This unload handler is called when the system unloads the intermediate driver. If [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) fails, this unload handler is not called; instead, the driver is simply unloaded. For more information about the unload handler, see [Unloading an Intermediate Driver](unloading-an-intermediate-driver.md).

The unload handler should call [**NdisDeregisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561743) to deregister the protocol portion of the intermediate driver. The unload handler should also perform any necessary cleanup operations, such as reallocating resources used by the protocol portion of the driver.

Note that an unload handler differs from a [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function: the unload handler has a more global scope, and the scope of the *MiniportHaltEx* function is restricted to a particular miniport adapter. The intermediate driver should clean up state information and reallocate resources when each underlying miniport driver that is bound to it is halted. For information about handling the halt operation for virtual miniports, see [Halting a Virtual Miniport](halting-a-virtual-miniport.md).

[*ProtocolUninstall*](https://msdn.microsoft.com/library/windows/hardware/ff570279) is an optional unload handler. Register an entry point for this function in the *ProtocolCharacteristics* structure that you pass to [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520). NDIS calls *ProtocolUninstall* in response to a user request to uninstall an intermediate driver. NDIS calls [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) once for each bound adapter, and then NDIS calls *ProtocolUninstall*. This handler is called before the system actually unloads the driver. This timing provides a chance to release any device objects or other resources that might otherwise prevent the system from calling the unload handler that is registered with **NdisMRegisterMiniportDriver** and unloading the driver.

**DriverEntry** can initialize spin locks to protect any globally-shared resources that the intermediate driver allocates, such as state variables, structures, and memory areas. The driver uses these resources to track connections and to track sends in progress or driver-allocated queues.

If **DriverEntry** fails to allocate any resources that the driver needs to carry out network I/O operations, it should release any previously allocated resources and return an appropriate error status.

The following topics further describe how to register intermediate drivers:

[Registering as an NDIS Intermediate Driver](registering-as-an-ndis-intermediate-driver.md)

[Registering an Intermediate Driver as a Miniport Driver](registering-an-intermediate-driver-as-a-miniport-driver.md)

[Registering an Intermediate Driver as a Protocol Driver](registering-an-intermediate-driver-as-a-protocol.md)

 

 





