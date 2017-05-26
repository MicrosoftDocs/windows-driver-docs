---
title: Handling Wake-Up Events
description: Handling Wake-Up Events
ms.assetid: 4989d5a4-158c-41db-ab2d-fc995b67a822
keywords:
- wake-up capabilities WDK networking , handling wake-up events
- bus-specific wake-up lines WDK networking
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Wake-Up Events


## <a href="" id="ddk-handling-wake-up-events-ng"></a>


A miniport driver does not handle a wake-up event detected by a NIC. When a NIC detects an enabled wake-up event, it asserts a bus-specific wake-up line. The power manager then sends a power IRP to NDIS, which, in response, sends the miniport driver an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) OID that requests the miniport driver to put a NIC in the highest-powered (D0) state.

 

 





