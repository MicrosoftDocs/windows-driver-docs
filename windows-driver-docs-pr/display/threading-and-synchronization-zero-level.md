---
title: Threading and Synchronization Zero Level
description: Threading and Synchronization Zero Level
keywords:
- threading WDK display , zero level
- synchronization WDK display , zero level
ms.date: 04/18/2022
---

# Threading and Synchronization Zero Level

The Windows Display Driver Model (WDDM) permits the following calls into the display miniport driver to be made in a reentrant fashion. That is, more than one thread can simultaneously enter the driver by calling the functions listed below.

> [!NOTE]
> Although two or more threads can be running in the driver at the same time, no two threads can belong to a single process.

- [*DxgkDdiCheckMultiPlaneOverlaySupport3*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport3) (or [*DxgkDdiCheckMultiPlaneOverlaySupport2*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport2)/[*DxgkDdiCheckMultiPlaneOverlaySupport*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_checkmultiplaneoverlaysupport))
- [*DxgkDdiCloseAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_closeallocation)
- [*DxgkDdiCollectDbgInfo*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_collectdbginfo). This function should collect debug information for various failures and can be called at any time and at high IRQL (that is, the IRQL that *DxgkDdiCollectDbgInfo* runs at is generally undefined). In all cases, *DxgkDdiCollectDbgInfo* must verify availability of the required debug information and proper synchronization. However, if the **Reason** member of the [**DXGKARG_COLLECTDBGINFO**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_collectdbginfo) structure that the *pCollectDbgInfo* parameter points to is set to [VIDEO_TDR_TIMEOUT_DETECTED](../debugger/bug-check-code-reference2.md) or [VIDEO_ENGINE_TIMEOUT_DETECTED](../debugger/bug-check-code-reference2.md), the driver must ensure that *DxgkDdiCollectDbgInfo* is pageable, runs at IRQL = **PASSIVE_LEVEL**, and supports synchronization zero level.
- [*DxgkDdiControlEtwLogging*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_control_etw_logging)
- [*DxgkDdiCreateAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation)
- [*DxgkDdiCreateContext*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createcontext)
- [*DxgkDdiCreateDevice*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createdevice)
- [*DxgkDdiDescribeAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_describeallocation)
- [*DxgkDdiDestroyAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroyallocation)
- [*DxgkDdiDestroyContext*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroycontext)
- [*DxgkDdiDestroyDevice*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_destroydevice)
- [*DxgkDdiDpcRoutine*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_dpc_routine)
- [*DxgkDdiEnumVidPnCofuncModality*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_enumvidpncofuncmodality)
- [*DxgkDdiGetScanLine*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getscanline)
- [*DxgkDdiGetStandardAllocationDriverData*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getstandardallocationdriverdata)
- [*DxgkDdiInterruptRoutine*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_interrupt_routine)
- [*DxgkDdiIsSupportedVidPn*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_issupportedvidpn)
- [*DxgkDdiMiracastCreateContext*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_create_context)
- [*DxgkDdiMiracastDestroyContext*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_destroy_context)
- [*DxgkDdiMiracastIoControl*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_handle_io_control)
- [*DxgkDdiMiracastQueryCaps*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_miracast_query_caps)
- [*DxgkDdiOpenAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_openallocationinfo)
- [*DxgkDdiPresent*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_present)
- [*DxgkDdiQueryAdapterInfo*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_queryadapterinfo)
- [*DxgkDdiQueryCurrentFence*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_querycurrentfence)
- [*DxgkDdiRecommendFunctionalVidPn*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_recommendfunctionalvidpn)
- [*DxgkDdiRecommendVidPnTopology*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_recommendvidpntopology)
- [*DxgkDdiRender*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_render)
- [*DxgkDdiRenderKm*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_renderkm)
- [*DxgkDdiResetDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_reset_device)
