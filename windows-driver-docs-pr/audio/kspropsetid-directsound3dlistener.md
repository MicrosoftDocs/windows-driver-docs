---
title: KSPROPSETID\_DirectSound3DListener
description: KSPROPSETID\_DirectSound3DListener
ms.assetid: 37eef2cb-5b45-4ff8-abb9-a685f0b290e3
keywords: ["KSPROPSETID_DirectSound3DListener"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPSETID\_DirectSound3DListener


## <span id="ddk_kspropsetid_directsound3dlistener_ks"></span><span id="DDK_KSPROPSETID_DIRECTSOUND3DLISTENER_KS"></span>


The `KSPROPSETID_DirectSound3DListener` property set contains all the device-specific properties that are needed to implement the **IDirectSound3DListener** interface (see the Microsoft Windows SDK documentation). Using this property set, the 3D-buffer properties that are specified by the API are passed directly between DirectSound and the WDM audio driver. This property set is handled by the [**KSNODETYPE\_3D\_EFFECTS**](ksnodetype-3d-effects.md) node. This node handles both the 3D-buffer and 3D-listener properties, so the WDM audio driver should apply any updated listener properties to other buffers that share the same listener.

The property items in this set are specified by KSPROPERTY\_DIRECTSOUND3DLISTENER enumeration values.

The `KSPROPSETID_DirectSound3DListener` property set contains the following properties:

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_ALL**](ksproperty-directsound3dlistener-all.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_ALLOCATION**](ksproperty-directsound3dlistener-allocation.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_BATCH**](ksproperty-directsound3dlistener-batch.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_DISTANCEFACTOR**](ksproperty-directsound3dlistener-distancefactor.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_DOPPLERFACTOR**](ksproperty-directsound3dlistener-dopplerfactor.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_ORIENTATION**](ksproperty-directsound3dlistener-orientation.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_POSITION**](ksproperty-directsound3dlistener-position.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_ROLLOFFFACTOR**](ksproperty-directsound3dlistener-rollofffactor.md)

[**KSPROPERTY\_DIRECTSOUND3DLISTENER\_VELOCITY**](ksproperty-directsound3dlistener-velocity.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPSETID_DirectSound3DListener%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




