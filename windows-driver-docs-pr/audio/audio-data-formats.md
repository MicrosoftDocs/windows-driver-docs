---
title: Audio Data Formats
description: Audio Data Formats
ms.assetid: e16c10ea-0193-4cf4-91a3-4f8d4a0d5cf6
keywords:
- data formats WDK audio
- formats WDK audio , data
- audio data formats WDK
- wave streams WDK audio
- digital formats WDK audio
- stream formats WDK audio
- KS data formats WDK audio
- KSDATAFORMAT structure
- WDM audio data formats WDK
- formats WDK audio
- data formats WDK audio , about audio data formats
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Audio Data Formats


## <span id="audio_data_formats"></span><span id="AUDIO_DATA_FORMATS"></span>


To specify the data format for a wave audio stream, the [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) structure is followed immediately by either a [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799) or [**KSDSOUND\_BUFFERDESC**](https://msdn.microsoft.com/library/windows/hardware/ff537121) structure, and the **Specifier** member of KSDATAFORMAT is accordingly set to one of the following two values:

-   KSDATAFORMAT\_SPECIFIER\_WAVEFORMATEX

    Indicates that the data format belongs to a wave stream that is being used by a waveIn or waveOut application. In this case, the data-format specifier following the KSDATAFORMAT structure is a WAVEFORMATEX structure.

-   KSDATAFORMAT\_SPECIFIER\_DSOUND

    Indicates that the data format belongs to a wave stream that is being used by a DirectSound application. In this case, the data-format specifier following the KSDATAFORMAT structure is a KSDSOUND\_BUFFERDESC structure, which contains an embedded WAVEFORMATEX structure.

The [**KSDATAFORMAT\_WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff537095) structure encapsulates both a KSDATAFORMAT structure and the WAVEFORMATEX structure that follows it. Similarly, the [**KSDATAFORMAT\_DSOUND**](https://msdn.microsoft.com/library/windows/hardware/ff537094) structure encapsulates both a KSDATAFORMAT structure and the DSOUND\_BUFFERDESC structure that follows it.

For either KSDATAFORMAT\_WAVEFORMATEX or KSDATAFORMAT\_DSOUND, the last item in the structure is an embedded WAVEFORMATEX structure; in the case of KSDATAFORMAT\_DSOUND, the WAVEFORMATEX structure is contained in the embedded DSOUND\_BUFFERDESC structure. In either case, the WAVEFORMATEX structure might be the beginning of a [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802) structure, in which case the **wFormatTag** member of WAVEFORMATEX is set to the value WAVE\_FORMAT\_EXTENSIBLE. For more information, see [Extensible Wave-Format Descriptors](extensible-wave-format-descriptors.md).

To specify the data format for a MIDI stream or DirectMusic stream, the KSDATAFORMAT structure is sufficient; it is not followed by any additional information.

For examples of wave and DirectSound data formats, see [PCM Stream Data Format](pcm-stream-data-format.md) and [DirectSound Stream Data Format](directsound-stream-data-format.md). For examples of MIDI and DirectMusic data formats, see [MIDI Stream Data Format](midi-stream-data-format.md) and [DirectMusic Stream Data Format](directmusic-stream-data-format.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Data%20Formats%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


