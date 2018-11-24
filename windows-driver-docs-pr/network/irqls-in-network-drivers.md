---
title: IRQLs in Network Drivers
description: IRQLs in Network Drivers
ms.assetid: d8720084-460e-4b62-90de-abfd96cd6364
keywords:
- network drivers WDK , IRQLs
- IRQLs WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IRQLs in Network Drivers





Every driver function called by NDIS runs at a system-determined IRQL (one of PASSIVE\_LEVEL &lt; DISPATCH\_LEVEL &lt; DIRQL). For example, a miniport driver's initialization function, halt function, reset function, and sometimes the shutdown function commonly run at PASSIVE\_LEVEL. Interrupt code runs at DIRQL, so an NDIS intermediate or protocol driver never runs at DIRQL. All other NDIS driver functions run at IRQL &lt;= DISPATCH\_LEVEL.

The IRQL at which a driver function runs affects which NDIS functions it can call. Certain functions can be called only at IRQL = PASSIVE\_LEVEL. Others can be called at DISPATCH\_LEVEL or lower. You should check every NDIS function for IRQL restrictions.

Any driver function that shares resources with the driver's interrupt service routine (ISR) must be able to raise its IRQL to DIRQL to prevent race conditions. NDIS provides such a mechanism.

 

 





