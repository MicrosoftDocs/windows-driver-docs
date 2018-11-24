---
title: Miniport Adapter Context
description: Miniport Adapter Context
ms.assetid: cb43d02d-cf52-46a4-b56d-aa3afcbd0ca5
keywords:
- logical adapters WDK networking
- context WDK miniport adapter
- miniport adapters WDK networking , context
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Adapter Context





NDIS uses a software object called a *miniport adapter* to represent each virtual or physical network device in the system. This object is maintained by NDIS and is opaque to the miniport driver and to protocol drivers. NDIS passes a handle to this structure to the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function. The miniport driver subsequently supplies this handle in all calls to **Ndis*Xxx*** functions that pertain to the miniport adapter that the handle specifies.

When a miniport driver is called to initialize a miniport adapter that it manages, it creates its own internal data structure to represent the miniport adapter. The driver uses this structure, referred to as the *miniport adapter context*, to maintain device-specific state information that the driver needs to manage the miniport adapter. The driver passes a handle to this structure to NDIS. For more information about specifying the miniport adapter context, see [Initializing an Adapter](initializing-a-miniport-adapter.md).

When NDIS calls one of the miniport driver's *MiniportXxx* functions that pertains to a miniport adapter, NDIS passes the miniport adapter context to identify the correct miniport adapter to the driver. The miniport adapter context is owned and maintained by the miniport driver and is opaque to NDIS and to protocol drivers.

 

 





