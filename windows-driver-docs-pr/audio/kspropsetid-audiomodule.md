---
title: KSPROPSETID\_AudioModule
description: The KSPROPSETID\_AudioModule property set is used by the audio driver to retrieve the list of audio modules.
ms.assetid: 6F167E5E-CA11-45F3-BF21-6B9A3F90DB9F
---

# KSPROPSETID\_AudioModule


The **KSPROPSETID\_AudioModule** property set is used by the audio driver to retrieve the list of audio modules.

The *Ksmedia.h* header file defines the **KSPROPSETID\_AudioModule** property set as follows:

``` syntax
#define STATIC_KSPROPSETID_AudioModule \
    0xc034fdb0, 0xff75, 0x47c8, 0xaa, 0x3c, 0xee, 0x46, 0x71, 0x6b, 0x50, 0xc6
DEFINE_GUIDSTRUCT("C034FDB0-FF75-47C8-AA3C-EE46716B50C6", KSPROPSETID_AudioModule);
#define KSPROPSETID_AudioModule DEFINE_GUIDNAMED(KSPROPSETID_AudioModule)
```

The **KSPROPSETID\_AudioModule** property set contains the following KS properties.

[**KSPROPERTY\_AUDIOMODULE\_DESCRIPTORS**](ksproperty-audiomodule-descriptors.md)

[**KSPROPERTY\_AUDIOMODULE\_COMMAND**](ksproperty-audiomodule-command.md)

[**KSPROPERTY\_AUDIOMODULE\_NOTIFICATION\_DEVICE\_ID**](ksproperty-audiomodule-notification-device-id.md)

This property name is defined in the [**KSPROPERTY\_AUDIOMODULE**](ksproperty-audiomodule.md) enum.

For more information about audio modules, see [Implementing Audio Module Discovery](https://msdn.microsoft.com/windows/hardware/drivers/audio/implementing-audio-module-communication).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPSETID_AudioModule%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




