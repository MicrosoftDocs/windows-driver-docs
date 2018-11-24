---
title: Porting Miniport Driver Check for Hang and Reset to NDIS 6.0
description: Porting Miniport Driver Check for Hang and Reset Operations to NDIS 6.0
ms.assetid: c0361e24-b1d5-407c-b69a-6fa9d768943f
keywords:
- adapters WDK networking , hang and reset operations
- hang and reset operations WDK networking
- porting miniport drivers WDK networking , hang and reset operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Adapter Check for Hang and Reset Operations to NDIS 6.0





In NDIS 6.0 miniport drivers, replace the NDIS 5.x [**MiniportCheckForHang**](https://msdn.microsoft.com/library/windows/hardware/ff549367) function with the [*MiniportCheckForHangEx*](https://msdn.microsoft.com/library/windows/hardware/ff559346) function. Also, replace NDIS 5.x [*MiniportReset*](https://msdn.microsoft.com/library/windows/hardware/ff550502) function with the [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function.

An NDIS 6.0 miniport driver's *MiniportResetEx* function differs from the NDIS 5.x *MiniportReset* function as follows:

-   NDIS 6.0 miniport drivers can complete pending OID requests and send requests in the context of a reset. NDIS no longer performs such completion for the driver. Alternatively, the miniport driver can complete pending OID requests after the reset completes.

-   Unlike the NDIS 5.x *MiniportReset* function, which can be called only at IRQL = DISPATCH\_LEVEL, the *MiniportResetEx* function can be called at IRQL &lt;= DISPATCH\_LEVEL.

For more information about check-for-hang and reset operations, see [Adapter Check-for-Hang and Reset](miniport-adapter-check-for-hang-and-reset-operations.md).

 

 





