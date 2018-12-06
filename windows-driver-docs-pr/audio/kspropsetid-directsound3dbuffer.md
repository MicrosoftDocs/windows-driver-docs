---
title: KSPROPSETID\_DirectSound3DBuffer
description: KSPROPSETID\_DirectSound3DBuffer
ms.assetid: 38ee775a-9b6c-4803-a024-fecc852d122d
keywords: ["KSPROPSETID_DirectSound3DBuffer"]
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_DirectSound3DBuffer


## <span id="ddk_kspropsetid_directsound3dbuffer_ks"></span><span id="DDK_KSPROPSETID_DIRECTSOUND3DBUFFER_KS"></span>


The `KSPROPSETID_DirectSound3DBuffer` property set contains all the device-specific properties that are needed to implement the **IDirectSound3DBuffer** interface (see the Microsoft Windows SDK documentation). Using this property set, the 3D-buffer properties that are specified by the API are passed directly between DirectSound and the WDM audio driver. This property set is handled by the [**KSNODETYPE\_3D\_EFFECTS**](ksnodetype-3d-effects.md) node, which handles both the 3D-buffer and 3D-listener properties.

The property items in this set are specified by KSPROPERTY\_DIRECTSOUND3DBUFFER enumeration values.

The `KSPROPSETID_DirectSound3DBuffer` property set contains the following properties:

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_ALL**](ksproperty-directsound3dbuffer-all.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEANGLES**](ksproperty-directsound3dbuffer-coneangles.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEORIENTATION**](ksproperty-directsound3dbuffer-coneorientation.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_CONEOUTSIDEVOLUME**](ksproperty-directsound3dbuffer-coneoutsidevolume.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_MAXDISTANCE**](ksproperty-directsound3dbuffer-maxdistance.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_MINDISTANCE**](ksproperty-directsound3dbuffer-mindistance.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_MODE**](ksproperty-directsound3dbuffer-mode.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_POSITION**](ksproperty-directsound3dbuffer-position.md)

[**KSPROPERTY\_DIRECTSOUND3DBUFFER\_VELOCITY**](ksproperty-directsound3dbuffer-velocity.md)

 

 





