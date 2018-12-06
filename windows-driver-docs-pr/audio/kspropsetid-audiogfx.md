---
title: KSPROPSETID\_AudioGfx
description: KSPROPSETID\_AudioGfx
ms.assetid: f872a5bb-6ab5-4f1e-b81b-86ba744b2d6e
keywords: ["KSPROPSETID_AudioGfx"]
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_AudioGfx


## <span id="ddk_kspropsetid_audiogfx_ks"></span><span id="DDK_KSPROPSETID_AUDIOGFX_KS"></span>


The `KSPROPSETID_AudioGfx` property set is used to inform GFX filters of the device IDs of the audio devices that are used for rendering and capture. A device ID is specified in the form of a null-terminated Unicode string (see [Device Identification Strings](https://msdn.microsoft.com/library/windows/hardware/ff541224)).

The property items in this set are specified by KSPROPERTY\_AUDIOGFX enumeration values.

The following properties are part of the `KSPROPSETID_AudioGfx` property set:

[**KSPROPERTY\_AUDIOGFX\_CAPTURETARGETDEVICEID**](ksproperty-audiogfx-capturetargetdeviceid.md)

[**KSPROPERTY\_AUDIOGFX\_RENDERTARGETDEVICEID**](ksproperty-audiogfx-rendertargetdeviceid.md)

 

 





