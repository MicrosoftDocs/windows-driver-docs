---
title: KSPROPSETID\_AudioEngine
description: The KSPROPSETID\_AudioEngine property set contains KS properties that the audio driver can use to provide more information about the hardware audio engine node.
ms.assetid: F3155DF6-0710-4941-94DC-478A8F5DE8D1
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_AudioEngine


The **KSPROPSETID\_AudioEngine** property set contains KS properties that the audio driver can use to provide more information about the hardware audio engine node.

**KSPROPSETID\_AudioEngine** is available with Windows 8 and later versions of the Windows operating system.

When a hardware solution supports audio offloading, the audio driver for the hardware must expose its capabilities in a specific manner so that the Windows 8 user-mode audio stack can discover these capabilities and take advantage of them.

To support the audio offloading architecture provided with Windows 8, the hardware solution must implement a hardware audio engine. The audio driver for this hardware must then expose the hardware audio engine as an audio engine kernel streaming (KS) node that is contained within a KS filter. The node type that has been newly defined for this purpose is [**KSNODETYPE\_AUDIO\_ENGINE**](ksnodetype-audio-engine.md). The [**KSPROPERTY\_AUDIOENGINE**](ksproperty-audioengine.md) enumeration is used to represent the new KS properties.

The *Ksmedia.h* header file defines the **KSPROPSETID\_AudioEngine** property set as follows:

``` syntax
#define STATIC_KSPROPSETID_AudioEngine\
    0x3A2F82DCL, 0x886F, 0x4BAA, 0x9E, 0xB4, 0x8, 0x2B, 0x90, 0x25, 0xC5, 0x36
DEFINE_GUIDSTRUCT("3A2F82DC-886F-4BAA-9EB4-082B9025C536", KSPROPSETID_AudioEngine);
#define KSPROPSETID_AudioEngine DEFINE_GUIDNAMED(KSPROPSETID_AudioEngine)
```

The **KSPROPSETID\_AudioEngine** property set contains the following KS properties.

## <span id="wdk_kspropsetid_audioengine"></span><span id="WDK_KSPROPSETID_AUDIOENGINE"></span>


[**KSPROPERTY\_AUDIOENGINE\_BUFFER\_SIZE\_RANGE**](ksproperty-audioengine-buffer-size-limits.md)

[**KSPROPERTY\_AUDIOENGINE\_DESCRIPTOR**](ksproperty-audioengine-descriptor.md)

[**KSPROPERTY\_AUDIOENGINE\_DEVICEFORMAT**](ksproperty-audioengine-deviceformat.md)

[**KSPROPERTY\_AUDIOENGINE\_GFXENABLE**](ksproperty-audioengine-gfx-enable.md)

[**KSPROPERTY\_AUDIOENGINE\_LFXENABLE**](ksproperty-audioengine-lfx-enable.md)

[**KSPROPERTY\_AUDIOENGINE\_LOOPBACK\_PROTECTION**](ksproperty-audioengine-loopback-protection.md)

[**KSPROPERTY\_AUDIOENGINE\_MIXFORMAT**](ksproperty-audioengine-mixformat.md)

[**KSPROPERTY\_AUDIOENGINE\_SUPPORTEDDEVICEFORMATS**](ksproperty-audioengine-supporteddeviceformats.md)

[**KSPROPERTY\_AUDIOENGINE\_VOLUMELEVEL**](ksproperty-audioengine-volumelevel.md)

These property names are defined in the [**KSPROPERTY\_AUDIOENGINE**](ksproperty-audioengine.md) enum.

 

 





