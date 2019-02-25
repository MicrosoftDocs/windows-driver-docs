---
title: USB Audio Support for Non-PCM Formats
description: USB Audio Support for Non-PCM Formats
ms.assetid: e4479a67-ec45-45f1-9c42-f050cb0f2eb2
keywords:
- USBAudio class system driver WDK audio
- non-PCM audio formats WDK , USBAudio
- raw AC-3 WDK audio
- AC-3 WDK audio
- non-PCM audio formats WDK , AC-3
- USB Audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Audio Support for Non-PCM Formats


## <span id="usb_audio_support_for_non_pcm_formats"></span><span id="USB_AUDIO_SUPPORT_FOR_NON_PCM_FORMATS"></span>


Microsoft's [USBAudio class system driver](kernel-mode-wdm-audio-components.md#usbaudio_class_system_driver), Usbaudio.sys, does not currently support USB Audio Type III formats with padded AC-3. For more information, see the *Universal Serial Bus Device Class Definition for Audio Data Formats* specification at the [USB Implementers Forum](https://go.microsoft.com/fwlink/p/?linkid=8780) website.

USBAudio can accept packed, "raw" AC-3 (as opposed to the padded, AC-3-over-S/PDIF format accepted by the PortCls driver). USBAudio supports the internal format of DirectShow's DVD-splitter filter (see [DVD Decoder Support in Windows](https://msdn.microsoft.com/library/windows/hardware/ff558763)), which can be connected directly to USBAudio under the control of KsProxy (see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877)). Specifically, the nonpadded AC-3 data range exposed by USBAudio is KSDATAFORMAT\_SUBTYPE\_AC3\_AUDIO, which is the same GUID value as MEDIASUBTYPE\_DOLBY\_AC3.

USBAudio currently does not support DirectSound playback of non-PCM audio data.

 

 




