---
title: Registering Optional NDIS 6.0 Protocol Driver Entry Points
description: Registering Optional NDIS 6.0 Protocol Driver Entry Points
ms.assetid: bb26cf47-1183-470c-84f1-5cb20999a0fc
keywords:
- registering entry points
- optional entry points WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering Optional NDIS 6.0 Protocol Driver Entry Points





NDIS calls the [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function during a protocol driver call to the [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520) function. If a driver does not register optional services, set the entry point for *ProtocolSetOptions* to **NULL** in the [**NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566825) structure. To provide additional entry points, the protocol driver calls the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from *ProtocolSetOptions*.

For more information about optional services, see [Configuring Optional Protocol Driver Services](configuring-optional-protocol-driver-services.md).

 

 





