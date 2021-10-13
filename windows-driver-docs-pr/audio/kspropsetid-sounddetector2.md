---
title: KSPROPSETID\_SoundDetector2
description: KSPROPSETID_SoundDetector2 property set contains properties that are used to register a filter for an audio capture device that also supports a detector.
ms.date: 09/25/2019
ms.localizationpriority: medium
---

# KSPROPSETID\_SoundDetector2

The `KSPROPSETID_SoundDetector2` property set contains properties that are used to register a filter for an audio capture device that also supports a detector. The filter has a KS pin factory that has pin category [KSNODETYPE\_AUDIO\_KEYWORDDETECTOR](ksnodetype-audio-keyworddetector.md). There cannot be more than one pin factory having this KS pin category in a given KS filter instance.

`KSPROPSETID_SoundDetector2` is supported in  Windows 10 Version 1903 and later. The KSPROPSETID_SoundDetector2 property set is used to support multiple voice agents. For more information, see [Multiple Voice Assistant](voice-activation-mva.md).  [KSPROPSETID\_SoundDetector](kspropsetid-sounddetector.md) property set is used on systems that support just Cortana.  

`KSPROPSETID_SoundDetector2` uses the [KSSOUNDDETECTORPROPERTY](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kssounddetectorproperty) structure, instead of a KSPROPERTY:

``` syntax
typedef struct {
    KSPROPERTY  Property;
    GUID        EventId;
} KSSOUNDDETECTORPROPERTY, *PKSSOUNDDETECTORPROPERTY;
```

All KSPROPSETID_SoundDetector2 properties are called with a [KSSOUNDDETECTORPROPERTY](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kssounddetectorproperty)  data structure. This data structure contains a KSPROPERTY and the event id for the keyword to be armed, reset, detected, etc.

The header file defines the **KSPROPSETID\_SoundDetector2** property set as follows:

``` syntax
#define STATIC_KSPROPSETID_SoundDetector2\
    0xfe07e322, 0x450c, 0x4bd5, 0x84, 0xca, 0xa9, 0x48, 0x50, 0xe, 0xa6, 0xaa
DEFINE_GUIDSTRUCT("FE07E322-450C-4BD5-84CA-A948500EA6AA", KSPROPSETID_SoundDetector2);
```

The `KSPROPSETID_SoundDetector2` property set contains the following properties:

- [KSPROPERTY\_SOUNDDETECTOR\_SUPPORTEDPATTERNS](ksproperty-sounddetector-supportedpatterns.md) - This property is set by the operating system to configure the keywords to be detected.

- [KSPROPERTY\_SOUNDDETECTOR\_PATTERNS](ksproperty-sounddetector-patterns.md) - The driver’s KS filter supports this read/write property. The OS sets this property to configure the keywords to be detected.

- [KSPROPERTY\_SOUNDDETECTOR\_ARMED](ksproperty-sounddetector-armed.md) - This read/write property is a simply Boolean status indicating whether the detector is armed. The OS sets this to engage the keyword detector. The OS can clear this to disengage. The driver automatically clears this when keyword patterns are set and also after a keyword is detected. (The OS must rearm.)

- [KSPROPERTY\_SOUNDDETECTOR\_RESET](ksproperty-sounddetector-reset.md) - Reset the detector to an unarmed state with no pattern set.

- [KSPROPERTY\_SOUNDDETECTOR\_STREAMINGSUPPORT](ksproperty-sounddetector-streamingsupport.md) - Future use for voice onset detectors only. Fail this request indicating property not supported or succeed and return true for all other drivers.

At keyword detection time, a PNP notification containing KSNOTIFICATIONID_SoundDetector is sent. NOTE: This is not a KSEvent, but rather a PNP event which is sent, with a payload, via [IoReportTargetDeviceChangeAsynchronous](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreporttargetdevicechangeasynchronous).
