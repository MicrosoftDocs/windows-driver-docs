---
title: KSNODETYPE\_AUDIO\_KEYWORDDETECTOR
description: The KSNODETYPE\_AUDIO\_KEYWORDDETECTOR audio endpoint is a new endpoint that is available with Windows 10 and later versions of Windows. The KSNODETYPE\_AUDIO\_KEYWORDDETECTOR allows an audio capture driver to support a detector.
ms.assetid: 7D4CD2B7-F4B4-4A81-B18A-2B7E86D1EF80
keywords: ["KSNODETYPE_AUDIO_KEYWORDDETECTOR Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_AUDIO_KEYWORDDETECTOR
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSNODETYPE\_AUDIO\_KEYWORDDETECTOR


The KSNODETYPE\_AUDIO\_KEYWORDDETECTOR audio endpoint is a new endpoint that is available with Windows 10 and later versions of Windows. The KSNODETYPE\_AUDIO\_KEYWORDDETECTOR allows an audio capture driver to support a detector.

This filter cannot be shared with other capture devices. The filter has a KS pin factory that has pin category KSNODETYPE\_AUDIO\_KEYWORDDETECTOR. There cannot be more than one pin factory having this KS pin category in a given KS filter instance.

The KSNODETYPE\_AUDIO\_KEYWORDDETECTOR audio endpoint must support the following KS properties:

[**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**](ksproperty-sounddetector-supportedpatterns.md)

[**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md)

[**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](ksproperty-sounddetector-armed.md)

[**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md)

## <span id="see_also"></span>See also


[KSPROPSETID\_SoundDetector](kspropsetid-sounddetector.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_AUDIO_KEYWORDDETECTOR%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





