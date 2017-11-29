---
title: KSNODETYPE\_AUDIO\_ENGINE
description: The KSNODETYPE\_AUDIO\_ENGINE audio endpoint is a new endpoint that is available with Windows 8 and later versions of Windows.
ms.assetid: C1A7E136-655A-4024-A280-F252F1AE1282
keywords: ["KSNODETYPE_AUDIO_ENGINE Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_AUDIO_ENGINE
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSNODETYPE\_AUDIO\_ENGINE


The KSNODETYPE\_AUDIO\_ENGINE audio endpoint is a new endpoint that is available with Windows 8 and later versions of Windows. The KSNODETYPE\_AUDIO\_ENGINE audio endpoint is contained within a Wave kernel streaming (KS) audio filter, and it allows an audio driver to expose the capabilities of the hardware audio engine.

The KSNODETYPE\_AUDIO\_ENGINE audio endpoint is a required endpoint and its introduction made it necessary to develop a new Wave data sink pin factory to which the new endpoint directly connects.

The KSNODETYPE\_AUDIO\_ENGINE audio endpoint must support the [**KSPROPERTY\_AUDIOENGINE**](ksproperty-audioengine.md) enumerated values in addition to the following KS properties:

[**KSPROPERTY\_AUDIO\_MUTE**](ksproperty-audio-mute.md)

[**KSPROPERTY\_AUDIO\_PEAKMETER**](ksproperty-audio-peakmeter.md)

[**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](ksproperty-audio-volumelevel.md)

[KSPROPSETID\_AudioEngine](kspropsetid-audioengine.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_AUDIO_ENGINE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




