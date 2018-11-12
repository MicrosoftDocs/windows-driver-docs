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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Decoding


## <span id="ddk_video_decoding_gg"></span><span id="DDK_VIDEO_DECODING_GG"></span>


DirectX VA permits one or more stages of the video decoding process to be divided between the [*host CPU*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-host-cpu) and the video hardware accelerator. The accelerator executes the [motion-compensated prediction](motion-compensated-prediction.md) (MCP), and may also execute the inverse discrete-cosine transform (IDCT) and the variable-length decoding (VLD) stages of the decoding process.

The DirectX VA API decodes a single video stream. Support of multiple video streams requires a separate DirectX VA session for each video stream (for example, a separate pair of output and input pins for the video decoder and acceleration driver to use in filter graph operation). For more information about a filter graph, see [KS Minidriver Architecture](https://msdn.microsoft.com/library/windows/hardware/ff567656).

 

 





