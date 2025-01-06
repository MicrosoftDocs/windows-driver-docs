---
title: Driver Residency in WDDM 2.0
description: This section provides details about the driver residency changes for Windows Display Driver Model (WDDM) 2.0. The functionality described is available starting with Windows 10.
keywords:
- WDDM 2.0 , driver residency
ms.date: 12/18/2024
---

# Driver residency in WDDM 2.0

The driver residency model changed in WDDM 2.0. The changes are available starting with Windows 10, and are described in the following articles.

| Article | Description |
| ------- | ----------- |
| [Residency overview](residency-overview.md) | Starting in WDDM 2.0, residency is moved to an explicit list on the device instead of the per-command buffer list. The video memory manager (*VidMm*) ensures that all allocations on a particular device residency requirement list are resident before any contexts belonging to that device are scheduled for execution. |
| [Allocation usage tracking](allocation-usage-tracking.md) | With the allocation list going away, *VidMm* no longer has visibility into the allocations being referenced in a particular command buffer. As a result, *VidMm* is no longer in a position to track allocation usage or handle related synchronization. This responsibility now falls to the user-mode driver (UMD). In particular, the UMD has to handle the synchronization with respect to direct CPU access to allocations and renaming. |
| [Offer and reclaim changes](offer-and-reclaim-changes.md) | Starting in WDDM 2.0, requirements around *Offer* and *Reclaim* are relaxed. UMDs are no longer required to use offer and reclaim on internal allocations. Idle and suspended applications instead get rid of driver internal resources by using the [**Trim**](/uwp/api/windows.graphics.directx.direct3d11.idirect3ddevice.trim?view=winrt-26100) method. |
| [Access to nonresident allocation](access-to-non-resident-allocation.md) | GPU access to allocations that aren't resident is illegal and will result in the device removed for the application that generated the error. |
| [Process residency budgets](process-residency-budgets.md) | Starting in WDDM 2.0, processes are assigned budgets for how much memory they can keep resident. This budget can change over time, but generally will only be imposed when the system is under memory pressure. |
