---
title: KSPROPSETID\_AudioEffectsDiscovery
description: The KSPROPSETID\_AudioEffectsDiscovery property set is implemented by audio device drivers that use Microsoft’s generic proxy audio processing object (APO).
ms.assetid: 68229885-1446-4BF0-B4E1-96A777006567
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_AudioEffectsDiscovery


The **KSPROPSETID\_AudioEffectsDiscovery** property set is implemented by audio device drivers that use Microsoft’s generic proxy audio processing object (APO).

**KSPROPSETID\_AudioEffectsDiscovery** is available with Windows 8.1 and later versions of the Windows operating system.

The *MsApoFxProxy.h* header file defines the **KSPROPSETID\_AudioEffectsDiscovery** property set as follows:

``` syntax
#define STATIC_KSPROPSETID_AudioEffectsDiscovery\  
    0xb217a72, 0x16b8, 0x4a4d, 0xbd, 0xed, 0xf9, 0xd6, 0xbb, 0xed, 0xcd, 0x8f  
DEFINE_GUIDSTRUCT("0B217A72-16B8-4A4D-BDED-F9D6BBEDCD8F", KSPROPSETID_AudioEffectsDiscovery);  
#define KSPROPSETID_AudioEffectsDiscovery DEFINE_GUIDNAMED(KSPROPSETID_AudioEffectsDiscovery)
```

The **KSPROPSETID\_AudioEffectsDiscovery** property set contains the following KS property.

[**KSPROPERTY\_AUDIOEFFECTSDISCOVERY\_EFFECTSLIST**](https://msdn.microsoft.com/library/windows/hardware/dn457706)

This property name is defined in the [**KSPROPERTY\_AUDIOEFFECTSDISCOVERY**](https://msdn.microsoft.com/library/windows/hardware/dn457705) enum.

 

 





