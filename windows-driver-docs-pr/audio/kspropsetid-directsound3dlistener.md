---
title: KSPROPSETID\_DirectSound3DListener
description: KSPROPSETID\_DirectSound3DListener
ms.assetid: 37eef2cb-5b45-4ff8-abb9-a685f0b290e3
keywords: ["KSPROPSETID_DirectSound3DListener"]
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





