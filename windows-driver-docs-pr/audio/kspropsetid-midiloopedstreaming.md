---
title: KSPROPSETID_MIDILOOPEDSTREAMING
description: KSPROPSETID_MIDILOOPEDSTREAMING
ms.date: 12/16/2025
ms.topic: reference
---

# KSPROPSETID_MIDILOOPEDSTREAMING

The `KSPROPSETID_MIDILOOPEDSTREAMING` property set specifies the properties of a MIDI looped streaming device. These properties are supported in Windows 11 version 25H2 and later Windows operating systems.

```cpp
#define STATIC_KSPROPSETID_MidiLoopedStreaming\  

            0x1f306ba6, 0xfd9b, 0x427a, 0xbc, 0xb3, 0x27, 0xcb, 0xcf, 0xe, 0xf, 0x19  

        DEFINE_GUIDSTRUCT("1F306BA6-FD9B-427A-BCB3-27CBCF0E0F19", KSPROPSETID_MidiLoopedStreaming);  

#define KSPROPSETID_MidiLoopedStreaming DEFINE_GUIDNAMED(KSPROPSETID_MidiLoopedStreaming)  
```

The `KSPROPSETID_MIDILOOPEDSTREAMING` property set contains the following properties:

- **[KSPROPERTY_MIDILOOPEDSTREAMING_BUFFER](ksproperty-midiloopedstreaming-buffer.md)**
- **[KSPROPERTY_MIDILOOPEDSTREAMING_REGISTERS](ksproperty-midiloopedstreaming-registers.md)**
- **[KSPROPERTY_MIDILOOPEDSTREAMING_NOTIFICATION_EVENT](ksproperty-midiloopedstreaming-notification-event.md)**
