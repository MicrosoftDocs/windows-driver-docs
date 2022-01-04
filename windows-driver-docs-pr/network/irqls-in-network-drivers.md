---
title: IRQLs in Network Drivers
description: IRQLs in Network Drivers
keywords:
- network drivers WDK , IRQLs
- IRQLs WDK networking
ms.date: 11/26/2018
---

# IRQLs in Network Drivers

Every driver function called by NDIS runs at a system-determined IRQL (one of PASSIVE\_LEVEL &lt; DISPATCH\_LEVEL &lt; DIRQL). For example, a miniport driver's [initialization](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function, [halt](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function, [reset](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset) function, and [shutdown](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_shutdown) function commonly run at PASSIVE\_LEVEL, although the reset and shutdown functions can be invoked at a higher IRQL if the system requires it. Interrupt code runs at DIRQL, so an NDIS intermediate or protocol driver never runs at DIRQL. All other NDIS driver functions run at or below IRQL = DISPATCH\_LEVEL.

The IRQL at which a driver function runs affects which NDIS functions it can call. Certain functions can be called only at IRQL = PASSIVE\_LEVEL. Others can be called at DISPATCH\_LEVEL or lower. You should check every NDIS function for IRQL restrictions.

Any driver function that shares resources with the driver's interrupt service routine (ISR) must be able to raise its IRQL to DIRQL to prevent race conditions. NDIS provides such a mechanism.
