---
title: KSPROPERTY_AUDIOLOOPBACK
description: The KSPROPERTY_AUDIOLOOPBACK property indicates if the loopback tap point is pre or post volume and mute.
keywords: ["KSPROPERTY_AUDIOLOOPBACKAudio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_AUDIOLOOPBACK
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 02/06/2024
---

# KSPROPERTY_AUDIOLOOPBACK

The **KSPROPERTY_AUDIOLOOPBACK** property indicates if the loopback tap point is pre or post volume and mute.

Starting in Windows 11 24H2, setting the KSPROPERTY_AUDIOLOOPBACK property is a requirement.

## Usage Summary Table

|Get|Set|Target|Property descriptor type|Property value type|
|-- |-- |---- |------------------------ |------------------ |
|Yes|No |Pin  |[KSATTRIBUTE_AUDIOLOOPBACK_TAPPOINT](ns-ksmedia-ksattribute_audioloopback_tappoint.md) | [KSATTRIBUTE structure](/windows-hardware/drivers/ddi/ks/ns-ks-ksattribute)|

KSPROPERTY_AUDIOLOOPBACK is an enum of properties that are associated with [KSPROPSETID_AudioLoopback](kspropsetid-audioloopback.md), with the following property implemented.

```cpp
typedef enum {
    KSPROPERTY_AUDIOLOOPBACK_TAPPOINT_CAPS,
} KSPROPERTY_AUDIOLOOPBACK;
```

The Windows AudioEndpointBuilder uses KSPROPSETID_AudioLoopback with KSPROPERTY_AUDIOLOOPBACK_TAPPOINT_CAPS to retrieve the `AUDIOLOOPBACK_TAPPOINT_CAPS_<*>`. This informs the OS as to whether the audio endpoint has the ability to do pre volume loopback, post volume loopback, or both.

Later, at pin creation time, the OS provides  an attribute, KSATTRIBUTEID_AUDIOLOOPBACK_TAPPOINT with a KSATTRIBUTE_AUDIOLOOPBACK_TAPPOINT, to communicate whether to create the loopback pin as pre volume or post volume.

The tappoint caps are defined as follows.

```cpp
#define AUDIOLOOPBACK_TAPPOINT_CAPS_PREVOLUMEMUTE      (0x1)
#define AUDIOLOOPBACK_TAPPOINT_CAPS_POSTVOLUMEMUTE     (0x2)
```

The [KSATTRIBUTE_AUDIOLOOPBACK_TAPPOINT structure](ns-ksmedia-ksattribute_audioloopback_tappoint.md) available in ksmedia.h can provide a wrapper for specifying the AUDIO_LOOPBACK_TAPPOINT_TYPE attribute about where to tap loopback in the stream graph.

### Return Value

A **KSPROPERTY_AUDIOLOOPBACK** property request returns STATUS_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Remarks

An audio system can be summarized as follows.

- Signal Processing Output: The output from the signal processing from offloaded or direct from the host provider.
- Volume: The next step in the flow, where the volume of the audio signal is adjusted.
- Mute: This stage mutes the audio signal if necessary.
- EFX (Effects): Here, effects are applied to the audio signal.
- Output: The final stage where the processed audio signal is outputted.

Systems with hardware audio engine must implement loopback pin. The loopback pin returns mixed audio output after all signal processing has been applied.

The loopback stream also gets affected by endpoint volume and mute. This property allows applications to  choose whether loopback stream should be returned before or after applying endpoint volume and mute.

The audio driver must connect Audio Engine output pin to Filter’s loopback pin. The loopback pin must advertise category as KSNODETYPE_AUDIO_LOOPBACK. The loopback does not implement signal processing modes.

The OS can query the audio driver for loopback tapping point capabilities. The capabilities are returned as a bit mask of flags.

The stream created on the loopback pin collects DSP-mixed output and provides it as a capture stream back to the OS. One way for the driver to get options from OS is through stream attributes. If no attributes are applied to the loopback stream, then loopback should be collected before volume and mute is applied on the mixer output.

For a user mode client, the switch between pre volume loopback and post volume loopback is done via AUDCLNT_STREAMOPTIONS_POST_VOLUME_LOOPBACK, passed in as a [AUDCLNT_STREAMOPTIONS (audioclient.h)](/windows/win32/api/audioclient/ne-audioclient-audclnt_streamoptions) when calling SetClientProperties.

### KSNODETYPE_AUDIO_LOOPBACK

KSNODETYPE_AUDIO_LOOPBACK represents audio loopback capabilities. It is defined in ksmedia.h as shown here.

```cpp
#define STATIC_KSNODETYPE_AUDIO_LOOPBACK\
    0x8f42c0b2, 0x91ce, 0x4bcf, 0x9c, 0xcd, 0xe, 0x59, 0x90, 0x37, 0xab, 0x35
DEFINE_GUIDSTRUCT("8F42C0B2-91CE-4BCF-9CCD-0E599037AB35", KSNODETYPE_AUDIO_LOOPBACK);
#define KSNODETYPE_AUDIO_LOOPBACK DEFINE_GUIDNAMED(KSNODETYPE_AUDIO_LOOPBACK)
```

## Requirements

| Requirement              | Value                   |
|--------------------------|-------------------------|
| Minimum supported client | Windows 11 Version 24H2 |
| Header                   | Ksmedia.h               |

## See also

[KSPROPSETID_AudioLoopback](kspropsetid-audioloopback.md)

[AUDIOLOOPBACK_TAPPOINT_TYPE enum](ne-ksmedia-audioloopback_tappoint_type.md)

[KSATTRIBUTE_AUDIOLOOPBACK_TAPPOINT structure](ns-ksmedia-ksattribute_audioloopback_tappoint.md)
