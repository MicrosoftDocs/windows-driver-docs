---
title: Supporting Non-PCM Wave Formats
description: Supporting Non-PCM Wave Formats
ms.assetid: 76455e1f-4b00-49c4-a4e4-3cb4abe8f445
keywords:
- non-PCM audio formats WDK
- WDM audio drivers WDK , non-PCM wave formats
- audio drivers WDK , non-PCM wave formats
- formats WDK audio , non-PCM
- PCM formats WDK audio
- audio non-PCM formats WDK
ms.date: 10/27/2017
ms.localizationpriority: medium
---

# Supporting Non-PCM Wave Formats


## <span id="supporting_non_pcm_wave_formats"></span><span id="SUPPORTING_NON_PCM_WAVE_FORMATS"></span>

This section describes limitations in earlier versions of Windows that prevented clients from playing non-PCM audio, and presents a set of guidelines for adapting a WDM audio driver to support non-PCM data formats on more recent versions of Windows.

Additionally, this section describes the new subformat GUIDs in Windows 7 that provide support for compressed audio formats.

This section includes the following topics:

[Background of Non-PCM Support](background-of-non-pcm-support.md)

[Requirements for a Non-PCM Pin Factory](requirements-for-a-non-pcm-pin-factory.md)

[Subformat GUIDs for Compressed Audio Formats](subformat-guids-for-compressed-audio-formats.md)

[Converting Between Format Tags and Subformat GUIDs](converting-between-format-tags-and-subformat-guids.md)

[KS Topology Considerations](ks-topology-considerations.md)

[Specifics for waveOut Clients](specifics-for-waveout-clients.md)

[Specifics for DirectSound Clients](specifics-for-directsound-clients.md)

[S/PDIF Pass-Through Transmission of Non-PCM Streams](s-pdif-pass-through-transmission-of-non-pcm-streams.md)

[Specifying AC-3 Data Ranges](specifying-ac-3-data-ranges.md)

[Specifying WMA Pro Data Ranges](specifying-wma-pro-data-ranges.md)

[USB Audio Support for Non-PCM Formats](usb-audio-support-for-non-pcm-formats.md)


 

 




