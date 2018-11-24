---
title: KSPROPSETID\_SoundDetector
description: .
ms.assetid: FC4A354B-D42C-4199-B613-1E1B75A600C6
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





