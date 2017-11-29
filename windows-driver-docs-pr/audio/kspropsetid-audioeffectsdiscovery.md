---
title: KSPROPSETID\_AudioEffectsDiscovery
description: The KSPROPSETID\_AudioEffectsDiscovery property set is implemented by audio device drivers that use Microsoft’s generic proxy audio processing object (APO).
ms.assetid: 68229885-1446-4BF0-B4E1-96A777006567
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPSETID_AudioEffectsDiscovery%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




