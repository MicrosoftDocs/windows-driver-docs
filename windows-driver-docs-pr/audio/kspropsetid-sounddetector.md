---
title: KSPROPSETID\_SoundDetector
description: .
ms.assetid: FC4A354B-D42C-4199-B613-1E1B75A600C6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPSETID\_SoundDetector


The `KSPROPSETID_SoundDetector` property set contains properties that are used to register a filter for an audio capture device that also supports a detector. The filter has a KS pin factory that has pin category **KSNODETYPE\_AUDIO\_KEYWORDDETECTOR**. There cannot be more than one pin factory having this KS pin category in a given KS filter instance.

Property items in this set are specified by [**KSPROPERTY\_SOUNDDETECTOR**](ksproperty-sounddetector.md) enumeration values, as defined in header file *ksmedia.h*.

The header file defines the **KSPROPSETID\_SoundDetector** property set as follows:

``` syntax
#define STATIC_KSPROPSETID_SoundDetector\
    0x113c425e, 0xfd17, 0x4057, 0xb4, 0x22, 0xed, 0x40, 0x74, 0xf1, 0xaf, 0xdf
DEFINE_GUIDSTRUCT("113C425E-FD17-4057-B422-ED4074F1AFDF", KSPROPSETID_SoundDetector);
#define KSPROPSETID_SoundDetector DEFINE_GUIDNAMED(KSPROPSETID_SoundDetector)
```

The `KSPROPSETID_SoundDetector` property set contains the following properties:

-   [**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](ksproperty-sounddetector-armed.md)

-   [**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md)

-   [**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md)

-   [**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**](ksproperty-sounddetector-supportedpatterns.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPSETID_SoundDetector%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




