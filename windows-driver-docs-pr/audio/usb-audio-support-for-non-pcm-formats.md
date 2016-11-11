---
title: USB Audio Support for Non-PCM Formats
description: USB Audio Support for Non-PCM Formats
ms.assetid: e4479a67-ec45-45f1-9c42-f050cb0f2eb2
keywords: ["USBAudio class system driver WDK audio", "non-PCM audio formats WDK , USBAudio", "raw AC-3 WDK audio", "AC-3 WDK audio", "non-PCM audio formats WDK , AC-3", "USB Audio"]
---

# USB Audio Support for Non-PCM Formats


## <span id="usb_audio_support_for_non_pcm_formats"></span><span id="USB_AUDIO_SUPPORT_FOR_NON_PCM_FORMATS"></span>


Microsoft's [USBAudio class system driver](kernel-mode-wdm-audio-components.md#usbaudio_class_system_driver), Usbaudio.sys, does not currently support USB Audio Type III formats with padded AC-3. For more information, see the *Universal Serial Bus Device Class Definition for Audio Data Formats* specification at the [USB Implementers Forum](http://go.microsoft.com/fwlink/p/?linkid=8780) website.

USBAudio can accept packed, "raw" AC-3 (as opposed to the padded, AC-3-over-S/PDIF format accepted by the PortCls driver). USBAudio supports the internal format of DirectShow's DVD-splitter filter (see [DVD Decoder Support in Windows](https://msdn.microsoft.com/library/windows/hardware/ff558763)), which can be connected directly to USBAudio under the control of KsProxy (see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877)). Specifically, the nonpadded AC-3 data range exposed by USBAudio is KSDATAFORMAT\_SUBTYPE\_AC3\_AUDIO, which is the same GUID value as MEDIASUBTYPE\_DOLBY\_AC3.

USBAudio currently does not support DirectSound playback of non-PCM audio data.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20USB%20Audio%20Support%20for%20Non-PCM%20Formats%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


