---
title: Initializing a Protocol Driver
description: Initializing a Protocol Driver
ms.assetid: 1479d59b-7c8b-495b-86c7-72f1b7e334e4
keywords: ["protocol drivers WDK networking , initializing", "NDIS protocol drivers WDK , initializing", "initializing protocol drivers"]
---

# Initializing a Protocol Driver


## <a href="" id="ddk-initializing-a-protocol-driver-ng"></a>


The system calls a protocol driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine after it loads the driver. Protocol drivers load as system services. They can load at any time before, during, or after the miniport drivers load.

Protocol drivers allocate driver resources and register *ProtocolXxx* functions in **DriverEntry**. To register its *ProtocolXxx* functions with NDIS, a protocol driver calls the [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520) function.

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

To allow a protocol driver to configure optional services, NDIS calls the *ProtocolSetOptions* function within the context of the protocol driver's call to **NdisRegisterProtocolDriver**. For more information about optional services, see [Configuring Optional Protocol Driver Services](configuring-optional-protocol-driver-services.md).

To unregister with NDIS, a protocol driver calls [**NdisDeregisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561743) from its [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine.

To perform cleanup operations before a protocol driver is uninstalled, a protocol driver can register a [*ProtocolUninstall*](https://msdn.microsoft.com/library/windows/hardware/ff570279) function. The *ProtocolUninstall* function is optional. For example, the protocol lower edge of an intermediate driver might require a *ProtocolUninstall* function. The intermediate driver can release its protocol edge resources in *ProtocolUninstall* before NDIS calls its [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) function.

 

 





