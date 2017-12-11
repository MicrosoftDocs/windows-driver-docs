---
title: KSPROPSETID\_AudioGfx
description: KSPROPSETID\_AudioGfx
ms.assetid: f872a5bb-6ab5-4f1e-b81b-86ba744b2d6e
keywords: ["KSPROPSETID_AudioGfx"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPSETID\_AudioGfx


## <span id="ddk_kspropsetid_audiogfx_ks"></span><span id="DDK_KSPROPSETID_AUDIOGFX_KS"></span>


The `KSPROPSETID_AudioGfx` property set is used to inform GFX filters of the device IDs of the audio devices that are used for rendering and capture. A device ID is specified in the form of a null-terminated Unicode string (see [Device Identification Strings](https://msdn.microsoft.com/library/windows/hardware/ff541224)).

The property items in this set are specified by KSPROPERTY\_AUDIOGFX enumeration values.

The following properties are part of the `KSPROPSETID_AudioGfx` property set:

[**KSPROPERTY\_AUDIOGFX\_CAPTURETARGETDEVICEID**](ksproperty-audiogfx-capturetargetdeviceid.md)

[**KSPROPERTY\_AUDIOGFX\_RENDERTARGETDEVICEID**](ksproperty-audiogfx-rendertargetdeviceid.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPSETID_AudioGfx%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




