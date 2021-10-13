---
title: Pageable and Discardable Code in a Protocol Driver
description: Pageable and Discardable Code in a Protocol Driver
keywords:
- protocol drivers WDK networking , pageable and discardable code
- NDIS protocol drivers WDK , pageable and discardable code
- pageable and discardable code WDK NDIS protocol
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pageable and Discardable Code in a Protocol Driver





Driver developers should designate code as pageable whenever possible, freeing system space for code that must be memory-resident. You can mark functions as pageable with the [**NDIS\_PAGEABLE\_FUNCTION**](/previous-versions/windows/hardware/network/ff557121(v=vs.85)) macro. The IRQL, resource management features, and other characteristics of a function might prohibit the function from being pageable.

Every *ProtocolXxx* function runs at an IRQL in the range from PASSIVE\_LEVEL to DISPATCH\_LEVEL. Functions that run exclusively at IRQL = PASSIVE\_LEVEL should be marked as pageable.

A driver function that runs at IRQL = PASSIVE\_LEVEL can be made pageable as long as it neither calls nor is called by any function that runs at IRQL &gt;= DISPATCH\_LEVEL--such as a function that acquires a spin lock. Acquiring a spin lock causes the IRQL of the acquiring thread to be raised to DISPATCH\_LEVEL. A driver function, such as [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex), that runs at IRQL = PASSIVE\_LEVEL must not call any **Ndis*Xxx*** functions that run at IRQL &gt;= DISPATCH\_LEVEL if that driver function is marked as pageable code. For more information about the IRQL for each **Ndis*Xxx*** function, see [NDIS Library Functions](/previous-versions/windows/hardware/network/ff557039(v=vs.85)).

The [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function of NDIS protocol drivers, as well as code that is called only from **DriverEntry**, should be specified as initialization-only code, by using the [**NDIS\_INIT\_FUNCTION**](/previous-versions/windows/hardware/network/ff557007(v=vs.85)) macro. Code that is identified with this macro is assumed to run only once at system initialization time, and, as a result, is mapped only during that time. After a function marked as initialization-only returns, it is discarded.

 

