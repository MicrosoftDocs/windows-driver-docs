---
title: Threading and Synchronization Zero Level
description: Threading and Synchronization Zero Level
ms.assetid: 2baf91e8-fafb-40e2-a24c-cbf04fe45274
keywords:
- threading WDK display , zero level
- synchronization WDK display , zero level
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Threading%20and%20Synchronization%20Zero%20Level%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




