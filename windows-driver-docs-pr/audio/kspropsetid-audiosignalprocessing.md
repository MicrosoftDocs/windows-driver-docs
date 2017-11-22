---
title: KSPROPSETID\_AudioSignalProcessing
description: The KSPROPSETID\_AudioSignalProcessing property set is used by the audio driver to retrieve the list of audio signal processing modes supported by a pin factory.
ms.assetid: D9EF0D65-4DCD-4936-B7AC-A17FA50D3AE7
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPSETID_AudioSignalProcessing%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




