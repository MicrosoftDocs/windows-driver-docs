---
title: KSPROPSETID_AudioLoopback
description: The KSPROPSETID_AudioLoopback property set is used by the audio driver to indicate the loopback tap point pre and post volume and mute.
ms.date: 02/06/2024
ms.topic: reference
---

# KSPROPSETID_AudioLoopback

The **KSPROPSETID_AudioLoopback** property set is used by the audio driver to indicate the loopback tap point pre and post volume and mute.

The *Ksmedia.h* header file defines the **KSPROPSETID_AudioLoopback** property set as follows:

```cpp
#define STATIC_KSPROPSETID_AudioLoopback 0xb3648bc8, 0x5b91, 0x468a, 0xb9, 0x4d, 0xf4, 0x64, 0x12, 0x50, 0x91, 0x7c
DEFINE_GUIDSTRUCT("B3648BC8-5B91-468A-B94D-F4641250917C", KSPROPSETID_AudioLoopback);
#define KSPROPSETID_AudioLoopback DEFINE_GUIDNAMED(KSPROPSETID_AudioLoopback)
```

The **KSPROPSETID_AudioLoopback** property set contains the following KS property:

[**KSPROPERTY_AUDIOLOOPBACK**](ksproperty-audioloopback.md)

## Remarks

KSPROPSETID_AudioLoopback with KSPROPERTY_AUDIOLOOPBACK_TAPPOINT_CAPS requesting KSPROPERTY_TYPE_BASICSUPPORT will return flags indicating support for get and basic support.

KSPROPERTY_TYPE_SET is not supported.

KSPROPSETID_AudioLoopback with KSPROPERTY_AUDIOLOOPBACK_TAPPOINT_CAPS and KSPROPERTY_TYPE_GET will return a bitwise OR of the supported capabilities:

`AUDIOLOOPBACK_TAPPOINT_CAPS_PREVOLUMEMUTE | AUDIOLOOPBACK_TAPPOINT_CAPS_POSTVOLUMEMUTE`

For backwards compatibility, if KSPROPERTY_AUDIOLOOPBACK_TAPPOINT_CAPS is not supported, then the driver is assumed to support `AUDIOLOOPBACK_TAPPOINT_CAPS_PREVOLUMEMUTE`.

By policy, support for AUDIOLOOPBACK_TAPPOINT_CAPS_PREVOLUMEMUTE is required. A driver implementing KSPROPERTY_AUDIOLOOPBACK_TAPPOINT_CAPS should return either `AUDIOLOOPBACK_TAPPOINT_CAPS_PREVOLUMEMUTE` or `AUDIOLOOPBACK_TAPPOINT_CAPS_PREVOLUMEMUTE | AUDIOLOOPBACK_TAPPOINT_CAPS_POSTVOLUMEMUTE`.

A driver which only supports `AUDIOLOOPBACK_TAPPOINT_CAPS_POSTVOLUMEMUTE` will fail HLK testing.

## AUDIOLOOPBACK_TAPPOINT_TYPE enum

The AUDIOLOOPBACK_TAPPOINT_TYPE enum contains the  pre and post tap point definitions. For more information, see [AUDIOLOOPBACK_TAPPOINT_TYPE enum](ne-ksmedia-audioloopback_tappoint_type.md).

### See also

[KSPROPERTY_AUDIOLOOPBACK](ksproperty-audioloopback.md)

[KSPROPERTY structure](/windows-hardware/drivers/stream/ksproperty-structure)

[AUDIOLOOPBACK_TAPPOINT_TYPE enum](ne-ksmedia-audioloopback_tappoint_type.md)

[KSATTRIBUTE_AUDIOLOOPBACK_TAPPOINT structure](ns-ksmedia-ksattribute_audioloopback_tappoint.md)
