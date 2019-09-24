---
title: KSPROPSETID\_SoundDetector2
description: .
ms.assetid: FC4A354B-D42C-4199-B613-1E1B75A600C7
ms.date: 09/24/2019
ms.localizationpriority: medium
---

# KSPROPSETID\_SoundDetector2

The `KSPROPSETID_SoundDetector2` property set contains properties that are used to register a filter for an audio capture device that also supports a detector. The filter has a KS pin factory that has pin category [KSNODETYPE\_AUDIO\_KEYWORDDETECTOR](ksnodetype-audio-keyworddetector.md). There cannot be more than one pin factory having this KS pin category in a given KS filter instance.

`KSPROPSETID_SoundDetector2` is supported in  Windows 10 Version 1903 and later.

`KSPROPSETID_SoundDetector2` uses the KSSOUNDDETECTORPROPERTY structure, instead of a KSPROPERTY:

``` syntax
typedef struct {
    KSPROPERTY  Property;
    GUID        EventId;
} KSSOUNDDETECTORPROPERTY, *PKSSOUNDDETECTORPROPERTY;
```

All KSPROPSETID_SoundDetector2 properties are called with a KSSOUNDDETECTORPROPERTY data structure. This data structure contains a KSPROPERTY and the event id for the keyword to be armed, reset, detected, etc.

The header file defines the **KSPROPSETID\_SoundDetector2** property set as follows:

``` syntax
#define STATIC_KSPROPSETID_SoundDetector2\
    0xfe07e322, 0x450c, 0x4bd5, 0x84, 0xca, 0xa9, 0x48, 0x50, 0xe, 0xa6, 0xaa
DEFINE_GUIDSTRUCT("FE07E322-450C-4BD5-84CA-A948500EA6AA", KSPROPSETID_SoundDetector2);
```

The `KSPROPSETID_SoundDetector2` property set contains the following properties:

- [**KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS**](ksproperty-sounddetector-supportedpatterns.md) - This property is set by the operating system to configure the keywords to be detected.

- [**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](ksproperty-sounddetector-armed.md) - This read/write property is a simply Boolean status indicating whether the detector is armed. The OS sets this to engage the keyword detector. The OS can clear this to disengage. The driver automatically clears this when keyword patterns are set and also after a keyword is detected. (The OS must rearm.)

- [**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md) is used to reset the sound detector at startup time.

- [**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md)

At keyword detection time, a PNP notification containing KSNOTIFICATIONID_SoundDetector is sent. NOTE: this is not a KSEvent, but rather a PNP event which is sent, with a payload, via [IoReportTargetDeviceChangeAsynchronous](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioreporttargetdevicechangeasynchronous).
