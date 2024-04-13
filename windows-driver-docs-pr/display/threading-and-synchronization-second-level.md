---
title: Threading and Synchronization Level Two
description: Threading and Synchronization Level Two
keywords:
- threading WDK display , Level Two
- synchronization WDK display , Level Two
ms.date: 10/03/2023
---

# Threading and Synchronization Level Two

Level Two threading and synchronization is the same as [Level Three](threading-and-synchronization-third-level.md), except that video memory is not evicted to host CPU memory. In other words, WDDM guarantees that:

* Only a single thread (the calling thread) is within the display miniport driver.
* The graphics hardware is idle.
* No direct memory access (DMA) buffers are currently being processed by the driver or passed through the GPU scheduler.

In order for some calls to be made under Level Two, the **HardwareAccess** flag must be set within the **D3DDDI_ESCAPEFLAGS** structure that is a member of **DXGKARG_ESCAPE**. If this flag is not set, then the call will fail.

The following list contains some of the calls into the display miniport driver that are made under Level Two:

* [**DxgkDdiCommitVidPn**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_commitvidpn)

* [**DxgkDdiControlInterrupt**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_controlinterrupt)

* [**DxgkDdiDispatchIoRequest**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_dispatch_io_request)

* [**DxgkDdiEscape**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_escape)

* [**DxgkDdiNotifyAcpiEvent**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_notify_acpi_event)

* [**DxgkDdiQueryInterface**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface)

* [**DxgkDdiRecommendFunctionalVidPn**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_recommendfunctionalvidpn)

* [**DxgkDdiRecommendMonitorModes**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_recommendmonitormodes)

* [**DxgkDdiSetPalette**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setpalette)

* [**DxgkDdiSetTimingsFromVidPn**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_settimingsfromvidpn)

* [**DxgkDdiSetVidPnSourceAddress**](/previous-versions/windows/hardware/drivers/ff560767(v=vs.85))

* [**DxgkDdiSetVidPnSourceVisibility**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_setvidpnsourcevisibility)

* [**DxgkDdiUpdateActiveVidPnPresentPath**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_updateactivevidpnpresentpath)
