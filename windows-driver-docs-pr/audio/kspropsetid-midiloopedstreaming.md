---
title: KSPROPSETID\_MIDILOOPEDSTREAMING
description: KSPROPSETID\_MIDILOOPEDSTREAMING
ms.date: 02/06/2025
ms.topic: reference
---

# KSPROPSETID\_MIDILOOPEDSTREAMING

The `KSPROPSETID_MIDILOOPEDSTREAMING` property set specifies the properties of a MIDI looped steraming device. These properties are supported in Windows TDB and later Windows operating systems.

In the following property definitions, the property is get-only and the target is a pin:

-   All properties in this property set support **Get** property requests from the client, but not **Set** property requests.

-   For all the properties in this set, the target to which a client sends a property request is a pin instance. (Other KS property sets, on the other hand, support properties on filter instances.)

The `KSPROPSETID_MIDILOOPEDSTREAMING` property set contains the following properties:

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_BUFFER**](ksproperty-midiloopedstreaming-buffer.md)

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_REGISTERS**](ksproperty-midiloopedstreaming-registers.md)

[**KSPROPERTY\_MIDILOOPEDSTREAMING\_NOTIFICATION\_EVENT**](ksproperty-midiloopedstreaming-notification-event.md)


 

 





