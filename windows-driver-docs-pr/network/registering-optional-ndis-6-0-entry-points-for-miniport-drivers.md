---
title: Registering Optional NDIS 6.0 Entry Points for Miniport Drivers
description: Registering Optional NDIS 6.0 Entry Points for Miniport Drivers
ms.assetid: 1442f78f-aee4-4ee8-899f-e79af893b98c
keywords:
- registering entry points
- optional entry points WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering Optional NDIS 6.0 Entry Points for Miniport Drivers





NDIS calls the [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function during a miniport driver call to the **NdisMRegisterMiniportDriver** function. If a driver does not register optional services, set the entry point for *MiniportSetOptions* to **NULL** in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure. To overwrite the default entry points, the miniport driver calls the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from *MiniportSetOptions*.

For more information about optional services, see [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md).

 

 





