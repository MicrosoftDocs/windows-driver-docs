---
title: Video VBI Capture
description: Video VBI Capture
keywords:
- video VBI capture WDK DirectDraw
- vertical blanking interval WDK DirectDraw
- VBI WDK DirectDraw
- DxTransfer
- DxApi miniport drivers WDK DirectDraw , VBI capture
ms.date: 04/20/2017
---

# Video VBI Capture


## <span id="ddk_video_vbi_capture_gg"></span><span id="DDK_VIDEO_VBI_CAPTURE_GG"></span>


DirectX 5.2 introduced two DirectDraw driver functions for video vertical blanking interval (VBI) capture. These functions are [*DxTransfer*](/windows/win32/api/dxmini/nc-dxmini-pdx_transfer) and [*DxGetTransferStatus*](/windows/win32/api/dxmini/nc-dxmini-pdx_gettransferstatus).

The *DxTransfer* function facilitates video and VBI capture. Because this function is called at IRQ time, it must return as quickly as possible. If the display hardware is not ready to do a bus master at the time *DxTransfer* is called, then the video miniport driver should keep an internal queue of a number of bus masters (the actual number of bus masters saved in the queue is up to the driver developer). This allows the hardware to perform the bus master when the hardware is ready. In other words, the driver should not poll and wait for the bus master to complete.

When DirectDraw calls the *DxTransfer* function, it supplies a transfer ID in the **dwTransferID** member of the [**DDTRANSFERININFO**](/windows/win32/api/dxmini/ns-dxmini-ddtransferininfo) structure. The video miniport driver can then use this identification when the *DxGetTransferStatus* function is called.

When a bus master completes, the display hardware must generate an IRQ. The video miniport driver must then call the [**IRQCallback**](/windows/win32/api/dxmini/nc-dxmini-pdx_irqcallback) function that was specified in [*DxEnableIRQ*](/windows/win32/api/dxmini/nc-dxmini-pdx_enableirq). In this **IRQCallback** call, the video miniport driver specifies the DDIRQ\_BUSMASTER flag. DirectDraw then calls the [*DxGetTransferStatus*](/windows/win32/api/dxmini/nc-dxmini-pdx_gettransferstatus) function to determine which bus master completed. The video miniport driver must return the transfer ID (**dwTransferID**) that DirectDraw passed to the driver in an earlier *DxTransfer* call. In this way, if the driver has five bus masters in the queue, DirectDraw can determine which one completed most recently.

 

