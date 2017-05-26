---
title: Video Decoding
description: Video Decoding
ms.assetid: 4e8bf7e9-7a3c-4732-9ac0-4f6f5ef07552
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , video decoding
- Video Acceleration WDK DirectX , video decoding
- VA WDK DirectX , video decoding
- decoding video WDK DirectX VA , about decoding video
- video decoding WDK DirectX VA , about decoding video
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Video Decoding


## <span id="ddk_video_decoding_gg"></span><span id="DDK_VIDEO_DECODING_GG"></span>


DirectX VA permits one or more stages of the video decoding process to be divided between the [*host CPU*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-host-cpu) and the video hardware accelerator. The accelerator executes the [motion-compensated prediction](motion-compensated-prediction.md) (MCP), and may also execute the inverse discrete-cosine transform (IDCT) and the variable-length decoding (VLD) stages of the decoding process.

The DirectX VA API decodes a single video stream. Support of multiple video streams requires a separate DirectX VA session for each video stream (for example, a separate pair of output and input pins for the video decoder and acceleration driver to use in filter graph operation). For more information about a filter graph, see [KS Minidriver Architecture](https://msdn.microsoft.com/library/windows/hardware/ff567656).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Video%20Decoding%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




