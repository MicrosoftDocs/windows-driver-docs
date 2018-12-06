---
title: Registering CoNDIS WAN Drivers
description: Registering CoNDIS WAN Drivers
ms.assetid: e699d1b0-9dbd-4845-b8e3-e83da20e997c
keywords:
- CoNDIS WAN drivers WDK networking , registering
- NdisMRegisterMiniportDriver
- registering CoNDIS WAN drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering CoNDIS WAN Drivers





A CoNDIS WAN miniport driver or MCM calls [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) from its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) function to register its standard *MiniportXxx* functions with NDIS. For more information about registering *MiniportXxx* functions, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

A CoNDIS WAN call manager is an NDIS protocol driver. As such, a call manager calls [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520) to register its standard *ProtocolXxx* functions. For more information about registering an NDIS protocol driver, see [Initializing a Protocol Driver](initializing-a-protocol-driver.md). For information about other differences between call manager initialization and MCM initialization, see [Differences in Initialization](differences-in-initialization.md).

The call to **NdisMRegisterMiniportDriver** provides an NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS structure from the miniport driver. You must specify the correct NDIS version number. For more information about setting the NDIS version number, see [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958).

CoNDIS WAN drivers must indicate NDIS version 5.0 or later.

NDIS 6.0 and later drivers must register CoNDIS callback functions as follows:

-   To register CoNDIS *ProtocolXxx* and *MiniportXxx* functions, all CoNDIS drivers must call the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function.

-   To register its CoNDIS *MiniportXxx* functions, a miniport driver or miniport call manager (MCM) must call the **NdisSetOptionalHandlers** function from its [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function and pass it an [**NDIS\_MINIPORT\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565948) structure. To register call manager *ProtocolXxx* functions, MCMs also provide an [**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564883) structure.

-   To register its CoNDIS *ProtocolXxx* functions, a client or call managers must call the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from its [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function and must provide an [**NDIS\_PROTOCOL\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566817) structure. Clients must also provide an [**NDIS\_CO\_CLIENT\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564884) structure and call managers must also provide an [**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564883) structure.

For more information about CoNDIS driver registration, see [CoNDIS Registration](condis-registration.md).

.

 

 





