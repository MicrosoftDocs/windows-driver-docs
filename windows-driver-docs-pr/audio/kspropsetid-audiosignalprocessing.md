---
title: KSPROPSETID\_AudioSignalProcessing
description: The KSPROPSETID\_AudioSignalProcessing property set is used by the audio driver to retrieve the list of audio signal processing modes supported by a pin factory.
ms.assetid: D9EF0D65-4DCD-4936-B7AC-A17FA50D3AE7
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_AudioSignalProcessing


The **KSPROPSETID\_AudioSignalProcessing** property set is used by the audio driver to retrieve the list of audio signal processing modes supported by a pin factory.

The *Ksmedia.h* header file defines the **KSPROPSETID\_AudioSignalProcessing** property set as follows:

``` syntax
#define STATIC_KSPROPSETID_AudioEffectsDiscovery\  
    0xb217a72, 0x16b8, 0x4a4d, 0xbd, 0xed, 0xf9, 0xd6, 0xbb, 0xed, 0xcd, 0x8f  
DEFINE_GUIDSTRUCT("0B217A72-16B8-4A4D-BDED-F9D6BBEDCD8F", KSPROPSETID_AudioEffectsDiscovery);  
#define KSPROPSETID_AudioEffectsDiscovery DEFINE_GUIDNAMED(KSPROPSETID_AudioEffectsDiscovery)
```

The **KSPROPSETID\_AudioSignalProcessing** property set contains the following KS property.

[**KSPROPERTY\_AUDIOSIGNALPROCESSING\_MODES**](ksproperty-audiosignalprocessing-modes.md)

This property name is defined in the [**KSPROPERTY\_AUDIOSIGNALPROCESSING**](ksproperty-audiosignalprocessing.md) enum.

 

 





