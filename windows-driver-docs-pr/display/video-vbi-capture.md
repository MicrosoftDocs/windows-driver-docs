---
title: Video VBI Capture
description: Video VBI Capture
ms.assetid: 40544838-8678-4832-8e6f-e96202f987ad
keywords:
- video VBI capture WDK DirectDraw
- vertical blanking interval WDK DirectDraw
- VBI WDK DirectDraw
- DxTransfer
- DxApi miniport drivers WDK DirectDraw , VBI capture
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Video VBI Capture


## <span id="ddk_video_vbi_capture_gg"></span><span id="DDK_VIDEO_VBI_CAPTURE_GG"></span>


DirectX 5.2 introduced two DirectDraw driver functions for video vertical blanking interval (VBI) capture. These functions are [*DxTransfer*](https://msdn.microsoft.com/library/windows/hardware/ff562887) and [*DxGetTransferStatus*](https://msdn.microsoft.com/library/windows/hardware/ff557438).

The *DxTransfer* function facilitates video and VBI capture. Because this function is called at IRQ time, it must return as quickly as possible. If the display hardware is not ready to do a bus master at the time *DxTransfer* is called, then the video miniport driver should keep an internal queue of a number of bus masters (the actual number of bus masters saved in the queue is up to the driver developer). This allows the hardware to perform the bus master when the hardware is ready. In other words, the driver should not poll and wait for the bus master to complete.

When DirectDraw calls the *DxTransfer* function, it supplies a transfer ID in the **dwTransferID** member of the [**DDTRANSFERININFO**](https://msdn.microsoft.com/library/windows/hardware/ff550356) structure. The video miniport driver can then use this identification when the *DxGetTransferStatus* function is called.

When a bus master completes, the display hardware must generate an IRQ. The video miniport driver must then call the [**IRQCallback**](https://msdn.microsoft.com/library/windows/hardware/ff568158) function that was specified in [*DxEnableIRQ*](https://msdn.microsoft.com/library/windows/hardware/ff557413). In this **IRQCallback** call, the video miniport driver specifies the DDIRQ\_BUSMASTER flag. DirectDraw then calls the [*DxGetTransferStatus*](https://msdn.microsoft.com/library/windows/hardware/ff557438) function to determine which bus master completed. The video miniport driver must return the transfer ID (**dwTransferID**) that DirectDraw passed to the driver in an earlier *DxTransfer* call. In this way, if the driver has five bus masters in the queue, DirectDraw can determine which one completed most recently.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Video%20VBI%20Capture%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




