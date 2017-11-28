---
title: KSPROPSETID\_AudioEngine
description: The KSPROPSETID\_AudioEngine property set contains KS properties that the audio driver can use to provide more information about the hardware audio engine node.
ms.assetid: F3155DF6-0710-4941-94DC-478A8F5DE8D1
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPSETID_AudioEngine%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




