---
title: Audio Data Formats
description: Audio Data Formats
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
ms.date: 02/15/2017
ms.localizationpriority: medium
---

# Audio Data Formats


## <span id="audio_data_formats"></span><span id="AUDIO_DATA_FORMATS"></span>


To specify the data format for a wave audio stream, the [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) structure is followed immediately by either a [**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex) or [**KSDSOUND\_BUFFERDESC**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdsound_bufferdesc) structure, and the **Specifier** member of KSDATAFORMAT is accordingly set to one of the following two values:

-   KSDATAFORMAT\_SPECIFIER\_WAVEFORMATEX

    Indicates that the data format belongs to a wave stream that is being used by a waveIn or waveOut application. In this case, if the KSDATAFORMAT structure's *FormatSize* is large enough, the data-format specifier following the KSDATAFORMAT structure is a WAVEFORMATEX structure.

-   KSDATAFORMAT\_SPECIFIER\_DSOUND

    Indicates that the data format belongs to a wave stream that is being used by a DirectSound application. In this case, the data-format specifier following the KSDATAFORMAT structure is a KSDSOUND\_BUFFERDESC structure, which contains an embedded WAVEFORMATEX structure.

The [**KSDATAFORMAT\_WAVEFORMATEX**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdataformat_waveformatex) structure encapsulates both a KSDATAFORMAT structure and the WAVEFORMATEX structure that follows it. Similarly, the [**KSDATAFORMAT\_DSOUND**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdataformat_dsound) structure encapsulates both a KSDATAFORMAT structure and the DSOUND\_BUFFERDESC structure that follows it.

For either KSDATAFORMAT\_WAVEFORMATEX or KSDATAFORMAT\_DSOUND, the last item in the structure is an embedded WAVEFORMATEX structure; in the case of KSDATAFORMAT\_DSOUND, the WAVEFORMATEX structure is contained in the embedded DSOUND\_BUFFERDESC structure. In either case, the WAVEFORMATEX structure might be the beginning of a [**WAVEFORMATEXTENSIBLE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-waveformatextensible) structure, in which case the **wFormatTag** member of WAVEFORMATEX is set to the value WAVE\_FORMAT\_EXTENSIBLE. For more information, see [Extensible Wave-Format Descriptors](extensible-wave-format-descriptors.md).

To specify the data format for a MIDI stream or DirectMusic stream, the KSDATAFORMAT structure is sufficient; it is not followed by any additional information.

For examples of wave and DirectSound data formats, see [PCM Stream Data Format](pcm-stream-data-format.md) and [DirectSound Stream Data Format](directsound-stream-data-format.md). For examples of MIDI and DirectMusic data formats, see [MIDI Stream Data Format](midi-stream-data-format.md) and [DirectMusic Stream Data Format](directmusic-stream-data-format.md).

 

