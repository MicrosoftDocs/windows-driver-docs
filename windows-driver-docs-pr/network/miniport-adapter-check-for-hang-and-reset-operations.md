---
title: Miniport Adapter Check-for-Hang and Reset Operations
description: Miniport Adapter Check-for-Hang and Reset Operations
ms.assetid: 53ffc5a9-bcba-4189-8845-73adfcf6816d
keywords:
- miniport adapters WDK networking , check-for-hang operations
- miniport adapters WDK networking , reset operations
- adapters WDK networking , check-for-hang operations
- adapters WDK networking , reset operations
- MiniportCheckForHangEx
- hang and reset o
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Adapter Check-for-Hang and Reset Operations

## Overview

> [!WARNING]
> Check-for-Hang (CFH) and Reset operations are discouraged for all NDIS 6.83 and later drivers. For more information, see [Check-for-Hang and Reset operations in NDIS 6.83 and later](#check-for-hang-and-reset-operations-in-ndis-683-and-later).

NDIS calls an NDIS miniport driver's [*MiniportCheckForHangEx*](https://msdn.microsoft.com/library/windows/hardware/ff559346) function to check the operational state of an NDIS adapter that represents a network interface card (NIC). *MiniportCheckForHangEx* checks the internal state of the adapter and returns **TRUE** if it detects that the adapter is not operating correctly.

By default, NDIS calls *MiniportCheckForHangEx* approximately every 2 seconds. If *MiniportCheckForHangEx* returns **TRUE**, NDIS calls the NDIS miniport driver's [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) function. If the default time-out value of 2 seconds is too small, your miniport driver can set a different value at initialization time as follows:

1.  Set the **CheckForHangTimeInSeconds** member of the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565934) structure to a nonzero value.
2.  Pass the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565934) structure in the *MiniportAttributes* parameter of the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function.

For more information about setting driver attributes, see [Initializing an Adapter](initializing-a-miniport-adapter.md).
The value of **CheckForHangTimeInSeconds** should be greater than the initialize time of your miniport driver. However, if your driver takes longer than **CheckForHangTimeInSeconds** seconds to initialize, this time-out expires, causing NDIS to call your driver's *MiniportCheckForHangEx* function. If *MiniportCheckForHangEx* returns **TRUE**, NDIS will then call your driver's *MiniportResetEx* function. For this reason, you should synchronize your driver's [*MiniportCheckForHangEx*](https://msdn.microsoft.com/library/windows/hardware/ff559346) function with driver initialization so that *MiniportCheckForHangEx* will not return **TRUE** if the driver has not finished initializing.

If your miniport driver does not complete an OID request within two successive calls to *MiniportCheckForHangEx*, NDIS can call the driver's *MiniportResetEx* function. For some OID requests, NDIS calls *MiniportResetEx* if the driver does not complete the request within four successive calls to *MiniportCheckForHangEx*.

The reset operation does not affect [miniport adapter operational states](miniport-adapter-states-and-operations.md). Also, the state of the adapter might change while a reset operation is in progress. For example, NDIS might call a driver's [*MiniportPause*](https://msdn.microsoft.com/library/windows/hardware/ff559418) function when there is a reset operation in progress. In this case, the driver can complete either the reset or the pause operation in any order while following the normal requirements for each operation.

For a reset operation, the driver can fail transmit request packets or it can keep them queued and complete them later. However, you should note that an overlying driver cannot complete a pause operation while its transmit packets are pending.

A miniport driver can complete a reset request synchronously by returning a success or failure status. The driver can complete a reset request asynchronously by returning **NDIS\_STATUS\_PENDING**. In this case, the driver must call [**NdisMResetComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563663) to complete the operation.

## Check-for-Hang and Reset operations in NDIS 6.83 and later

In versions of NDIS before 6.83, Check-for-Hang (CFH) and Reset operations were discouraged for Always On, Always Connected (AOAC) systems due to battery life issues. However, drivers could still use CFH on other non-AOAC Windows systems by implementing the optional [*MiniportCheckForHangEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_check_for_hang) and [*MiniportResetEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_reset) callback functions. 

Starting in NDIS 6.83, these callback functions are discouraged on **all** Windows systems regardless of power capabilities. Although it is not a logo test violation to use CFH in NDIS 6.83 and later, NDIS drivers should use the following table for guidance about its usage.

| Caller | Recommendation | Notes |
| --- | --- | --- |
| Drivers targeting AOAC systems | Must not implement | Causes battery life issues due to periodic check-for-hang activity |
| Drivers targeting Windows Server systems | Must not implement | Causes issues when the CPU is stressed |
| Virtual (software-only) miniport drivers | Must not implement | Reset not possible without hardware |
| Other new NDIS 6.83 and later drivers | Should not implement |
| Other existing NDIS 6.82 and earlier code | Not required to change, but should consider removing Check-for-Hang and Reset in future rework |

## Related topics


[Miniport Driver Hardware Reset](hardware-reset.md)

[Miniport Driver Reset and Halt Functions](https://msdn.microsoft.com/library/windows/hardware/ff564064)

 

 






