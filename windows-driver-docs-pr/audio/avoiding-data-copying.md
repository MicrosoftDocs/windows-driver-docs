---
title: Avoiding Data Copying
description: Avoiding Data Copying
ms.assetid: bf4dab5e-5800-4888-af96-68a152ac5e39
keywords:
- data copying WDK audio
- copying audio data
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Avoiding Data Copying


## <span id="avoiding_data_copying"></span><span id="AVOIDING_DATA_COPYING"></span>


You can improve driver performance by designing your audio hardware to avoid unnecessary data copying.

You can achieve the best results by implementing your hardware to perform true scatter/gather DMA and by writing a WavePci miniport driver to manage the hardware. Your device can then directly access playback data buffers or empty record buffers wherever they are located in system memory. This eliminates a lot of unnecessary software intervention and time-consuming data copying.

If you are designing a WaveCyclic device, however, you can improve its performance by making its hardware buffer directly accessible as system memory. This eliminates the overhead of copying data from an intermediate buffer in system memory.

Also, if your device requires an audio format with a channel ordering that is incompatible with the standard WDM audio formats, the driver might have to perform in-place conversion of each audio frame in an intermediate buffer before the hardware can process it. This can degrade performance. For additional information, see the white paper titled Multiple Channel Audio Data and WAVE Files at the [audio technology](https://go.microsoft.com/fwlink/p/?linkid=8751) website.

 

 




