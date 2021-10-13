---
title: Analog Video Category
description: The Analog Video In category represents the stream of analog video input to a video decoder filter.
keywords:
- stream categories WDK video capture , analog video
- analog video category WDK video capture
- PINNAME_VIDEO_ANALOGVIDEOIN
- analog audio WDK video capture
ms.date: 07/26/2021
ms.localizationpriority: medium
---

# Analog Video Category

The following GUID corresponds to the analog video in category:

- **PINNAME_VIDEO_ANALOGVIDEOIN**

    The Analog Video In category represents the stream of analog video input to a video decoder filter.

When specifying **PINNAME_VIDEO_ANALOGVIDEOIN** pins, use the information listed in the following table.

| Attribute | Value |
|--|--|
| **DataRange Structure** | [**KS_DATARANGE_ANALOGVIDEO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_datarange_analogvideo) |
| **DataFormat Structure** | [**KS_DATARANGE_ANALOGVIDEO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_datarange_analogvideo) |
| **MajorFormat GUID** | KSDATAFORMAT_TYPE_ANALOGVIDEO |
| **Sub-Format GUID** | KSDATAFORMAT_SUBTYPE_NONE |
| **Specifier GUID** | KSDATAFORMAT_SPECIFIER_ANALOGVIDEO |
| **Extended Header Size** | 0 |
| **Required Property Sets** | None |
| **Required Event Sets** | None |
| **DirectShow majortype** | MEDIATYPE_AnalogVideo |
| **DirectShow formattype** | FORMAT_AnalogVideo |

There is no special category defined for analog audio, such as TV or radio audio. When specifying a category for devices with analog audio pins, the value of the **MajorFormat** member should be KSDATAFORMAT_TYPE_ANALOGAUDIO. The value of the **Specifier** member should be KSDATAFORMAT_SPECIFIER_NONE and the **subtype** member and the format block should be set to KSDATAFORMAT_SUBTYPE_NONE. For more information about radio audio, see [Video Capture Devices with Radio Tuners](video-capture-devices-with-radio-tuners.md).

Although the analog video stream essentially mimics the input to the analog video decoder, it simultaneously acts as a data transport for tuning information. Tuning packets, originating at the TV tuner filter, are passed through any intervening crossbar filters at the start and end of every tuning operation. The data packet is a [**KS_TVTUNER_CHANGE_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_tvtuner_change_info) structure that contains the country/region code, channel, frequency, and analog video standard in use.

Capture filters must propagate this tuning packet in the extended header of VBI output streams to downstream VBI codecs.
