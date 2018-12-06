---
title: Threading and Synchronization Zero Level
description: Threading and Synchronization Zero Level
ms.assetid: 2baf91e8-fafb-40e2-a24c-cbf04fe45274
keywords:
- threading WDK display , zero level
- synchronization WDK display , zero level
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Threading and Synchronization Zero Level


The Windows Display Driver Model (WDDM) permits the following calls into the display miniport driver to be made in a reentrant fashion. That is, more than one thread can simultaneously enter the driver by calling the following functions:

**Note**   Although two or more threads can be running in the driver at the same time, no two threads can belong to a single process.

 

-   [*DxgkDdiCloseAllocation*](https://msdn.microsoft.com/library/windows/hardware/ff559592)

-   [*DxgkDdiCollectDbgInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559595)
    **Note**  [*DxgkDdiCollectDbgInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559595) should collect debug information for various failures and can be called at any time and at high IRQL (that is, the IRQL that *DxgkDdiCollectDbgInfo* runs at is generally undefined). In any case, *DxgkDdiCollectDbgInfo* must verify availability of the required debug information and proper synchronization. However, if the **Reason** member of the [**DXGKARG\_COLLECTDBGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff557545) structure that the *pCollectDbgInfo* parameter of *DxgkDdiCollectDbgInfo* points to is set to [VIDEO\_TDR\_TIMEOUT\_DETECTED](https://msdn.microsoft.com/library/windows/hardware/hh994433) or [VIDEO\_ENGINE\_TIMEOUT\_DETECTED](https://msdn.microsoft.com/library/windows/hardware/hh994433), the driver must ensure that *DxgkDdiCollectDbgInfo* is pageable, runs at IRQL = **PASSIVE\_LEVEL**, and supports synchronization zero level.

     

-   [*DxgkDdiControlEtwLogging*](https://msdn.microsoft.com/library/windows/hardware/ff559599)

-   [*DxgkDdiCreateAllocation*](https://msdn.microsoft.com/library/windows/hardware/ff559606)

-   [*DxgkDdiCreateContext*](https://msdn.microsoft.com/library/windows/hardware/ff559612)

-   [*DxgkDdiCreateDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559615)

-   [*DxgkDdiDescribeAllocation*](https://msdn.microsoft.com/library/windows/hardware/ff559620)

-   [*DxgkDdiDestroyAllocation*](https://msdn.microsoft.com/library/windows/hardware/ff559630)

-   [*DxgkDdiDestroyContext*](https://msdn.microsoft.com/library/windows/hardware/ff559636)

-   [*DxgkDdiDestroyDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559639)

-   [*DxgkDdiDpcRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff559645)

-   [*DxgkDdiEnumVidPnCofuncModality*](https://msdn.microsoft.com/library/windows/hardware/ff559649)

-   [*DxgkDdiGetScanLine*](https://msdn.microsoft.com/library/windows/hardware/ff559668)

-   [*DxgkDdiGetStandardAllocationDriverData*](https://msdn.microsoft.com/library/windows/hardware/ff559673)

-   [*DxgkDdiInterruptRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff559680)

-   [*DxgkDdiIsSupportedVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559684)

-   [*DxgkDdiMiracastCreateContext*](https://msdn.microsoft.com/library/windows/hardware/dn323748)

-   [*DxgkDdiMiracastDestroyContext*](https://msdn.microsoft.com/library/windows/hardware/dn323749)

-   [*DxgkDdiMiracastIoControl*](https://msdn.microsoft.com/library/windows/hardware/dn323750)

-   [*DxgkDdiMiracastQueryCaps*](https://msdn.microsoft.com/library/windows/hardware/dn323751)

-   [*DxgkDdiOpenAllocation*](https://msdn.microsoft.com/library/windows/hardware/ff559699)

-   [*DxgkDdiPresent*](https://msdn.microsoft.com/library/windows/hardware/ff559743)

-   [*DxgkDdiQueryAdapterInfo*](https://msdn.microsoft.com/library/windows/hardware/ff559746)

-   [*DxgkDdiQueryCurrentFence*](https://msdn.microsoft.com/library/windows/hardware/ff559758)

-   [*DxgkDdiRecommendFunctionalVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559775)

-   [*DxgkDdiRecommendVidPnTopology*](https://msdn.microsoft.com/library/windows/hardware/ff559782)

-   [*DxgkDdiRender*](https://msdn.microsoft.com/library/windows/hardware/ff559793)

-   [*DxgkDdiRenderKm*](https://msdn.microsoft.com/library/windows/hardware/ff559800)

-   [*DxgkDdiResetDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559808)

 

 





