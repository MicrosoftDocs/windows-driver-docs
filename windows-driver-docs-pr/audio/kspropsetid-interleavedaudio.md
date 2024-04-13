---
title: KSPROPSETID\_InterleavedAudio
description: The KSPROPSETID\_InterleavedAudio property set is implemented by audio device drivers that would like to provide extra information about the interleaving of loopback audio and capture audio.
ms.date: 12/13/2018
---

# KSPROPSETID\_InterleavedAudio

The **KSPROPSETID\_InterleavedAudio** property set is implemented by audio device drivers that would like to contain extra information about the interleaving of loopback audio and capture audio in the audio stream.

**KSPROPSETID\_InterleavedAudio** is available with Windows 10 version 19H1 and later versions of Windows.

The *ksmedia.h* header file defines the **KSPROPSETID\_InterleavedAudio** property set as follows:

``` syntax
#define STATIC_KSPROPSETID_InterleavedAudio\
    0xe9ebe550, 0xd619, 0x4c0a, 0x97, 0x6b, 0x70, 0x62, 0x32, 0x2b, 0x30, 0x6
DEFINE_GUIDSTRUCT("E9EBE550-D619-4C0A-976B-7062322B3006", KSPROPSETID_InterleavedAudio);
#define KSPROPSETID_InterleavedAudio DEFINE_GUIDNAMED(KSPROPSETID_InterleavedAudio)
```

The **KSPROPSETID\_InterleavedAudio** property set contains the following KS property.

[**KSPROPERTY\_INTERLEAVEDAUDIO_FORMATINFORMATION**](ksproperty-interleavedaudio-formatinformation.md)

This property name is defined in the [**KSPROPERTY\_INTERLEAVEDAUDIO**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-ksproperty_interleavedaudio) enum.
