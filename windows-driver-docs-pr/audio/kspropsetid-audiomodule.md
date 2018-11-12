---
title: KSPROPSETID\_AudioModule
description: The KSPROPSETID\_AudioModule property set is used by the audio driver to retrieve the list of audio modules.
ms.assetid: 6F167E5E-CA11-45F3-BF21-6B9A3F90DB9F
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





